"""Analytic-property entries -> properties.json micro-format.  [spike #12]

Routing rule: an entry is a *property entry* when its formula's top-level
shape is one of

    Equal(Op(f, <generator>), V)        Op in METADATA_HEADS (set/value-valued)
    Op(f, <generator>)                  Op in {IsHolomorphic, IsMeromorphic}

with <generator> one of

    ForElement(z, S) [, cond]   ->  var=z, domain=S
    For(z, p)                   ->  var=z, point=p        (Residue,
                                    ComplexZeroMultiplicity)
    For(z, a, b)                ->  var=z, path=[a, b]    (AnalyticContinuation)
    z, S  (positional)          ->  var=z, domain=S       (BranchPoints, ...)

Output record (deterministic key order; absent generator slots are null):

    { "id", "property", "operator", "expr", "var", "domain", "point",
      "path", "condition", "value", "assumptions", "topics" }

- ``operator``: the (post-mapping) head of f when f is a simple call of a
  named function, else null.
- Solutions' Brackets(Equal(...)) wrapper is stripped.
- Set-builder values Set(body, ForElement(n, S)) -> ["Set", body,
  ["Element", "n", S]] (box-verified).
- A value hitting an untranslatable construct keeps ``"value": null`` plus
  ``"valueSource": "<str(Expr)>"``.

Nested (expression-position) uses of metadata heads are NOT routed here --
they translate verbatim with a Function-literal first argument
(structural.translate_generator_head).

The For(z, p) / For(z, a, b) "point"/"path" slots extend the spike's
micro-format: the atan/exp testbed only exhibited the domain forms, but
Residue/ComplexZeroMultiplicity/AnalyticContinuation entries use point/path
generators; recording them faithfully beats forcing them into "domain".
"""

from . import mapping
from . import walker
from .structural import _head_name, _is_plain_symbol, _sym


def is_property_entry(formula):
    """Does this formula route to properties.json?"""
    h = _head_name(formula)
    if h in ("IsHolomorphic", "IsMeromorphic"):
        return True
    if h == "Equal" and len(formula.args()) == 2 \
            and _head_name(formula.args()[0]) in mapping.METADATA_HEADS:
        return True
    return False


def route_property_entry(formula, ctx):
    """Build the properties.json record fields for a property entry.
    Raises walker.TranslationSkip / UnknownHeadError like the main walker."""
    h = _head_name(formula)
    if h in ("IsHolomorphic", "IsMeromorphic"):
        op_expr, value = formula, None
    else:
        op_expr, value = formula.args()[0], formula.args()[1]

    prop = _head_name(op_expr)
    gargs = op_expr.args()
    f = gargs[0]
    if _head_name(f) == "Brackets":
        f = f.args()[0]

    var = domain = point = path = condition = None
    if len(gargs) >= 2 and _head_name(gargs[1]) in ("For", "ForElement"):
        gen = gargs[1]
        gvar = gen.args()[0]
        if not _is_plain_symbol(gvar):
            raise walker.TranslationSkip("tuple-indexing-set", heads=[prop])
        var = _sym(gvar)
        if _head_name(gen) == "ForElement":
            domain = walker.walk(gen.args()[1], ctx)
        elif len(gen.args()) == 2:
            point = walker.walk(gen.args()[1], ctx)
        elif len(gen.args()) == 3:
            path = [walker.walk(gen.args()[1], ctx),
                    walker.walk(gen.args()[2], ctx)]
        if len(gargs) > 2:
            conds = [walker.walk(c, ctx) for c in gargs[2:]]
            condition = conds[0] if len(conds) == 1 else ["And"] + conds
    elif len(gargs) == 3 and _is_plain_symbol(gargs[1]):
        var = _sym(gargs[1])
        domain = walker.walk(gargs[2], ctx)

    operator = _operator_name(f)
    expr = walker.walk(f, ctx)

    record = {
        "property": prop,
        "operator": operator,
        "expr": expr,
        "var": var,
        "domain": domain,
        "point": point,
        "path": path,
        "condition": condition,
        "value": None,
    }
    if value is not None:
        try:
            record["value"] = walker.walk(value, ctx)
        except (walker.TranslationSkip, walker.UnknownHeadError):
            record["value"] = None
            record["valueSource"] = str(value)
    return record


_NOT_OPERATORS = frozenset([
    # relational / logical / structural heads are not "the operator whose
    # property this is" (e.g. Solutions of Equal(Atan(z), w) -> null)
    "Equal", "NotEqual", "Less", "LessEqual", "Greater", "GreaterEqual",
    "And", "Or", "Not", "Implies", "Equivalent",
    "Add", "Sub", "Mul", "Div", "Pow", "Neg", "Pos",
])


def _operator_name(f):
    """Post-mapping name of f's head when f is a simple named-function call."""
    if f.is_atom():
        return None
    h = f.head()
    if not (h.is_atom() and h.is_symbol()):
        return None
    name = h._symbol
    if name in _NOT_OPERATORS:
        return None
    if name in mapping.SYMBOL_MAP:
        return mapping.SYMBOL_MAP[name]
    if name in mapping.SHELL_HEADS:
        return name
    return None
