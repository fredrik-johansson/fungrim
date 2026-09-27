"""Entry annotations: ``class`` taxonomy and ``guardLevel`` classifier (M3).

Both classifiers operate on the *translated* (MathJSON) formula/assumptions
of a corpus record, so all names below are post-mapping CE names
(``Element``/``NotElement``/``Less``/``IsOdd``/``ComplexNumbers``/``HH``/...).

``class`` decision tree (plan FUNGRIM-PLAN-1-TRANSLATOR.md SS3.3, applied in
order; analytic-property routing already happened in properties.py, so the
corpus never sees that class):

1. top head in LOGICAL_HEADS                       -> "logical"
2. top head in INEQUALITY_HEADS                    -> "inequality"
3. top head Equal-like (Equal, EqualNearestDecimal,
   *IndefiniteIntegralEqual):
   a. an operand is a big-op (Sum/Product/Integrate/Limit) up to a
      Negate/Multiply/Divide scalar-prefactor spine -> "representation"
      (sub-tagged series/integral/product/limit via ``subclass``)
   b. zero free variables                           -> "specific-value"
   c. otherwise                                     -> "identity"
4. top head in OTHER_HEADS                          -> "other"
5. anything else: ClassifyError (a new top-level head must be added to a
   table deliberately -- no silent guessing).

Two deliberate refinements of the plan's literal tree, both validated
against the FUNGRIM.md SS1 measured taxonomy (+-10% acceptance):

- The representation check (3a) precedes the zero-variable check (3b):
  ``Pi = 4 Sum(...)`` is a representation, not a specific value. With the
  plan's literal order the specific-value count lands at 558 vs the
  measured ~437 (+27%); with representation first it lands at 439 (+0.5%).
- "either side's top head in {Sum, Product, Integrate, Limit}" is widened
  to a scalar-prefactor *spine*: the big-op may be wrapped in
  Negate/Multiply/Divide (``Gamma(z) = c * Integrate(...)`` is a
  representation). A big-op buried under Add/Subtract or inside function
  arguments does NOT count. Direct-head-only yields 340 reps (-19.8% vs
  ~424); the spine yields 458 (+8.0%); Add/Subtract-spines overshoot
  (+27%). All five classes are within +-10% with this rule (see report).

``guardLevel`` (plan SS3.4): flatten assumptions over And; classify each
conjunct; entry level = max over conjuncts of

    none < real-simple < complex-domain < undischargeable

The conjunct classifier keeps explicit tables and raises GuardClassifyError
on any unrecognized statement head or membership-domain head. Interior
*terms* of relations are open-ended (any special function may appear in a
bound), so term classification uses explicit SIMPLE/COMPLEX/STRUCTURAL
tables plus one deliberate default: an unlisted compound term head is
treated as ``complex-domain`` (a numeric condition involving a special
function, e.g. ``NotEqual(JacobiTheta(3,0,tau), 0)``), never silently
``real-simple`` or ``undischargeable``.

Notable deliberate calls (vocabulary verified against the full-corpus
census of conjunct shapes):

- ``Or``: max of branch levels, floored at complex-domain (plan SS3.4).
- ``Not``/nested ``And``: level of the inner statement(s).
- Compound Element LHS (``Element(Subtract(a, b), Integers)``): floored at
  complex-domain -- not dischargeable by typing a single variable.
- Indexed-family LHS (``Element(e_(k), S)`` with free k): undischargeable
  (implicitly quantified over the family index).
- ``Element(tau, HH)`` and the equivalent ``Greater(Imaginary(tau), 0)``
  both classify complex-domain (HH is a complex domain; Imaginary is a
  complex-inspection head).
- Set algebra (Set/SetMinus/Union/Intersection/Interval/Range) takes the
  max over its content: ``SetMinus(RealNumbers, Set(0))`` is real-simple,
  ``SetMinus(ComplexNumbers, ...)`` is complex-domain.

Reclassified against measured CE capability (Track 3: part-bound facts over
Re/Im/Abs/Arg, SetMinus decomposition, NotEqual/NotElement/membership facts,
intervals with infinite endpoints, Range bounds; ground truth =
compute-engine/scripts/fungrim/guard-census.json):

- Membership of a *plain symbol* in an inert shell set is dischargeable via
  stored-membership facts (``assume(Element(x, S))`` + exact-match lookup),
  so shell-set membership classifies complex-domain, not undischargeable:
  atoms ``SL2Z``/``PSL2Z``/``ModularGroupFundamentalDomain``/
  ``ModularLambdaFundamentalDomain``/``Rings``/``Fields``; parameterized
  shells ``DirichletGroup(q)``/``PrimitiveDirichletCharacters(q)``/
  ``Lattice(...)``; set operators ``Interior``/``InteriorClosure``; and
  membership in a *symbolic* set (``Element(z, R)``, incl. the upstream
  typo ``Element(w, tau)`` in jacobi_theta.py:2004). A compound LHS (e.g.
  ``Element(Matrix(...), SL2Z)``) is still floored by the term level of the
  LHS, so Matrix membership stays undischargeable.
- Quantifiers, ``IsHolomorphic``/``IsMeromorphic``, ``Subset(Equal)``,
  Riemann-hypothesis atoms, indexed-family memberships, and structural
  objects in term position (Matrix, DirichletCharacter, Lattice-in-a-bound,
  ...) remain undischargeable.
"""


class ClassifyError(Exception):
    """A top-level formula head not covered by the class tables."""


class GuardClassifyError(Exception):
    """An assumption conjunct (or membership domain) head not covered by
    the guardLevel tables."""


# ---------------------------------------------------------------------------
# class taxonomy
# ---------------------------------------------------------------------------

LOGICAL_HEADS = frozenset([
    "Implies", "Equivalent", "ForAll", "Exists",
    "Divides", "CongruentMod",
    "Element", "NotElement", "Subset", "SubsetEqual",
    "And", "Or", "Not", "NotEqual",
    "Which",            # piecewise statements (branches are relations)
    "IsOdd", "IsEven",
])

INEQUALITY_HEADS = frozenset([
    "Less", "LessEqual", "Greater", "GreaterEqual", "AsymptoticTo",
])

# Equal-like heads: classified by the rule-3 sub-tree. EqualNearestDecimal
# (50-digit reference values) and the IndefiniteIntegralEqual family
# (antiderivative identities) state equalities.
EQUAL_HEADS = frozenset([
    "Equal", "EqualNearestDecimal",
    "ComplexIndefiniteIntegralEqual", "RealIndefiniteIntegralEqual",
    "IndefiniteIntegralEqual",
])

# Deliberate "other" bucket: the two Multiply-top entries (e54e61, 6c2b31)
# are upstream source artifacts (an Equal multiplied into an expression).
OTHER_HEADS = frozenset(["Multiply"])

_BIGOP_SUBCLASS = {
    "Sum": "series",
    "Integrate": "integral",
    "Product": "product",
    "Limit": "limit",
}

# Scalar-prefactor spine: heads through which a big-op still "is" the side.
_PREFACTOR_HEADS = frozenset(["Negate", "Multiply", "Divide"])


def _spine_subclass(op):
    """Sub-tag if ``op`` is a big-op up to a Negate/Multiply/Divide spine."""
    if not isinstance(op, list) or not op or not isinstance(op[0], str):
        return None
    if op[0] in _BIGOP_SUBCLASS:
        return _BIGOP_SUBCLASS[op[0]]
    if op[0] in _PREFACTOR_HEADS:
        for arg in op[1:]:
            sub = _spine_subclass(arg)
            if sub is not None:
                return sub
    return None


def classify_class(formula, variables):
    """Returns (class, subclass) for a corpus formula. subclass is non-None
    only for representations."""
    if not isinstance(formula, list) or not formula \
            or not isinstance(formula[0], str):
        raise ClassifyError(f"unclassifiable formula shape: {formula!r}")
    head = formula[0]
    if head in LOGICAL_HEADS:
        return ("logical", None)
    if head in INEQUALITY_HEADS:
        return ("inequality", None)
    if head in EQUAL_HEADS:
        for op in formula[1:]:
            sub = _spine_subclass(op)
            if sub is not None:
                return ("representation", sub)
        if not variables:
            return ("specific-value", None)
        return ("identity", None)
    if head in OTHER_HEADS:
        return ("other", None)
    raise ClassifyError(f"unrecognized top-level head: {head}")


# ---------------------------------------------------------------------------
# guardLevel
# ---------------------------------------------------------------------------

NONE, REAL_SIMPLE, COMPLEX_DOMAIN, UNDISCHARGEABLE = 0, 1, 2, 3
LEVEL_NAMES = {
    NONE: "none",
    REAL_SIMPLE: "real-simple",
    COMPLEX_DOMAIN: "complex-domain",
    UNDISCHARGEABLE: "undischargeable",
}

# --- atoms in TERM position ------------------------------------------------

_SIMPLE_ATOMS = frozenset([
    # real constants and extended-real endpoints
    "Pi", "ExponentialE", "EulerGamma", "CatalanConstant", "GoldenRatio",
    "ConstGlaisher", "HalphenConstant",
    "PositiveInfinity", "NegativeInfinity",
    "True", "False",
])
_COMPLEX_ATOMS = frozenset(["ImaginaryUnit", "ComplexInfinity", "NaN"])
_STRUCTURAL_ATOMS = frozenset([
    "RiemannHypothesis", "GeneralizedRiemannHypothesis",
    "Rings", "Fields", "SL2Z", "PSL2Z",
    "ModularGroupFundamentalDomain", "ModularLambdaFundamentalDomain",
])

# --- compound TERM heads ---------------------------------------------------

# Arithmetic / integer-valued operations: level = max of operands.
_SIMPLE_TERM_HEADS = frozenset([
    "Add", "Subtract", "Multiply", "Divide", "Negate", "Power", "Sqrt",
    "Root", "GCD", "LCM", "Mod", "Floor", "Ceil", "Max", "Min",
    "Factorial", "Factorial2", "Binomial", "Sign", "Exp", "Ln", "Log",
])
# Complex-inspection heads: floor complex-domain (plan SS3.4 row 3).
_COMPLEX_TERM_HEADS = frozenset([
    "Real", "Imaginary", "Abs", "Argument", "Conjugate", "Csgn",
])
# Structural objects in term position: undischargeable.
_STRUCTURAL_TERM_HEADS = frozenset([
    "DirichletCharacter", "DirichletGroup", "ConreyGenerator",
    "PrimitiveDirichletCharacters", "ModularGroupAction",
    "Matrix", "Lattice", "Interior", "InteriorClosure", "Spectrum",
    "GeneralLinearGroup", "SpecialLinearGroup", "Matrices",
])


def _term_level(t):
    if isinstance(t, (int, float)) or isinstance(t, dict):
        return REAL_SIMPLE
    if isinstance(t, str):
        if t in _COMPLEX_ATOMS:
            return COMPLEX_DOMAIN
        if t in _STRUCTURAL_ATOMS:
            return UNDISCHARGEABLE
        # known real constants and plain variables alike
        return REAL_SIMPLE
    if isinstance(t, list) and t and isinstance(t[0], str):
        head = t[0]
        args = [_term_level(a) for a in t[1:]]
        worst = max(args, default=REAL_SIMPLE)
        if head in _STRUCTURAL_TERM_HEADS:
            return UNDISCHARGEABLE
        if head in _SIMPLE_TERM_HEADS:
            return worst
        if head in _COMPLEX_TERM_HEADS:
            return max(COMPLEX_DOMAIN, worst)
        if head.endswith("_"):
            # indexed-family value with a (free) symbolic index: implicitly
            # quantified -> undischargeable
            return UNDISCHARGEABLE
        # deliberate default: any other function value (special functions,
        # Which, Infimum, set algebra in term position, ...) is a checkable
        # complex-domain condition, never real-simple/undischargeable.
        return max(COMPLEX_DOMAIN, worst)
    raise GuardClassifyError(f"unclassifiable term: {t!r}")


# --- membership DOMAINS ----------------------------------------------------

_REAL_DOMAIN_ATOMS = frozenset([
    "Integers", "RationalNumbers", "RealNumbers", "Primes",
    "NonNegativeIntegers", "PositiveIntegers", "NonPositiveIntegers",
])
# Complex domains AND inert shell sets: a plain-symbol membership in any of
# these is dischargeable via stored-membership facts (census-verified, e.g.
# Element(gamma, SL2Z) in modular_transformations/5636db, Element(R, Rings)
# in powers/6c2b31, Element(tau, ModularGroupFundamentalDomain) in
# modular_transformations/e28209).
_COMPLEX_DOMAIN_ATOMS = frozenset([
    "ComplexNumbers", "HH", "AlgebraicNumbers", "UnitCircle",
    "SL2Z", "PSL2Z", "ModularGroupFundamentalDomain",
    "ModularLambdaFundamentalDomain", "Rings", "Fields",
])
# Domain heads whose membership is structurally undischargeable.
_STRUCTURAL_DOMAIN_HEADS = frozenset([
    "Matrices", "GeneralLinearGroup", "SpecialLinearGroup", "CartesianPower",
    "PrimitiveReducedPositiveIntegralBinaryQuadraticForms",
])
# Parameterized inert-shell sets: plain-symbol membership discharges via
# membership facts (census: 32 dirichlet entries with DirichletGroup(q),
# 9 weierstrass entries with NotElement(z, Lattice(1, tau))). Classified
# like regions: complex-domain max'ed with the term level of the arguments.
_SHELL_DOMAIN_HEADS = frozenset([
    "DirichletGroup", "PrimitiveDirichletCharacters", "Lattice",
])
# Complex planar regions: complex-domain (max'ed with content).
_COMPLEX_REGION_HEADS = frozenset([
    "OpenDisk", "ClosedDisk", "BernsteinEllipse",
])
# Set algebra recursing over member domains.
_SET_ALGEBRA_HEADS = frozenset([
    "SetMinus", "Union", "Intersection", "CartesianProduct",
])
# Set operators recursing over a member domain, floored complex-domain
# (census: Union(Interior(ModularLambdaFundamentalDomain), ...) in
# modular_lambda/b7174d discharges).
_SET_OPERATOR_HEADS = frozenset(["Interior", "InteriorClosure"])
# Real-content domains built from terms (endpoints / listed elements).
_TERM_CONTENT_DOMAIN_HEADS = frozenset(["Interval", "Range", "Set", "Which"])
_INTEGER_DOMAIN_HEADS = frozenset(["Divisors", "RealBall"])


def _domain_level(d):
    if isinstance(d, str):
        if d in _REAL_DOMAIN_ATOMS:
            return REAL_SIMPLE
        if d in _COMPLEX_DOMAIN_ATOMS:
            return COMPLEX_DOMAIN
        # a symbolic (variable) set: plain-symbol membership discharges via
        # stored-membership facts (census: jacobi_theta Element(w, tau) x23,
        # powers/6c2b31 Element(z, R))
        return COMPLEX_DOMAIN
    if isinstance(d, list) and d and isinstance(d[0], str):
        head = d[0]
        if head in _STRUCTURAL_DOMAIN_HEADS:
            return UNDISCHARGEABLE
        if head in _SET_ALGEBRA_HEADS:
            return max((_domain_level(a) for a in d[1:]),
                       default=REAL_SIMPLE)
        if head in _SET_OPERATOR_HEADS:
            return max([COMPLEX_DOMAIN] + [_domain_level(a) for a in d[1:]])
        if head in _SHELL_DOMAIN_HEADS:
            return max([COMPLEX_DOMAIN] + [_term_level(a) for a in d[1:]])
        if head in _COMPLEX_REGION_HEADS:
            return max([COMPLEX_DOMAIN] + [_term_level(a) for a in d[1:]])
        if head in _INTEGER_DOMAIN_HEADS:
            return REAL_SIMPLE
        if head == "Which":
            # conditional set (from a Cases translation)
            return max([COMPLEX_DOMAIN] + [_term_level(a) for a in d[1:]])
        if head in ("Interval", "Range", "Set"):
            levels = [REAL_SIMPLE]
            for a in d[1:]:
                if isinstance(a, list) and a and a[0] == "Open":
                    a = a[1]
                levels.append(_term_level(a))
            return max(levels)
        if head in ("Filter", "Map"):
            # Set-builder comprehensions translate to Filter/Map collections
            # (structural.translate_set); membership in them is not
            # dischargeable by the assumptions machinery. (The previous
            # literal-Set encoding under-guarded these: it graded the
            # *operands* of a fictitious 2-element set.)
            return UNDISCHARGEABLE
        raise GuardClassifyError(f"unrecognized domain head: {head}")
    raise GuardClassifyError(f"unclassifiable domain: {d!r}")


# --- statements (conjuncts) ------------------------------------------------

_RELATION_HEADS = frozenset([
    "Equal", "NotEqual", "Less", "LessEqual", "Greater", "GreaterEqual",
    "Divides", "CongruentMod", "IsOdd", "IsEven", "AsymptoticTo",
])
_QUANTIFIER_HEADS = frozenset(["ForAll", "Exists"])
_UNDISCHARGEABLE_STMT_HEADS = frozenset([
    "IsHolomorphic", "IsMeromorphic", "Subset", "SubsetEqual",
])


def _statement_level(s):
    if isinstance(s, str):
        if s == "True":
            return NONE
        if s in _STRUCTURAL_ATOMS:
            return UNDISCHARGEABLE
        raise GuardClassifyError(f"unrecognized atom conjunct: {s}")
    if not isinstance(s, list) or not s or not isinstance(s[0], str):
        raise GuardClassifyError(f"unclassifiable conjunct: {s!r}")
    head = s[0]
    if head == "And":
        return max((_statement_level(c) for c in s[1:]), default=NONE)
    if head == "Or":
        branches = max((_statement_level(c) for c in s[1:]), default=NONE)
        return max(COMPLEX_DOMAIN, branches)  # plan SS3.4: floor cplx-domain
    if head == "Not":
        return _statement_level(s[1])
    if head in _QUANTIFIER_HEADS:
        return UNDISCHARGEABLE
    if head in _UNDISCHARGEABLE_STMT_HEADS:
        return UNDISCHARGEABLE
    if head in ("Element", "NotElement"):
        lhs, dom = s[1], s[2]
        base = _domain_level(dom)
        if isinstance(lhs, str):
            return max(REAL_SIMPLE, base)
        if isinstance(lhs, list) and lhs and isinstance(lhs[0], str) \
                and lhs[0].endswith("_"):
            return UNDISCHARGEABLE  # indexed-family membership
        # compound LHS: a relation between variables, floored complex-domain
        return max(COMPLEX_DOMAIN, base, _term_level(lhs))
    if head in _RELATION_HEADS:
        return max([REAL_SIMPLE] + [_term_level(a) for a in s[1:]])
    raise GuardClassifyError(f"unrecognized conjunct head: {head}")


def _flatten_and(a):
    if isinstance(a, list) and a and a[0] == "And":
        for c in a[1:]:
            yield from _flatten_and(c)
    else:
        yield a


def classify_guard_level(assumptions):
    """guardLevel name for a corpus entry's translated assumptions."""
    if assumptions is None:
        return LEVEL_NAMES[NONE]
    level = max((_statement_level(c) for c in _flatten_and(assumptions)),
                default=NONE)
    return LEVEL_NAMES[level]
