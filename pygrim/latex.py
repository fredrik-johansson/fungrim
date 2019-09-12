# -*- coding: utf-8 -*-

from .expr import *

latex_cache = {}

def latex(expr, in_small=False):
    if (expr, in_small) in latex_cache:
        return latex_cache[(expr, in_small)]
    else:
        tex = _latex(expr, in_small=in_small)
        latex_cache[(expr, in_small)] = tex
        return tex

def _latex(expr, in_small=False):

    if expr in symbol_latex_table:
        return symbol_latex_table[expr]

    if expr.is_atom():
        if expr._symbol is not None:
            if expr._symbol in variable_names:
                if len(expr._symbol) == 1:
                    return expr._symbol
                else:
                    if expr._symbol == "epsilon":
                        return "\\varepsilon"
                    return "\\" + expr._symbol
            return "\\operatorname{" + expr._symbol + "}"
        if expr._integer is not None:
            return str(expr._integer)
        if expr._text is not None:
            return "\\text{``" + str(expr._text).replace("_","\\_") + "''}"
        raise NotImplementedError

    head = expr._args[0]
    args = expr._args[1:]

    if head in infix_latex_table:
        argstr = [latex(arg, in_small=in_small) for arg in args]
        return (" " + infix_latex_table[head] + " ").join(argstr)

    # F(n,x,...) -> F_n(x,...)
    if head in subscript_call_latex_table:
        arg0 = latex(args[0], in_small=True)
        args1 = ", ".join(latex(arg, in_small=in_small) for arg in args[1:])
        return subscript_call_latex_table[head] + "_{" + arg0 + "}" + "\!\\left(" + args1 + "\\right)"

    if head in latex_conversion_functions:
        return latex_conversion_functions[head](head, args, in_small=in_small)

    if head in subscript_latex_table:
        assert len(args) == 1
        return subscript_latex_table[head] + "_{" + latex(args[0], in_small=True) + "}"

    if head in subscript_pair_latex_table:
        assert len(args) == 2
        arg0 = latex(args[0], in_small=True)
        arg1 = latex(args[1], in_small=True)
        return subscript_pair_latex_table[head] + "_{" + arg0 + "," + arg1 + "}"

    argstr = [latex(arg, in_small=in_small) for arg in args]
    fstr = latex(expr._args[0])
    if in_small:
        spacer = ""
    else:
        spacer = "\\!"
    s = fstr + spacer + "\\left(" + ", ".join(argstr) + "\\right)"
    return s


# heads with their own conversion functions
latex_conversion_functions = {}

infix_latex_table = {
    Mod: "\\bmod",
    Element: "\\in",
    NotElement: "\\notin",
    SetMinus: "\\setminus",
    Union: "\\cup",
    Intersection: "\\cap",
    Less: "<",
    LessEqual: "\\le",
    Greater: ">",
    GreaterEqual: "\\ge",
    Equal: "=",
    Unequal: "\\ne",
    Subset: "\\subset",
    SubsetEqual: "\\subseteq",
    Divides: "\\mid",
}

subscript_latex_table = {
    BernoulliB: "B",
    Fibonacci: "F",
    BellNumber: "B",
    HarmonicNumber: "H",
    PrimeNumber: "p",
    RiemannZetaZero: "\\rho",
    LambertWPuiseuxCoefficient: "\\mu",
    DirichletGroup: "G",
    ConreyGenerator: "g",
    KeiperLiLambda: "\\lambda",
}

subscript_pair_latex_table = {
    DirichletLZero: "\\rho",
    LegendrePolynomialZero: "x",
    GaussLegendreWeight: "w",
    GeneralizedBernoulliB: "B",
}

subscript_call_latex_table = {
    BernoulliPolynomial: "B",
    LegendrePolynomial: "P",
    ChebyshevT: "T",
    ChebyshevU: "U",
    HermitePolynomial: "H",
    HilbertClassPolynomial: "H",
    EisensteinG: "G",
    EisensteinE: "E",
    DivisorSigma: "\\sigma",
    IncompleteBeta: "\\mathrm{B}",
    IncompleteBetaRegularized: "I",
    PolyGamma: "\\psi",
    JacobiThetaEpsilon: "\\varepsilon",
    JacobiThetaPermutation: "S",
#    JacobiTheta: "\\theta",
    SquaresR: "r",
    StirlingSeriesRemainder: "R",
}

symbol_latex_table = {
    True_: "\\operatorname{True}",
    False_: "\\operatorname{False}",
    ConstPi: "\\pi",
    ConstI: "i",
    ConstE: "e",
    ConstGamma: "\\gamma",
    ConstCatalan: "G",
    GoldenRatio: "\\varphi",
    Infinity: "\\infty",
    UnsignedInfinity: "{\\tilde \\infty}",
    GammaFunction: "\\Gamma",
    LogGamma: "\\log \\Gamma",
    UpperGamma: "\\Gamma",
    Erf: "\\operatorname{erf}",
    Erfc: "\\operatorname{erfc}",
    Erfi: "\\operatorname{erfi}",
    DigammaFunction: "\\psi",
    DedekindEta: "\\eta",
    DedekindEtaEpsilon: "\\varepsilon",
    DedekindSum: "s",
    ModularJ: "j",
    ModularLambda: "\\lambda",
    WeierstrassP: "\\wp",
    WeierstrassSigma: "\\sigma",
    WeierstrassZeta: "\\zeta",
    EllipticK: "K",
    EllipticE: "E",
    EulerQSeries: "\\phi",
    PartitionsP: "p",
    MoebiusMu: "\\mu",
    HardyRamanujanA: "A",
    Sin: "\\sin",
    Sinh: "\\sinh",
    Cos: "\\cos",
    Cosh: "\\cosh",
    Tan: "\\tan",
    Tanh: "\\tanh",
    Cot: "\\cot",
    Coth: "\\coth",
    Sec: "\\sec",
    Sech: "\\sech",
    Csc: "\\csc",
    Csch: "\\csch",
    Exp: "\\exp",
    Log: "\\log",
    Atan: "\\operatorname{atan}",
    Acos: "\\operatorname{acos}",
    Asin: "\\operatorname{asin}",
    Acot: "\\operatorname{acot}",
    Atanh: "\\operatorname{atanh}",
    Acosh: "\\operatorname{acosh}",
    Asinh: "\\operatorname{asinh}",
    Acoth: "\\operatorname{acoth}",
    Atan2: "\\operatorname{atan2}",
    Sinc: "\\operatorname{sinc}",
    Hypergeometric0F1: "\\,{}_0F_1",
    Hypergeometric1F1: "\\,{}_1F_1",
    Hypergeometric2F1: "\\,{}_2F_1",
    Hypergeometric2F0: "\\,{}_2F_0",
    Hypergeometric3F2: "\\,{}_3F_2",
    HypergeometricU: "U",
    HypergeometricUStar: "U^{*}",
    Hypergeometric0F1Regularized: "\\,{}_0{\\textbf F}_1",
    Hypergeometric1F1Regularized: "\\,{}_1{\\textbf F}_1",
    Hypergeometric2F1Regularized: "\\,{}_2{\\textbf F}_1",
    Hypergeometric2F0Regularized: "\\,{}_2{\\textbf F}_0",
    Hypergeometric3F2Regularized: "\\,{}_3{\\textbf F}_2",
    BesselJ: "J",
    BesselI: "I",
    BesselY: "Y",
    BesselK: "K",
    HankelH1: "H^{(1)}",
    HankelH2: "H^{(2)}",
    AiryAi: "\\operatorname{Ai}",
    AiryBi: "\\operatorname{Bi}",
    LogIntegral: "\\operatorname{li}",
    GCD: "\\gcd",
    LCM: "\\operatorname{lcm}",
    XGCD: "\\operatorname{xgcd}",
    Totient: "\\varphi",
    Sign: "\\operatorname{sgn}",
    Csgn: "\\operatorname{csgn}",
    Arg: "\\arg",
    Min: "\\min",
    Max: "\\max",
    PP: "\\mathbb{P}",
    ZZ: "\\mathbb{Z}",
    QQ: "\\mathbb{Q}",
    RR: "\\mathbb{R}",
    CC: "\\mathbb{C}",
    HH: "\\mathbb{H}",
    AlgebraicNumbers: "\\overline{\\mathbb{Q}}",
    UnitCircle: "\\mathbb{T}",
    PrimePi: "\\pi",
    SL2Z: "\\operatorname{SL}_2(\\mathbb{Z})",
    PSL2Z: "\\operatorname{PSL}_2(\\mathbb{Z})",
    ModularGroupFundamentalDomain: "\\mathcal{F}",
    ModularLambdaFundamentalDomain: "\\mathcal{F}_{\\lambda}",
    PowerSet: "\\mathscr{P}",
    Ellipsis: "\\ldots",
    Spectrum: "\\operatorname{spec}",
    Det: "\\operatorname{det}",
    RiemannHypothesis: "\\operatorname{RH}",
    GeneralizedRiemannHypothesis: "\\operatorname{GRH}",
    RiemannZeta: "\\zeta",
    HurwitzZeta: "\\zeta",
    DirichletL: "L",
    DirichletLambda: "\\Lambda",
    BetaFunction: "\\mathrm{B}",
    LandauG: "g",
    LiouvilleLambda: "\\lambda",
    DeBruijnNewmanLambda: "\\Lambda",
    RiemannXi: "\\xi",
}

def deftex(f):
    fname = f.__name__[4:]
    latex_conversion_functions[Expr(symbol_name=fname)] = f
    return f

def deftex_heads(heads):
    def decorator(f):
        for head in heads:
            latex_conversion_functions[head] = f
        return f
    return decorator

@deftex
def tex_Exp(head, args, **kwargs):
    assert len(args) == 1
    if args[0].show_exponential_as_power():
        return Pow(ConstE, args[0]).latex(**kwargs)
    else:
        return Call(Exp, args[0]).latex(**kwargs)

@deftex
def tex_Div(head, args, **kwargs):
    assert len(args) == 2
    num, den = args
    in_small = kwargs.get("in_small", False)
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
        #if num.is_integer() and den.is_integer():
        #    return "\\frac{" + numstr + "}{" + denstr + "}"
        #else:
        return "\\frac{" + numstr + "}{" + denstr + "}"

@deftex
def tex_Where(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return argstr[0] + "\; \\text{ where } " + ",\,".join(argstr[1:])

@deftex
def tex_Pos(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "+" + argstr[0]

@deftex
def tex_Neg(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "-" + argstr[0]

@deftex
def tex_Add(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return " + ".join(argstr)

@deftex
def tex_Sub(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    for i in range(1, len(args)):
        if not args[i].is_atom() and args[i]._args[0] in (Neg, Sub):
            argstr[i] = "\\left(" + argstr[i] + "\\right)"
    return " - ".join(argstr)

@deftex
def tex_Mul(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    for i in range(len(args)):
        if args[i].need_parens_in_mul():
            argstr[i] = "\\left(" + argstr[i] + "\\right)"
    return " ".join(argstr)

@deftex
def tex_Pow(head, args, **kwargs):
    assert len(args) == 2
    # remove frac to try to keep it on one line
    base = args[0]
    expo = args[1]
    in_small = kwargs.get("in_small", False)
    # todo: more systematic solutions
    if not base.is_atom() and base.head() in (Sin, Cos, Csc, Tan, Sinh, Cosh, Tanh, DedekindEta):
        return base.head().latex() + "^{" + expo.latex(in_small=True) + "}" + "\\!\\left(" + base.args()[0].latex(in_small=in_small) + "\\right)"
    if not base.is_atom() and base.head() == Fibonacci:
        return "F_{%s}^{%s}" % (base.args()[0].latex(in_small=in_small), expo.latex(in_small=True))
    if not base.is_atom() and base.head() == Subscript:
        assert len(base.args()) == 2
        return "{%s}_{%s}^{%s}" % (base.args()[0].latex(in_small=in_small), base.args()[1].latex(in_small=True), expo.latex(in_small=True))
    # todo: generalized to subscript functions?
    if not base.is_atom() and base.head() == JacobiTheta and len(base.args()) == 3:
        return "\\theta" + "_{%s}^{%s}\\!\\left(%s, %s\\right)" % \
            (base.args()[0].latex(), expo.latex(in_small=True), base.args()[1].latex(), base.args()[2].latex())
    if not base.is_atom() and base.head() in subscript_call_latex_table and len(base.args()) == 2:
        h = subscript_call_latex_table[base.head()]
        s = base.args()[0].latex(in_small=True)
        e = expo.latex(in_small=True)
        v = base.args()[1].latex(in_small=in_small)
        return "%s_{%s}^{%s}\\!\\left(%s\\right)" % (h, s, e, v)
    basestr = base.latex(in_small=in_small)
    expostr = expo.latex(in_small=True)
    if base.is_symbol() or (base.is_integer() and base._integer >= 0) or (not base.is_atom() and base._args[0] in (Abs, Binomial, PrimeNumber, Matrix2x2, Parentheses, Braces, Brackets)):
        return "{" + basestr + "}^{" + expostr + "}"
    else:
        return "{\\left(" + basestr + "\\right)}^{" + expostr + "}"

@deftex
def tex_Matrix2x2(head, args, **kwargs):
    assert len(args) == 4
    argstr = tuple(arg.latex(**kwargs) for arg in args)
    return r"\begin{pmatrix} %s & %s \\ %s & %s \end{pmatrix}" % argstr

@deftex
def tex_Matrix2x1(head, args, **kwargs):
    assert len(args) == 2
    argstr = tuple(arg.latex(**kwargs) for arg in args)
    return r"\begin{pmatrix} %s \\ %s \end{pmatrix}" % argstr

@deftex
def tex_JacobiTheta(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    #midsep = "\\,\\middle|\\,"
    midsep = ","
    if len(args) == 3:
        index = args[0].latex(in_small=True)
        z = argstr[1]
        tau = argstr[2]
        return "\\theta_{%s}\\!\\left(%s %s %s\\right)" % (index, z, midsep, tau)
    if len(args) == 4:
        index = args[0].latex(in_small=True)
        z = argstr[1]
        tau = argstr[2]
        if args[3].is_integer():
            r = args[3]._integer
            if r >= 0 and r <= 3:
                return "\\theta%s_{%s}\\!\\left(%s %s %s\\right)" % ("'" * r, index, z, midsep, tau)
        r = args[3].latex(in_small=True)
        return "\\theta^{(%s)}_{%s}\\!\\left(%s %s %s\\right)" % (r, index, z, midsep, tau)
    raise ValueError

@deftex
def tex_Cases(head, args, **kwargs):
    in_small = kwargs.get("in_small", False)
    s = "\\begin{cases} "
    for arg in args:
        assert arg.head() == Tuple
        v, c = arg.args()
        #v = v.latex(in_small=True)
        v = v.latex(in_small=in_small)
        if c == Otherwise:
            c = "\\text{otherwise}"
        else:
            #c = c.latex(in_small=True)
            c = c.latex(in_small=in_small)
        s += "%s, & %s\\\\" % (v, c)
    s += " \\end{cases}"
    return s

@deftex
def tex_And(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    for i in range(len(args)):
        if (not args[i].is_atom()) and args[i].head() in (And, Or):
            argstr[i] = "\\left(%s\\right)" % argstr[i]
    in_small = kwargs.get("in_small", False)
    if in_small:
        # see ff190c
        #return "\\text{ and }".join(argstr)
        return ",\\,".join(argstr)
    else:
        return " \\,\\mathbin{\\operatorname{and}}\\, ".join(argstr)
        #return " \\,\\land\\, ".join(argstr)

@deftex
def tex_Or(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    for i in range(len(args)):
        if (not args[i].is_atom()) and args[i].head() in (And, Or, Not):
            argstr[i] = "\\left(%s\\right)" % argstr[i]
    return " \\,\\mathbin{\\operatorname{or}}\\, ".join(argstr)
    #return " \\,\\lor\\, ".join(argstr)

@deftex
def tex_Sqrt(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\sqrt{" + argstr[0] + "}"

@deftex
def tex_Abs(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left|" + argstr[0] + "\\right|"

@deftex
def tex_Floor(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left\\lfloor " + argstr[0] + " \\right\\rfloor"

@deftex
def tex_Ceil(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left\\lceil " + argstr[0] + " \\right\\rceil"

@deftex
def tex_Tuple(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left(" + ", ".join(argstr) + "\\right)"

@deftex
def tex_Set(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left\{" + ", ".join(argstr) + "\\right\}"

@deftex
def tex_List(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left[" + ", ".join(argstr) + "\\right]"

@deftex
def tex_Parentheses(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left(" + argstr[0] + "\\right)"

@deftex
def tex_Brackets(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left[" + argstr[0] + "\\right]"

@deftex
def tex_Braces(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left\\{" + argstr[0] + "\\right\\}"

@deftex
def tex_Call(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return argstr[0] + "\!\\left(" + ", ".join(argstr[1:]) + "\\right)"

@deftex
def tex_Subscript(head, args, **kwargs):
    assert len(args) == 2
    argstr0 = args[0].latex(**kwargs)
    kwargs["in_small"] = True
    argstr1 = args[1].latex(**kwargs)
    return "{" + argstr0 + "}_{" + argstr1 + "}"

@deftex_heads([Limit, SequenceLimit, RealLimit, LeftLimit, RightLimit, ComplexLimit, MeromorphicLimit, SequenceLimitInferior, SequenceLimitSuperior])
def tex_Limit(head, args, **kwargs):
    if len(args) == 3:
        formula, var, point = args
        cond = ""
    elif len(args) == 4:
        formula, var, point, cond = args
        cond = ", " + cond.latex(in_small=True)
    else:
        raise ValueError
    var = var.latex()
    point = point.latex(in_small=True)
    formula = formula.latex()
    if (not args[2].is_atom() and args[2].head() not in [Abs]):
        formula = "\\left[ %s \\right]" % formula
    if head == LeftLimit:
        s = "\\lim_{%s \\to {%s}^{-}%s} %s" % (var, point, cond, formula)
    elif head == RightLimit:
        s = "\\lim_{%s \\to {%s}^{+}%s} %s" % (var, point, cond, formula)
    elif head == SequenceLimitInferior:
        s = "\\liminf_{%s \\to %s%s} %s" % (var, point, cond, formula)
    elif head == SequenceLimitSuperior:
        s = "\\limsup_{%s \\to %s%s} %s" % (var, point, cond, formula)
    else:
        s = "\\lim_{%s \\to %s%s} %s" % (var, point, cond, formula)
    return s

@deftex_heads([Minimum, Maximum, ArgMin, ArgMax, ArgMinUnique, ArgMaxUnique, Supremum, Infimum, Zeros, UniqueZero, Solutions, UniqueSolution])
def tex_std_operator(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    opname = {Minimum:"\\min", Maximum:"\\max",
              ArgMin:"\\operatorname{arg\,min}",ArgMinUnique:"\\operatorname{arg\,min*}",
              ArgMax:"\\operatorname{arg\,max}",ArgMaxUnique:"\\operatorname{arg\,max*}",
              Infimum:"\\operatorname{inf}", Supremum:"\\operatorname{sup}",
              Zeros:"\\operatorname{zeros}\\,", UniqueZero:"\\operatorname{zero*}\\,",
              Solutions:"\\operatorname{solutions}\\,", UniqueSolution:"\\operatorname{solution*}\\,"}[head]
    if head in (Minimum, Maximum, Supremum, Infimum) and len(args) == 1:
        if args[0].head() in (Set, SetBuilder):
            return opname + " " + argstr[0]
        else:
            return "%s\\left(%s\\right)" % (opname, argstr[0])
    assert len(args) == 3
    formula, var, predicate = args
    #var = var.latex()
    if 0 and predicate.head() == And and len(predicate.args()) > 1:
        # katex does not support substack
        predicate = "\\begin{matrix}" + "\\\\".join("\\scriptstyle %s " % s.latex(in_small=True) for s in predicate.args()) + "\\end{matrix}"
    else:
        predicate = predicate.latex(in_small=True)
    if formula.head() in (Add, Sub):
        formula = "\\left(" + formula.latex() + "\\right)"
    else:
        formula = formula.latex()
    return "\\mathop{%s}\\limits_{%s} %s" % (opname, predicate, formula)

@deftex_heads([Derivative, RealDerivative, ComplexDerivative, ComplexBranchDerivative, MeromorphicDerivative])
def tex_Derivative(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    if len(args) == 2:
        assert args[1]._args[0] == Tuple
        _, var, point, order = args[1]._args
    elif len(args) == 3:
        _, var, point = args
        order = Expr(1)
    elif len(args) == 4:
        _, var, point, order = args
    if not args[0].is_atom():
        f = args[0].head()
        if f.is_symbol() and f not in (Exp, Sqrt) and args[0].args() == (var,):
            pointstr = point.latex(in_small=True)
            fstr = args[0].head().latex()
            if order.is_integer() and order._integer == 0:
                return "%s(%s)" % (fstr, pointstr)
            if order.is_integer() and order._integer == 1:
                return "%s'(%s)" % (fstr, pointstr)
            if order.is_integer() and order._integer == 2:
                return "%s''(%s)" % (fstr, pointstr)
            if order.is_integer() and order._integer == 3:
                return "%s'''(%s)" % (fstr, pointstr)
            return "{%s}^{(%s)}(%s)" % (fstr, order.latex(), pointstr)
        if 1 and (f in subscript_call_latex_table and len(args[0].args()) == 2 and args[0].args()[1] == var):
            arg0 = args[0].args()[0].latex(in_small=True)
            fstr = subscript_call_latex_table[f]
            pointstr = point.latex(in_small=True)
            if order.is_integer() and order._integer == 0:
                return "%s_{%s}(%s)" % (fstr, arg0, pointstr)
            if order.is_integer() and order._integer == 1:
                return "%s'_{%s}(%s)" % (fstr, arg0, pointstr)
            if order.is_integer() and order._integer == 2:
                return "%s''_{%s}(%s)" % (fstr, arg0, pointstr)
            if order.is_integer() and order._integer == 3:
                return "%s'''_{%s}(%s)" % (fstr, arg0, pointstr)
            return "{%s}^{(%s)}_{%s}(%s)" % (fstr, order.latex(), arg0, pointstr)
    varstr = var.latex()
    pointstr = point.latex(in_small=True)
    orderstr = order.latex()
    if var == point:
        if order.is_integer() and order._integer == 1:
            return "\\frac{d}{d %s}\, %s" % (varstr, argstr[0])
        else:
            return "\\frac{d^{%s}}{{d %s}^{%s}} %s" % (orderstr, varstr, orderstr, argstr[0])
    else:
        if order.is_integer() and order._integer == 1:
            return "\\left[ \\frac{d}{d %s}\, %s \\right]_{%s = %s}" % (varstr, argstr[0], varstr, pointstr)
        else:
            return "\\left[ \\frac{d^{%s}}{{d %s}^{%s}} %s \\right]_{%s = %s}" % (orderstr, varstr, orderstr, argstr[0], varstr, pointstr)

@deftex
def tex_Integral(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    assert len(args) == 2
    assert args[1]._args[0] == Tuple
    _, var, low, high = args[1]._args
    var = var.latex()
    low = low.latex(in_small=True)
    high = high.latex(in_small=True)
    return "\\int_{%s}^{%s} %s \, d%s" % (low, high, argstr[0], var)

@deftex_heads([IndefiniteIntegralEqual, RealIndefiniteIntegralEqual, ComplexIndefiniteIntegralEqual])
def tex_IndefiniteIntegralEqual(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    # IndefiniteIntegralEqual(f(z), g(z), z, c)
    if len(args) == 3:
        fx, gx, x = args
        fx = argstr[0]
        gx = argstr[1]
        x = argstr[2]
        return "\\int %s \, d%s = %s + \\mathcal{C}" % (fx, x, gx)
    elif len(args) == 4:
        fx, gx, x, c = args
        fx = argstr[0]
        gx = argstr[1]
        x = argstr[2]
        if x == c:
            return "\\int %s \, d%s = %s + \\mathcal{C}" % (fx, x, gx)
        else:
            return "\\int %s \, d%s = %s + \\mathcal{C}, %s = %s" % (fx, x, gx, x, c)
    else:
        raise ValueError

@deftex_heads([Sum, Product])
def tex_Sum_Product(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    # Sum(f(n), Tuple(n, a, b))
    # Sum(f(n), Tuple(n, a, b), P(n)) ???
    # Sum(f(n), n, P(n))
    if head == Sum:
        ss = "\\sum"
    else:
        ss = "\\prod"
    # todo: auto-parenthesis for Add/...?
    if len(args) == 2 and not args[1].is_atom() and args[1]._args[0] == Tuple:
        _, var, low, high = args[1]._args
        var = var.latex()
        low = low.latex(in_small=True)
        high = high.latex(in_small=True)
        return ss + ("_{%s=%s}^{%s} %s" % (var, low, high, argstr[0]))
    elif len(args) == 2:
        func, var = args
        return ss + ("_{%s} %s" % (var, argstr[0]))
    elif len(args) == 3:
        func, var, cond = args
        cond = cond.latex(in_small=True)
        return ss + ("_{%s} %s" % (cond, argstr[0]))
    elif len(args) == 1:
        return ss + " " + argstr[0]
    else:
        raise ValueError

@deftex_heads([DivisorSum, DivisorProduct])
def tex_DivisorSum_DivisorProduct(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    if len(args) == 3:
        formula, var, number = args
        formula = argstr[0]
        var = var.latex()
        number = number.latex(in_small=True)
        ss = "_{%s \\mid %s} %s" % (var, number, formula)
    elif len(args) == 4:
        formula, var, number, cond = args
        formula = argstr[0]
        var = var.latex()
        number = number.latex(in_small=True)
        cond = cond.latex(in_small=True)
        #ss = "_{\\begin{matrix} {\\scriptstyle %s \\mid %s} \\\\ {\\scriptstyle %s} \\end{matrix}} %s" % (var, number, cond, formula)
        ss = "_{%s \\mid %s,\\, %s} %s" % (var, number, cond, formula)
    else:
        raise ValueError
    if head == DivisorSum:
        return "\\sum" + ss
    else:
        return "\\prod" + ss

@deftex_heads([PrimeSum, PrimeProduct])
def tex_PrimeSum_PrimeProduct(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    if len(args) == 2:
        formula, var = args
        formula = argstr[0]
        var = var.latex()
        ss = "_{%s} %s" % (var, formula)
    elif len(args) == 3:
        formula, var, cond = args
        formula = argstr[0]
        var = var.latex()
        cond = cond.latex(in_small=True)
        ss = "_{%s} %s" % (cond, formula)
    else:
        raise ValueError
    if head == PrimeSum:
        return "\\sum" + ss
    else:
        return "\\prod" + ss

@deftex
def tex_ComplexZeroMultiplicity(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    assert len(args) == 3
    f, var, point = argstr
    if args[1] == args[2]:
        return "\\mathop{\\operatorname{ord}}\\limits_{%s} %s" % (point, f)
    else:
        return "\\mathop{\\operatorname{ord}}\\limits_{%s=%s} %s" % (var, point, f)

@deftex
def tex_Residue(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    assert len(args) == 3
    f, var, point = argstr
    if args[1] == args[2]:
        return "\\mathop{\\operatorname{Res}}\\limits_{%s} %s" % (point, f)
    else:
        return "\\mathop{\\operatorname{Res}}\\limits_{%s=%s} %s" % (var, point, f)

@deftex
def tex_CongruentMod(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s \\equiv %s \\pmod {%s}" % (argstr[0], argstr[1], argstr[2])

@deftex
def tex_Odd(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s \\text{ odd}" % (argstr[0])

@deftex
def tex_Even(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s \\text{ even}" % (argstr[0])

@deftex
def tex_ZZGreaterEqual(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    # if args[0].is_integer():
    #    return "\{%s, %s, \ldots\}" % (args[0]._integer, args[0]._integer + 1)
    return "\\mathbb{Z}_{\ge %s}" % argstr[0]

@deftex
def tex_ZZLessEqual(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    if args[0].is_integer():
        return "\{%s, %s, \ldots\}" % (args[0]._integer, args[0]._integer - 1)
    return "\\mathbb{Z}_{\le %s}" % argstr[0]

@deftex
def tex_ZZBetween(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    if args[0].is_integer():
        return "\{%s, %s, \ldots %s\}" % (argstr[0], args[0]._integer + 1, argstr[1])
    else:
        return "\{%s, %s + 1, \ldots %s\}" % (argstr[0], argstr[0], argstr[1])

@deftex_heads([ClosedInterval, OpenInterval, ClosedOpenInterval, OpenClosedInterval])
def tex_Interval(head, args, **kwargs):
    assert len(args) == 2
    in_small = kwargs.get("in_small", False)
    #arg0 = args[0].latex(in_small=True)
    #arg1 = args[1].latex(in_small=True)
    arg0 = args[0].latex(in_small=in_small)
    arg1 = args[1].latex(in_small=in_small)
    if head == ClosedInterval:
        return "\\left[%s, %s\\right]" % (arg0, arg1)
    if head == OpenInterval:
        return "\\left(%s, %s\\right)" % (arg0, arg1)
    if head == ClosedOpenInterval:
        return "\\left[%s, %s\\right)" % (arg0, arg1)
    if head == OpenClosedInterval:
        return "\\left(%s, %s\\right]" % (arg0, arg1)

@deftex
def tex_RealBall(head, args, **kwargs):
    assert len(args) == 2
    return "\\left[%s \\pm %s\\right]" % (args[0].latex(in_small=True), args[1].latex(in_small=True))

@deftex
def tex_BernsteinEllipse(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\mathcal{E}_{" + argstr[0] + "}"

@deftex
def tex_Conjugate(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\overline{%s}" % argstr[0]

@deftex
def tex_SetBuilder(head, args, **kwargs):
    assert len(args) == 3
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left\\{ %s : %s \\right\\}" % (argstr[0], argstr[2])

@deftex
def tex_Cardinality(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    #return "\\text{card }" + argstr[0]
    return "\\# " + argstr[0]
    #return "\\left|" + argstr[0] + "\\right|"

@deftex
def tex_Decimal(head, args, **kwargs):
    assert len(args) == 1
    text = args[0]._text
    if "e" in text:
        mant, expo = text.split("e")
        expo = expo.lstrip("+")
        text = mant + " \\cdot 10^{" + expo + "}"
    return text

@deftex_heads([BesselJ, BesselY, BesselI, BesselK, HankelH1, HankelH2])
def tex_Bessel(head, args, **kwargs):
    assert len(args) in (2, 3)
    fsym = symbol_latex_table[head]
    if len(args) == 2:
        in_small = kwargs.get("in_small", False)
        n, z = args
        nstr = n.latex(in_small=True)
        zstr = z.latex(in_small=in_small)
        return fsym + "_{" + nstr + "}" + "\!\\left(" + zstr + "\\right)"
    else:
        n, z, r = args
        in_small = kwargs.get("in_small", False)
        nstr = n.latex(in_small=True)
        zstr = z.latex(in_small=in_small)
        rstr = r.latex(in_small=in_small)
        if r.is_integer() and r._integer >= 0 and r._integer <= 3:
            return fsym + ("'" * r._integer) + "_{" + nstr + "}" + "\!\\left(" + zstr + "\\right)"
        else:
            return fsym + "^{(" + rstr + ")}_{" + nstr + "}" + "\!\\left(" + zstr + "\\right)"

@deftex_heads([AiryAi, AiryBi])
def tex_Airy(head, args, **kwargs):
    assert len(args) in (1, 2)
    if len(args) == 1:
        return latex(Call(head, *args), **kwargs)
    else:
        fsym = symbol_latex_table[head]
        z, r = args
        in_small = kwargs.get("in_small", False)
        zstr = z.latex(in_small=in_small)
        rstr = r.latex(in_small=in_small)
        if r.is_integer() and r._integer >= 0 and r._integer <= 3:
            return fsym + ("'" * r._integer) + "\!\\left(" + zstr + "\\right)"
        else:
            return fsym + "^{(" + rstr + ")}" + "\!\\left(" + zstr + "\\right)"

@deftex_heads([CoulombF, CoulombG])
def tex_Coulomb(head, args, **kwargs):
    assert len(args) == 3
    l, eta, z = args
    lstr = l.latex(in_small=True)
    etastr = eta.latex(in_small=True)
    zstr = z.latex()
    F = {CoulombF:"F", CoulombG:"G"}[head]
    return F + ("_{%s,%s}\!\\left(" % (lstr, etastr)) + zstr + "\\right)"

@deftex
def tex_CoulombH(head, args, **kwargs):
    assert len(args) == 4
    omega, l, eta, z = args
    if omega.is_integer():
        omegastr = "+"
        if omega._integer == -1:
            omegastr = "-"
    else:
        omegastr = omega.latex(in_small=True)
    lstr = l.latex(in_small=True)
    etastr = eta.latex(in_small=True)
    zstr = z.latex()
    return "H" + ("^{%s}_{%s,%s}\!\\left(" % (omegastr, lstr, etastr)) + zstr + "\\right)"

@deftex
def tex_CoulombC(head, args, **kwargs):
    l, eta = args
    lstr = l.latex(in_small=True)
    etastr = eta.latex()
    return "C_{%s}\!\\left(%s\\right)" % (lstr, etastr)

@deftex
def tex_CoulombSigma(head, args, **kwargs):
    l, eta = args
    lstr = l.latex(in_small=True)
    etastr = eta.latex()
    return "\\sigma_{%s}\!\\left(%s\\right)" % (lstr, etastr)

@deftex_heads([Factorial, DoubleFactorial])
def tex_Factorial(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    ss = "!"
    if head == DoubleFactorial:
        ss += "!"
    if args[0].is_symbol() or (args[0].is_integer() and args[0]._integer >= 0):
        return argstr[0] + " " + ss
    else:
        return "\\left(" + argstr[0] + "\\right)" + ss

@deftex
def tex_RisingFactorial(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left(" + argstr[0] + "\\right)_{" + argstr[1] + "}"

@deftex
def tex_FallingFactorial(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left(" + argstr[0] + "\\right)^{\\underline{" + argstr[1] + "}}"

@deftex
def tex_Binomial(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "{" + argstr[0] + " \\choose " + argstr[1] + "}"

@deftex
def tex_StirlingCycle(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left[{%s \\atop %s}\\right]" % (argstr[0], argstr[1])

@deftex
def tex_StirlingS1(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "s\!\\left(%s, %s\\right)" % (argstr[0], argstr[1])

@deftex
def tex_StirlingS2(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\left\\{{%s \\atop %s}\\right\\}" % (argstr[0], argstr[1])

@deftex
def tex_LambertW(head, args, **kwargs):
    assert len(args) in (2,3)
    in_small = kwargs.get("in_small", False)
    if len(args) == 2:
        n, z = args
        nstr = n.latex(in_small=True)
        zstr = z.latex(in_small=in_small)
        return "W_{" + nstr + "}" + "\!\\left(" + zstr + "\\right)"
    else:
        n, z, r = args
        nstr = n.latex(in_small=True)
        zstr = z.latex(in_small=in_small)
        rstr = r.latex(in_small=in_small)
        if r.is_integer() and r._integer >= 0 and r._integer <= 3:
            return "W" + ("'" * r._integer) + "_{" + nstr + "}" + "\!\\left(" + zstr + "\\right)"
        else:
            return "W" + "^{(" + rstr + ")}_{" + nstr + "}" + "\!\\left(" + zstr + "\\right)"

@deftex
def tex_AsymptoticTo(head, args, **kwargs):
    assert len(args) == 4
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s \\sim %s, \; %s \\to %s" % tuple(argstr)

@deftex
def tex_Not(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return " \\operatorname{not} \\left(%s\\right)" % argstr[0]

@deftex
def tex_Implies(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return " \\implies ".join("\\left(%s\\right)" % s for s in argstr)

@deftex
def tex_Equivalent(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return " \\iff ".join("\\left(%s\\right)" % s for s in argstr)

@deftex
def tex_EqualAndElement(head, args, **kwargs):
    assert len(args) == 3
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s = %s \\in %s" % (argstr[0], argstr[1], argstr[2])

@deftex
def tex_KroneckerDelta(head, args, **kwargs):
    assert len(args) == 2
    xstr = args[0].latex(in_small=True)
    ystr = args[1].latex(in_small=True)
    return "\delta_{(%s,%s)}" % (xstr, ystr)

@deftex_heads([LegendreSymbol, JacobiSymbol, KroneckerSymbol])
def tex_LegendreSymbol(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    if 0 and in_small:
        return "(%s \\mid %s)" % (argstr[0], argstr[1])
    else:
        return "\\left( \\frac{%s}{%s} \\right)" % (argstr[0], argstr[1])

@deftex
def tex_Lattice(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\Lambda_{(%s)}" % (", ".join(argstr))

@deftex
def tex_DomainCodomain(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    assert len(args) == 2
    #return "%s \\rightarrow %s" % (argstr[0], argstr[1])

@deftex
def tex_ModularGroupAction(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s \\circ %s" % tuple(argstr)

@deftex
def tex_PrimitiveReducedPositiveIntegralBinaryQuadraticForms(head, args, **kwargs):
    assert len(args) == 1
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\mathcal{Q}^{*}_{%s}" % argstr[0]

@deftex
def tex_HypergeometricUStarRemainder(head, args, **kwargs):
    assert len(args) == 4
    argstr = [arg.latex(**kwargs) for arg in args]
    return "R_{%s}\!\\left(%s,%s,%s\\right)" % tuple(argstr)

@deftex
def tex_DirichletCharacter(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    if len(args) == 2:
        return "\\chi_{%s}(%s, \\cdot)" % tuple(argstr)
    elif len(args) == 3:
        return "\\chi_{%s}(%s, %s)" % tuple(argstr)
    else:
        raise ValueError

@deftex
def tex_PrimitiveDirichletCharacters(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    return "G_{%s}^{\\text{primitive}}" % argstr[0]

@deftex
def tex_GaussSum(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "G_{" + argstr[0] + "}" + "\!\\left(" + argstr[1] + "\\right)"

@deftex
def tex_StieltjesGamma(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    arg0 = args[0].latex(in_small=True)
    if len(args) == 1:
        return "\\gamma_{%s}" % arg0
    if len(args) == 2:
        return "\\gamma_{%s}\\!\\left(%s\\right)" % (arg0, argstr[1])

@deftex
def tex_FormalPowerSeries(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s[[%s]]" % tuple(argstr)

@deftex
def tex_FormalLaurentSeries(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s(\!(%s)\!)" % tuple(argstr)

@deftex
def tex_SeriesCoefficient(head, args, **kwargs):
    assert len(args) == 3
    argstr = [arg.latex(**kwargs) for arg in args]
    return "[{%s}^{%s}] %s" % (argstr[1], argstr[2], argstr[0])

@deftex
def tex_FormalGenerator(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "%s \\text{ is the generator of } %s" % (argstr[0], argstr[1])

@deftex
def tex_Spectrum(head, args, **kwargs):
    assert len(args) == 1
    if args[0].head() == Matrix2x2:
        argstr = [arg.latex(**kwargs) for arg in args]
        return "\\operatorname{spec}" + argstr[0]
    else:
        return Call(head, *args).latex(**kwargs)

@deftex
def tex_Det(head, args, **kwargs):
    assert len(args) == 1
    if args[0].head() == Matrix2x2:
        argstr = [arg.latex(**kwargs) for arg in args]
        return "\\operatorname{det}" + argstr[0]
    else:
        return Call(head, *args).latex(**kwargs)

@deftex
def tex_ForAll(head, args, **kwargs):
    assert len(args) == 3
    argstr = [arg.latex(**kwargs) for arg in args]
    if args[1].head() == Element:
        return "\\text{for all } %s, \\,\\, %s" % (argstr[1], argstr[2])
    return "\\text{for all } %s \\text{ with } %s, \\,\\, %s" % (argstr[0], argstr[1], argstr[2])

@deftex
def tex_Exists(head, args, **kwargs):
    assert len(args) == 2
    argstr = [arg.latex(**kwargs) for arg in args]
    return "\\text{there exists } %s \\text{ with } %s" % (argstr[0], argstr[1])

@deftex
def tex_DiscreteLog(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    n, b, p = args
    n, b, p = argstr[0], b.latex(in_small=True), argstr[2]
    return "\\log_{%s}\!\\left(%s\\right) \\bmod %s" % (b, n, p)

@deftex
def tex_QSeriesCoefficient(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    fun, tau, q, n, qdef = argstr
    return "[%s^{%s}] %s \; \\left(%s\\right)" % (q, n, fun, qdef)

@deftex
def tex_EqualQSeriesEllipsis(head, args, **kwargs):
    argstr = [arg.latex(**kwargs) for arg in args]
    fun, tau, q, ser, qdef = argstr
    return "%s = %s + \\ldots \; \\text{ where } %s" % (fun, ser, qdef)

@deftex
def tex_Description(head, args, **kwargs):
    s = ""
    for arg in args:
        if arg._text is not None:
            s += "\\text{ " + arg._text + " }"
        else:
            s += arg.latex()
    return s

