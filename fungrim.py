# -*- coding: utf-8 -*-

int_types = (int, type(1<<128))

class Expr(object):

    def __new__(self, arg=None, symbol_name=None):
        if isinstance(arg, Expr):
            return arg
        self = object.__new__(Expr)
        self._symbol = None
        self._integer = None
        self._text = None
        self._args = None
        if symbol_name is not None:
            self._symbol = symbol_name
        elif isinstance(arg, str):
            self._text = arg
        elif isinstance(arg, int_types):
            self._integer = arg
        return self

    def is_atom(self):
        return self._args is None

    def is_symbol(self):
        return self._symbol is not None

    def is_integer(self):
        return self._integer is not None

    def is_text(self):
        return self._text is not None

    def __call__(self, *args):
        v = Expr()
        v._args = (self,) + tuple(Expr(arg) for arg in args)
        return v

    def __pos__(self):
        return Pos(self)
    def __neg__(self):
        return Neg(self)
    def __abs__(self):
        return Abs(self)

    def __add__(self, other):
        return Add(Expr(self), Expr(other))
    def __radd__(self, other):
        return Add(Expr(other), Expr(self))

    def __sub__(self, other):
        return Sub(Expr(self), Expr(other))
    def __rsub__(self, other):
        return Sub(Expr(other), Expr(self))

    def __mul__(self, other):
        return Mul(Expr(self), Expr(other))
    def __rmul__(self, other):
        return Mul(Expr(other), Expr(self))

    def __div__(self, other):
        return Div(Expr(self), Expr(other))
    def __rdiv__(self, other):
        return Div(Expr(other), Expr(self))
    def __truediv__(self, other):
        return Div(Expr(self), Expr(other))
    def __rtruediv__(self, other):
        return Div(Expr(other), Expr(self))

    def __pow__(self, other):
        return Pow(Expr(self), Expr(other))
    def __rpow__(self, other):
        return Pow(Expr(other), Expr(self))

    def str(self, level=0, **kwargs):
        if self._symbol is not None:
            s = str(self._symbol)
        elif self._integer is not None:
            s = str(self._integer)
        elif self._text is not None:
            s = self._text.replace('"', '\\"')
            return '"' + s + '"'
        elif self._args is not None:
            fstr = self._args[0].str(level, **kwargs)
            argstrs = [arg.str(level+1, **kwargs) for arg in self._args[1:]]
            if self._args[0] is Entry:
                s = fstr + "(" + ",\n    ".join(argstrs) + ")"
            else:
                s = fstr + "(" + ", ".join(argstrs) + ")"
        else:
            raise ValueError("no content")
        return s

    def __str__(self):
        return self.str()

    def __repr__(self):
        return self.str()

    def all_symbols(self):
        if self._symbol is not None:
            return [self]
        symbols = []
        if self._args is not None:
            for arg in self._args:
                arg_symbols = arg.all_symbols()
                for s in arg_symbols:
                    if s not in symbols:
                        symbols.append(s)
        return symbols

    # needs work
    def need_parens_in_mul(self):
        if self.is_atom():
            if self.is_integer() and self._integer < 0:
                return True
            return False
        if self._args[0] in (Add, Sub, Neg, Pos):
            return True
        return False

    # needs work
    def show_exponential_as_power(self, allow_div=True):
        if self.is_atom():
            return True
        head = self._args[0]
        if head is Div:
            allow_div = False
        if head not in (Pos, Neg, Add, Sub, Mul, Div):
            return False
        for arg in self._args[1:]:
            if not arg.show_exponential_as_power(allow_div=allow_div):
                return False
        return True

    def latex(self, in_small=False):
        if self is ConstPi: return "\\pi"
        if self is ConstI: return "i"
        if self is ConstE: return "e"
        if self is ConstGamma: return "\\gamma"
        if self is RiemannZeta: return "\\zeta"
        if self is Infinity: return "\\infty"
        if self is UnsignedInfinity: return "{\\tilde \\infty}"
        if self is GammaFunction: return "\\Gamma"
        if self is DigammaFunction: return "\\psi"
        if self is DedekindEta: return "\\eta"
        if self is DedekindEtaEpsilon: return "\\varepsilon"
        if self is DedekindSum: return "s"
        if self is EulerQSeries: return "\\phi"
        if self is PartitionsP: return "p"
        if self is DivisorSigma: return "\\sigma"
        if self is HardyRamanujanA: return "A"
        if self is Sin: return "\\sin"
        if self is Sinh: return "\\sinh"
        if self is Cos: return "\\cos"
        if self is Cosh: return "\\cosh"
        if self is Exp: return "\\exp"
        if self is Log: return "\\log"
        if self is Atan: return "\\operatorname{atan}"
        if self is Acot: return "\\operatorname{acot}"
        if self is GCD: return "\\gcd"
        if self is Sign: return "\\operatorname{sgn}"
        if self is Arg: return "\\arg"
        if self is ZZ: return "\\mathbb{Z}"
        if self is QQ: return "\\mathbb{Q}"
        if self is RR: return "\\mathbb{R}"
        if self is CC: return "\\mathbb{C}"
        if self is HH: return "\\mathbb{H}"
        if self.is_atom():
            if self._symbol is not None:
                if self._symbol in variable_names:
                    if len(self._symbol) == 1:
                        return self._symbol
                    else:
                        return "\\" + self._symbol
                return "\\operatorname{" + self._symbol + "}"
            if self._integer is not None:
                return str(self._integer)
            if self._text is not None:
                return "\\text{``" + str(self._text) + "''}"

        head = self._args[0]
        args = self._args[1:]

        if head is Exp:
            assert len(args) == 1
            if args[0].show_exponential_as_power():
                return Pow(ConstE, args[0]).latex(in_small=in_small)

        if head is Div:
            assert len(args) == 2
            num, den = args
            if in_small:
                numstr = num.latex(in_small=True)
                denstr = den.latex(in_small=True)
                if num.need_parens_in_mul():  # fixme!
                    numstr = "\\left( %s \\right)" % numstr
                if den.need_parens_in_mul():  # fixme!
                    denstr = "\\left( %s \\right)" % denstr
                return numstr + " / " + denstr
            else:
                numstr = num.latex()
                denstr = den.latex()
                return "\\frac{" + numstr + "}{" + denstr + "}"

        argstr = [arg.latex(in_small=in_small) for arg in args]
        if head is Where:
            return argstr[0] + "\; \\text{ where } " + ",\,".join(argstr[1:])
        if head is Pos:
            assert len(args) == 1
            return "+" + argstr[0]
        if head is Neg:
            assert len(args) == 1
            return "-" + argstr[0]
        if head is Add:
            return " + ".join(argstr)
        if head is Sub:
            for i in range(1, len(args)):
                if not args[i].is_atom() and args[i]._args[0] in (Neg, Sub):
                    argstr[i] = "\\left(" + argstr[i] + "\\right)"
            return " - ".join(argstr)
        if head is Mul:
            for i in range(len(args)):
                if args[i].need_parens_in_mul():
                    argstr[i] = "\\left(" + argstr[i] + "\\right)"
            return " ".join(argstr)
        if head is Pow:
            assert len(args) == 2
            # remove frac to try to keep it on one line
            base = args[0]
            expo = args[1]
            basestr = base.latex(in_small=in_small)
            expostr = expo.latex(in_small=True)
            if base.is_symbol() or (base.is_integer() and base._integer >= 0) or (not base.is_atom() and base._args[0] in (Abs, Binomial)):
                return "{" + basestr + "}^{" + expostr + "}"
            else:
                return "{\\left(" + basestr + "\\right)}^{" + expostr + "}"
        if head in (Sum, Integral, Product):
            assert len(args) == 2
            assert args[1]._args[0] is Tuple
            _, var, low, high = args[1]._args
            var = var.latex()
            low = low.latex(in_small=True)
            high = high.latex(in_small=True)
            if head is Sum:
                return "\\sum_{%s=%s}^{%s} %s" % (var, low, high, argstr[0])
            if head is Integral:
                return "\\int_{%s}^{%s} %s \, d%s" % (low, high, argstr[0], var)
            if head is Product:
                return "\\prod_{%s=%s}^{%s} \\left( %s \\right)" % (var, low, high, argstr[0])
        if head is Limit:
            assert len(args) == 3
            formula, var, point = args
            var = var.latex()
            point = point.latex(in_small=True)
            formula = formula.latex()
            return "\\lim_{%s \\to %s} \\left[ %s \\right]" % (var, point, formula)
        if head is Derivative:
            assert len(args) == 2
            assert args[1]._args[0] is Tuple
            _, var, point, order = args[1]._args
            var = var.latex()
            point = point.latex(in_small=True)
            orderstr = order.latex()
            if order.is_integer() and order._integer == 1:
                return "\\left[ \\frac{d}{d %s}\, %s \\right]_{%s = %s}" % (var, argstr[0], var, point)
            else:
                return "\\left[ \\left(\\frac{d}{d %s}\\right)^{%s} %s \\right]_{%s = %s}" % (var, orderstr, argstr[0], var, point)
        if head is Sqrt:
            assert len(args) == 1
            return "\\sqrt{" + argstr[0] + "}"
        if head is Abs:
            assert len(args) == 1
            return "\\left|" + argstr[0] + "\\right|"
        if head is Floor:
            assert len(args) == 1
            return "\\left\\lfloor " + argstr[0] + " \\right\\rfloor"
        if head is Ceil:
            assert len(args) == 1
            return "\\left\\lceil " + argstr[0] + " \\right\\rceil"
        if head is Less:
            return " \\lt ".join(argstr)
        if head is LessEqual:
            return " \\le ".join(argstr)
        if head is Greater:
            return " \\gt ".join(argstr)
        if head is GreaterEqual:
            return " \\ge ".join(argstr)
        if head is Equal:
            return " = ".join(argstr)
        if head is Unequal:
            return " \\ne ".join(argstr)
        if head is Tuple:
            return "\\left(" + ", ".join(argstr) + "\\right)"
        if head is Set:
            return "\\left\{" + ", ".join(argstr) + "\\right\}"
        if head is BernoulliB:
            assert len(args) == 1
            return "B_{" + argstr[0] + "}"
        if head is HarmonicNumber:
            assert len(args) == 1
            return "H_{" + argstr[0] + "}"
        if head is RiemannZetaZero:
            assert len(args) == 1
            return "\\rho_{" + argstr[0] + "}"
        if head is BernoulliPolynomial:
            assert len(args) == 2
            return "B_{" + argstr[0] + "}" + "\\left(" + argstr[1] + "\\right)"
        if head is BesselI:
            assert len(args) == 2
            n, z = args
            nstr = n.latex(in_small=True)
            zstr = z.latex(in_small)
            return "I_{" + nstr + "}" + "\\left(" + zstr + "\\right)"
        if head is Factorial:
            assert len(args) == 1
            if args[0].is_symbol():
                return argstr[0] + " !"
            else:
                return "\\left(" + argstr[0] + "\\right)!"
        if head is RisingFactorial:
            assert len(args) == 2
            return "\\left(" + argstr[0] + "\\right)_{" + argstr[1] + "}"
        if head is Binomial:
            assert len(args) == 2
            return "{" + argstr[0] + " \\choose " + argstr[1] + "}"
        if head is AsymptoticTo:
            assert len(argstr) == 4
            return "%s \\sim %s, \; %s \\to %s" % tuple(argstr)
        if head is Mod:
            return " \\bmod ".join(argstr)
        if head is Element:
            return " \\in ".join(argstr)
        if head is NotElement:
            return " \\not\\in ".join(argstr)
        if head is SetMinus:
            return " \\setminus ".join(argstr)
        if head is Union:
            return " \\cup ".join(argstr)
        if head is Intersection:
            return " \\cap ".join(argstr)
        if head is And:
            return " \\mathbin{\\operatorname{and}} ".join("\\left(%s\\right)" % s for s in argstr)
        if head is Or:
            return " \\mathbin{\\operatorname{or}} ".join("\\left(%s\\right)" % s for s in argstr)
        if head is Not:
            assert len(args) == 1
            return " \\operatorname{not} \\left(%s\\right)" % argstr[0]
        if head is Implies:
            return " \\implies ".join("\\left(%s\\right)" % s for s in argstr)
        if head is KroneckerDelta:
            assert len(args) == 2
            xstr = args[0].latex(in_small=True)
            ystr = args[1].latex(in_small=True)
            return "\delta_{(%s,%s)}" % (xstr, ystr)
        if head is ZZGreaterEqual:
            assert len(args) == 1
            # if args[0].is_integer():
            #    return "\{%s, %s, \ldots\}" % (args[0]._integer, args[0]._integer + 1)
            return "\\mathbb{Z}_{\ge %s}" % argstr[0]
        if head is ZZLessEqual:
            assert len(args) == 1
            if args[0].is_integer():
                return "\{%s, %s, \ldots\}" % (args[0]._integer, args[0]._integer - 1)
            return "\\mathbb{Z}_{\le %s}" % argstr[0]
        if head is ZZBetween:
            assert len(args) == 2
            if args[0].is_integer():
                return "\{%s, %s, \ldots %s\}" % (argstr[0], args[0]._integer + 1, argstr[1])
            else:
                return "\{%s, %s + 1, \ldots %s\}" % (argstr[0], args[0], argstr[1])
        if head is ClosedInterval:
            assert len(args) == 2
            return "\\left[%s, %s\\right]" % (args[0].latex(in_small=True), args[1].latex(in_small=True))
        if head is OpenInterval:
            assert len(args) == 2
            return "\\left(%s, %s\\right)" % (args[0].latex(in_small=True), args[1].latex(in_small=True))
        if head is ClosedOpenInterval:
            assert len(args) == 2
            return "\\left[%s, %s\\right)" % (args[0].latex(in_small=True), args[1].latex(in_small=True))
        if head is OpenClosedInterval:
            assert len(args) == 2
            return "\\left(%s, %s\\right]" % (args[0].latex(in_small=True), args[1].latex(in_small=True))
        if head is RealBall:
            assert len(args) == 2
            return "\\left[%s \\pm %s\\right]" % (args[0].latex(in_small=True), args[1].latex(in_small=True))
        if head is DomainCodomain:
            assert len(args) == 2
            #return "%s \\rightarrow %s" % (argstr[0], argstr[1])
        if head is Conjugate:
            assert len(args) == 1
            return "\\overline{%s}" % argstr[0]
        if head is SetBuilder:
            assert len(args) == 2
            return "\\left\\{ %s : %s \\right\\}" % tuple(argstr)
        if head is Decimal:
            assert len(args) == 1
            text = args[0]._text
            if "e" in text:
                mant, expo = text.split("e")
                expo.lstrip("+")
                text = mant + " \\cdot 10^{" + expo + "}"
            return text
        if head is Parenthesis:
            assert len(args) == 1
            return "\\left(" + args[0].latex() + "\\right)"
        fstr = self._args[0].latex()
        if in_small:
            spacer = ""
        else:
            spacer = "\\!"
        s = fstr + spacer + "\\left(" + ", ".join(argstr) + "\\right)"
        return s


def inject_builtin(string):
    for sym in string.split():
        globals()[sym] = Expr(symbol_name=sym)

variable_names = set()

def inject_vars(string):
    for sym in string.split():
        e = Expr(symbol_name=sym)
        globals()[sym] = e
        variable_names.add(sym)

inject_builtin("""
Parenthesis
Unknown Undefined
Where
Set List Tuple
SetBuilder
Union Intersection SetMinus Not And Or Equivalent Implies
Element NotElement Subset SubsetEqual
ZZ QQ RR CC HH
ZZGreaterEqual ZZLessEqual ZZBetween
ClosedInterval OpenInterval ClosedOpenInterval OpenClosedInterval
RealBall
Decimal
Equal Unequal Greater GreaterEqual Less LessEqual
Pos Neg Add Sub Mul Div Mod Inv Pow
Max Min Sign Abs Floor Ceil Arg Re Im Conjugate
Sum Product Limit Integral Derivative
AsymptoticTo
HolomorphicDomain Poles BranchPoints BranchCuts EssentialSingularities Zeros
Infinity UnsignedInfinity
Sqrt NthRoot Log LogBase Exp
Sin Cos Tan Sec Cot Csc
Asin Acos Atan Asec Acot Acsc
Sinh Cosh Tanh Sech Coth Csch
Asinh Acosh Atanh Asech Acoth Acsch
Sinc LambertW
ConstPi ConstE ConstGamma ConstI
Binomial Factorial GammaFunction LogGamma DigammaFunction RisingFactorial HarmonicNumber
BernoulliB BernoulliPolynomial EulerE EulerPolynomial
RiemannZeta RiemannZetaZero
BesselJ BesselI BesselY BesselK
DedekindEta EulerQSeries DedekindEtaEpsilon DedekindSum
GCD DivisorSigma
PartitionsP HardyRamanujanA
KroneckerDelta
""")

inject_builtin("""
Entry Formula ID Assumptions References Variables DomainCodomain
""")

inject_vars("""a b c d e f g h i j k l m n o p q r s t u v w x y z""")
inject_vars("""A B C D E F G H I J K L M N O P Q R S T U V W X Y Z""")
inject_vars("""alpha beta gamma delta epsilon zeta eta theta iota kappa mu nu xi pi rho sigma tau phi chi psi omega""")
inject_vars("""Alpha Beta Gamma Delta Epsilon Zeta Eta Theta Iota Kappa Mu Nu Xi Pi Rho Sigma Tau Phi Chi Psi Omega""")

described_symbols = []
descriptions = {}

def describe(symbol, example, domain, codomain, description):
    described_symbols.append(symbol)
    descriptions[symbol] = (example, domain, codomain, description)

describe(ZZ, ZZ, [], None, "Integers")
describe(QQ, QQ, [], None, "Rational numbers")
describe(RR, RR, [], None, "Real numbers")
describe(CC, CC, [], None, "Complex numbers")
describe(HH, HH, [], None, "Upper complex half-plane")
describe(ConstPi, ConstPi, [], RR, "The constant pi (3.14...)")
describe(ConstE, ConstE, [], RR, "The constant e (2.718...)")
describe(ConstGamma, ConstGamma, [], RR, "The constant gamma (0.577...)")
describe(ConstI, ConstI, [], CC, "Imaginary unit")
describe(Exp, Exp(z), [Element(z, CC)], CC, "Exponential function")
describe(Log, Log(z), [Element(z, SetMinus(CC, Set(0)))], CC, "Natural logarithm")
describe(RiemannZeta, RiemannZeta(s), [Element(s, SetMinus(CC, Set(1)))], CC, "Riemann zeta function")
describe(GammaFunction, GammaFunction(z), [Element(z, SetMinus(CC, ZZLessEqual(0)))], CC, "Gamma function")
describe(Factorial, Factorial(n), [Element(n, SetMinus(CC, ZZLessEqual(-1)))], CC, "Factorial")
describe(RisingFactorial, RisingFactorial(z, k), [Element(z, CC), Element(k, ZZGreaterEqual(0))], CC, "Rising factorial")
describe(BernoulliB, BernoulliB(n), [Element(n, ZZGreaterEqual(0))], QQ, "Bernoulli number")
describe(BernoulliPolynomial, BernoulliPolynomial(n, z), [Element(n, ZZGreaterEqual(0)), Element(z, CC)], CC, "Bernoulli polynomial")
describe(EulerQSeries, EulerQSeries(q), [Element(q, CC), Less(Abs(q), 1)], CC, "Euler's q-series")
describe(DedekindEta, DedekindEta(tau), [Element(tau, CC), Greater(Im(tau), 0)], CC, "Dedekind eta function")
describe(DedekindEtaEpsilon, DedekindEtaEpsilon(a,b,c,d), [Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ)], CC, "Root of unity in the functional equation of the Dedekind eta function")
describe(DedekindSum, DedekindSum(n,k), [Element(n, ZZ), Element(k, ZZGreaterEqual(1)), Equal(GCD(n,k), 1)], QQ, "Dedekind sum")
describe(GCD, GCD(n,k), [Element(n, ZZ), Element(k, ZZ)], ZZ, "Greatest common divisor")
describe(DivisorSigma, DivisorSigma(n), [Element(n, ZZ)], ZZ, "Sum of divisors function")
describe(PartitionsP, PartitionsP(n), [Element(n, ZZ)], ZZGreaterEqual(0), "Integer partition function")
describe(HardyRamanujanA, A(n,k), [Element(n, ZZ), Element(k, ZZ)], CC, "Exponential sum in the Hardy-Ramanujan-Rademacher formula")
describe(KroneckerDelta, KroneckerDelta(x,y), [Element(x, CC), Element(y, CC)], Set(0, 1), "Kronecker delta")
describe(RiemannZetaZero, RiemannZetaZero(n), [Element(n, SetMinus(ZZ, Set(0)))], CC, "Nontrivial zero of the Riemann zeta function")

all_entries = []

def make_entry(*args):
    entry = Entry(*args)
    all_entries.append(entry)

make_entry(ID("6505a9"),
    Formula(Element(ConstPi,
        RealBall(Decimal("3.1415926535897932384626433832795028841971693993751"), Decimal("5.83e-51")))))

make_entry(ID("0c838a"),
    Formula(NotElement(ConstPi, QQ)))

make_entry(ID("0c9939"),
    Formula(Equal(ConstPi, 4*Atan(1))))

make_entry(ID("f8d280"),
    Formula(Equal(ConstPi, 16*Acot(5) - 4*Acot(239))))

make_entry(ID("590136"),
    Formula(Equal(ConstPi, -(ConstI * Log(-1)))))

make_entry(ID("464961"),
    Formula(Equal(ConstPi, 2 * Integral(Sqrt(1-x**2), Tuple(x, -1, 1)))))

make_entry(ID("04cd99"),
    Formula(Equal(ConstPi, Integral(1/(x**2+1), Tuple(x, -Infinity, Infinity)))))

make_entry(ID("dae4a7"),
    Formula(Equal(ConstPi, Integral(Exp(-x**2), Tuple(x, -Infinity, Infinity))**2)))

make_entry(ID("f617c0"),
    Formula(Equal(ConstPi, 4*Sum((-1)**k / (2*k+1), Tuple(k, 0, Infinity)))))

make_entry(ID("fddfe6"),
    Formula(Equal(ConstPi, Sum((1 / 16**k) * (4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)), Tuple(k, 0, Infinity)))))

make_entry(ID("69fe63"),
    Formula(Equal(ConstPi, 2*Product((4*k**2)/(4*k**2-1), Tuple(k, 1, Infinity)))))

make_entry(ID("e1e106"),
    Formula(Equal(ConstPi, Limit(16**k/(k*Binomial(2*k,k)**2), k, Infinity))))

make_entry(ID("4c0698"),
    Formula(Element(1/ConstPi, RealBall(
        Parenthesis(12*Sum((-1)**k*Factorial(6*k)*(13591409+545140134*k)/(Factorial(3*k)*Factorial(k)**3*640320**(3*k+Div(3,2))),
            Tuple(k, 0, N-1))), Parenthesis(Div(1,151931373056000**N))))),
    Variables(N),
    Assumptions(Element(N, ZZGreaterEqual(0))))

index_ConstPi = ("ConstPi", "The constant pi (3.14...)",
    [
        ("Numerical value", ["6505a9","0c838a"]),
        ("Elementary function representations", ["0c9939","f8d280","590136"]),
        ("Integral representations", ["464961","04cd99","dae4a7"]),
        ("Series representations", ["f617c0","fddfe6"]),
        ("Product representations", ["69fe63"]),
        ("Limit representations", ["e1e106"]),
        ("Approximations", ["4c0698"]),
    ])



make_entry(ID("e876e8"),
    Formula(Element(ConstGamma,
        RealBall(Decimal("0.57721566490153286060651209008240243104215933593992"), Decimal("3.60e-51")))))

make_entry(ID("4644c0"),
    Formula(Equal(ConstGamma, Limit(Sum(1/k, Tuple(k, 1, n)) - Log(n), n, Infinity))))

make_entry(ID("28bf9a"),
    #Formula(Implies(And(Equal(ConstGamma, p/q), Element(p, ZZ), Element(q, ZZGreaterEqual(1))), Greater(q, Pow(10,242080)))))
    Formula(NotElement(ConstGamma, SetBuilder(p/q, And(Element(p,ZZ), Element(q, ZZGreaterEqual(1)), LessEqual(q, Pow(10,242080)))))),
    References("J. Havil (2003): Exploring Euler's Constant. Princeton University Press. Page 97."))

make_entry(ID("a1f1ec"),
    Formula(Equal(ConstGamma, Limit(RiemannZeta(s) - 1/(s-1), s, 1))))

make_entry(ID("cf3977"),
    Formula(Equal(ConstGamma, -Derivative(Gamma(z), Tuple(z, 1, 1)))))

make_entry(ID("d17d0b"),
    Formula(Equal(ConstGamma, -DigammaFunction(1))))

make_entry(ID("818008"),
    Formula(Equal(ConstGamma, 1-Sum((RiemannZeta(k)-1) / k, Tuple(k, 2, Infinity)))))

make_entry(ID("39fe5f"),
    Formula(Equal(ConstGamma, -Integral(Exp(-x)*Log(x), Tuple(x, 0, Infinity)))))

make_entry(ID("a1ca3e"),
    Formula(Equal(ConstGamma, -Integral(Log(Log(1/x)), Tuple(x, 0, 1)))))

make_entry(ID("014c4e"),
#    Formula(Where(Less(Abs(ConstGamma - (S/I - T/I**2 - Log(n))), 24*Exp(-(8*n))),
#        Equal(Tuple(S, I, T), Tuple(Sum(HarmonicNumber(k) * n**(2*k) / Factorial(k)**2, Tuple(k, 0, N - 1)),
#                Sum(n**(2*k) / Factorial(k)**2, Tuple(k, 0, N - 1)),
#                Div(1,4*n) * Sum(Factorial(2*k)**3 / (Factorial(k)**4 * 8**(2*k) * (2*n)**(2*k)), Tuple(k, 0, 2*n-1)))))),
    Formula(Where(Element(ConstGamma, RealBall(Parenthesis(S/I - T/I**2 - Log(n)), 24*Exp(-(8*n)))),
        Equal(Tuple(S, I, T), Tuple(Sum(HarmonicNumber(k) * n**(2*k) / Factorial(k)**2, Tuple(k, 0, N - 1)),
                Sum(n**(2*k) / Factorial(k)**2, Tuple(k, 0, N - 1)),
                Div(1,4*n) * Sum(Factorial(2*k)**3 / (Factorial(k)**4 * 8**(2*k) * (2*n)**(2*k)), Tuple(k, 0, 2*n-1)))))),
    Variables(n, N),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(N, ZZ), GreaterEqual(N, Div(497063,100000)*n + 1))),
    References("R. Brent and F. Johansson. A bound for the error term in the Brent-McMillan algorithm. Mathematics of Computation 2015, 84(295). DOI: 10.1090/S0025-5718-2015-02931-7"))

index_ConstGamma = ("ConstGamma", "The constant gamma (0.577...)",
    [
        ("Numerical value", ["e876e8","28bf9a"]),
        ("Limit representations", ["4644c0"]),
        ("Special function representations", ["a1f1ec","cf3977","d17d0b","818008"]),
        ("Integral representations", ["39fe5f","a1ca3e"]),
        ("Approximations", ["014c4e"]),
    ])

make_entry(ID("27ca8d"),
    Formula(Equal(Exp(0), 1)))

make_entry(ID("9a944c"),
    Formula(Equal(Exp(1), ConstE)))

make_entry(ID("54aaf1"),
    Formula(Equal(Exp(ConstPi*ConstI), -1)))

make_entry(ID("a90f35"),
    Formula(Equal(Exp(ConstPi*ConstI/2), ConstI)))

make_entry(ID("812707"),
    Formula(Equal(Exp(a+b), Exp(a) * Exp(b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("e51ec3"),
    Formula(Equal(Exp(z)**n, Exp(n*z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZ))))

make_entry(ID("2f4f74"),
    Formula(Equal(Exp(-z), 1 / Exp(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("77d6bf"),
    Formula(Equal(Exp(a+b*ConstI), Exp(a) * (Cos(b) + Sin(b)*ConstI))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("97ba8d"),
    Formula(Equal(Exp(z+n*ConstPi*ConstI), (-1)**n * Exp(z)),
    Variables(z, n),
    Assumptions(And(Element(a, CC), Element(n, ZZ)))))

make_entry(ID("1fa6b7"),
    Formula(Equal(Exp(z+2*n*ConstPi*ConstI), Exp(z)),
    Variables(z, n),
    Assumptions(And(Element(a, CC), Element(n, ZZ)))))

make_entry(ID("28d158"),
    Formula(Equal(HolomorphicDomain(Exp(z), z, Union(CC, Set(UnsignedInfinity))), CC)))

make_entry(ID("0901a1"),
    Formula(Equal(Poles(Exp(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("be4b28"),
    Formula(Equal(EssentialSingularities(Exp(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("184c11"),
    Formula(Equal(BranchPoints(Exp(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("b62d05"),
    Formula(Equal(BranchCuts(Exp(z), z, CC), Set())))

make_entry(ID("bceb84"),
    Formula(Equal(Zeros(Exp(z), z, CC), Set())))

make_entry(ID("1635f5"),
    Formula(Equal(Exp(z), Sum(z**k/Factorial(k), Tuple(k, 0, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("bad502"),
    Formula(Equal(Exp(c+z), Exp(c) * Sum(z**k/Factorial(k), Tuple(k, 0, Infinity)))),
    Variables(c, z),
    Assumptions(And(Element(c, CC), Element(z, CC))))

make_entry(ID("935b2f"),
    Formula(Equal(Integral(Exp(z), Tuple(z, a, b)), Exp(b) - Exp(a))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("96af56"),
    Formula(Equal(Derivative(Exp(t), Tuple(t, z, 1)), Exp(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("4491b8"),
    Formula(Equal(Derivative(Exp(t), Tuple(t, z, n)), Exp(z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC)), Element(n, ZZGreaterEqual(0))))


make_entry(ID("1568e1"),
    Formula(Equal(Exp(z), Cosh(z) + Sinh(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e103e7"),
    Formula(Equal(Exp(ConstI*z), Cos(z) + ConstI*Sin(z))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("1b3014"),
    Formula(Equal(Abs(Exp(z)), Exp(Re(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("caf706"),
    Formula(Equal(Sign(Exp(z)), Exp(Im(z)*ConstI))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("b7d62b"),
    Formula(Equal(Re(Exp(z)), Exp(Re(z))*Cos(Im(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e2fac7"),
    Formula(Equal(Im(Exp(z)), Exp(Re(z))*Sin(Im(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("a0d93c"),
    Formula(Equal(Arg(Exp(z)), Im(z))),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(Im(z), OpenClosedInterval(-Pi, Pi)))))

make_entry(ID("52d827"),
    Formula(Equal(Exp(Conjugate(z)), Conjugate(Exp(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

index_Exp = ("Exp", "Exponential function",
    [
        ("Particular values", ["27ca8d","9a944c","54aaf1","a90f35"]),
        ("Functional equations and connection formulas", ["812707","e51ec3","2f4f74","77d6bf","97ba8d","1fa6b7","1568e1", "e103e7"]),
        ("Analytic properties", ["28d158","0901a1","be4b28","184c11","b62d05","bceb84"]),
        ("Complex parts", ["1b3014","caf706","b7d62b","e2fac7","a0d93c","52d827"]),
        ("Taylor series", ["1635f5","bad502"]),
        ("Integrals and derivatives", ["935b2f","96af56","4491b8"]),
    ])

Log_branch_cut = OpenClosedInterval(-Infinity, 0)
Log_holomorphic_domain = SetMinus(CC, Log_branch_cut)

make_entry(ID("07731b"),
    Formula(Equal(Log(1), 0)))

make_entry(ID("699c83"),
    Formula(Equal(Log(ConstE), 1)))

make_entry(ID("c331da"),
    Formula(Equal(Log(ConstI), ConstPi*ConstI/2)))

make_entry(ID("2f1f7b"),
    Formula(Equal(Log(-1), ConstPi*ConstI)))

make_entry(ID("4538ba"),
    Formula(Equal(HolomorphicDomain(Log(z), z, Union(CC, Set(UnsignedInfinity))), Log_holomorphic_domain)))

make_entry(ID("c464e3"),
    Formula(Equal(Poles(Log(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("ddc8a1"),
    Formula(Equal(EssentialSingularities(Log(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("940c48"),
    Formula(Equal(BranchPoints(Log(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity, 0))))

make_entry(ID("b5ded1"),
    Formula(Equal(BranchCuts(Log(z), z, CC), Set(Log_branch_cut))))

make_entry(ID("1d447b"),
    Formula(Equal(Zeros(Log(z), z, CC), Set(1))))

make_entry(ID("13895b"),
    Formula(Equal(Log(Conjugate(z)), Conjugate(Log(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Log_branch_cut))))

make_entry(ID("099b19"),
    Formula(Equal(Re(Log(z)), Log(Abs(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("fbfb81"),
    Formula(Equal(Im(Log(z)), Arg(z))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("dcc1e5"),
    Formula(Equal(Abs(Log(z)), Sqrt(Log(Abs(z))**2 + Arg(z)**2))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("4986ed"),
    Formula(LessEqual(Abs(Log(x)), x-1)),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0,Infinity))))

make_entry(ID("792c76"),
    Formula(LessEqual(Abs(Log(z)), Abs(Log(Abs(z))) + ConstPi)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("d87f6e"),
    Formula(Equal(Exp(Log(z)), z)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("4c1e1e"),
    Formula(Equal(Log(Exp(z)), z)),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(Im(z), OpenClosedInterval(-ConstPi, ConstPi)))))

make_entry(ID("c43533"),
    Formula(Equal(Log(z), Log(Abs(z)) + Arg(z)*ConstI)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("f67fa2"),
    Formula(Equal(Log(c*z), Log(c) + Log(z))),
    Variables(c, z),
    Assumptions(And(Element(c, OpenInterval(0, Infinity)), Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("0ba9b2"),
    Formula(Equal(Log(z), Integral(1/t, Tuple(t, 1, z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Log_branch_cut))))


index_Log = ("Log", "Natural logarithm",
    [
        ("Particular values", ["07731b","699c83","c331da","2f1f7b"]),
        ("Functional equations and connection formulas", ["d87f6e","4c1e1e","c43533","f67fa2"]),
        ("Analytic properties", ["4538ba","c464e3","ddc8a1","940c48","b5ded1","1d447b"]),
        ("Complex parts", ["13895b","099b19","fbfb81","dcc1e5"]),
        ("Bounds and inequalities", ["4986ed","792c76"]),
        ("Integral representations", ["0ba9b2"]),
    ])

GammaFunction_domain = SetMinus(CC, ZZLessEqual(0))
GammaFunction_sub1_domain = SetMinus(CC, ZZLessEqual(1))

make_entry(ID("f1d31a"),
    Formula(Equal(GammaFunction(n), Factorial(n-1))),
    Variables(n),
    Assumptions(Element(n, GammaFunction_domain)))

make_entry(ID("e68d11"),
    Formula(Equal(GammaFunction(1), 1)))

make_entry(ID("19d480"),
    Formula(Equal(GammaFunction(2), 1)))

make_entry(ID("f826a6"),
    Formula(Equal(GammaFunction(Div(1,2)), Sqrt(ConstPi))))

make_entry(ID("48ac55"),
    Formula(Equal(GammaFunction(Div(3,2)), Sqrt(ConstPi)/2)))

make_entry(ID("78f1f4"),
    Formula(Equal(GammaFunction(z+1), z * GammaFunction(z))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_domain)))

make_entry(ID("639d91"),
    Formula(Equal(GammaFunction(z), (z-1) * GammaFunction(z-1))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_sub1_domain)))

make_entry(ID("14af98"),
    Formula(Equal(GammaFunction(z-1), GammaFunction(z) / (z-1))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_sub1_domain)))

make_entry(ID("56d710"),
    Formula(Equal(GammaFunction(z+n), RisingFactorial(z, n) * GammaFunction(z))),
    Variables(z, n),
    Assumptions(And(Element(z, GammaFunction_domain), Element(n, ZZGreaterEqual(0)))))



make_entry(ID("b510b6"),
    Formula(Equal(GammaFunction(z), (ConstPi/Sin(ConstPi*z)) * (1/GammaFunction(1-z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ZZ))))

make_entry(ID("a787eb"),
    Formula(Equal(GammaFunction(z) * GammaFunction(z+Div(1,2)), 2**(1-2*z) * Sqrt(ConstPi) * GammaFunction(2*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(2*z, ZZLessEqual(0)))))

make_entry(ID("90a1e1"),
    Formula(Equal(Product(GammaFunction(z+Div(k,m)), Tuple(k, 0, m-1)), (2*pi)**((m-1)/2) * m**(Div(1,2)-m*z) * Gamma(m*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(m, ZZGreaterEqual(1)), NotElement(m*z, ZZLessEqual(0)))))

make_entry(ID("4e4e0f"),
    Formula(Equal(GammaFunction(z), Integral(t**(z-1) * Exp(-t), Tuple(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("798c5d"),
    Formula(Equal(HolomorphicDomain(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), GammaFunction_domain)))

make_entry(ID("2870f0"),
    Formula(Equal(Poles(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), ZZLessEqual(0))))

make_entry(ID("34d6ae"),
    Formula(Equal(EssentialSingularities(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("d086bd"),
    Formula(Equal(BranchPoints(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("9a44c5"),
    Formula(Equal(BranchCuts(GammaFunction(z), z, CC), Set())))

make_entry(ID("a76328"),
    Formula(Equal(Zeros(GammaFunction(z), z, CC), Set())))

make_entry(ID("d7d2a0"),
    Formula(Equal(GammaFunction(Conjugate(z)), Conjugate(GammaFunction(z)))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_domain)))

index_GammaFunction = ("GammaFunction", "Gamma function",
    [
        ("Particular values", ["f1d31a","e68d11","19d480","f826a6","48ac55"]),
        ("Functional equations", ["78f1f4","639d91","14af98","56d710","b510b6","a787eb","90a1e1"]),
        ("Integral representations", ["4e4e0f"]),
        ("Analytic properties", ["798c5d","2870f0","34d6ae","d086bd","9a44c5","a76328"]),
        ("Complex parts", ["d7d2a0"]),
    ])


make_entry(ID("da2fdb"),
    Formula(Equal(RiemannZeta(s), Sum(1/k**s, Tuple(k, 1, Infinity)))),
    Variables(s),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("a01b6e"),
    Formula(Equal(RiemannZeta(2), ConstPi**2 / 6)))

make_entry(ID("e84983"),
    Formula(NotElement(RiemannZeta(3), QQ)),
    References("R. Apéry (1979), Irrationalité de ζ(2) et ζ(3), Astérisque, 61: 11-13."))

make_entry(ID("72ccda"),
    Formula(Equal(RiemannZeta(2*n), (-1)**(n+1) * BernoulliB(2*n) * (2*ConstPi)**(2*n) / (2 * Factorial(2*n)))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), GreaterEqual(n, 1))))

make_entry(ID("51fd98"),
    Formula(Equal(RiemannZeta(-n), (-1)**n * BernoulliB(n+1) / (n+1))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), GreaterEqual(n, 0))))

make_entry(ID("9ee8bc"),
    Formula(Equal(RiemannZeta(s), 2 * (2*ConstPi)**(s-1) * Sin(ConstPi*s/2) * GammaFunction(1-s) * RiemannZeta(1-s))),
    Variables(s),
    Assumptions(And(Element(s, CC), NotElement(s, ZZGreaterEqual(1)))))

make_entry(ID("809bc0"),
    Formula(LessEqual(Abs(RiemannZeta(s)), RiemannZeta(Re(s)))),
    Variables(s),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("3a5eb6"),
    Formula(Less(Abs(RiemannZeta(s)), 3 * Abs((1+s)/(1-s)) * Abs((1+s)/(2*ConstPi))**((1+eta-Re(s))/2) * RiemannZeta(1+eta))),
    Variables(s, eta),
    Assumptions(
        And(Element(s, CC), Element(eta, RR), Unequal(s, 1), Element(eta, OpenClosedInterval(0, Div(1,2))), LessEqual(-eta, Re(s), 1 + eta))),
    References("H. Rademacher, Topics in analytic number theory, Springer, 1973. Equation 43.3."))

make_entry(ID("792f7b"),
    Formula(Equal(RiemannZeta(s),
        Sum(1/k**s, Tuple(k, 1, N-1)) + N**(1-s)/(s-1) + 1/N**s * (Div(1,2) +
            Sum((BernoulliB(2*k) / Factorial(2*k)) * (RisingFactorial(s, 2*k-1) / N**(2*k-1)), Tuple(k, 1, M))) -
                Integral((BernoulliPolynomial(2*M, t - Floor(t)) / Factorial(2 * M)) * (RisingFactorial(s, 2*M) / t**(s+2*M)), Tuple(t, N, Infinity)))),
    Assumptions(And(Element(s, CC), Unequal(s, 1), Element(N, ZZ), Element(M, ZZ), Greater(Re(s+2*M-1), 0), GreaterEqual(N, 1), GreaterEqual(M, 1))),
    Variables(s, N, M),
    References("""F. Johansson (2015), Rigorous high-precision computation of the Hurwitz zeta function and its derivatives, Numerical Algorithms 69:253, DOI: 10.1007/s11075-014-9893-1""",
        """F. W. J. Olver, Asymptotics and Special Functions, AK Peters, 1997. Chapter 8."""))

make_entry(ID("69348a"),
    Formula(Equal(RiemannZeta(Conjugate(s)), Conjugate(RiemannZeta(s)))),
    Variables(s),
    Assumptions(And(Element(s, CC), Unequal(s, 1))))

make_entry(ID("8b5ddb"),
    Formula(Equal(HolomorphicDomain(RiemannZeta(s), s, Union(CC, Set(UnsignedInfinity))), SetMinus(CC, Set(1)))))

make_entry(ID("52c4ab"),
    Formula(Equal(Poles(RiemannZeta(s), s, Union(CC, Set(UnsignedInfinity))), Set(1))))

make_entry(ID("fdb94b"),
    Formula(Equal(EssentialSingularities(RiemannZeta(s), s, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("36a095"),
    Formula(Equal(BranchPoints(RiemannZeta(s), s, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("9a258f"),
    Formula(Equal(BranchCuts(RiemannZeta(s), s, Union(CC)), Set())))

make_entry(ID("2e1ff3"),
    Formula(Equal(Zeros(RiemannZeta(s), s, RR), SetBuilder(-(2*n), Element(n, ZZGreaterEqual(1))))))

make_entry(ID("692e42"),
    Formula(Equal(Zeros(RiemannZeta(s), s, CC), Union(SetBuilder(-(2*n), Element(n, ZZGreaterEqual(1))),
        SetBuilder(RiemannZetaZero(n), And(Element(n, ZZ), Unequal(n, 0)))))))

make_entry(ID("cbbf16"),
    Formula(Less(0, Re(RiemannZetaZero(n)), 1)),
    Variables(n),
    Assumptions(And(Element(n, ZZ), Unequal(n, 0))))

make_entry(ID("60c2ec"),
    Formula(Equal(RiemannZetaZero(-n), Conjugate(RiemannZetaZero(n)))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), Unequal(n, 0))))

make_entry(ID("e6ff64"),
    Formula(Equal(Re(RiemannZetaZero(n)), Div(1,2))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), Unequal(n, 0), Less(Abs(n), 103800788359))),
    References("""D. J. Platt (2016), Isolating some non-trivial zeros of zeta, Mathematics of Computation 86(307):1, DOI: 10.1090/mcom/3198"""))

index_RiemannZeta = ("RiemannZeta", "Riemann zeta function",
    [("L-series", ["da2fdb"]),
     ("Analytic properties", ["8b5ddb","52c4ab","fdb94b","36a095","9a258f","2e1ff3","692e42","cbbf16","e6ff64","60c2ec"]),
     ("Complex parts", ["69348a"]),
     ("Special values", ["a01b6e","e84983","72ccda","51fd98"]),
     ("Functional equation", ["9ee8bc"]),
     ("Bounds and inequalities", ["809bc0","3a5eb6"]),
     ("Euler-Maclaurin formula", ["792f7b"])])


make_entry(ID("2e7fdb"),
    Formula(Equal(EulerQSeries(q), Product((1 - q**k), Tuple(k, 1, Infinity)))),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("8f10b0"),
    Formula(Equal(EulerQSeries(q), Sum((-1)**k * q**(k*(3*k-1)/2), Tuple(k, -Infinity, Infinity)))),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("ff587a"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * EulerQSeries(Exp(2*ConstPi*ConstI*tau)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("1dc520"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * Product((1 - Exp(2*ConstPi*ConstI*k*tau)), Tuple(k, 1, Infinity)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("9b8c9f"),
    Formula(Equal(DedekindEta(ConstI), GammaFunction(Div(1,4)) / (2 * ConstPi ** Div(3,4)))))

make_entry(ID("204acd"),
    Formula(Equal(DedekindEta(Exp(2*ConstPi*ConstI/3)), Exp(-(ConstPi*ConstI/24)) * (Pow(3,Div(1,8)) * Pow(GammaFunction(Div(1,3)), Div(3,2)) / (2 * ConstPi)))))

make_entry(ID("1bae52"),
    Formula(Equal(DedekindEta(tau+1), Exp(ConstPi*ConstI/12) * DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("acee1a"),
    Formula(Equal(DedekindEta(tau+24), DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("3b806f"),
    Formula(Equal(DedekindEta(-(1/tau)), (-(ConstI*tau))**Div(1,2) * DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("29d9ab"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)) ** 24, (c*tau+d)**12 * DedekindEta(tau)**24)),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH),
        Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1))))

make_entry(ID("9f19c1"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)), DedekindEtaEpsilon(a,b,c,d) * (c*tau+d)**Div(1,2) * DedekindEta(tau))),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH),
        Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1), Or(Greater(c, 0), And(Equal(c, 0), Equal(d, 1))))))

make_entry(ID("f04e01"),
    Formula(Equal(DedekindEtaEpsilon(1,b,0,1), Exp((ConstPi*ConstI*b)/12))),
    Variables(b),
    Element(b, ZZ))

make_entry(ID("921ef0"),
    Formula(Equal(DedekindEtaEpsilon(a,b,c,d), Exp((ConstPi*ConstI*((a+d)/(12*c) - DedekindSum(d,c) - Div(1,4)))))),
    Variables(a,b,c,d),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1), Greater(c, 0))))

make_entry(ID("23961e"),
    Formula(Equal(DedekindSum(n,k), Sum((r/k) * ((n*r/k) - Floor(n*r/k) - Div(1,2)), Tuple(r, 1, k-1)))),
    Variables(n,k),
    Assumptions(And(Element(n, ZZ), Element(k, ZZ), Greater(k, 0), Equal(GCD(n, k), 1))))

make_entry(ID("e06d87"),
    Formula(Equal(HolomorphicDomain(DedekindEta(tau), tau, HH), HH)))

make_entry(ID("04f4a0"),
    Formula(Equal(Poles(DedekindEta(tau), tau, Union(HH, Set(UnsignedInfinity))), Set())))

make_entry(ID("f2e2c2"),
    Formula(Equal(BranchPoints(DedekindEta(tau), tau, Union(HH, Set(UnsignedInfinity))), Set())))

make_entry(ID("6d7668"),
    Formula(Equal(BranchCuts(DedekindEta(tau), tau, HH), Set())))

make_entry(ID("39fb36"),
    Formula(Equal(Zeros(DedekindEta(tau), tau, HH), Set())))

index_DedekindEta = ("DedekindEta", "Dedekind eta function",
    [("Fourier series (q-series)", ["1dc520","ff587a","2e7fdb","8f10b0"]),
     ("Special values", ["9b8c9f", "204acd"]),
     ("Modular transformations", ["1bae52","acee1a","3b806f","29d9ab","9f19c1","f04e01","921ef0"]),
     ("Analytic properties", ["e06d87","04f4a0","f2e2c2","6d7668","39fb36"]),
     ("Dedekind sums", ["23961e"])])

make_entry(ID("cebe1b"),
    Formula(Equal(PartitionsP(0), 1)))

make_entry(ID("e84642"),
    Formula(Equal(PartitionsP(1), 1)))

make_entry(ID("b2583f"),
    Formula(Equal(PartitionsP(10), 42)))

make_entry(ID("7ef291"),
    Formula(Equal(PartitionsP(100), 190569292)))

make_entry(ID("cd3013"),
    Formula(Equal(PartitionsP(n), 0)),
    Variables(n),
    Assumptions(Element(n, ZZLessEqual(-1))))

make_entry(ID("599417"),
    Formula(Equal(Sum(PartitionsP(n) * q**n, Tuple(n, 0, Infinity)),
        1/EulerQSeries(q))),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("acdce8"),
    Formula(Equal(PartitionsP(n), Sum((-1)**(k+1) * (PartitionsP(n - k*(3*k-1)/2) + PartitionsP(n - k*(3*k+1)/2)), Tuple(k, 1, n+1)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("4d2e45"),
    Formula(Equal(PartitionsP(n), Div(1,n) * Sum(DivisorSigma(n-k) * PartitionsP(k), Tuple(k, 0, n-1)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("d8e37d"),
    Formula(Equal(Mod(PartitionsP(5*n+4), 5), 0)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("89260d"),
    Formula(Equal(Mod(PartitionsP(7*n+5), 7), 0)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("dacd74"),
    Formula(Equal(Mod(PartitionsP(11*n+6), 11), 0)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("f7407a"),
    Formula(LessEqual(PartitionsP(n), PartitionsP(n+1))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("df3c07"),
    Formula(Less(PartitionsP(n), PartitionsP(n+1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("d72123"),
    Formula(GreaterEqual(PartitionsP(n), n)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("e1f15b"),
    Formula(LessEqual(PartitionsP(n), 2**n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("7697af"),
    Formula(AsymptoticTo(PartitionsP(n), Exp(ConstPi*Sqrt(2*n/3)) / (4 * n * Sqrt(3)), n, Infinity)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# todo: fix bessel subscript printing
hrr_term = Div(HardyRamanujanA(n,k), k) * BesselI(Div(3,2), (ConstPi/k) * Sqrt(Div(2,3) * (n - Div(1,24))))

make_entry(ID("fb7a63"),
    Formula(Equal(PartitionsP(n), ((2*ConstPi) / Pow(24*n-1, Div(3,4))) * Sum(hrr_term, Tuple(k, 1, Infinity)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("5adbc3"),
    Formula(Equal(HardyRamanujanA(n,k), Sum(KroneckerDelta(GCD(r,k), 1) * Exp(ConstPi*ConstI*(DedekindSum(r,k) - 2*n*r/k)), Tuple(r, 0, k-1)))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(k, ZZGreaterEqual(1)))))

make_entry(ID("afd27a"),
    Formula(LessEqual(Abs(PartitionsP(n) - ((2*ConstPi) / Pow(24*n-1, Div(3,4))) * Sum(hrr_term, Tuple(k, 1, N))),
        (44*ConstPi**2/(225*Sqrt(3*N))) + (ConstPi * Sqrt(2) / 75) * Sqrt(N / (n - 1)) * Sinh((ConstPi/N) * Sqrt(2*n/3)))),
    Variables(n, N),
    Assumptions(And(Element(n, ZZGreaterEqual(2)), Element(N, ZZGreaterEqual(1)))))

index_PartitionsP = ("PartitionsP", "Integer partition function",
    [("Specific values", ["cebe1b","e84642","b2583f","7ef291","cd3013"]),
     ("Generating functions", ["599417"]),
     ("Sums and recurrence relations", ["acdce8","4d2e45"]),
     ("Congruences", ["d8e37d","89260d","dacd74"]),
     ("Inequalities", ["f7407a","df3c07","d72123","e1f15b"]),
     ("Asymptotic expansions", ["7697af"]),
     ("Hardy-Ramanujan-Rademacher formula", ["fb7a63", "5adbc3", "afd27a"])])

import os
if not os.path.exists("build"):
    os.makedirs("build")
if not os.path.exists("build/html"):
    os.makedirs("build/html")
if not os.path.exists("build/html/entry"):
    os.makedirs("build/html/entry")

import pickle
katex_cache = {}

import subprocess

try:
    with open("build/katex_cache.pickle", "rb") as fp:
        katex_cache = pickle.load(fp)
except UnicodeDecodeError as e:
    with open("build/katex_cache.pickle", "rb") as fp:
        katex_cache = pickle.load(fp, encoding="latin1")
except IOError:
    print("Unable to read katex_cache")

def katex(string, display=True):
    if (string, display) in katex_cache:
        return katex_cache[(string, display)]
    s = subprocess.check_output(["node", "katex.js",
                                 {True:"display",False:"inline"}[display], string],
                                universal_newlines=True)
    katex_cache[(string, display)] = s
    return s

import datetime
datestamp = str(datetime.date.today())
timestamp = str(datetime.datetime.now())

html_start = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>%%PAGETITLE%%</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.css" integrity="sha384-dbVIfZGuN1Yq7/1Ocstc1lUEm+AT+/rCkibIcC/OmWo5f0EA48Vf8CytHzGrSwbQ" crossorigin="anonymous">
<style type="text/css">
body { margin:0.5em; font-family: roboto; background-color: #fafafa; color: black; }
h1 { text-align:center; color:#256; }
h2, h3 { text-align: center; }
p { line-height:1.5em; }
pre { white-space: pre-wrap; background-color: #ffffff; border: 1px solid #cccccc; padding: 0.5em; margin: 0.1em; }
.entry { border:1px solid #bbb; padding-left:0.4em; padding-right:0.4em; padding-top:0em; padding-bottom:0em; margin-left:0; margin-right:0; margin-bottom:0.5em; background-color: #fff; overflow: hidden; }
.entrysubhead { font-weight: bold; padding-bottom: 0.1em; padding-top: 0.6em; }
table { border-collapse:collapse; background-color:#fff; }
table, th, td { border: 1px solid #aaa; }
th, td { padding:0.2em; }
</style>
<script type='text/javascript'>
function toggleVisible(id) {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 
</script>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> 
</head>
<body>
"""

html_end = """
<div style="margin:2em">
<p style="text-align:center">Copyright (C) <a href="http://fredrikj.net">Fredrik Johansson</a> and <a href="https://github.com/fredrik-johansson/fungrim/graphs/contributors">contributors</a>.
Fungrim is provided under the
<a href="https://github.com/fredrik-johansson/fungrim/blob/master/LICENSE">MIT license</a>.
The <a href="https://github.com/fredrik-johansson/fungrim">source code is on GitHub</a>.
</p></div>
<p style="text-align:center">%%TIMESTAMP%%</p></div>
</body>
</html>
"""

html_end = html_end.replace("%%TIMESTAMP%%", timestamp)

index_text = """
<h1>The Mathematical Functions Grimoire</h1>

<p style="text-align:center; color:red"><b>Pre-alpha version</b></p>

<p style="margin:1em">Welcome! The Mathematical Functions Grimoire (<i>Fungrim</i>) is an open source library of formulas for mathematical functions. The data is fully symbolic (designed for use by computer algebra software) and the whole library can be browsed online, with a permanent ID and URL for each entry. There are currently %%NUMTOTAL%% entries in Fungrim; see one example below. Click "Details" to show an expanded view of an entry, or click the ID to show the expanded view on its own page. You can <a href="https://github.com/fredrik-johansson/fungrim">contribute on GitHub</a>.
</p>
"""

index_text = index_text.replace("%%NUMTOTAL%%", str(len(all_entries)))

def makeurl(id):
    return "fungrim/entry/%s" % id

def write_definitions_table(fp, symbols, center=False):
    if center:
        fp.write("""<table style="margin: 0 auto">""")
    else:
        fp.write("""<table>""")
    fp.write("""<tr><th>Fungrim symbol</th> <th>Notation</th> <th>Domain</th> <th>Codomain</th> <th>Description</th></tr>""")
    for symbol in symbols:
        if symbol in descriptions:
            example, domain, codomain, description = descriptions[symbol]
            fp.write("""<tr><td><tt>%s</tt>""" % symbol.str())
            fp.write("""<td>%s</td>""" % katex(example.latex(), False))
            domstr = ",\, ".join(dom.latex() for dom in domain)
            fp.write("""<td>%s</td>""" % katex(domstr, False))
            if codomain is None:
                fp.write("""<td></td>""")
            else:
                fp.write("""<td>%s</td>""" % katex(codomain.latex(), False))
            fp.write("""<td>%s</td></tr>""" % description)
    fp.write("""</table>""")

class EntryObject:
    def __init__(self, entry):
        self.entry = entry
        self.source = self.entry.str()
        self.symbols = []
        self.formula = None
        self.assumptions = None
        self.variables = None
        self.references = None
        for arg in entry._args[1:]:
            if arg._args[0] is ID:
                self.id = arg._args[1]._text
            if arg._args[0] is Formula:
                self.formula = arg._args[1]
            if arg._args[0] is Assumptions:
                self.assumptions = arg._args[1]
            if arg._args[0] is Variables:
                self.variables = arg._args[1]
            if arg._args[0] is References:
                self.references = arg._args[1:]
        if self.formula is not None:
            self.formula_tex = self.formula.latex()
            self.symbols = self.formula.all_symbols()
        if self.assumptions is not None:
            self.assumptions_tex = self.assumptions.latex()
            self.symbols += [s for s in self.assumptions.all_symbols() if s not in self.symbols]

    def write_html(self, fp, single=False):
        fp.write("""<div class="entry">""")
        if single:
            fp.write("""<div>""")
            fp.write(katex(self.formula_tex))
            fp.write("""</div>""")
        else:
            fp.write("""<div style="float:left; margin-top:0.5em;">""")
            fp.write("""<a href="entry/%s.html" style="margin-left:3pt">%s</a><br/>""" % (self.id, self.id))
            fp.write("""<button style="margin-top:0.5em; margin-bottom: 0.5em;" onclick="toggleVisible('%s:info')">Details</button>""" % self.id)
            fp.write("""</div>""")
            fp.write("""<div style="margin-left:50pt">""")
            fp.write(katex(self.formula_tex))
            fp.write("""</div>""")
        if single:
            fp.write('<div id="%s:info" style="padding: 1em; clear:both">' % self.id)
        else:
            fp.write('<div id="%s:info" style="display:none; padding: 1em; clear:both">' % self.id)
        if self.assumptions is not None:
            fp.write("""<div class="entrysubhead">Assumptions:</div>""")
            fp.write(katex(self.assumptions_tex))
        fp.write("""<div class="entrysubhead">TeX:</div>""")
        fp.write("<pre>")
        fp.write(self.formula_tex)
        if self.assumptions is not None:
            fp.write("\n\n")
            fp.write(self.assumptions_tex)
        fp.write("</pre>")
        if self.symbols:
            fp.write("""<div class="entrysubhead">Definitions:</div>""")
            write_definitions_table(fp, self.symbols, center=True)
        if self.references is not None:
            fp.write("""<div class="entrysubhead">References:</div>""")
            fp.write("<ul>")
            for ref in self.references:
                fp.write("<li>%s</li>" % ref._text)
            fp.write("</ul>")
        fp.write("""<div class="entrysubhead">Source code for this entry:</div>""")
        fp.write("<pre>")
        fp.write(self.source)
        fp.write("</pre>")
        fp.write("</div>")
        fp.write("</div>\n")

all_entry_objects = [EntryObject(entry) for entry in all_entries]
entries_dict = {}
for entry in all_entry_objects:
    if entry.id in entries_dict:
        raise ValueError("duplicated ID %s" % entry.id)
    entries_dict[entry.id] = entry

class Webpage:

    def start(self):
        self.fp = open(self.filepath, "w")
        self.fp.write(html_start.replace("%%PAGETITLE%%", self.title))

    def entry(self, id):
        entries_dict[id].write_html(self.fp, single=False)

    def section(self, title):
        self.fp.write("""<h2>%s</h2>""" % title)

    def end(self):
        self.fp.write(html_end)
        self.fp.close()

class FrontPage(Webpage):

    def __init__(self):
        self.filepath = "build/html/index.html"
        self.title = "Fungrim: the Mathematical Functions Grimoire"

    def start(self):
        Webpage.start(self)
        self.fp.write(index_text)

class EntryPage(Webpage):

    def __init__(self, id):
        self.id = id
        self.filepath = "build/html/entry/%s.html" % self.id
        self.title = "Entry %s"

    def entry(self, id):
        entries_dict[id].write_html(self.fp, single=True)

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center"><a href="../index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>Fungrim entry: %s</h1>""" % self.id)

    def write(self):
        self.start()
        self.entry(self.id)
        self.end()

class IndexPage(Webpage):

    def __init__(self, url, title, sections_ids):
        self.filepath = "build/html/%s.html" % url
        self.title = title
        self.sections_ids = sections_ids

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center"><a href="index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>%s</h1>""" % self.title)

    def write(self):
        count = 0
        self.start()
        for sect, ids in self.sections_ids:
            self.section(sect)
            for id in ids:
                self.entry(id)
                count += 1
        self.end()
        return count

class DefinitionsPage(Webpage):

    def __init__(self):
        self.filepath = "build/html/definitions.html"
        self.title = "All symbol definitions"
        self.pagetitle = "All symbol definitions"

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center"><a href="index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>%s</h1>""" % self.title)

    def write(self):
        self.start()
        write_definitions_table(self.fp, described_symbols, center=True)
        self.end()

for entry in all_entry_objects:
    EntryPage(entry.id).write()


count_ConstPi = IndexPage(*index_ConstPi).write()
count_ConstGamma = IndexPage(*index_ConstGamma).write()
count_Exp = IndexPage(*index_Exp).write()
count_Log = IndexPage(*index_Log).write()
count_GammaFunction = IndexPage(*index_GammaFunction).write()
count_RiemannZeta = IndexPage(*index_RiemannZeta).write()
count_DedekindEta = IndexPage(*index_DedekindEta).write()
count_PartitionsP = IndexPage(*index_PartitionsP).write()
DefinitionsPage().write()

frontpage = FrontPage()
frontpage.start()
frontpage.entry("9ee8bc")
frontpage.section("Browse by function")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="ConstPi.html">The constant pi (3.14...)</a> &nbsp;(%i total entries)</li>""" % count_ConstPi)
frontpage.fp.write("""<li><a href="ConstGamma.html">The constant gamma (0.577...)</a> &nbsp;(%i total entries)</li>""" % count_ConstGamma)
frontpage.fp.write("""<li><a href="Exp.html">Exponential function</a> &nbsp;(%i total entries)</li>""" % count_Exp)
frontpage.fp.write("""<li><a href="Log.html">Natural logarithm</a> &nbsp;(%i total entries)</li>""" % count_Log)
frontpage.fp.write("""<li><a href="GammaFunction.html">Gamma function</a> &nbsp;(%i total entries)</li>""" % count_GammaFunction)
frontpage.fp.write("""<li><a href="RiemannZeta.html">Riemann zeta function</a> &nbsp;(%i total entries)</li>""" % count_RiemannZeta)
frontpage.fp.write("""<li><a href="DedekindEta.html">Dedekind eta function</a> &nbsp;(%i total entries)</li>""" % count_DedekindEta)
frontpage.fp.write("""<li><a href="PartitionsP.html">Integer partition function</a> &nbsp;(%i total entries)</li>""" % count_PartitionsP)
frontpage.fp.write("""</ul>""")
frontpage.section("General")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="definitions.html">All symbol definitions</a> &nbsp;(%i total entries)</li>""" % len(described_symbols))
frontpage.fp.write("""</ul>""")
frontpage.end()

print("The grimoire was built successfully!")

try:
    with open("build/katex_cache.pickle", "wb") as fp:
        pickle.dump(katex_cache, fp, protocol=pickle.HIGHEST_PROTOCOL)
except IOError:
    print("Error writing katex_cache")

