# -*- coding: utf-8 -*-

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
        elif isinstance(arg, int):
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
        if self is GammaFunction: return "\\Gamma"
        if self is DedekindEta: return "\\eta"
        if self is DedekindEtaEpsilon: return "\\varepsilon"
        if self is DedekindSum: return "s"
        if self is EulerQSeries: return "\\phi"
        if self is PartitionsP: return "p"
        if self is DivisorSigma: return "\\sigma"
        if self is HardyRamanujanA: return "A"
        if self is Sin: return "\\sin"
        if self is Sinh: return "\\sinh"
        if self is Exp: return "\\exp"
        if self is GCD: return "\\gcd"
        if self is ZZ: return "\\mathbb{Z}"
        if self is QQ: return "\\mathbb{Q}"
        if self is RR: return "\\mathbb{R}"
        if self is CC: return "\\mathbb{C}"
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
            if base.is_symbol() or (base.is_integer() and base._integer >= 0) or (not base.is_atom() and base._args[0] is Abs):
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
        if head is And:
            return " \\mathbin{\\operatorname{and}} ".join("\\left(%s\\right)" % s for s in argstr)
        if head is Or:
            return " \\mathbin{\\operatorname{or}} ".join("\\left(%s\\right)" % s for s in argstr)
        if head is Not:
            assert len(args) == 1
            return " \\operatorname{not} \\left(%s\\right)" % argstr[0]
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
        if head is DomainCodomain:
            assert len(args) == 2
            #return "%s \\rightarrow %s" % (argstr[0], argstr[1])
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
Unknown Undefined
Where
Set List Tuple
Union Intersection SetMinus Not And Or
Element NotElement Subset SubsetEqual
ZZ QQ RR CC
ZZGreaterEqual ZZLessEqual ZZBetween
ClosedInterval OpenInterval ClosedOpenInterval OpenClosedInterval
Equal Unequal Greater GreaterEqual Less LessEqual
Pos Neg Add Sub Mul Div Mod Inv Pow
Max Min Sign Abs Floor Ceil Arg Re Im
Sum Product Limit Integral Derivative
AsymptoticTo
Infinity UnsignedInfinity
Sqrt NthRoot Log LogBase Exp
Sin Cos Tan Sec Cot Csc
Asin Acos Atan Asec Acot Acsc
Sinh Cosh Tanh Sech Coth Csch
Asinh Acosh Atanh Asech Acoth Acsch
Sinc LambertW
ConstPi ConstE ConstGamma ConstI
Binomial Factorial GammaFunction LogGamma RisingFactorial
BernoulliB BernoulliPolynomial EulerE EulerPolynomial
RiemannZeta
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



describe(ConstPi, ConstPi, [], RR, "The constant pi (3.141...)")
describe(ConstE, ConstE, [], RR, "The constant e (2.718...)")
describe(ConstGamma, ConstGamma, [], RR, "The constant gamma (0.577...)")
describe(ConstI, ConstI, [], CC, "Imaginary unit")
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

all_entries = []

def make_entry(*args):
    entry = Entry(*args)
    all_entries.append(entry)

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

index_RiemannZeta = ("RiemannZeta", "Riemann zeta function",
    [("L-series", ["da2fdb"]),
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
    Assumptions(And(Element(tau, CC), Greater(Im(tau), 0))))

make_entry(ID("1dc520"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * Product((1 - Exp(2*ConstPi*ConstI*k*tau)), Tuple(k, 1, Infinity)))),
    Variables(tau),
    Assumptions(And(Element(tau, CC), Greater(Im(tau), 0))))

make_entry(ID("9b8c9f"),
    Formula(Equal(DedekindEta(ConstI), GammaFunction(Div(1,4)) / (2 * ConstPi ** Div(3,4)))))

make_entry(ID("204acd"),
    Formula(Equal(DedekindEta(Exp(2*ConstPi*ConstI/3)), Exp(-(ConstPi*ConstI/24)) * (Pow(3,Div(1,8)) * Pow(GammaFunction(Div(1,3)), Div(3,2)) / (2 * ConstPi)))))

make_entry(ID("1bae52"),
    Formula(Equal(DedekindEta(tau+1), Exp(ConstPi*ConstI/12) * DedekindEta(tau))),
    Variables(tau),
    Assumptions(And(Element(tau, CC), Greater(Im(tau), 0))))

make_entry(ID("3b806f"),
    Formula(Equal(DedekindEta(-(1/tau)), (-(ConstI*tau))**Div(1,2) * DedekindEta(tau))),
    Variables(tau),
    Assumptions(And(Element(tau, CC), Greater(Im(tau), 0))))

make_entry(ID("29d9ab"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)) ** 24, (c*tau+d)**12 * DedekindEta(tau)**24)),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, CC), Greater(Im(tau), 0),
        Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1))))

make_entry(ID("9f19c1"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)), DedekindEtaEpsilon(a,b,c,d) * (c*tau+d)**Div(1,2) * DedekindEta(tau))),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, CC), Greater(Im(tau), 0),
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

index_DedekindEta = ("DedekindEta", "Dedekind eta function",
    [("Fourier series (q-series)", ["1dc520","ff587a","2e7fdb","8f10b0"]),
     ("Special values", ["9b8c9f", "204acd"]),
     ("Modular transformations", ["1bae52","3b806f","29d9ab","9f19c1","f04e01","921ef0"]),
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
<title>Fungrim: the Mathematical Functions Grimoire</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.css" integrity="sha384-dbVIfZGuN1Yq7/1Ocstc1lUEm+AT+/rCkibIcC/OmWo5f0EA48Vf8CytHzGrSwbQ" crossorigin="anonymous">
<style type="text/css">
body { margin:0.5em; font-family: roboto; background-color: #fafafa; color: black; }
h1 { text-align:center; color:#256; }
h2, h3 { text-align: center; }
p { line-height:1.5em; }
pre { white-space: pre-wrap; background-color: #ffffff; border: 1px solid #cccccc; padding: 0.5em; margin: 0.1em; }
.entry { border:1px solid #bbb; padding-left:0.4em; padding-right:0.4em; padding-top:0em; padding-bottom:0em; margin-left:0; margin-right:0; margin-bottom:0.5em; background-color: #fff; overflow: hidden; }
.entrysubhead { font-weight: bold; padding-bottom: 0.1em; padding-top: 0.6em; }
table { border-collapse:collapse; }
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
<div style="margin-bottom:2em"><p style="text-align:center">%%TIMESTAMP%%</p></div>
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
            fp.write("""<td>%s</td>""" % katex(codomain.latex(), False))
            fp.write("""<td>%s</td></tr>""" % description)
    fp.write("""</table>""")

class EntryObject:
    def __init__(self, entry):
        self.entry = entry
        self.source = self.entry.str()
        self.symbols = None
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
            write_definitions_table(fp, self.symbols)
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
entries_dict = {entry.id:entry for entry in all_entry_objects}


class Webpage:

    def start(self):
        self.fp = open(self.filepath, "w")
        self.fp.write(html_start)

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

    def start(self):
        Webpage.start(self)
        self.fp.write(index_text)

class EntryPage(Webpage):

    def __init__(self, id):
        self.id = id
        self.filepath = "build/html/entry/%s.html" % self.id

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


count_RiemannZeta = IndexPage(*index_RiemannZeta).write()
count_DedekindEta = IndexPage(*index_DedekindEta).write()
count_PartitionsP = IndexPage(*index_PartitionsP).write()
DefinitionsPage().write()

frontpage = FrontPage()
frontpage.start()
frontpage.entry("9ee8bc")
frontpage.section("Browse by function")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="RiemannZeta.html">Riemann zeta function</a> &nbsp;(%i total entries)</li>""" % count_RiemannZeta)
frontpage.fp.write("""<li><a href="DedekindEta.html">Dedekind eta function</a> &nbsp;(%i total entries)</li>""" % count_DedekindEta)
frontpage.fp.write("""<li><a href="PartitionsP.html">Integer partition function</a> &nbsp;(%i total entries)</li>""" % count_PartitionsP)
frontpage.fp.write("""</ul>""")
frontpage.section("General")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="definitions.html">All symbol definitions</a> &nbsp;(%i total entries)</li>""" % len(described_symbols))
frontpage.fp.write("""</ul>""")
frontpage.end()


try:
    with open("build/katex_cache.pickle", "wb") as fp:
        pickle.dump(katex_cache, fp, protocol=pickle.HIGHEST_PROTOCOL)
except IOError:
    print("Error writing katex_cache")

