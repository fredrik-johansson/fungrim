from .expr import *

# operators that may introduce bound variables, complicating symbol substitution
dangerous_operators = set([
    Where,
    SetBuilder,
    ForAll, Exists,
    Minimum, Maximum, ArgMin, ArgMax, ArgMinUnique, ArgMaxUnique,
    Solutions, UniqueSolution,
    Supremum, Infimum,
    Limit, SequenceLimit, RealLimit, LeftLimit, RightLimit, ComplexLimit, MeromorphicLimit,
    SequenceLimitInferior, SequenceLimitSuperior,
    Derivative, RealDerivative, ComplexDerivative, ComplexBranchDerivative, MeromorphicDerivative,
    Sum, Product,
    PrimeSum, DivisorSum, PrimeProduct, DivisorProduct,
    Integral,
    IndefiniteIntegralEqual, RealIndefiniteIntegralEqual, ComplexIndefiniteIntegralEqual,
    AsymptoticTo,
    FormalGenerator,
    FormalPowerSeries, FormalLaurentSeries, SeriesCoefficient,
    HolomorphicDomain, Poles, BranchPoints, BranchCuts, EssentialSingularities, Zeros, UniqueZero, AnalyticContinuation,
    ComplexZeroMultiplicity,
    Residue,
    QSeriesCoefficient, EqualQSeriesEllipsis])

def substitute(expr, dictionary):
    if expr in dictionary:
        v = dictionary[expr]
        assert isinstance(v, Expr)
        return v
    if expr.is_atom():
        return expr
    head = expr.head()
    args = expr.args()
    return Expr(call=[head]+[substitute(arg, dictionary) for arg in args])

def substitute(expr, dictionary):
    if expr in dictionary:
        v = dictionary[expr]
        assert isinstance(v, Expr)
        return v
    if expr.is_atom():
        return expr
    head = expr.head()
    args = expr.args()
    return Expr(call=[head]+[substitute(arg, dictionary) for arg in args])

function_arb_method_table = {
    Exp : "exp",
    Sqrt : "sqrt",
    Log : "log",
    Sin : "sin",
    Cos : "cos",
    Tan : "tan",
    Sinh : "sinh",
    Cosh : "cosh",
    Tanh : "tanh",
    Atan : "atan",
    LogGamma : "lgamma",
    DigammaFunction : "digamma",
    GammaFunction : "gamma",
    RiemannZeta : "zeta",
    Erf : "erf",
    Erfc : "erfc",
    Erfi : "erfi",
    AiryAi : "airy_ai",
    AiryBi : "airy_bi",
}

function_acb_method_table = {
    DedekindEta : "modular_eta",
    ModularJ : "modular_j",
    ModularLambda : "modular_eta",
}

class ArbFiniteError(ValueError):
    pass

def arb_as_fungrim(x, d):
    import flint
    if not x.is_finite():
        raise ValueError
    if isinstance(x, flint.arb):
        if x.is_zero():
            return RealBall(0, 0)
        s = x.str(d)
        if "+/-" in s:
            mid, rad = s[1:-1].split("+/-")
            mid = mid.strip()
            rad = rad.strip()
            if mid == "":
                return RealBall(0, Decimal(rad))
            return RealBall(Decimal(mid), Decimal(rad))
        else:
            return RealBall(Decimal(s), 0)
    if isinstance(x, flint.acb):
        re = x.real
        im = x.imag
        if im.is_zero():
            return arb_as_fungrim(re, d)
        if re.is_zero():
            return arb_as_fungrim(im, d) * ConstI
        return arb_as_fungrim(re, d) + arb_as_fungrim(im, d) * ConstI
    raise TypeError


class ArbNumericalEvaluation(object):

    def __init__(self, cache=None):
        import flint
        self.flint = flint
        self.cache = cache

    def eval(self, expr, **kwargs):
        # todo: don't re-evaluate non-numerical expressions
        stack = kwargs.get("symbol_stack")

        if self.cache is not None and stack is None:
            wp = kwargs["wp"]
            if expr in self.cache:
                cached_wp, v = self.cache[expr]
                if cached_wp >= wp:
                    return +v

        v = self.eval_inner(expr, **kwargs)

        if self.cache is not None and stack is None:
            wp = kwargs["wp"]
            self.cache[expr] = (wp, v)

        return v

    def eval_inner(self, expr, **kwargs):

        arb = self.flint.arb
        acb = self.flint.acb

        if expr.is_atom():
            if expr.is_integer():
                return arb(expr._integer)
            if expr.is_symbol():
                if expr == ConstPi:
                    return arb.pi()
                if expr == ConstE:
                    return arb.const_e()
                if expr == ConstGamma:
                    return arb.const_euler()
                if expr == ConstI:
                    return acb(0,1)
                if expr == GoldenRatio:
                    return (1+arb(5).sqrt())/2
                if expr == ConstCatalan:
                    return arb.const_catalan()
                stack = kwargs.get("symbol_stack")
                if stack is not None:
                    for (sym, val) in reversed(stack):
                        if sym == expr:
                            return val
            raise NotImplementedError

        head = expr.head()
        args = expr.args()

        if head is Mul:
            if len(args) == 0:
                return arb(1)
            x = self.eval(args[0], **kwargs)
            for y in args[1:]:
                y = self.eval(y, **kwargs)
                x *= y
            return x

        if head is Add:
            if len(args) == 0:
                return arb(0)
            x = self.eval(args[0], **kwargs)
            for y in args[1:]:
                y = self.eval(y, **kwargs)
                x += y
            return x

        if head is Neg:
            assert len(args) == 1
            x = self.eval(args[0], **kwargs)
            return (-x)

        if head is Sub:
            assert len(args) == 2
            x = self.eval(args[0], **kwargs)
            y = self.eval(args[1], **kwargs)
            return x - y

        if head is Div:
            assert len(args) == 2
            x = self.eval(args[0], **kwargs)
            y = self.eval(args[1], **kwargs)
            if y != 0:
                return x / y
            raise ArbFiniteError

        if head is Pow:
            assert len(args) == 2
            x = self.eval(args[0], **kwargs)
            y = self.eval(args[1], **kwargs)
            v = x ** y
            if v.is_finite():
                return v
            else:
                if isinstance(x, arb) and isinstance(y, arb):
                    v = acb(x) ** acb(y)
                    if v.is_finite():
                        return v
            raise ArbFiniteError

        if head is Abs:
            assert len(args) == 1
            x = self.eval(args[0], **kwargs)
            return abs(x)

        if head is Re:
            assert len(args) == 1
            v = self.eval(args[0], **kwargs)
            if v.is_finite():
                if isinstance(v, arb):
                    return v
                else:
                    return v.real
            raise ArbFiniteError

        if head is Im:
            assert len(args) == 1
            v = self.eval(args[0], **kwargs)
            if v.is_finite():
                if isinstance(v, arb):
                    return arb(0)
                else:
                    return v.imag
            raise ArbFiniteError

        if head in (Parentheses, Brackets, Braces):
            assert len(args) == 1
            return self.eval(args[0], **kwargs)

        if head in function_arb_method_table:
            method = function_arb_method_table[head]
            assert len(args) == 1
            x = self.eval(args[0], **kwargs)
            v = getattr(x, method)()
            if v.is_finite():
                return v
            # possible complex extension
            if isinstance(x, arb):
                x = acb(x)
                v = getattr(x, method)()
                if v.is_finite():
                    return v
            raise ArbFiniteError

        if head in function_acb_method_table:
            method = function_acb_method_table[head]
            assert len(args) == 1
            x = self.eval(args[0], **kwargs)
            v = getattr(x, method)()
            if v.is_finite():
                return v
            x = acb(x)
            v = getattr(x, method)()
            if v.is_finite():
                return v
            raise ArbFiniteError

        if head in (Hypergeometric1F1, Hypergeometric1F1Regularized):
            assert len(args) == 3
            a, b, z = [self.eval(arg, **kwargs) for arg in args]
            z = acb(z)
            v = z.hypgeom_1f1(a, b, regularized=(head == Hypergeometric1F1Regularized))
            if v.is_finite():
                return v
            raise ArbFiniteError

        if head in (Hypergeometric2F1, Hypergeometric2F1Regularized):
            assert len(args) == 4
            a, b, c, z = [self.eval(arg, **kwargs) for arg in args]
            z = acb(z)
            v = z.hypgeom_2f1(a, b, c, regularized=(head == Hypergeometric2F1Regularized))
            if v.is_finite():
                return v
            raise ArbFiniteError

        if head is JacobiTheta:
            if len(args) == 3:
                j, z, tau = args
                r = 0
            else:
                j, z, tau, r = args
                if not (r.is_integer() and r._integer >= 0):
                    raise ValueError
                r = r._integer
            if not (j.is_integer() and j._integer in (1,2,3,4)):
                raise ValueError
            j = j._integer
            z = self.eval(z, **kwargs)
            tau = self.eval(tau, **kwargs)
            z = acb(z)
            v = z.modular_theta(tau, r)[j-1]
            if v.is_finite():
                return v
            raise ArbFiniteError

        if head is Decimal:
            assert len(args) == 1
            x = arb(args[0]._text)
            return x

        if head is DirichletCharacter:
            if len(args) == 3:
                q, l, n = args
                if q.is_integer() and l.is_integer() and n.is_integer():
                    q = q._integer
                    l = l._integer
                    n = n._integer
                    try:
                        chi = self.flint.dirichlet_char(q, l)
                        return chi(n)
                    except (AssertionError, ValueError):
                        pass

        if head is DirichletL:
            if len(args) == 2:
                s, chi = args
                if chi.head() == DirichletCharacter and len(chi.args()) == 2:
                    q, l = chi.args()
                    if q.is_integer() and l.is_integer():
                        chi = self.flint.dirichlet_char(q._integer, l._integer)
                        s = self.eval(s, **kwargs)
                        v = chi.l(s)
                        if v.is_finite():
                            return v
                        raise ArbFiniteError

        if head is LambertW:
            if len(args) == 2:
                k, x = args
                if k.is_integer():
                    k = k._integer
                    x = self.eval(x, **kwargs)
                    x = acb(x) 
                    v = x.lambertw(k)
                    if v.is_finite():
                        return v
                    raise ArbFiniteError

        if head is Where:
            symbol_stack = kwargs.get("symbol_stack", [])[:]
            nv = len(args) - 1
            assert nv >= 0
            for arg in args[1:]:
                if arg.head() == Equal and len(arg.args()) == 2:
                    var = arg.args()[0]
                    if var.is_symbol():
                        val = arg.args()[1]
                        val = self.eval(val, **kwargs)
                        symbol_stack += [(var, val)]
                        kwargs["symbol_stack"] = symbol_stack
                    else:
                        raise NotImplementedError
            v = self.eval(args[0], **kwargs)
            # note: **kwargs is a new copy, so we don't have to restore the stack
            return v

        # todo: delete
        if kwargs.get("full_traversal"):
            for arg in expr.args():
                try:
                    self.eval(arg, **kwargs)
                except (NotImplementedError, ValueError, ArbFiniteError):
                    continue

        raise ValueError

def neval(expr, digits=20, **kwargs):
    from flint import ctx, acb
    assert digits >= 1
    orig = ctx.prec
    target = digits * 3.33 + 5
    wp = digits * 3.33 + 30
    maxprec = wp * 10 + 4000
    evaluator = ArbNumericalEvaluation()
    try:
        while 1:
            ctx.prec = wp
            try:
                v = evaluator.eval(expr)
            except ArbFiniteError:
                v = acb("nan")
            if v.rel_accuracy_bits() >= target:
                break
            wp *= 2
            if wp > maxprec:
                #raise ValueError("failed to converge")
                break
    finally:
        ctx.prec = orig
    if not v.is_finite():
        raise ValueError("failed to converge to a finite value")
    if isinstance(v, acb) and v.imag == 0:
        v = v.real
    return arb_as_fungrim(v, digits)
    # return v

def subexpressions(expr):
    if not expr.is_atom():
        for arg in expr.args():
            for v in subexpressions(arg):
                yield v
    yield expr

