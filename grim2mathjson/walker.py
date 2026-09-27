"""Expr -> MathJSON recursive translator core.

The walker turns a pygrim ``Expr`` into MathJSON (plain Python data:
str | int | dict | list). It emits *source form* (non-canonical) MathJSON:
``["Subtract", a, b]``, ``["Negate", x]``, raw Interval/Range encodings, etc.
CE's ``ce.box()`` performs canonicalization downstream.

Dispatch rule (mapping.py docstring): every head is either mapped, kept
verbatim + shell-declared, structural, metadata-extracted, or skipped.
Anything else raises :class:`UnknownHeadError`, which the pipeline converts
into an ``unknown-head`` skip record (a hard error under ``--strict``).
"""

from . import mapping
from . import structural

# IEEE-754 safe-integer range: integers outside it are emitted as
# {"num": "<digits>"} per MathJsonNumberObject (math-json/types.ts:100).
_MAX_SAFE_INT = 9007199254740991


class TranslationSkip(Exception):
    """The entry (or assumption) hits an enumerated untranslatable construct."""

    def __init__(self, reason, heads=None):
        super().__init__(reason)
        self.reason = reason
        self.heads = sorted(set(heads or []))


class UnknownHeadError(Exception):
    """A head that is in none of the mapping tables: a translator error."""

    def __init__(self, head):
        super().__init__(head)
        self.head = head


class Ctx:
    """Per-entry translation context (annotation collectors)."""

    def __init__(self):
        self.heads = set()              # post-mapping function heads used
        self.shells = set()             # verbatim (shell) heads used
        self.flavors = []               # typed limit/derivative variants, ordered
        self.directed_infinity = False  # Multiply(c, +/-oo) passthrough present
        self.indexed_families = set()   # family heads like "z_"

    def add_flavor(self, flavor):
        if flavor and flavor not in self.flavors:
            self.flavors.append(flavor)

    def add_head(self, name):
        self.heads.add(name)

    def add_shell(self, name):
        self.shells.add(name)
        self.heads.add(name)


# Heads excluded from the per-entry "heads" index (structural / arithmetic
# noise). Starting blacklist: Fungrim's own exclude_symbols (expr.py:1232),
# post-mapping, plus arithmetic/relational/structural artifacts.
NOISE_HEADS = frozenset([
    # arithmetic core
    "Add", "Subtract", "Multiply", "Divide", "Power", "Negate", "Sqrt", "Root",
    # relations
    "Equal", "NotEqual", "Less", "LessEqual", "Greater", "GreaterEqual",
    # logic
    "And", "Or", "Not", "Implies", "Equivalent", "ForAll", "Exists",
    # sets / membership (Fungrim exclude_symbols)
    "Element", "NotElement", "Union", "Intersection", "SetMinus",
    "Subset", "SubsetEqual", "Set", "List", "Tuple", "PowerSet",
    # structural artifacts of the translation itself
    "Function", "Apply", "Limits", "Which", "Open", "Interval", "Range",
    "Matrix", "At", "Count",
])


def builtins_set():
    from pygrim import expr as pg
    return pg.all_builtins_set


def sym_name(expr):
    """Name of a symbol atom, with collision renames applied (variables only)."""
    name = expr._symbol
    if name in mapping.VARIABLE_RENAMES and name not in builtins_set():
        return mapping.VARIABLE_RENAMES[name]
    return name


def encode_int(value):
    if -_MAX_SAFE_INT <= value <= _MAX_SAFE_INT:
        return value
    return {"num": str(value)}


# ---------------------------------------------------------------------------
# Structural dispatch (head name -> handler in structural.py).
# Handlers have signature (expr, ctx, walk) and return MathJSON.
# ---------------------------------------------------------------------------
STRUCTURAL_HEADS = {
    "Where": structural.translate_where,
    "Sum": structural.translate_bigop,
    "Product": structural.translate_bigop,
    "Integral": structural.translate_bigop,
    "PrimeSum": structural.translate_bigop,
    "PrimeProduct": structural.translate_bigop,
    "DivisorSum": structural.translate_bigop,
    "DivisorProduct": structural.translate_bigop,
    "Derivative": structural.translate_derivative,
    "RealDerivative": structural.translate_derivative,
    "ComplexDerivative": structural.translate_derivative,
    "ComplexBranchDerivative": structural.translate_derivative,
    "MeromorphicDerivative": structural.translate_derivative,
    "Limit": structural.translate_limit,
    "SequenceLimit": structural.translate_limit,
    "RealLimit": structural.translate_limit,
    "LeftLimit": structural.translate_limit,
    "RightLimit": structural.translate_limit,
    "ComplexLimit": structural.translate_limit,
    "MeromorphicLimit": structural.translate_limit,
    "SequenceLimitInferior": structural.translate_seq_extremum_limit,
    "SequenceLimitSuperior": structural.translate_seq_extremum_limit,
    "Cases": structural.translate_cases,
    "Parentheses": structural.strip_decorations,
    "Brackets": structural.strip_decorations,
    "Braces": structural.strip_decorations,
    "AngleBrackets": structural.strip_decorations,
    "Pos": structural.strip_decorations,
    "Neg": structural.translate_neg,
    "Pow": structural.translate_pow,
    "Inv": structural.translate_inv,
    "Subscript": structural.translate_subscript,
    "OpenInterval": structural.translate_interval,
    "ClosedInterval": structural.translate_interval,
    "OpenClosedInterval": structural.translate_interval,
    "ClosedOpenInterval": structural.translate_interval,
    "ZZGreaterEqual": structural.translate_integer_sets,
    "ZZLessEqual": structural.translate_integer_sets,
    "Range": structural.translate_integer_sets,
    "Matrix2x2": structural.translate_matrix2x2,
    "Matrix2x1": structural.translate_matrix2x2,
    "Matrix": structural.translate_matrix,
    "Decimal": structural.translate_decimal,
    "Set": structural.translate_set,
    "List": structural.translate_list,
    "Tuple": structural.translate_list,
    "All": structural.translate_quantifier,
    "Exists": structural.translate_quantifier,
    "Minimum": structural.translate_optimum,
    "Maximum": structural.translate_optimum,
    "Supremum": structural.translate_optimum,
    "Infimum": structural.translate_optimum,
    "ArgMin": structural.translate_optimum,
    "ArgMax": structural.translate_optimum,
    "ArgMinUnique": structural.translate_optimum,
    "ArgMaxUnique": structural.translate_optimum,
    "Fun": structural.translate_fun,
    "Call": structural.translate_call,
    "Item": structural.translate_item,
    "EqualAndElement": structural.translate_equal_and_element,
    "AiryAi": structural.translate_optional_derivative_order,
    "AiryBi": structural.translate_optional_derivative_order,
    "BesselJ": structural.translate_optional_derivative_order,
    "BesselY": structural.translate_optional_derivative_order,
    "BesselI": structural.translate_optional_derivative_order,
    "BesselK": structural.translate_optional_derivative_order,
    "LambertW": structural.translate_lambertw,
    "DigammaFunction": structural.translate_digamma,
    # metadata/generator heads in *expression* position (top-level routing to
    # properties.json happens before the walker is invoked):
    "Zeros": structural.translate_generator_head,
    "Poles": structural.translate_generator_head,
    "BranchPoints": structural.translate_generator_head,
    "BranchCuts": structural.translate_generator_head,
    "EssentialSingularities": structural.translate_generator_head,
    "Residue": structural.translate_generator_head,
    "AnalyticContinuation": structural.translate_generator_head,
    "ComplexZeroMultiplicity": structural.translate_generator_head,
    "Solutions": structural.translate_generator_head,
    "UniqueSolution": structural.translate_generator_head,
    "UniqueZero": structural.translate_generator_head,
    "IsHolomorphic": structural.translate_generator_head,
    "IsMeromorphic": structural.translate_generator_head,
}


def walk(expr, ctx):
    """Translate a pygrim Expr to MathJSON. Raises TranslationSkip /
    UnknownHeadError for untranslatable constructs."""
    if expr.is_atom():
        return walk_atom(expr, ctx)

    head = expr.head()
    if head.is_atom() and head.is_symbol():
        name = head._symbol

        if name in mapping.SKIP_HEADS:
            raise TranslationSkip(mapping.SKIP_HEADS[name], heads=[name])

        if name in STRUCTURAL_HEADS:
            return STRUCTURAL_HEADS[name](expr, ctx, walk)

        if name in mapping.SYMBOL_MAP:
            target = mapping.SYMBOL_MAP[name]
            ctx.add_head(target)
            out = [target] + [walk(a, ctx) for a in expr.args()]
            # Directed infinity c*oo: passthrough + entry flag (spike #5).
            if target == "Multiply" and any(
                    a in ("PositiveInfinity", "NegativeInfinity")
                    for a in out[1:]):
                ctx.directed_infinity = True
            return out

        if name in mapping.SHELL_HEADS:
            ctx.add_shell(name)
            return [name] + [walk(a, ctx) for a in expr.args()]

        if name in builtins_set():
            raise UnknownHeadError(name)

        # Variable head: generic function variable f(x) or indexed-family
        # call z_(k) (spike #7: call form preserves binding).
        vname = sym_name(head)
        if vname.endswith("_"):
            ctx.indexed_families.add(vname)
        return [vname] + [walk(a, ctx) for a in expr.args()]

    # Non-atomic head (e.g. Subscript(chi, 0)(p)): walk the head; if it
    # collapses to a symbol keep call form, else use Apply (a MathJSON call
    # with a non-symbol head throws in ce.box -- SPIKE-DECISIONS.md #1).
    whead = walk(head, ctx)
    args = [walk(a, ctx) for a in expr.args()]
    if isinstance(whead, str):
        if whead.endswith("_"):
            ctx.indexed_families.add(whead)
        return [whead] + args
    ctx.add_head("Apply")
    return ["Apply", whead] + args


def walk_atom(expr, ctx):
    if expr.is_integer():
        return encode_int(expr._integer)
    if expr.is_text():
        return {"str": expr._text}
    name = expr._symbol
    if name in mapping.SKIP_HEADS:
        raise TranslationSkip(mapping.SKIP_HEADS[name], heads=[name])
    if name in mapping.SYMBOL_MAP:
        return mapping.SYMBOL_MAP[name]
    if name in mapping.SHELL_HEADS:
        ctx.add_shell(name)
        return name
    if name in builtins_set():
        raise UnknownHeadError(name)
    vname = sym_name(expr)
    if vname.endswith("_"):
        ctx.indexed_families.add(vname)
    return vname
