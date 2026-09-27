"""Structural constructs: Fungrim binding/branching forms -> MathJSON.

Implements the M0 spike decisions (SPIKE-DECISIONS.md, same item numbers).
Every encoding below is backed by an actual ce.box() verification recorded
there or in the M1 verification batch.

All handlers have signature ``handler(expr, ctx, walk)`` where ``walk`` is
:func:`walker.walk` (passed in to avoid a circular import) and ``ctx`` is a
:class:`walker.Ctx`. Handlers raise ``walker.TranslationSkip`` for the
enumerated skip codes.
"""


def _pg():
    from pygrim import expr as pg
    return pg


def _skip(reason, heads=None):
    from .walker import TranslationSkip
    raise TranslationSkip(reason, heads=heads)


def _head_name(e):
    if e.is_atom():
        return None
    h = e.head()
    if h.is_atom() and h.is_symbol():
        return h._symbol
    return None


def _sym(e):
    from .walker import sym_name
    return sym_name(e)


def _is_plain_symbol(e):
    return e.is_atom() and e.is_symbol()


def _fresh_var(expr, preferred):
    """A deterministic variable name not colliding with any symbol in expr."""
    used = set(s._symbol for s in expr.symbols(unique=True))
    if preferred not in used:
        return preferred
    for cand in ("z", "w", "t", "u", "v"):
        if cand not in used:
            return cand
    i = 0
    while f"{preferred}{i}" in used:
        i += 1
    return f"{preferred}{i}"


# ---------------------------------------------------------------------------
# Where / Def  [spike #1]
# ---------------------------------------------------------------------------

def translate_where(expr, ctx, walk):
    """Eliminate Where(body, Def(...), ...) by substitution.  [spike #1]

    - Plain ``Def(x, val)`` (143 entries): substitute right-to-left with
      ``Expr.replace({x: val}, semantic=True)`` (capture-avoiding).
    - ``Def(Tuple(...), rhs)`` (20 entries): substitute componentwise only
      when rhs is a literal Tuple; otherwise SKIP ``where-def-tuple``.
    - Function defs ``Def(f(z), body)`` (41 entries): BETA-REDUCE at
      translation time when body does not reference f; each call site
      f(args) is replaced by body[params := args]. (Direct MathJSON calls
      with a Function-literal head THROW in ce.box() -- use
      ``["Apply", ["Function", body, "z"], arg]`` if an unreduced function
      value must ever be emitted.)
    - Recursive defs: SKIP ``where-recursive-def``. Bare function-value uses
      of f (not call position): SKIP ``where-function-def``.
    - Old-style ``Where(body, Equal(lhs, rhs))`` treated like Def (pygrim
      does the same in free_variables/replace).
    """
    pg = _pg()
    args = expr.args()
    body = args[0]
    for d in reversed(args[1:]):
        dh = _head_name(d)
        if dh not in ("Def", "Equal") or len(d.args()) != 2:
            _skip("where-def-tuple", heads=["Where"])
        lhs, rhs = d.args()[0], d.args()[1]
        if _is_plain_symbol(lhs):
            body = body.replace({lhs: rhs}, semantic=True)
        elif _head_name(lhs) == "Tuple":
            sub_vars = lhs.args()
            if any(not _is_plain_symbol(v) for v in sub_vars):
                # incl. Def(Tuple(f(i), For(i, 1, n)), T) indexed families
                _skip("where-def-tuple", heads=["Where"])
            if _head_name(rhs) == "Tuple" and len(rhs.args()) == len(sub_vars):
                body = body.replace(dict(zip(sub_vars, rhs.args())),
                                    semantic=True)
            else:
                _skip("where-def-tuple", heads=["Where"])
        elif (not lhs.is_atom()) and _is_plain_symbol(lhs.head()):
            body = _beta_reduce(body, lhs.head(), lhs.args(), rhs)
        else:
            _skip("where-def-tuple", heads=["Where"])
    return walk(body, ctx)


def _beta_reduce(body, fsym, params, fbody):
    """Replace every call f(args) in body with fbody[params := args]."""
    pg = _pg()
    if fsym in fbody.free_variables():
        _skip("where-recursive-def", heads=["Where"])
    if any(not _is_plain_symbol(p) for p in params):
        _skip("where-function-def", heads=["Where"])

    def transform(e):
        if e.is_atom():
            if e == fsym:
                # f used as a bare function value -- cannot reduce
                _skip("where-function-def", heads=["Where"])
            return e
        head = e.head()
        new_args = [transform(a) for a in e.args()]
        if head.is_atom() and head == fsym:
            if len(new_args) != len(params):
                _skip("where-function-def", heads=["Where"])
            return fbody.replace(dict(zip(params, new_args)), semantic=True)
        new_head = transform(head)
        return pg.Expr(call=[new_head] + new_args)

    return transform(body)


# ---------------------------------------------------------------------------
# Indexing sets (shared by big-ops, Set comprehensions, optima)  [spike #3, #4]
# ---------------------------------------------------------------------------

def _indexing_set(gen, cond, ctx, walk):
    """Translate For/ForElement (+ optional condition) into CE's indexing
    forms: ["Element", var, S] or the EL-3 ["Element", var, S, cond]."""
    gh = _head_name(gen)
    if gh == "ForElement":
        var, S = gen.args()[0], gen.args()[1]
        if not _is_plain_symbol(var):
            _skip("tuple-indexing-set", heads=["ForElement"])
        elt = ["Element", _sym(var), walk(S, ctx)]
        if cond is not None:
            elt.append(walk(cond, ctx))
        return elt
    if gh == "For" and len(gen.args()) == 1:
        var = gen.args()[0]
        if not _is_plain_symbol(var):
            _skip("tuple-indexing-set", heads=["For"])
        if cond is None:
            _skip("bare-for-generator", heads=["For"])
        # Extract the Element(var, S) conjunct as the base set (EL-3 cond rest)
        pg = _pg()
        conjuncts = list(cond.head_args_flattened(pg.And)) \
            if _head_name(cond) == "And" else [cond]
        base, rest = None, []
        for c in conjuncts:
            if base is None and _head_name(c) == "Element" \
                    and c.args()[0] == var:
                base = c.args()[1]
            else:
                rest.append(c)
        if base is None:
            _skip("bare-for-generator", heads=["For"])
        elt = ["Element", _sym(var), walk(base, ctx)]
        if rest:
            if len(rest) == 1:
                elt.append(walk(rest[0], ctx))
            else:
                elt.append(["And"] + [walk(r, ctx) for r in rest])
        return elt
    _skip("bare-for-generator")


# ---------------------------------------------------------------------------
# Sum / Product / Integral / PrimeSum / DivisorSum / ...  [spike #3, #4]
# ---------------------------------------------------------------------------

_BIGOP_TARGET = {
    "Sum": "Sum", "Product": "Product", "Integral": "Integrate",
    "PrimeSum": "Sum", "PrimeProduct": "Product",
    "DivisorSum": "Sum", "DivisorProduct": "Product",
}


def translate_bigop(expr, ctx, walk):
    """Big operators with For/ForElement indexing sets.  [spike #3, #4]

    - ``Sum(body, For(k, a, b))``      -> ["Sum", body, ["Limits", "k", a, b]]
    - ``Sum(body, ForElement(k, S))``  -> ["Sum", body, ["Element", "k", S]]
    - Trailing condition argument      -> EL-3 ["Element", "k", S, cond]
      (condition heads must be boolean-typed shells: Divides, CongruentMod)
    - ``PrimeSum/PrimeProduct(f, For(p) [, cond])``
        -> ["Sum"/"Product", f, ["Element", "p", "Primes" [, cond]]]
    - ``DivisorSum/DivisorProduct(f, For(d, n) [, cond])``
        -> ["Sum"/"Product", f, ["Element", "d", ["Divisors", n] [, cond]]]
    - ``ForElement(Tuple(m, n), S)``: SKIP ``tuple-indexing-set`` (CE's
      canonicalIndexingSet requires a symbol index).
    """
    name = _head_name(expr)
    op = _BIGOP_TARGET[name]
    args = expr.args()
    ctx.add_head(op)
    body = args[0]
    if len(args) == 1:
        return [op, walk(body, ctx)]
    gen = args[1]
    cond = None
    if len(args) > 2:
        if len(args) == 3:
            cond = args[2]
        else:
            pg = _pg()
            cond = pg.And(*args[2:])
    gh = _head_name(gen)

    if gh == "For":
        fa = gen.args()
        var = fa[0]
        if not _is_plain_symbol(var):
            _skip("tuple-indexing-set", heads=[name])
        v = _sym(var)
        if name in ("PrimeSum", "PrimeProduct"):
            ctx.add_shell("Primes")
            elt = ["Element", v, "Primes"]
        elif name in ("DivisorSum", "DivisorProduct"):
            if len(fa) < 2:
                _skip("bare-for-generator", heads=[name])
            ctx.add_shell("Divisors")
            elt = ["Element", v, ["Divisors", walk(fa[1], ctx)]]
        elif len(fa) == 3:
            lo, hi = walk(fa[1], ctx), walk(fa[2], ctx)
            if cond is None:
                return [op, walk(body, ctx), ["Limits", v, lo, hi]]
            elt = ["Element", v, ["Range", lo, hi]]
        else:
            _skip("bare-for-generator", heads=[name])
        if cond is not None:
            elt.append(walk(cond, ctx))
        return [op, walk(body, ctx), elt]

    if gh == "ForElement":
        return [op, walk(body, ctx), _indexing_set(gen, cond, ctx, walk)]

    _skip("bare-for-generator", heads=[name])


# ---------------------------------------------------------------------------
# Derivatives  [spike #2]
# ---------------------------------------------------------------------------

_DERIVATIVE_FLAVOR = {
    "Derivative": None,
    "ComplexDerivative": None,
    "RealDerivative": "real",
    "ComplexBranchDerivative": "complex-branch",
    "MeromorphicDerivative": "meromorphic",
}


def translate_derivative(expr, ctx, walk):
    """ComplexDerivative(f, For(z, z0[, n])) and typed variants.  [spike #2]

    Uniform target (box-verified, incl. symbolic order):

        ["Apply", ["Derivative", ["Function", f, z], n], z0]

    order omitted -> 1; point == var keeps the same shape with z0 = z.
    Typed variants collapse to the same encoding + entry-level ``flavor``.
    CAVEAT: symbolic orders must be typed `integer` by the validation
    harness before boxing.
    """
    name = _head_name(expr)
    args = expr.args()
    f, gen = args[0], args[1]
    if _head_name(gen) != "For":
        _skip("bare-for-generator", heads=[name])
    fa = gen.args()
    var = fa[0]
    if not _is_plain_symbol(var):
        _skip("tuple-indexing-set", heads=[name])
    v = _sym(var)
    point = walk(fa[1], ctx) if len(fa) > 1 else v
    order = walk(fa[2], ctx) if len(fa) > 2 else 1
    ctx.add_head("Derivative")
    ctx.add_flavor(_DERIVATIVE_FLAVOR[name])
    return ["Apply", ["Derivative", ["Function", walk(f, ctx), v], order],
            point]


# ---------------------------------------------------------------------------
# Limits  [spike #13]
# ---------------------------------------------------------------------------

_LIMIT_FLAVOR = {
    "Limit": None,
    "SequenceLimit": "sequence",
    "RealLimit": "real",
    "ComplexLimit": "complex",
    "MeromorphicLimit": "meromorphic",
    "LeftLimit": "left",
    "RightLimit": "right",
}


def translate_limit(expr, ctx, walk):
    """Typed limit variants -> CE Limit.  [spike #13]

    ["Limit", ["Function", body, var], point] with direction +1 for
    RightLimit, -1 for LeftLimit (CE numerics/numeric.ts:limit). The variant
    goes to the entry-level ``flavor`` field, not the expression.
    """
    name = _head_name(expr)
    args = expr.args()
    f, gen = args[0], args[1]
    if len(args) > 2:
        _skip("limit-condition", heads=[name])
    if _head_name(gen) != "For":
        _skip("bare-for-generator", heads=[name])
    fa = gen.args()
    var = fa[0]
    if not _is_plain_symbol(var) or len(fa) != 2:
        _skip("bare-for-generator", heads=[name])
    v = _sym(var)
    ctx.add_head("Limit")
    ctx.add_flavor(_LIMIT_FLAVOR[name])
    out = ["Limit", ["Function", walk(f, ctx), v], walk(fa[1], ctx)]
    if name == "RightLimit":
        out.append(1)
    elif name == "LeftLimit":
        out.append(-1)
    return out


def translate_seq_extremum_limit(expr, ctx, walk):
    """SequenceLimitInferior/Superior(f, For(n, oo)): no CE equivalent --
    verbatim shell head with a Function-literal argument (binding kept):
    ["SequenceLimitInferior", ["Function", body, n], point]."""
    name = _head_name(expr)
    args = expr.args()
    f, gen = args[0], args[1]
    if _head_name(gen) != "For" or len(gen.args()) != 2 \
            or not _is_plain_symbol(gen.args()[0]):
        _skip("bare-for-generator", heads=[name])
    v = _sym(gen.args()[0])
    ctx.add_shell(name)
    return [name, ["Function", walk(f, ctx), v], walk(gen.args()[1], ctx)]


# ---------------------------------------------------------------------------
# Cases -> Which  [spike #6]
# ---------------------------------------------------------------------------

def translate_cases(expr, ctx, walk):
    """Cases(Tuple(v, c), ..., [Tuple(v, Otherwise)]) -> Which.  [spike #6]

    Argument-order swap: Fungrim (value, cond) -> Which (cond, value).
    Otherwise -> trailing ("True", value). Partial Cases (no Otherwise):
    Which WITHOUT a default (uncovered branch evaluates to CE "Undefined",
    the honest semantics -- no synthetic default).
    """
    out = ["Which"]
    ctx.add_head("Which")
    for t in expr.args():
        if _head_name(t) != "Tuple" or len(t.args()) != 2:
            _skip("cases-malformed", heads=["Cases"])
        value, cond = t.args()
        if cond.is_atom() and cond.is_symbol() and cond._symbol == "Otherwise":
            out.append("True")
        else:
            out.append(walk(cond, ctx))
        out.append(walk(value, ctx))
    return out


# ---------------------------------------------------------------------------
# Subscripts / family variables  [spike #7]
# ---------------------------------------------------------------------------

def translate_subscript(expr, ctx, walk):
    """Subscripts and generator-variable calls.  [spike #7]

    - ``Subscript(a, <literal int>)`` -> fused symbol "a_1" (CE does this
      canonicalization itself; round-trips).
    - ``Subscript(a, k)`` symbolic k -> call form ["a_", "k"]: CE
      canonicalizes ["Subscript", "a", "k"] to the fused symbol "a_k",
      silently severing the binding to a surrounding binder -- the call
      form is the safe, verified encoding. The synthesized family head is
      recorded in ``indexedFamilies``.
    """
    base, idx = expr.args()
    if not _is_plain_symbol(base):
        _skip("subscript-base", heads=["Subscript"])
    # NOTE: VARIABLE_RENAMES does not apply here -- the synthesized names
    # ("a_1", "a_") never collide with CE constants even when the base does
    # (Subscript(e, k) -> family "e_", not "e_var_").
    bname = base._symbol
    if idx.is_integer():
        return f"{bname}_{idx._integer}"
    family = bname if bname.endswith("_") else bname + "_"
    ctx.indexed_families.add(family)
    return [family, walk(idx, ctx)]


# ---------------------------------------------------------------------------
# Intervals  [spike #10]
# ---------------------------------------------------------------------------

def translate_interval(expr, ctx, walk):
    """Interval family -> CE Interval with Open markers.  [spike #10]

    OpenInterval(a,b)       -> ["Interval", ["Open", a], ["Open", b]]
    ClosedInterval(a,b)     -> ["Interval", a, b]
    OpenClosedInterval(a,b) -> ["Interval", ["Open", a], b]
    ClosedOpenInterval(a,b) -> ["Interval", a, ["Open", b]]
    """
    name = _head_name(expr)
    a, b = (walk(x, ctx) for x in expr.args())
    if name in ("OpenInterval", "OpenClosedInterval"):
        a = ["Open", a]
    if name in ("OpenInterval", "ClosedOpenInterval"):
        b = ["Open", b]
    ctx.add_head("Interval")
    return ["Interval", a, b]


# ---------------------------------------------------------------------------
# Integer sets  [spike #11]
# ---------------------------------------------------------------------------

def translate_integer_sets(expr, ctx, walk):
    """ZZGreaterEqual / ZZLessEqual / Range.  [spike #11]

    ZZGreaterEqual(0) -> "NonNegativeIntegers"   (CE type-backed set)
    ZZGreaterEqual(1) -> "PositiveIntegers"
    ZZGreaterEqual(a) -> ["Range", a, "PositiveInfinity"]
    ZZLessEqual(0)    -> "NonPositiveIntegers"
    ZZLessEqual(b)    -> ["Range", "NegativeInfinity", b]
    Range(a, b)       -> ["Range", a, b]
    CAVEAT (M5/Phase-1): Element(<untyped symbol>, <these sets>) EVALUATES
    to False in CE -- do not evaluate assumptions over undeclared symbols.
    """
    name = _head_name(expr)
    args = expr.args()
    if name == "ZZGreaterEqual":
        a = args[0]
        if a.is_integer() and a._integer == 0:
            return "NonNegativeIntegers"
        if a.is_integer() and a._integer == 1:
            return "PositiveIntegers"
        ctx.add_head("Range")
        return ["Range", walk(a, ctx), "PositiveInfinity"]
    if name == "ZZLessEqual":
        b = args[0]
        if b.is_integer() and b._integer == 0:
            return "NonPositiveIntegers"
        ctx.add_head("Range")
        return ["Range", "NegativeInfinity", walk(b, ctx)]
    ctx.add_head("Range")
    return ["Range", walk(args[0], ctx), walk(args[1], ctx)]


# ---------------------------------------------------------------------------
# Matrices  [spike #14]
# ---------------------------------------------------------------------------

def translate_matrix2x2(expr, ctx, walk):
    """Matrix2x2(a,b,c,d) -> ["Matrix", ["List",["List",a,b],["List",c,d]]]
    (spike #14; Determinant evaluates, SL2Z membership boxes).
    Matrix2x1(a,b) -> column matrix ["Matrix", ["List",["List",a],["List",b]]].
    Where-destructuring of Matrix2x2 occurs 0 times in the corpus."""
    name = _head_name(expr)
    args = [walk(a, ctx) for a in expr.args()]
    ctx.add_head("Matrix")
    if name == "Matrix2x2":
        return ["Matrix", ["List", ["List", args[0], args[1]],
                           ["List", args[2], args[3]]]]
    return ["Matrix", ["List", ["List", args[0]], ["List", args[1]]]]


def translate_matrix(expr, ctx, walk):
    """Matrix(...): the only corpus occurrences are the generator form
    Matrix(body, For(i, ...), For(j, ...)) -> SKIP ``matrix-generator``
    (CE Matrix has no generator syntax). A literal Matrix(List(...), ...)
    would pass through."""
    if any(_head_name(a) in ("For", "ForElement") for a in expr.args()):
        _skip("matrix-generator", heads=["Matrix"])
    ctx.add_head("Matrix")
    return ["Matrix"] + [walk(a, ctx) for a in expr.args()]


# ---------------------------------------------------------------------------
# Misc small structural forms
# ---------------------------------------------------------------------------

def strip_decorations(expr, ctx, walk):
    """Parentheses/Brackets/Braces/AngleBrackets/Pos: strip, keep child."""
    return walk(expr.args()[0], ctx)


def translate_neg(expr, ctx, walk):
    """Neg(x) -> ["Negate", x]; Neg(Infinity) -> "NegativeInfinity"."""
    arg = expr.args()[0]
    if arg.is_atom() and arg.is_symbol() and arg._symbol == "Infinity":
        return "NegativeInfinity"
    return ["Negate", walk(arg, ctx)]


def translate_inv(expr, ctx, walk):
    """Inv(x) -> ["Divide", 1, x] (CE Inverse is matrix inverse)."""
    return ["Divide", 1, walk(expr.args()[0], ctx)]


def translate_decimal(expr, ctx, walk):
    """Decimal("...") -> {"num": "..."} (lossless, per MathJsonNumberObject)."""
    return {"num": expr.args()[0]._text}


def _comprehension(body, gen, cond, ctx, walk):
    """Translate a comprehension (body, For/ForElement generator, optional
    condition) into its real CE encoding — a filtered/mapped collection:

        {x : x in S}             -> S
        {x : x in S, P(x)}       -> ["Filter", S, ["Function", P, x]]
        {f(x) : x in S}          -> ["Map", ["Function", f, x], S]
        {f(x) : x in S, P(x)}    -> ["Map", ["Function", f, x],
                                     ["Filter", S,
                                      ["Function", P, x]]]

    CE's Map is callback-FIRST (`Map(f, xs)`, the 2026-08-14 argument-order
    repair); Filter stays collection-first.

    Shared by translate_set (set-builder values) and translate_optimum
    (Min/Max/Supremum/Infimum image sets). Fidelity note: Filter/Map
    preserve the source collection's character rather than re-imposing set
    semantics (no dedup of f(x) collisions); membership, emptiness and
    extrema agree with the set-builder reading, which is what the corpus
    exercises."""
    # ["Element", var, S] or ["Element", var, S, cond] (EL-3)
    elt = _indexing_set(gen, cond, ctx, walk)
    var, source = elt[1], elt[2]
    if len(elt) > 3:
        ctx.add_head("Filter")
        source = ["Filter", source, ["Function", elt[3], var]]
    body_tr = walk(body, ctx)
    if body_tr == var:
        return source
    ctx.add_head("Map")
    return ["Map", ["Function", body_tr, var], source]


def translate_set(expr, ctx, walk):
    """Set enumeration passes through; the comprehension form
    Set(body, For/ForElement(...) [, cond]) translates via _comprehension.

    The previous encoding, a literal ["Set", body, indexing-set] (spike
    #12), boxed fine but CE *reads* it as a 2-element literal set —
    Count/Element gave wrong scalars (Stage-2 audit, gcd/4099d2 graded
    False from Count)."""
    args = expr.args()
    if len(args) >= 2 and _head_name(args[1]) in ("For", "ForElement"):
        cond = None
        if len(args) > 2:
            cond = args[2] if len(args) == 3 else _pg().And(*args[2:])
        return _comprehension(args[0], args[1], cond, ctx, walk)
    ctx.add_head("Set")
    return ["Set"] + [walk(a, ctx) for a in args]


def translate_list(expr, ctx, walk):
    """List/Tuple pass through; a generator splice List(z_(k), For(k, ...))
    has no CE representation -> SKIP ``generator-list``."""
    name = "List" if _head_name(expr) == "List" else "Tuple"
    if any(_head_name(a) in ("For", "ForElement") for a in expr.args()):
        _skip("generator-list", heads=[name])
    ctx.add_head(name)
    return [name] + [walk(a, ctx) for a in expr.args()]


def translate_quantifier(expr, ctx, walk):
    """All/Exists -> CE ForAll/Exists (logic.ts, "(value, boolean) ->
    boolean"; first argument is a symbol or an Element expression --
    box-verified in the M1 batch).

    All(p, ForElement(x, S))        -> ["ForAll", ["Element","x",S], p]
    All(p, ForElement(x, S), cond)  -> ["ForAll", ["Element","x",S],
                                        ["Implies", cond, p]]
    Exists(p, gen, cond)            -> ["Exists", ..., ["And", cond, p]]
    All(p, For(x), cond)            -> first argument "x", cond folded.
    For(Tuple(...)) binders         -> SKIP ``tuple-indexing-set``.
    """
    name = _head_name(expr)
    target = "ForAll" if name == "All" else "Exists"
    args = expr.args()
    pred, gen = args[0], args[1]
    cond = None
    if len(args) > 2:
        cond = args[2] if len(args) == 3 else _pg().And(*args[2:])
    gh = _head_name(gen)
    if gh == "ForElement":
        var, S = gen.args()[0], gen.args()[1]
        if not _is_plain_symbol(var):
            _skip("tuple-indexing-set", heads=[name])
        first = ["Element", _sym(var), walk(S, ctx)]
    elif gh == "For" and len(gen.args()) == 1:
        var = gen.args()[0]
        if not _is_plain_symbol(var):
            _skip("tuple-indexing-set", heads=[name])
        first = _sym(var)
    else:
        _skip("tuple-indexing-set" if gh in ("For", "ForElement")
              else "bare-for-generator", heads=[name])
    body = walk(pred, ctx)
    if cond is not None:
        joiner = "Implies" if target == "ForAll" else "And"
        body = [joiner, walk(cond, ctx), body]
    ctx.add_head(target)
    return [target, first, body]


_OPTIMUM_TARGET = {
    "Minimum": "Min", "Maximum": "Max",
    "Supremum": "Supremum", "Infimum": "Infimum",
}


def translate_optimum(expr, ctx, walk):
    """Minimum/Maximum/Supremum/Infimum and ArgMin/ArgMax(+Unique).

    Value-extrema map onto CE Min/Max/Supremum/Infimum ("(value*) ->
    number", collections accepted -- M1 batch verified). Generator forms
    become the image set via _comprehension:
        Minimum(f, ForElement(x, S) [, cond])
          -> ["Min", ["Map", ["Function", f, "x"], S']]
    (S' = S or its Filter; previously a literal ["Set", f, indexing] that
    CE read as a 2-element enumeration — same fiction as translate_set's,
    fixed together; CE keeps extrema over unenumerable collections inert).
    Arg-extrema have no CE equivalent: verbatim shells with a
    Function-literal first argument (binding kept):
        ArgMinUnique(f, ForElement(x, S)) ->
          ["ArgMinUnique", ["Function", f, "x"], S]
    """
    name = _head_name(expr)
    args = expr.args()
    if len(args) == 1:
        if name in _OPTIMUM_TARGET:
            target = _OPTIMUM_TARGET[name]
            ctx.add_head(target)
            return [target, walk(args[0], ctx)]
        ctx.add_shell(name)
        return [name, walk(args[0], ctx)]
    f, gen = args[0], args[1]
    cond = None
    if len(args) > 2:
        cond = args[2] if len(args) == 3 else _pg().And(*args[2:])
    if name in _OPTIMUM_TARGET:
        target = _OPTIMUM_TARGET[name]
        ctx.add_head(target)
        return [target, _comprehension(f, gen, cond, ctx, walk)]
    # ArgMin / ArgMax / ArgMinUnique / ArgMaxUnique
    gh = _head_name(gen)
    if gh != "ForElement" or not _is_plain_symbol(gen.args()[0]):
        _skip("bare-for-generator", heads=[name])
    v = _sym(gen.args()[0])
    ctx.add_shell(name)
    out = [name, ["Function", walk(f, ctx), v], walk(gen.args()[1], ctx)]
    if cond is not None:
        out.append(walk(cond, ctx))
    return out


def translate_fun(expr, ctx, walk):
    """Fun(x, body) -> ["Function", body, "x"] (lambda literal)."""
    params, body = expr.args()[0], expr.args()[1]
    if _head_name(params) == "Tuple":
        names = [_sym(p) for p in params.args()]
    elif _is_plain_symbol(params):
        names = [_sym(params)]
    else:
        _skip("bare-for-generator", heads=["Fun"])
    ctx.add_head("Function")
    return ["Function", walk(body, ctx)] + names


def translate_call(expr, ctx, walk):
    """Call(f, args...): plain call when f translates to a symbol, else
    ["Apply", f, args...] (a non-symbol call head throws in ce.box)."""
    args = expr.args()
    whead = walk(args[0], ctx)
    wargs = [walk(a, ctx) for a in args[1:]]
    if isinstance(whead, str):
        if whead.endswith("_"):
            ctx.indexed_families.add(whead)
        return [whead] + wargs
    ctx.add_head("Apply")
    return ["Apply", whead] + wargs


def translate_item(expr, ctx, walk):
    """Item(t, Tuple(i, j)) -> ["At", t, i, j] (CE At, collections.ts:914)."""
    coll, idx = expr.args()
    ctx.add_head("At")
    if _head_name(idx) == "Tuple":
        return ["At", walk(coll, ctx)] + [walk(a, ctx) for a in idx.args()]
    return ["At", walk(coll, ctx), walk(idx, ctx)]


def translate_equal_and_element(expr, ctx, walk):
    """EqualAndElement(x, y, S) (sugar: x = y and x in S) ->
    ["And", ["Equal", x, y], ["Element", x, S]]."""
    x, y, S = (walk(a, ctx) for a in expr.args())
    return ["And", ["Equal", x, y], ["Element", x, S]]


def translate_optional_derivative_order(expr, ctx, walk):
    """AiryAi/AiryBi(z [, r]) and BesselJ/Y/I/K(nu, z [, r]): the optional
    trailing argument is a derivative order (Fungrim docs). CE's kernels are
    fixed-arity, so the derivative order uses the spike #2 encoding:

        AiryAi(z, r) -> ["Apply", ["Derivative",
                          ["Function", ["AiryAi", z*], z*], r], z]

    (box-verified in the M1 batch; CE evaluation of the AiryAi form hits a
    stack overflow -- CE bug, boxing unaffected)."""
    from . import mapping
    name = _head_name(expr)
    target = mapping.SYMBOL_MAP[name]
    args = expr.args()
    base_arity = 1 if name in ("AiryAi", "AiryBi") else 2
    ctx.add_head(target)
    if len(args) <= base_arity:
        return [target] + [walk(a, ctx) for a in args]
    order = args[base_arity]
    zarg = args[base_arity - 1]
    fixed = [walk(a, ctx) for a in args[:base_arity - 1]]
    if _is_plain_symbol(zarg):
        v = _sym(zarg)
        point = v
    else:
        v = _fresh_var(expr, "z")
        point = walk(zarg, ctx)
    ctx.add_head("Derivative")
    return ["Apply",
            ["Derivative", ["Function", [target] + fixed + [v], v],
             walk(order, ctx)],
            point]


def translate_lambertw(expr, ctx, walk):
    """LambertW(z [, k [, r]]). CE LambertW is natively 2-arg (z, k) with the
    branch index last (SymPy/Fungrim convention).

    - LambertW(z) / LambertW(z, 0) -> ["LambertW", z]
    - LambertW(z, k), k != 0       -> ["LambertW", z, k]  (boxes directly; no
      harness re-declaration needed -- see mapping.py note)
    - LambertW(z, k, r) (r-th derivative) -> spike #2 derivative encoding
      around the branch form.
    """
    args = expr.args()
    ctx.add_head("LambertW")
    z = args[0]
    if len(args) == 1:
        return ["LambertW", walk(z, ctx)]
    k = args[1]
    branch_is_principal = k.is_integer() and k._integer == 0
    if len(args) == 2:
        if branch_is_principal:
            return ["LambertW", walk(z, ctx)]
        return ["LambertW", walk(z, ctx), walk(k, ctx)]
    # 3-arg: derivative of order r with respect to z
    order = walk(args[2], ctx)
    if _is_plain_symbol(z):
        v = _sym(z)
        point = v
    else:
        v = _fresh_var(expr, "z")
        point = walk(z, ctx)
    body = ["LambertW", v] if branch_is_principal \
        else ["LambertW", v, walk(k, ctx)]
    ctx.add_head("Derivative")
    return ["Apply", ["Derivative", ["Function", body, v], order], point]


def translate_digamma(expr, ctx, walk):
    """DigammaFunction(z [, m]): the optional trailing argument is the
    polygamma order (Fungrim docs: DigammaFunction(z, m) "represents the
    order m derivative of the digamma function").

    - DigammaFunction(z) / DigammaFunction(z, 0) -> ["Digamma", z]
    - DigammaFunction(z, m), m != 0 -> ["PolyGamma", m, z]  (CE PolyGamma is
      order-FIRST; semantics verified numerically: PolyGamma(1, 1/4) =
      pi^2 + 8*Catalan, PolyGamma(2, 1) = -2*Zeta(3))
    """
    args = expr.args()
    z = args[0]
    if len(args) == 1:
        ctx.add_head("Digamma")
        return ["Digamma", walk(z, ctx)]
    m = args[1]
    if m.is_integer() and m._integer == 0:
        ctx.add_head("Digamma")
        return ["Digamma", walk(z, ctx)]
    ctx.add_head("PolyGamma")
    return ["PolyGamma", walk(m, ctx), walk(z, ctx)]


def translate_generator_head(expr, ctx, walk):
    """Metadata/generator heads in *expression* position (top-level entries
    are routed to properties.json before the walker runs; nested uses --
    e.g. Cardinality(Zeros(...)), Sum over ComplexZeroMultiplicity -- keep
    the verbatim head with a Function-literal first argument so the binding
    survives):

        Zeros(f, ForElement(z, S) [, cond]) -> ["Zeros", ["Function", f, "z"],
                                                S [, cond]]
        Residue(f, For(z, p))               -> ["Residue", Fn, p]
        AnalyticContinuation(f, For(z,a,b)) -> [head, Fn, a, b]
        Op(f, z, S) positional              -> [head, Fn, S]
    """
    name = _head_name(expr)
    args = expr.args()
    ctx.add_shell(name)
    f = args[0]
    if _head_name(f) == "Brackets":
        f = f.args()[0]
    if len(args) >= 2 and _head_name(args[1]) in ("For", "ForElement"):
        gen = args[1]
        cond = None
        if len(args) > 2:
            cond = args[2] if len(args) == 3 else _pg().And(*args[2:])
        var = gen.args()[0]
        if not _is_plain_symbol(var):
            _skip("tuple-indexing-set", heads=[name])
        v = _sym(var)
        fn = ["Function", walk(f, ctx), v]
        extra = [walk(x, ctx) for x in gen.args()[1:]]
        if cond is not None:
            extra.append(walk(cond, ctx))
        return [name, fn] + extra
    if len(args) == 3 and _is_plain_symbol(args[1]):
        # positional (f, z, S) generator syntax
        v = _sym(args[1])
        return [name, ["Function", walk(f, ctx), v], walk(args[2], ctx)]
    return [name] + [walk(a, ctx) for a in args]


def translate_chain(expr, ctx, walk):
    """Multi-arg relation chains pass through unchanged.  [spike #9]

    CE Equal/Less/LessEqual/Greater/GreaterEqual are n-ary with chain
    semantics (verified: Equal(2,2,3) -> False, Less(1,2,3) -> True). NO
    pairwise-And expansion -- handled by the plain SYMBOL_MAP path in the
    walker; this stub documents the decision."""
    raise AssertionError("chains pass through the SYMBOL_MAP path")


# Heads and atoms that denote a SET in pygrim. `Pow` over one of them is the
# Cartesian power (`Pow(ZZ, 2)` is the lattice of integer pairs, `Pow(Range(1,
# N), n)` the n-tuples drawn from 1..N), not an elementwise power.
_SET_VALUED_ATOMS = {"ZZ", "QQ", "RR", "CC", "PP", "AlgebraicNumbers", "HH"}
_SET_VALUED_HEADS = {
    "ZZGreaterEqual", "ZZLessEqual", "ZZBetween", "Range", "Set",
    "OpenInterval", "ClosedInterval", "OpenClosedInterval",
    "ClosedOpenInterval", "Union", "Intersection", "SetMinus",
    "CartesianProduct", "CartesianPower", "PowerSet",
}


def translate_pow(expr, ctx, walk):
    """Pow(x, y) -> ["Power", x, y], except over a set-valued base:
    Pow(S, n) -> ["CartesianPower", S, n] (a shell head; the Compute Engine
    reads ["Power", S, n] as an ELEMENTWISE power, which silently changes the
    meaning of entries such as gcd 4099d2, `Element(T, Pow(Range(1, N), n))`).
    """
    base, expo = expr.args()
    is_set = (base.is_atom() and base.is_symbol()
              and base._symbol in _SET_VALUED_ATOMS) or (
              _head_name(base) in _SET_VALUED_HEADS)
    if is_set:
        ctx.add_shell("CartesianPower")
        return ["CartesianPower", walk(base, ctx), walk(expo, ctx)]
    ctx.add_head("Power")
    return ["Power", walk(base, ctx), walk(expo, ctx)]
