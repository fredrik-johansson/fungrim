import os
if not os.path.exists("build"):
    os.makedirs("build")
if not os.path.exists("build/grimdoc"):
    os.makedirs("build/grimdoc")

import pygrim

import datetime
datestamp = str(datetime.date.today())
timestamp = str(datetime.datetime.utcnow())
timestamp = timestamp[:timestamp.index(".")]

def escape_title(name):
    # paren = name.find("(")
    # if paren >= 0:
    #     name = name[:paren].rstrip(" ")
    return name.replace(" ", "_")

html_start = """
<!DOCTYPE html>
<html>
<head>
<title>Grim formula language</title>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
<meta name="viewport" content="width=device-width, initial-scale=1">
<style type="text/css">
body { font-family: roboto, arial, sans-serif; font-size:14px; line-height: 1.5em; margin: 0; padding: 0; background-color:#fcfcfc; }
#main { }
/* #main { max-width:900px; margin-left: 1em; margin-right: auto; } */
/* p { text-align:justify; text-justify:inter-word; } */
h1 { margin-bottom: 1em; }
h2 { margin-top: 2em; border-bottom:0.1em solid black; }
h3 { margin-top: 1.5em; }
table { border-collapse:collapse; background-color:#fff; }
table, th, td { border: 1px solid #aaa; }
th, td { padding:0.3em; }
tt { border:1px solid #ccc; background-color:#fff; padding:0.2em; font-size:13px; }
pre {
 background-color: #f4f4f4;
 line-height: 1.3em;
 margin-left: 2em;
 margin-right: 2em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
}

/*
tt a { text-decoration: none; color: #000; background-color:#fff9cf; }
tt a:hover { background-color: #eee; }
*/

tt a { text-decoration: underline; color: #000; }
tt a:hover { background-color: #eee; }

tt { border: 0; }

.sidebar {
  margin: 0;
  padding: 0;
  width: 250px;
  background-color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
  top: 0;
}

.sidebar a {
  display: block;
  color: #246;
  padding: 0;
  text-decoration: none;
  font-size: 12px;
}

.sidebar a.active {
  background-color: #4CAF50;
  color: white;
}

.sidebar a:hover:not(.active) {
  background-color: #555;
  color: white;
}

div.tophead {
  position: fixed;
  top: 0;
  width: 100%;
  height: 4em;
}

div.content {
  margin-left: 250px;
  padding: 0 2em 2em 2em;
  margin-top: 0;
  height: 1000px;
}

/*
@media screen and (max-width: 700px) {
  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
  }
  .sidebar a {float: left;}
  div.content {margin-left: 0;}
}

@media screen and (max-width: 400px) {
  .sidebar a {
    text-align: center;
    float: none;
  }
}
*/

#sidebarUL, .sidebar ul {
  font-size: 12px;
  list-style-type: none;
  margin-left:1em;
  padding: 1px;
}

.caret {
  cursor: pointer;
  -webkit-user-select: none; /* Safari 3.1+ */
  -moz-user-select: none; /* Firefox 2+ */
  -ms-user-select: none; /* IE 10+ */
  user-select: none;
}

.caret::before {
  content: "\\25B6";
  color: black;
  display: inline-block;
  margin-right: 3px;
}

.caret-down::before {
  -ms-transform: rotate(90deg); /* IE 9 */
  -webkit-transform: rotate(90deg); /* Safari */'
  transform: rotate(90deg);  
}

.nested {
  display: none;
}

.active {
  display: block;
}


</style>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> 

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.js" integrity="sha384-y23I5Q6l+B6vatafAwxRu/0oK/79VlbSz7Q9aiSZUvyWYIYsd+qj+o24G5ZU2zJz" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {delimiters: [
              {left: "$$", right: "$$", display: true},
              {left: "$", right: "$", display: false},
            ]
        });
    });
</script>


</head>
<body>

"""




try:
    already_indexed = set([_s.strip() for _s in open("build/indexed.txt", "r").readlines()])
except IOError:
    already_indexed = set()


# note: note a set!
from pygrim.expr import all_builtins

def markup_source(src, replace_ellipsis=True):
    import re
    parts = re.findall(r"[\w']+|[.,!?;()\[\]\+\-/\*\" ]", src)
    out = []
    for part in parts:
        if part == "Ellipsis" and replace_ellipsis:
            part = "..."
        if part in all_builtins:
            if part == "True_":
                part = "True"
            if part == "False_":
                part = "False"
            part = """<a href="%s.html">%s</a>""" % (part, part)
        out.append(part)
    return "".join(out)



toc = [
    "Home",
    "Language syntax",
#    "Working with Pygrim",
    ("Variables and iteration",
    [
        "For",
        "ForElement",
        "Repeat",
        "Step",
        "Fun",
        "Where",
        "Def",
    ]),
    ("Booleans and logic",
    [
        "Equal",
        "NotEqual",
        "True",
        "False",
        "Not",
        "And",
        "Or",
        "Equivalent",
        "Implies",
        "Exists",
        "All",
        "Cases",
        "Otherwise",
    ]),
    ("Tuples, lists and sets",
    [
        "Tuple",
        "List",
        "Set",
        "Item",
        "Element",
        "NotElement",
        "Length",
        "Cardinality",
        "Concatenation",
        "Union",
        "Intersection",
        "SetMinus",
        "Subset",
        "SubsetEqual",
        "CartesianProduct",
        "CartesianPower",
        "Sets",
        "PowerSet",
        "Tuples",
        "Universe",
        "Undefined",
    ]),
    ("Numbers and arithmetic",
    [
        ("Sets of numbers",
        [
            "ZZ",
            "QQ",
            "RR",
            "CC",
            "PP",
            "AlgebraicNumbers",
        ]),
        ("Particular numbers",
        [
            "Decimal",
#            "AlgebraicNumber",
            "Pi",
            "ConstI",
            "ConstE",
            "ConstGamma",
            "GoldenRatio",
            "ConstCatalan",
        ]),
        ("Arithmetic operations",
        [
            "Pos",
            "Neg",
            "Add",
            "Sub",
            "Mul",
            "Div",
            "Pow",
            "Sqrt",
        ]),
        ("Inequalities",
        [
            "Less",
            "LessEqual",
            "Greater",
            "GreaterEqual",
        ]),
        ("Ranges and intervals",
        [
            "ZZGreaterEqual",
            "ZZLessEqual",
            "Range",
            "ClosedInterval",
            "OpenInterval",
            "ClosedOpenInterval",
            "OpenClosedInterval",
        ]),
        ("Infinities",
        [
            "Infinity",
            "UnsignedInfinity",
        ]),
    ]),
    ("Operators and calculus",
    [
        ("Sums and products",
        [
            "Sum",
            "Product",
            "PrimeSum",
            "PrimeProduct",
            "DivisorSum",
            "DivisorProduct",
        ]),
        ("Solutions and zeros",
        [
            "Zeros",
            "UniqueZero",
            "Solutions",
            "UniqueSolution",
        ]),
        ("Extreme values",
        [
            "Supremum",
            "Infimum",
            "Minimum",
            "Maximum",
            "ArgMin",
            "ArgMax",
            "ArgMinUnique",
            "ArgMaxUnique",
        ]),
        ("Limits",
        [
            "Limit",
            "SequenceLimit",
            "RealLimit",
            "LeftLimit",
            "RightLimit",
            "ComplexLimit",
            "MeromorphicLimit",
            "SequenceLimitInferior",
            "SequenceLimitSuperior",
        ]),
        ("Derivatives",
        [
            "Derivative",
            "RealDerivative",
            "ComplexDerivative",
            "ComplexBranchDerivative",
            "MeromorphicDerivative",
        ]),
        ("Integrals",
        [
            "Integral",
        ]),
        ("Complex analysis",
        [
            "IsHolomorphic",
            "IsMeromorphic",
            "ComplexZeroMultiplicity",
            "Residue",
            "Path",
            "CurvePath",
            "AnalyticContinuation",
        ]),
    ]),
    ("Matrices and linear algebra",
    [
        "Matrix",
        "Matrix2x2",
        "Matrix2x1",
        "IdentityMatrix",
        "Det",
        "Spectrum",
        "SingularValues",
        "Matrices",
        "SL2Z",
        "SpecialLinearGroup",
        "GeneralLinearGroup",
        "HilbertMatrix",
    ]),
    ("Special functions",
    [
        ("Number parts and step functions",
        [
            "Abs",
            "Sign",
            "Re",
            "Im",
            "Arg",
            "Conjugate",
            "Csgn",
            "RealAbs",
            "Max",
            "Min",
            "Floor",
            "Ceil",
            "KroneckerDelta",
        ]),
        ("Primes and divisibility",
        [
            "Odd",
            "Even",
            "CongruentMod",
            "Divides",
            "GCD",
            "LCM",
            "XGCD",
            "PrimeNumber",
            "PrimePi",
            "DivisorSigma",
            "MoebiusMu",
            "Totient",
            "DiscreteLog",
            "LegendreSymbol",
            "JacobiSymbol",
            "KroneckerSymbol",
            "SquaresR",
            "LiouvilleLambda",
        ]),
        ("Elementary functions",
        [
            "Exp",
            "Log",
            "Sin",
            "Cos",
            "Tan",
            "Cot",
            "Sec",
            "Csc",
            "Sinh",
            "Cosh",
            "Tanh",
            "Coth",
            "Sech",
            "Csch",
            "Asin",
            "Acos",
            "Atan",
            "Acot",
            "Asec",
            "Acsc",
            "Asinh",
            "Acosh",
            "Atanh",
            "Acoth",
            "Asech",
            "Acsch",
            "Atan2",
            "Sinc",
            "LambertW",
            "LambertWPuiseuxCoefficient",
        ]),
        ("Combinatorial functions",
        [
            "SymmetricPolynomial",
            "Cyclotomic",
            "Fibonacci",
            "BernoulliB",
            "BernoulliPolynomial",
            "StirlingCycle",
            "StirlingS1",
            "StirlingS2",
            "EulerE",
            "EulerPolynomial",
            "BellNumber",
            "LandauG",
            "PartitionsP",
            "HardyRamanujanA",
        ]),
        ("Gamma and factorials",
        [
            "Factorial",
            "Binomial",
            "Gamma",
            "LogGamma",
            "DoubleFactorial",
            "RisingFactorial",
            "FallingFactorial",
            "HarmonicNumber",
            "DigammaFunction",
            "DigammaFunctionZero",
            "BetaFunction",
            "BarnesG",
            "LogBarnesG",
            "StirlingSeriesRemainder",
            "LogBarnesGRemainder",
        ]),
        ("Orthogonal polynomials",
        [
            "ChebyshevT",
            "ChebyshevU",
            "LegendrePolynomial",
            "LegendrePolynomialZero",
            "GaussLegendreWeight",
            "HermitePolynomial",
        ]),
        ("Exponential integrals",
        [
            "Erf",
            "Erfc",
            "Erfi",
            "UpperGamma",
            "LowerGamma",
            "IncompleteBeta",
            "IncompleteBetaRegularized",
            "SinIntegral",
            "LogIntegral",
        ]),
        ("Bessel and Airy functions",
        [
            "AiryAi",
            "AiryBi",
            "AiryAiZero",
            "AiryBiZero",
            "BesselJ",
            "BesselI",
            "BesselY",
            "BesselK",
            "HankelH1",
            "HankelH2",
            "BesselJZero",
            "BesselYZero",
            "CoulombF",
            "CoulombG",
            "CoulombH",
            "CoulombC",
            "CoulombSigma",
        ]),
        ("Hypergeometric functions",
        [
            "Hypergeometric0F1",
            "Hypergeometric1F1",
            "Hypergeometric2F1",
            "Hypergeometric2F0",
            "Hypergeometric3F2",
            "HypergeometricU",
            "HypergeometricUStar",
            "Hypergeometric0F1Regularized",
            "Hypergeometric1F1Regularized",
            "Hypergeometric2F1Regularized",
            "Hypergeometric3F2Regularized",
            "HypergeometricUStarRemainder",
        ]),
        ("Zeta and L-functions",
        [
            "RiemannZeta",
            "RiemannZetaZero",
            "RiemannHypothesis",
            "RiemannXi",
            "HurwitzZeta",
            "LerchPhi",
            "PolyLog",
            "MultiZetaValue",
            "DirichletL",
            "DirichletLZero",
            "DirichletLambda",
            "DirichletCharacter",
            "DirichletGroup",
            "PrimitiveDirichletCharacters",
            "GeneralizedRiemannHypothesis",
            "ConreyGenerator",
            "GeneralizedBernoulliB",
            "StieltjesGamma",
            "KeiperLiLambda",
            "DeBruijnNewmanLambda",
            "GaussSum",
        ]),
        ("Elliptic integrals",
        [
            "AGM",
            "EllipticK",
            "EllipticE",
            "EllipticPi",
            "IncompleteEllipticF",
            "IncompleteEllipticE",
            "IncompleteEllipticPi",
            "CarlsonRF",
            "CarlsonRG",
            "CarlsonRJ",
            "CarlsonRD",
            "CarlsonRC",
        ]),
        ("Elliptic, theta and modular functions",
        [
            "JacobiTheta",
            "DedekindEta",
            "ModularJ",
            "ModularLambda",
            "EisensteinG",
            "EisensteinE",
            "DedekindSum",
            "WeierstrassP",
            "WeierstrassZeta",
            "WeierstrassSigma",
            "HilbertClassPolynomial",
            "EulerQSeries",
            "DedekindEtaEpsilon",
            "ModularGroupAction",
            "ModularGroupFundamentalDomain",
            "ModularLambdaFundamentalDomain",
            "PrimitiveReducedPositiveIntegralBinaryQuadraticForms",
            "JacobiThetaEpsilon",
            "JacobiThetaPermutation",
        ]),
    ]),
    ("Polynomials, series and rings",
    [
        "Pol",
        "Ser",
        "PolX",
        "SerX",
        "Coefficient",
        "PolynomialDegree",
        "Polynomials",
        "PolynomialFractions",
        "FormalPowerSeries",
        "FormalLaurentSeries",
        "FormalPuiseuxSeries",
        "Zero",
        "One",
        "Characteristic",
        "Rings",
        "CommutativeRings",
        "Fields",
        "QuotientRing",
    ]),
#    ("Non-semantic markup",
#    [
#    ]),
]

def has_content(toc, name):
    if isinstance(toc, str):
        return toc == name
    else:
        return any(has_content(item, name) for item in toc)

def write_toc(toc, title, root=False, opened=False):
    print("TOC", toc)
    s = ""
    if isinstance(toc, list):
        if root:
            s += """<ul id="sidebarUL">\n"""
        else:
            s += """<ul class="nested">\n"""
        for item in toc:
            s += write_toc(item, title, opened=opened)
        s += "</ul>\n"
    elif isinstance(toc, tuple):
        head, items = toc
        if has_content(items, title):
            opened = True
            s += """<li><span class="caret opened">%s</span>""" % head
        else:
            s += """<li><span class="caret">%s</span>""" % head
        s += write_toc(items, title, opened=opened)
        s += """</li>\n"""
    elif isinstance(toc, str):
        toctext = toc
        if toc not in already_indexed:
            toctext += " *"
        if toc == title:
            s += """<li style="color:#246; font-weight: bold">%s</li>\n""" % toctext
        else:
            link = toc
            if link == "Home":
                link = "index"
            if link == "True_":
                link = "True"
            if link == "False_":
                link = "False"
            s += """<li><a href="%s.html">%s</a></li>\n""" % (escape_title(link), toctext)
    else:
        raise ValueError
    return s

html_sidebar_template = """
<div class="sidebar">
<div style="text-align:center; padding:1em; padding-bottom:0.1em"><a href="index.html"><b>Grim</b> reference <span style="color:red">(alpha)</span></a></div>
"""

html_sidebar_template_end = """

</div>
<div class="content">
"""


def html_sidebar(title):
    outp = ""
    outp += html_sidebar_template
    toctext = write_toc(toc, title, root=True)
    outp += toctext
    outp += html_sidebar_template_end
    return outp


import pygrim
import pygrim.expr

html_end = """
</div>

<script>
var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}
</script>
<script>
var toggler = document.getElementsByClassName("opened");
var i;
for (i = 0; i < toggler.length; i++) {
    toggler[i].click();
}

</script>

</body>
</html>
"""


def markup_text(source):
    source = source.split("@@@")
    for i in range(1, len(source), 2):
        source[i] = "Expr(" + source[i] + ")"
        source[i] = "$$" + eval(source[i], pygrim.__dict__).latex() + "$$"
    source = "".join(source)

    source = source.split("@@")
    for i in range(1, len(source), 2):
        source[i] = "Expr(" + source[i] + ")"
        source[i] = "$" + eval(source[i], pygrim.__dict__).latex() + "$"
    source = "".join(source)

    source = source.split("@")
    for i in range(1, len(source), 2):
        source[i] = "<tt>" + markup_source(source[i]) + "</tt>"
    source = "".join(source)

    return source

def code_example_html2(expr_source, description, evaluate=False, enclosure=False):
    fmt_expr_source = markup_source(expr_source)
    formula = eval(expr_source, pygrim.__dict__)
    formula_latex = formula.latex()
    description = markup_text(description)
    if 1:
        s = ""
        s += """<div style="background-color:#fff; border:1px solid #eee; padding:0.5em; padding-bottom:0; margin-bottom:0.5em">"""
        s += """<div><span style="color:#888">Input:</span> <tt style="color:#444">""" + fmt_expr_source + """</tt></div>"""
        s += """$$""" + formula_latex + """$$"""
        if evaluate:
            from time import time
            formula2 = eval(expr_source, pygrim.__dict__)
            t1 = time()
            if enclosure:
                formula2 = formula2.n()
            else:
                formula2 = formula2.simple()
            t2 = time()
            formula2_latex = formula2.latex()
            formula2_source = str(formula2)
            formula2_source = markup_source(formula2_source)
            s += """<div><span style="color:#888">Output:</span> <tt style="color:#444; background-color:#eee">""" + formula2_source + """</tt>"""
            s += """ &nbsp;&nbsp;<span style="color:#888">(evaluated by pygrim in %.4f s)</span>""" % (t2-t1)
            s += """</div>"""
            s += """$$""" + formula2_latex + """$$"""
        s += "<p>"
        s += description
        s += "</p>"
        s += "</div>"
        return s

indexed = open("build/indexed.txt", "w")
documentified = set()

def documentify(symbol, short_description=None, long_description=None, text=None, examples=[], evaluation_examples=[], numerical_examples=[]):
    documentified.add(symbol)
    title = str(symbol)
    if title == "True_":
        title = "True"
    if title == "False_":
        title = "False"

    if title == "Home":
        path = "index"
    else:
        path = escape_title(title)

    print("DOCUMENTIFY", path, title)
    indexed.write(title + "\n")

    outtext = html_start
    outtext += html_sidebar(title)
    if title == "Home":
        outtext += "<h1>Welcome to the Grim documentation</h1>"
    else:
        outtext += "<h1>%s</h1>" % title

    if text:
        outtext += markup_text(text)

    for example in examples:
        code, explanation = example
        outtext += code_example_html2(code, explanation)

    if evaluation_examples:
        outtext += "<h2>Symbolic evaluation examples</h2>"

    for example in evaluation_examples:
        if len(example) == 1:
            code, = example
            explanation = ""
        else:
            code, explanation = example
        outtext += code_example_html2(code, explanation, evaluate=True)

    if numerical_examples:
        outtext += "<h2>Numerical evaluation examples</h2>"

    for example in numerical_examples:
        if len(example) == 1:
            code, = example
            explanation = ""
        else:
            code, explanation = example
        outtext += code_example_html2(code, explanation, evaluate=True, enclosure=True)

    outtext += """<div style="margin-top: 2em; font-style: italic">Last updated: %s</div>""" % timestamp
    outtext += html_end
    
    open("build/grimdoc/%s.html" % path, "w").write(outtext)



from pygrim import *

documentify("Home",
text=r"""
<p>
<b>Grim</b> is a symbolic language for representing mathematical formulas.
</p>

<p>Source code: <a href="https://github.com/fredrik-johansson/fungrim">https://github.com/fredrik-johansson/fungrim</a></p>

<p>
Grim is human-readable, computer-readable, and can be converted to LaTeX for rendering.
It can be used both as a mathematical markup language
and as a simple functional programming language for expressing mathematical objects.
Grim is being developed as a means to represent mathematics in semantic form
in <a href="http://fungrim.org">Fungrim: the Mathematical Functions Grimoire</a>.
A second goal is to have a symbolic interface to
<a href="http://arblib.org">Arb</a>.
</p>

<p>
This project has the following components:
<ul>
<li>A simple core language for symbolic expressions (similar to Lisp S-expressions
and Wolfram language M-expressions).</li>
<li>A vocabulary of hundreds of builtin symbols for mathematical
objects and operations.
</li>
<li>A reference implementation in Python (Pygrim),
which currently handles LaTeX conversion and
symbolic or numerical evaluation of a subset of the functions.</li>
<li>The 2600+ formulas added Fungrim so far which both serve
as documentation and as a test suite.</li>
</ul>
</p>

<p><span style="color:red"><b>Warning: Grim is currently alpha-level, and anything in this documentation may change. There
are many known inconsistencies. Feedback is welcome on anything from mathematical foundations
to syntax and naming.</b></span></p>

<h2>Quick formula examples</h2>

<table class="exampletable">
<tr><th>Grim</th><th>Generated LaTeX</th><th>Rendered formula</th></tr>
<tr>
<td>
@Implies(Element(n, ZZ), Equal(Sin(Mul(Pi, n)), 0))@
</td>
<td>
<tt style="border:0">
\left(n \in \mathbb{Z}\right) \implies \left(\sin\!\left(\pi n\right) = 0\right)</tt>
</td>
<td>
@@@Implies(Element(n, ZZ), Equal(Sin(Mul(Pi, n)), 0))@@@
</td>
</tr>
<tr>
<td>
@Equal(Exp(z), Sum(Div(Pow(z, n), Factorial(n)), For(n, 0, Infinity)))@
</td>
<td>
<tt style="border:0">
{e}^{z} = \sum_{n=0}^{\infty} \frac{{z}^{n}}{n !}</tt>
</td>
<td>
@@@Equal(Exp(z), Sum(Div(Pow(z, n), Factorial(n)), For(n, 0, Infinity)))@@@
</td>
</tr>
<tr>
<td>
@Equal(Det(Matrix(BellNumber(Add(i, j)), For(i, 0, n), For(j, 0, n))), Product(Factorial(k), For(k, 1, n)), BarnesG(Add(n, 2)))@
</td>
<td>
<tt style="border:0">
\operatorname{det}\displaystyle{\begin{pmatrix} B_{0 + 0} & B_{0 + 1} & \cdots & B_{0 + n} \\ B_{1 + 0} & B_{1 + 1} & \cdots & B_{1 + n} \\ \vdots & \vdots & \ddots & \vdots \\ B_{n + 0} & B_{n + 1} & \ldots & B_{n + n} \end{pmatrix}} = \prod_{k=1}^{n} k ! = G\!\left(n + 2\right)</tt></td>
<td>@@@Equal(Det(Matrix(BellNumber(Add(i, j)), For(i, 0, n), For(j, 0, n))), Product(Factorial(k), For(k, 1, n)), BarnesG(Add(n, 2)))@@@</td>
</tr>
</table>

<p>In the table above, the Grim expressions are written in a rather verbose way using explicit function calls
for arithmetic operators. Pygrim also supports infix Python syntax: <tt>x**2 + 3*y</tt> for <tt>Add(Pow(x, 2), Mul(3, y))</tt>.</p>
""",
    evaluation_examples=[
        ("Zeros(x**5 - x**4 - 4*x**3 + 4*x**2 + 2*x - 2, ForElement(x, CC), Greater(Re(x), 0))",
            """By default, Grim expressions are inert (remain unevaluated). Calling the <tt>.eval()</tt> method in Pygrim
            evaluates an expression symbolically; that is, Pygrim produces an equivalent symbolic expression consisting
            of more explicit (and hopefully simpler) objects.
            For example, an implicit description of a finite set might be replaced by an explicit listing of the elements.
            This example demonstrates computing the set of roots of a polynomial which satisfy a given condition."""),
        ("Re(Gamma(Div(7,4)) * DedekindEta(5+4*ConstI))",
            """Pygrim can find symbolic closed form evaluations of various transcendental functions."""
        ),
    ],
    numerical_examples=[
        ("RiemannZetaZero(10**6)",
            "Calling the <tt>.n()</tt> method on an expression in Pygrim produces an enclosure of the numerical value. This shows an example output."),
    ])

documentify("Language syntax",
    text="""

<p>Grim has a single data structure: symbolic expression trees.
A <i>Grim expression</i> is either of the following:</p>

<ul>
<li>An atom (atomic expression), being either:</li>
<ul>
<li>An integer literal, like <tt>0</tt>, <tt>1</tt> or <tt>-42</tt>.</li>
<li>A symbol, like <tt>x</tt>, <tt>Pi</tt>, <tt>Sin</tt> or <tt>Integral</tt>.</li>
<li>A Unicode string, like <tt>"A grim expression: 😀"</tt>.</li>
</ul>
<li>
A non-atom (non-atomic expression), having the form <tt>f(x1, x2, ..., xn)</tt> where
<tt>f</tt>, <tt>x1</tt>, <tt>x2</tt>, ..., <tt>xn</tt> are expressions. The expression
<tt>f</tt> is called the <i>head</i> and
<tt>x1</tt>, <tt>x2</tt>, ..., <tt>xn</tt> are called the <i>arguments</i> of the expression.
</li>
</ul>

<h2>Example</h2>

<p>
An entry in Fungrim is represented by a single Grim expression
that contains various metadata as well as the main formula
as subexpressions. For example:</p>

<pre>
Entry(ID("22dc6e"),
    Formula(Equal(Fibonacci(n), Add(Fibonacci(Sub(n, 1)), Fibonacci(Sub(n, 2))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))
</pre>

<p>The formula is the recurrence relation for Fibonacci numbers: @@Equal(Fibonacci(n), Add(Fibonacci(Sub(n, 1)), Fibonacci(Sub(n, 2))))@@.
The metadata in this case specifies the Fungrim entry ID (<tt>22dc6e</tt>, as a string),
lists the free variables in the formula (here the single variable @n@),
and provides conditions on the variables ("assumptions"),
in this case @@Element(n, ZZ)@@, such that the formula represents a theorem.
</p>

<h3>Some points of caution</h3>

<ul>
<li>Grim distinguishes between
the atomic expression @f@ and the non-atomic
expression @f()@ where @f@ is called with an empty argument list.

<ul>
<li><span style="color:red">TODO: should atoms also have a head (e.g. <tt>Integer</tt>, <tt>Symbol</tt>, <tt>Text</tt>)?</span></li>
</ul>
</li>

<li>The head of an expression need not be an atom; @f(g(a))(x, y)@ is valid.</li>

<li>
Symbol names at this time are limited to ASCII Latin letters, digits and underscores,
where a digit may not appear as the first character. Since symbol names
cannot start with digits or the minus symbol, integer literals can also just
be thought of as a distinguished class of symbols.
<ul>
<li><span style="color:red">TODO: should probably allow Unicode</span></li>
</ul>
</li>
</ul>

<h2>String representation and infix operators</h2>

<p>
Every Grim expression has a canonical string representation, for example
@Add(3, Mul(-5, x))@. The simple syntax ensures that Grim expressions
are syntactically valid in common programming languages.
Pygrim simply embeds Grim as a domain-specific
language within Python, using Python's native integer literals and
function call syntax (the necessary symbols have to be created
as Python variables).</p>

<p>Because function-call syntax is clumsy for complex arithmetic expressions,
we frequently write Grim expressions in an extended syntactical form
using infix arithmetic operators (<tt>+</tt>, <tt>-</tt>, <tt>*</tt>, <tt>/</tt>, <tt>**</tt>) as well as parentheses
for grouping and with use of parentheses and brackets for tuples and lists.
Pygrim supports this syntax by overloading
the Python-level arithmetic operators (with the operator precedence rules of Python).
We need to be careful: for example, we can do @x / 3@ to construct
the Grim expression @Div(x, 3)@ in Python when @x@ is a Grim
symbol, but <tt>1 / 3</tt> in Python
does not give @Div(1, 3)@.
</p>

<h2>Symbols available for variables</h2>

<p>
Symbols reserved for builtin objects (such as @Add@ and @ZZ@)
start with an uppercase letter and are at least two
characters long, so all single-letter symbols and all symbols beginning
with a lowercase character can be used for variables.
</p>

<p>
Most Greek letter names are available as symbols and are recognized by the LaTeX converter.
There are some exceptions: @Gamma@ is reserved for the gamma function, and @Pi@ is reserved for the
constant &pi;; one should use @GreekGamma@ and @GreekPi@ for the Greek capital letters as variables. 
The alternative spelling @lamda@ / @Lamda@ is used for "lambda" since <tt>lambda</tt> is a reserved
keyword in Python. 
</p>

<p>
As a convenience hack: a symbol name ending with an underscore results in function calls being
rendered as subscripts (but watch out as <tt>a_</tt> is not the same symbol as <tt>a</tt>,
and the symbols are not implicitly connected.
</p>
    """,
    examples=[
    ("Set(a, b, c, d, e, f, g, h, i, j, k, l, ell, m, n, o, p, q, r, s, t, u, v, w, x, y, z)",
        "Python variables predefined in Pygrim."),
    ("Set(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z)",
        "Python variables predefined in Pygrim."),
    ("Set(alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lamda, mu, nu, xi, pi, rho, sigma, tau, phi, chi, psi, omega)",
        "Python variables predefined in Pygrim."),
    ("Set(Alpha, Beta, GreekGamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lamda, Mu, Nu, Xi, GreekPi, Rho, Sigma, Tau, Phi, Chi, Psi, Omega)",
        "Python variables predefined in Pygrim."),
    ("Tuple(f(n), a_(n), gamma_(m,n), f_(n)(x))",
        "Function calls."),
    ])

documentify(Decimal,
    examples=[
    ("Decimal(s)",
        "Constructs the rational number represented by the decimal floating-point literal string @@s@@."),
    ('Decimal("3.141592653589793238462643")',
        "A precise approximation of @@Pi@@."),
    ('Equal(Decimal("-6.75e12345"), -Div(675,100) * Pow(10, 12345))',
        "A large negative number."),
    ])

documentify(Pol,
    examples=[
    ("Pol()",
        "A formal indeterminate (formal variable) which may be used to construct polynomials or rational functions as algebraic objects."),
    ("Pol(n)",
        "A formal indeterminate (formal variable) which may be used to construct polynomials or rational functions as algebraic objects, distinguished by an index @@n@@."),
    ("Tuple(Pol(1), Pol(2), Pol(3))",
        "Three formal indeterminates."),
    ("And(NotEqual(Pol(1), 0), NotEqual(Pol(1), Pol(2)))",
        "A formal indeterminate is not the same thing as an expression-level variable; it is a concrete mathematical object, and in particular an object distinct from any number and from any other indeterminate."),
    ("And(Equal(Pol(n) - Pol(n), 0 * Pol(n), 0), Equal(Pol(n)**0, Pol(n) / Pol(n), 1))",
        "Indeterminates of this type generates algebras with ordinary numbers as coefficients. They are not suitable for working in rings with different @Zero@ and @One@ elements."),
    ("Equal(Pol(1) * Pol(2), Pol(2) * Pol(1))",
        "Indeterminates of this type commutes with numbers and with other indeterminates of the same kind."),
    ("""Where(Equal(Sum(Pol(i), For(i, 1, m))**n,
                Sum((Factorial(n) / Product(Factorial(Item(k, i)), For(i, 1, m)) * Product(Pol(i)**Item(k, i), For(i, 1, m))),
                    ForElement(k, S))),
            Def(S, Set(k, ForElement(k, CartesianPower(Range(0,n), m)),
                Equal(Sum(Item(k, i), For(i, 1, m)), n))))""",
        "The multinomial theorem for formal indeterminates."),
    ])

documentify(Ser,
    examples=[
    ("Ser()",
        "A formal indeterminate (formal variable) which may be used to construct formal power series (or Laurent series, Puiseux series) as algebraic objects."),
    ("Equal(SequenceLimit(Ser()**n, For(n, Infinity)), 0)",
        "Powers of series indeterminates converge in the topology of formal power series. (This is in contrast to @Pol@ indeterminates, for which this limit does not exist.)"),
    ("Equal(Exp(Ser()), Sum(Ser()**n / Factorial(n), For(n, 0, Infinity)))",
        "Analytic functions can be applied to formal power series, generating new formal power series. (This is in contrast to @Pol@ indeterminates, with @Exp(Pol())@ representing a formal exponential polynomial.)"),
    ])

documentify(PolX,
    examples=[
    ("PolX",
        "A formal indeterminate (formal variable) which may be used to construct polynomials or rational functions as algebraic objects."),
    ])

documentify(PolY,
    examples=[
    ("PolY",
        "A formal indeterminate (formal variable) which may be used to construct polynomials or rational functions as algebraic objects; see @Pol@ and @PolX@."),
    ])

documentify(PolZ,
    examples=[
    ("PolZ",
        "A formal indeterminate (formal variable) which may be used to construct polynomials or rational functions as algebraic objects; see @Pol@ and @PolX@."),
    ])

documentify(SerX,
    examples=[
    ("SerX",
        "A formal indeterminate (formal variable) which may be used to construct formal power series algebraic objects."),
    ])


documentify(Coefficient,
    examples=[
    ("Coefficient(S, x, n)",
        "The coefficient of @@x**n@@ in the formal polynomial or formal series @@S@@."),
    ("Equal(Coefficient(7*PolX - PolX**2/3, x, 2), -Div(1,3))",
        "Extraction of a coefficient."),
    ])

documentify(PolynomialDegree,
    examples=[
    ("PolynomialDegree(f, x)",
        "The degree of the formal polynomial @@f@@ with respect to the formal indeterminate @@x@@."),
    ("Equal(PolynomialDegree(PolX**2+PolX+1, PolX), 2)",
        "A quadratic polynomial."),
    ("Equal(PolynomialDegree(0, PolX), -Infinity)",
        "Degree of the zero polynomial, as a matter of convention."),
    ])

documentify(Polynomials,
    examples=[
    ("Polynomials(R, x)",
        "The set of values that can be expressed using polynomial expressions with coefficients in the ring @@R@@ together with @@x@@. If @@x@@ is a formal polynomial indeterminate, this describes a ring of formal polynomials."),
    ("Polynomials(R, (PolX, PolY, PolZ))",
        "The set of formal polynomials in the three indeterminates @@(PolX, PolY, PolZ)@@, with coefficients in the ring @@R@@."),
    ("Element(PolX**2+1, Polynomials(QQ, PolX))",
        "An element of a formal polynomial ring."),
    ("Element(3*Pi**2-Pi, Polynomials(QQ, Pi))",
        "An element of a transcendental number ring."),
    ])

documentify(PolynomialFractions,
    examples=[
    ("PolynomialFractions(K, x)",
        "The set of values that can be expressed using quotients of polynomial expressions with coefficients in the field @@K@@ together with @@x@@. If @@x@@ is formal polynomial indeterminate, this describes a field of formal rational functions."),
    ("PolynomialFractions(K, (PolX, PolY, PolZ))",
        "The set of formal rational functions in the three indeterminates @@(PolX, PolY, PolZ)@@, with coefficients in the field @@K@@."),
    ("Element(PolX/(PolX**2+1), PolynomialFractions(QQ, PolX))",
        "An element of a formal rational function field."),
    ("Element(1/Pi, PolynomialFractions(QQ, Pi))",
        "An element of a transcendental number field."),
    ])

documentify(FormalPowerSeries,
    examples=[
    ("FormalPowerSeries(R, SerX)",
        "The set of formal power series in the series indeterminate @@SerX@@, with coefficients in the ring @@R@@."),
    ("FormalPowerSeries(R, (SerX, SerY))",
        "The set of bivariate formal power series in the series indeterminates @@SerX@@ and @@SerY@@, with coefficients in the ring @@R@@."),
    ("Element(Sum(Factorial(n) * SerX**n, For(n, 0, Infinity)), FormalPowerSeries(ZZ, SerX))",
        "Formal power series need not have a nonzero radius of convergence."),
    ("Subset(Polynomials(R, SerX), FormalPowerSeries(R, SerX), FormalLaurentSeries(R, SerX), FormalPuiseuxSeries(R, SerX))",
        "Formal power series generalize polynomials and are generalized by formal Laurent series and formal Puiseux series."),
    ])

documentify(FormalLaurentSeries,
    examples=[
    ("FormalLaurentSeries(R, SerX)",
        "The set of formal Laurent series in the series indeterminate @@SerX@@, with coefficients in the ring @@R@@."),
    ("Element(Sum(n * SerX**n, For(n, -2, Infinity)), FormalLaurentSeries(ZZ, SerX))",
        "An example of a formal Laurent series."),
    ])

documentify(FormalPuiseuxSeries,
    examples=[
    ("FormalPuiseuxSeries(R, SerX)",
        "The set of formal Puiseux series in the series indeterminate @@SerX@@, with coefficients in the ring @@R@@."),
    ("Element(Sum(n * SerX**(n/3), For(n, 0, Infinity)), FormalPuiseuxSeries(ZZ, SerX))",
        "An example of a formal Puiseux series."),
    ])

documentify(Rings,
    examples=[
    ("Rings",
        "This abstract set has as elements all sets satisfying the ring axioms."),
    ("Element(ZZ, Rings)",
        "An example of a ring."),
    ("NotElement(2*ZZ, Rings)",
        "An example of a non-ring (lacks unit element)."),
    ])

documentify(CommutativeRings,
    examples=[
    ("CommutativeRings",
        "This abstract set has as elements all sets satisfying the ring axioms with commutative multiplication."),
    ("Element(ZZ, CommutativeRings)",
        "An example of a commutative ring."),
    ("NotElement(Matrices(ZZ, 2, 2), CommutativeRings)",
        "An example of a noncommutative ring."),
    ("Implies(And(Element(R, CommutativeRings), Elements(x, y, R)), Equal((x+y)**2, x**2+2*x*y+y**2))",
        "An identity valid in commutative rings."),
    ])

documentify(Fields,
    examples=[
    ("Fields",
        "This abstract set has as elements all sets satisfying the field axioms."),
    ("Element(QQ, Fields)",
        "An example of a field."),
    ("NotElement(ZZ, Fields)",
        "An example of a non-field."),
    ])

documentify(One,
    examples=[
    ("One(R)",
        "The unit element (multiplicative identity) of the ring @@R@@."),
    ("Equal(One(ZZ), One(QQ), One(CC), 1)",
        "All numbers belong to the same 'type'."),
    ("Equal(One(Matrices(ZZ, 2, 2)), Matrix2x2(1, 0, 0, 1))",
        "A ring with different unit element than the number 1."),
    ])

documentify(Zero,
    examples=[
    ("Zero(R)",
        "The zero element (additive identity) of the ring @@R@@."),
    ("Equal(Zero(ZZ), Zero(QQ), Zero(CC), 1)",
        "All numbers belong to the same 'type'."),
    ("Equal(Zero(Matrices(ZZ, 2, 2)), Matrix2x2(0, 0, 0, 0))",
        "A ring with different zero element than the number 0."),
    ])

documentify(Characteristic,
    examples=[
    ("Characteristic(R)",
        "The characteristic of the ring @@R@@"),
    ("Equal(Characteristic(QQ), 0)",
        "Ordinary numbers have characteristic zero."),
    ("Equal(Characteristic(QuotientRing(ZZ, 3*ZZ)), 3)",
        "A ring with nonzero characteristic."),
    ])

documentify(QuotientRing,
    examples=[
    ("QuotientRing(R, I)",
        "The quotient ring of residue classes of the ring @@R@@ modulo the ideal @@I@@."),
    ("NotElement(2, QuotientRing(ZZ, 3*ZZ))",
        "The elements of a quotient ring are formal residue class objects, not elements of the original ring."),
    ])

documentify(Matrix,
    examples=[
    ("Matrix([[1, 2, 3], [4, 5, 6]])",
        "Matrix with explicit elements."),
    ("Matrix(f(i,j), For(i, 1, m), For(j, 1, n))",
        "Matrix with entries @@f(i,j)@@ for row indices @@LessEqual(1, i, m)@@ and column indices @@LessEqual(1, j, n)@@."),
    ("Matrix(c_(i,j), For(i, 0, m), For(j, 0, n))",
        "Matrix with entries @@c_(i,j)@@ for row indices @@LessEqual(0, i, m)@@ and column indices @@LessEqual(0, j, n)@@."),
    ])

documentify(Matrix2x2,
    examples=[
    ("Matrix2x2(a, b, c, d)",
        "Equivalent to @Matrix([[a, b], [c, d]])@."),
    ])

documentify(Matrix2x1,
    examples=[
    ("Matrix2x1(a, b)",
        "Equivalent to @Matrix([[a], [b]])@."),
    ])

documentify(IdentityMatrix,
    examples=[
    ("IdentityMatrix(n)",
        "The identity matrix of size @@n@@."),
    ])

documentify(Det,
    examples=[
    ("Det(A)",
        "The determinant of the matrix @@A@@."),
    ("Equal(Det(Matrix2x2(a, b, c, d)), a*d-b*c)",
        "An explicit determinant."),
    ],
    evaluation_examples=[
        ("Det(HilbertMatrix(10))",),
    ])

documentify(Matrices,
    examples=[
    ("Matrices(R, m, n)",
        "The set of @@m@@ by @@n@@ matrices with coefficients in @@R@@. TODO: reorder arguments?"),
    ])

documentify(SL2Z,
    examples=[
    ("SL2Z",
        "Equivalent to @SpecialLinearGroup(2, ZZ)@."),
    ])

documentify(SpecialLinearGroup,
    examples=[
    ("SpecialLinearGroup(n, R)",
        "The special linear group consisting of @@n@@ by @@n@@ matrices with coefficients in @@R@@ and having determinant 1."),
    ])

documentify(GeneralLinearGroup,
    examples=[
    ("GeneralLinearGroup(n, R)",
        "The general linear group consisting of @@n@@ by @@n@@ matrices with coefficients in @@R@@ and having determinant invertible in @@R@@."),
    ])

documentify(HilbertMatrix,
    examples=[
    ("HilbertMatrix(n)",
        "The Hilbert matrix of size @@n@@."),
    ("Equal(HilbertMatrix(n), Where(Matrix(c_(i,j), For(i, 1, n), For(j, 1, n)), Def(c_, Fun(Tuple(i, j), 1/(i+j-1)))))",
        "Description of the Hilbert matrix."),
    ])

documentify(SingularValues,
    examples=[
    ("SingularValues(A)",
        "The set of singular values of the matrix @@A@@."),
    ],
    evaluation_examples=[
        ("SingularValues(Matrix([[1, 1, -1], [-1, 0, 1], [-1, 1, 1]]))",),
    ])


documentify(Spectrum,
    examples=[
    ("Spectrum(A)",
        "The set of eigenvalues of the matrix @@A@@."),
    ])

documentify(For,
    examples=[
    ("For(x, Ellipsis)",
        "Generator expression. This is a syntactical construct which does not represent a mathematical object on its own. The @For@ expression defines the symbol passed as the first argument (here @x@) as a locally bound variable in the scope of the parent expression. Additional arguments @Ellipsis@ specify an iteration range or evaluation point for @x@ (the interpretation of these arguments depends on the parent operator)."),
    ("Set(f(n), For(n, a, b))",
        "Typically, @For(n, a, b)@ specifies iteration over @@n@@ from @@a@@ to @@b@@. The iteration is empty if @@Less(b, a)@@."),
    ("Sum(f(n), For(n, a, b))",
        "Typically, @For(n, a, b)@ specifies iteration over @@n@@ from @@a@@ to @@b@@. The iteration is empty if @@Less(b, a)@@."),
    ("Integral(f(x), For(x, a, b))",
        "In an integral operator, @For(n, a, b)@ specifies a straight-line path for @@x@@ from @@a@@ to @@b@@. Swapping the endpoints negates the integral."),
    ("RealLimit(f(x), For(x, Pi))",
        "In a limit or derivative operator, @For(x, c)@ specifies the limit or differentiation point @c@."),
    ])

documentify(ForElement,
    examples=[
    ("ForElement(x, S)",
        "Generator expression. This is a syntactical construct which does not represent a mathematical object on its own. The @ForElement@ expression defines the symbol passed as the first argument (here @x@) as a locally bound variable in the scope of the parent expression. The second argument (here @S@) should be a set; the meaning is that @x@ is taken over all values in @S@ in the parent expression."),
    ("Set(f(x), ForElement(x, S))",
        "A typical use is to perform a set comprehension or fold-type operation."),
    ("Minimum(x**2, ForElement(x, RR))",
        "The set does not need to be countable."),
    ("Set(f(x), ForElement(x, S), P(x))",
        "Most operators that allow @ForElement@ interpret an expression following @ForElement@ as a filter predicate."),
    ("Sum(f(x), ForElement(x, S))",
        "A summation done over all elements of a set."),
    ])

documentify(Repeat,
    examples=[
    ("Repeat(x, n)",
        "Repeating sequence. This is a syntactical construct which does not represent a mathematical object on its own. It can be interjected among the arguments to a function or operator."),
    ("Repeat(1, 2, 3, n)",
        "A repeated run of several elements."),
    ("List(Repeat(a, n))",
        "A repeated element in a list."),
    ("Tuple(Repeat(1, N), 0, Repeat(1, 2, 3, M), 1, 2)",
        "Repeated elements among other elements in a tuple."),
    ("f(0, 0, Repeat(1, n), 2)",
        "A repeated argument in a function call."),
    ])

documentify(Step,
    examples=[
    ("Step(f(n), For(n, a, b))",
        "Enumerated sequence. This is a syntactical construct which does not represent a mathematical object on its own. It can be inserted among the arguments to a function or operator to generate a run of arguments."),
    ("f(Step(Pow(k, 2), For(k, 1, 10)))",
        "Calling a function with a run of arguments."),
    ("Tuple(Step(1/k, For(k, a, b)))",
        "Constructing a tuple with a run of elements. Note: the @Tuple@ operator understands iteration directly, so in this case @Tuple(1/k, For(k, a, b))@ would be equivalent."),
    ("f(Step(Repeat(n, n), For(n, 0, N)))",
        "Composing @Step@ with @Repeat@."),
    ])

documentify(Fun,
    examples=[
    ("Fun(x, x**2)",
        "Defines a univariate function mapping the symbol given as the first argument to the expression in the second argument. The symbol @@x@@ representing the dummy variable becomes locally bound within the function expression. This function is improper; that is, it does not belong to a particular function space."),
    ("Fun(x, x**2)(42)",
        "Calling a named function."),
    ("Where(f(42), Def(f, Fun(x, x**2)))",
        "Calling a function assigned to a variable."),
    ("Fun(Tuple(x, y), 2*x+3*y)",
        "Defines a bivariate function. The symbols @x@ and @y@ become locally bound."),
    ("Fun(Tuple(x), x**2)",
        "Equivalent to defining a univariate function."),
    ("Fun(Tuple(x_(i), For(i, 1, n)), Sum(i * x_(i), For(i, 1, n)))",
        "Defines a multivariate function with arity @@n@@. In this special case, the variable binding @x_@ in the scope of the @Tuple@ call propagates through to the @Fun@ operator. "),
    ("Where(g(c_(2), c_(3)), Def(c_, Fun(n, n**2+n+1)), Def(g, Fun(Tuple(x, y), (x+y)*(x-y))))",
        "Defining and calling named improper functions in the context of a @Where@-expression."),
    ])

documentify(Where,
    examples=[
    ("Where(f(x), Def(x, a))",
        "Defines the symbol @x@ as an alias for @a@ and evaluates the expression @f(x)@ with this bound value of @x@. This is equivalent to @f(a)@."),
    ("Where(a**2 + 2*a + 1, Def(a, x + y))",
        "Using a bound variable in an expression."),
    ("Where(f(a) + f(b), Def(f(x), x**2))",
        "Defines the symbol @f@ as a function and uses it in an expression. The symbol @x@ is a dummy variable which becomes bound locally only within the @Def@-expression."),
    ("Where(x*y*z, Def(x, 1), Def(y, x+2), Def(z, x+y+3))",
        "There can be multiple definitions in one @Where@-expression. The definitions are parsed left to right: @x@ can be used in the right-hand side defining @y@, both @x@ and @y@ can be used in the right-hand side defining @z@, and all three (@x@, @y@ and @z@) can be used in the main expression."),
    ("Where(a+b, Def(Tuple(a, b), T))",
        "Destructuring assignment."),
    ("Where(a*d-b*c, Def(Matrix2x2(a, b, c, d), M))",
        "Destructuring assignment. This sets @a@, @b@, @c@ and @d@ to the entries of the matrix @M@."),
    ("Where(Sum(a_(i), For(i, 1, n)), Def(Tuple(a_(i), For(i, 1, n)), T))",
        "Special destructuring assignment. This sets @n@ to the length of the tuple @T@ and sets @a_@ to a function mapping @@Range(1,n)@@ to the elements of @T@."),
    ("Where(f(2,3), Def(f(x,y), x*y + y + x**2))",
        "Defines @f@ as a function of two variables and evaluates it. The symbols @x@ and @y@ are dummy variables which become bound locally only within the @Def@-expression."),
    ])

documentify(Def,
    examples=[
    ("Def(x, a)",
        "Defines @x@ as an alias for @a@; used within a @Where@-expression."),
    ])

documentify(Cases,
    examples=[
    ("Cases(Tuple(f(x), P(x)), Tuple(g(x), Otherwise))",
        "Gives the value @f(x)@ if the predicate @P(x)@ is @True@, otherwise gives the value @g(x)@."),
    ("Cases(Tuple(f(x), P(x)), Tuple(g(x), Q(x)), Tuple(h(x), Otherwise))",
        "Gives the value @f(x)@ if the predicate @P(x)@ is @True@, the value @g(x)@ if the predicate @Q(x)@ is @True@, and otherwise gives the value @h(x)@. If both @P(x)@ and @Q(x)@ are true simultaneously, no ordering is implied; it is assumed that @f(x)@ and @g(x)@ give the same value for any such @x@."),
    ("Cases(Tuple(f(x), P(x)), Tuple(g(x), Q(x)))",
        "Gives the value @f(x)@ if the predicate @P(x)@ is @True@, and the value @g(x)@ if the predicate @Q(x)@ is @True@. If both @P(x)@ and @Q(x)@ are true simultaneously, no ordering is implied; it is assumed that @f(x)@ and @g(x)@ give the same value for any such @x@. The result is undefined if neither predicate is @True@."),
    ])

documentify(Otherwise,
    examples=[
    ("Otherwise",
        "This special symbol is used to denote the fallback case in a @Cases@ expression."),
    ])


documentify(All,
    examples=[
    ("All(f(x), ForElement(x, S))",
        "True if @@f(x)@@ is true for all @@x@@ in @@S@@, and false otherwise."),
    ("All(f(x), ForElement(x, S), P(x))",
        "True if @@f(x)@@ is true for all @@x@@ in @@S@@ satisfying the condition @@P(x)@@, and false otherwise."),
    ("All(GreaterEqual(Exp(x), 1), ForElement(x, RR), GreaterEqual(x, 0))",
        "An example of a quantified formula."),
    ("All(Implies(GreaterEqual(x, 0), GreaterEqual(Exp(x), 1)), ForElement(x, RR))",
        "Logically equivalent to the previous example."),
    ("All(Implies(And(Element(x, RR), GreaterEqual(x, 0)), GreaterEqual(Exp(x), 1)), For(x))",
        "Normally, the domain of the bound variable should be specified with a @ForElement@ expression, but a raw @For(x)@ can be used to quantify over the entire universe. This form is acceptable when the @Implies@ expression contains a domain statement."),
#    ("Implies(And(Element(x, RR), GreaterEqual(x, 0)), GreaterEqual(Exp(x), 1))",
    ("Equivalent(All(P(x), ForElement(x, S)), NotElement(False, Set(P(x), ForElement(x, S))))",
        "Equivalent characterization of this operator."),
    ("Equivalent(All(P(x), ForElement(x, S), Q(x)), NotElement(False, Set(P(x), ForElement(x, S), Q(x))))",
        "Equivalent characterization of this operator."),
    ])

documentify(Exists,
    examples=[
    ("Exists(f(x), ForElement(x, S))",
        "True if @@f(x)@@ is true for some @@x@@ in @@S@@, and false otherwise."),
    ("Exists(Equal(Exp(x), 2), ForElement(x, RR), GreaterEqual(x, 0))",
        "An example of a quantified formula."),
    ("Equivalent(Exists(P(x), ForElement(x, S)), Element(True, Set(P(x), ForElement(x, S))))",
        "Equivalent characterization of this operator."),
    ("Equivalent(Exists(P(x), ForElement(x, S), Q(x)), Element(True, Set(P(x), ForElement(x, S), Q(x))))",
        "Equivalent characterization of this operator."),
    ])

documentify(Equal,
    examples=[
    ("Equal(a, b)",
        "True if @@a@@ and @@b@@ are the same mathematical object, and False otherwise."),
    ("Equal(a, b, c, d)",
        "This operator can be called with any number of arguments."),
    ("Equal(Step(x_(i), For(i, 1, n)))",
        "Testing equality of a sequence of objects."),
    ])

documentify(NotEqual,
    examples=[
    ("NotEqual(a, b)",
        "Equivalent to @Not(Equal(a, b))@."),
    ])

documentify(True_,
    examples=[
    ("True_",
        "Boolean constant. Note: because <tt>True</tt> is a reserved keyword in Python, Pygrim actually uses the Python variable name <tt>True_</tt> for this symbol. The Python constant <tt>True</tt> can nevertheless be used when writing Grim expressions, since it gets converted when used as a function argument."),
    ])

documentify(False_,
    examples=[
    ("False_",
        "Boolean constant. Note: because <tt>False</tt> is a reserved keyword in Python, Pygrim actually uses the Python variable name <tt>False_</tt> for this symbol. The Python constant <tt>False</tt> can nevertheless be used when writing Grim expressions, since it gets converted when used as a function argument."),
    ])

documentify(Undefined,
    examples=[
    ("Undefined",
        "This special object represents the value of a function or operation applied outside its domain of definition."),
    ("Equal(Div(0, 0), Undefined)",
        "An example of an undefined result."),
    ("And(Equal(Undefined, Undefined), Element(Undefined, Universe))",
        "@Undefined@ itself obeys the usual rules of logic."),
    ])

documentify(Universe,
    examples=[
    ("Universe",
        "The universe of mathematical objects; this abstract set has any object as a member."),
    ("Element(Universe, Universe)",
        "An interesting question..."),
    ])

documentify(Parentheses,
    examples=[
    ("Parentheses(Ellipsis)",
        "Parentheses"),
    ])

documentify(Brackets,
    examples=[
    ("Brackets(Ellipsis)",
        "Square brackets"),
    ])

documentify(Braces,
    examples=[
    ("Braces(Ellipsis)",
        "Curly braces"),
    ])

documentify(HurwitzZeta,
    examples=[
    ("HurwitzZeta(s, a)",
        "Hurwitz zeta function."),
    ])

documentify(LerchPhi,
    examples=[
    ("LerchPhi(z, s, a)",
        "Lerch transcendent."),
    ])

documentify(PolyLog,
    examples=[
    ("PolyLog(s, z)",
        "Polylogarithm."),
    ])

documentify(Not,
    examples=[
    ("Not(x)",
        "Logical not."),
    ])

documentify(And,
    examples=[
    ("And(x, y)",
        "Logical and."),
    ])

documentify(Or,
    examples=[
    ("Or(x, y)",
        "Logical or."),
    ])

documentify(Equivalent,
    examples=[
    ("Equivalent(x, y)",
        "Logical equivalence."),
    ])

documentify(Implies,
    examples=[
    ("Implies(x, y)",
        "Logical implication."),
    ])

documentify(Set,
    examples=[
    ("Set(Ellipsis)",
        "Set with given elements."),
    ("Set(a, b)",
        "Set with elements @a@ and @b@ (if @@Equal(a, b)@@, this is actually a set with a single element)."),
    ("Set(a, b, c)",
        "Set with elements @a@, @b@ and @c@."),
    ("Set(a)",
        "Set with a single element."),
    ("Set()",
        "The empty set."),
    ("Set(f(n), For(n, 1, N))",
        "Set with elements constructed using a generator expression."),
    ("Set(f(x), ForElement(x, S))",
        "Set comprehension."),
    ("Set(f(x), ForElement(x, S), P(x))",
        "Set comprehension with a filter predicate."),
    ("Set(n**3+1, ForElement(n, ZZ), And(Greater(n, 1), Equal(GCD(n, m), 1)))",
        "Set comprehension with a filter predicate."),
    ])

documentify(Sets,
    examples=[
    ("Sets(S)",
        "The set of all sets with elements in @@S@@."),
    ("Sets(S, n)",
        "The set of all sets with elements in @@S@@ and having cardinality @@n@@."),
    ])

documentify(Tuples,
    examples=[
    ("Tuples(S)",
        "The set of all tuples with elements in @@S@@."),
    ("Tuples(S, n)",
        "The set of all tuples with elements in @@S@@ and having length @@n@@."),
    ])

documentify(CartesianProduct,
    examples=[
    ("CartesianProduct(X, Y)",
        "The set of all tuples @@(x,y)@@ with @@Element(x, X)@@ and @@Element(y, Y)@@. More generally, this function can be called with @@n@@ arguments to construct @@n@@-tuples. This function should not be confused with the ordinary product function @Mul@ which computes arithmetic products pointwise when applied to sets."),
    ])

documentify(CartesianPower,
    examples=[
    ("Equal(CartesianPower(X, n), CartesianProduct(Repeat(X, n)))",
        "Cartesian power. This function should not be confused with the ordinary power function @Pow@ which computes arithmetic powers pointwise when applied to sets."),
    ("NotEqual(CartesianPower(X, 1), X)",
        "@@CartesianPower(X, 1)@@ gives a set of 1-tuples, different from the original set @@X@@."),
    ])


documentify(Concatenation,
    examples=[
    ("Concatenation(A, B)",
        "Concatenation of tuples."),
    ("Equal(Concatenation(Tuple(a, b), Tuple(c, d, e), Tuple()), Tuple(a, b, c, d, e))",
        "Concatenation of multiple tuples."),
    ])

documentify(Item,
    examples=[
    ("Item(a, n)",
        "Item @n@ in the tuple @a@, indexed from 1."),
    ])

documentify(Cardinality,
    examples=[
    ("Cardinality(S)",
        "Set cardinality."),
    ])

documentify(Length,
    examples=[
    ("Length(L)",
        "Length of a tuple or list."),
    ])

documentify(PowerSet,
    examples=[
    ("PowerSet(S)",
        "Power set."),
    ])

documentify(Union,
    examples=[
    ("Union(S, T)",
        "Set union."),
    ])

documentify(Intersection,
    examples=[
    ("Intersection(S, T)",
        "Set intersection."),
    ])

documentify(SetMinus,
    examples=[
    ("SetMinus(S, T)",
        "Set difference."),
    ])

documentify(Element,
    examples=[
    ("Element(x, S)",
        "Set membership."),
    ])

documentify(NotElement,
    examples=[
    ("NotElement(x, S)",
        "Set non-membership."),
    ])

documentify(Subset,
    examples=[
    ("Subset(S, T)",
        "Strict subset."),
    ])

documentify(SubsetEqual,
    examples=[
    ("SubsetEqual(S, T)",
        "Subset."),
    ])

documentify(ZZ,
    examples=[
    ("ZZ",
        "The set of integers."),
    ])

documentify(QQ,
    examples=[
    ("QQ",
        "The set of rational numbers."),
    ])

documentify(RR,
    examples=[
    ("RR",
        "The set of real numbers."),
    ])

documentify(CC,
    examples=[
    ("CC",
        "The set of complex numbers."),
    ])

documentify(AlgebraicNumbers,
    examples=[
    ("AlgebraicNumbers",
        "The set of algebraic numbers."),
    ])

documentify(Infinity,
    examples=[
    ("Infinity",
        "Positive infinity."),
    ("-Infinity",
        "Negative infinity."),
    ("Exp(ConstI / 3) * Infinity",
        "Infinity with a complex direction."),
    ],
    evaluation_examples=[
        ("Tuple(Infinity + (3 + 4*ConstI), ConstI * Infinity - 5, 2 * ConstI * Infinity)", "Infinities absorb complex numbers"),
        ("Tuple(Infinity + Infinity, Infinity * Infinity, (-Infinity) + (-Infinity))", "Arithmetic involving infinities is well-defined when the limits are unambiguous"),
        ("Tuple(Infinity - Infinity, Infinity / Infinity, 0 * Infinity)", "Arithmetic involving infinities is undefined when the limits are ambiguous.")
    ])

documentify(UnsignedInfinity,
    examples=[
    ("UnsignedInfinity",
        "Unsigned infinity. Generally used to represent @@Limit(f(z), For(z, c))@@ for functions where @@Equal(Limit(Abs(f(z)), For(z, c)), Infinity)@@ but @@Limit(Sign(f(z)), For(z, c))@@ is undefined."),
    ],
    evaluation_examples=[
        ("Div(1, 0)", "@UnsignedInfinity@ is the result of division by zero."),
        ("Tuple(Abs(UnsignedInfinity), Sign(UnsignedInfinity))", "@UnsignedInfinity@ has infinite magnitude, but undefined sign."),
        ("Tuple(Infinity * UnsignedInfinity, UnsignedInfinity * UnsignedInfinity)", "Arithmetic involving infinities is well-defined when the limits are unambiguous"),
        ("Tuple(UnsignedInfinity + UnsignedInfinity, 0 * UnsignedInfinity)", "Arithmetic involving infinities is undefined when the limits are ambiguous.")
    ])

documentify(ZZGreaterEqual,
    examples=[
    ("ZZGreaterEqual(n)",
        "Integers greater than or equal to @@n@@."),
    ])

documentify(ZZLessEqual,
    examples=[
    ("ZZLessEqual(n)",
        "Integers less than or equal to @@n@@."),
    ])

documentify(Range,
    examples=[
    ("Range(a, b)",
        "The set of integers in the range @@LessEqual(a, n, b)@@."),
    ])

documentify(ClosedInterval,
    examples=[
    ("ClosedInterval(a, b)",
        "Closed interval."),
    ])

documentify(OpenInterval,
    examples=[
    ("OpenInterval(a, b)",
        "Open interval."),
    ])

documentify(ClosedOpenInterval,
    examples=[
    ("ClosedOpenInterval(a, b)",
        "Closed-open interval."),
    ])

documentify(OpenClosedInterval,
    examples=[
    ("OpenClosedInterval(a, b)",
        "Open-closed interval."),
    ])

#    ("Sum(f(n), For(n))",

documentify(Sum,
    examples=[
    ("Sum(f(n), For(n, a, b))",
        """
        Sum of @@f(n)@@ for integers @@n@@ from @@a@@ to @@b@@, where @@a@@ and @@b@@
        should be integers or @@Neg(Infinity)@@ or @@Infinity@@.
        If @@Less(b, a)@@, the sum is empty. The sum @@Sum(f(n), For(n, 0, Infinity))@@
        is interpreted as @@SequenceLimit(Sum(f(n), For(n, 0, N)), For(N, Infinity))@@
        and can be conditionally convergent.
        """),
    ("Sum(f(n), For(n, a, b), P(n))",
        "The same meaning as @@Sum(f(n), For(n, a, b))@@, except that only terms satisfying the predicate @@P(n)@@ are included in the sum."),
    ("Sum(f(x), ForElement(x, S))",
        "Sum of @@f(x)@@ for all @@x@@ in the set @@S@@. The sum is required to be absolutely convergent."),
    ("Sum(f(x), ForElement(x, S), P(x))",
        "Sum of @@f(x)@@ for all @@x@@ in the set @@S@@ satisfying the predicate @@P(x)@@. The sum is required to be absolutely convergent."),
    ("Sum(f(x), For(x), P(x))",
        """Sum of @@f(x)@@ for all @@x@@ satisfying the predicate @@P(x)@@.
        The predicate @@P(x)@@ should define the domain of @@x@@ unambiguously; that is,
        it should include a statement such as @@Element(x, S)@@ where @@S@@
        is a known set. The sum is required to be absolutely convergent."""),
    ("Equal(Sum(f(x), ForElement(x, Set())), 0)",
        "The empty sum is the number @@0@@."),
    ("Equal(Sum(KroneckerDelta(x, 0), ForElement(x, RR)), 1)",
        "A sum can range over an uncountable number of terms, as long as only countably many terms are nonzero."),
    ],
    evaluation_examples=[
        ("Sum(1/n, For(n, 1, 10))",),
        ("Sum(f(1/n), For(n, -3, 3), NotEqual(n, 0))",),
        ("Sum(f(n), For(n, 1, 0))",),
    ])

documentify(Product,
    examples=[
    ("Product(f(n), For(n, a, b))",
        """
        Product of @@f(n)@@ for integers @@n@@ from @@a@@ to @@b@@, where @@a@@ and @@b@@
        should be integers or @@Neg(Infinity)@@ or @@Infinity@@.
        If @@Less(b, a)@@, the product is empty and equal to the integer 1. The product @@Product(f(n), For(n, 0, Infinity))@@
        is interpreted as @@SequenceLimit(Product(f(n), For(n, 0, N)), For(N, Infinity))@@
        and can be conditionally convergent.
        """),
    ("Product(f(n), For(n, a, b), P(n))",
        "The same meaning as @@Product(f(n), For(n, a, b))@@, except that only terms satisfying the predicate @@P(n)@@ are included in the product."),
    ("Product(f(x), ForElement(x, S))",
        "Product of @@f(x)@@ for all @@x@@ in the set @@S@@. The product is required to be absolutely convergent."),
    ("Product(f(x), ForElement(x, S), P(x))",
        "Product of @@f(x)@@ for all @@x@@ in the set @@S@@ satisfying the predicate @@P(x)@@. The product is required to be absolutely convergent."),
    ("Product(f(x), For(x), P(x))",
        """Product of @@f(x)@@ for all @@x@@ satisfying the predicate @@P(x)@@.
        The predicate @@P(x)@@ should define the domain of @@x@@ unambiguously; that is,
        it should include a statement such as @@Element(x, S)@@ where @@S@@
        is a known set. The product is required to be absolutely convergent."""),
    ])

documentify(PrimeSum,
    examples=[
    ("PrimeSum(f(p), For(p))",
        "The sum of @@f(p)@@ taken over all prime numbers @@p@@."),
    ("PrimeSum(f(p), For(p), P(p))",
        "The sum of @@f(p)@@ taken over all prime numbers @@p@@ satisfying the predicate @@P(p)@@."),
    ])

documentify(PrimeProduct,
    examples=[
    ("PrimeProduct(f(p), For(p))",
        "The product of @@f(p)@@ taken over all prime numbers @@p@@."),
    ("PrimeProduct(f(p), For(p), P(p))",
        "The product of @@f(p)@@ taken over all prime numbers @@p@@ satisfying the predicate @@P(p)@@."),
    ])

documentify(DivisorSum,
    examples=[
    ("DivisorSum(f(k), For(k, n))",
        "The sum of @@f(k)@@ taken over all positive integers @@k@@ dividing the integer @@n@@."),
    ("DivisorSum(f(k), For(k, n), P(k))",
        "The sum of @@f(k)@@ taken over all positive integers @@k@@ dividing the integer @@n@@ and satisfying the predicate @@P(k)@@."),
    ])

documentify(DivisorProduct,
    examples=[
    ("DivisorProduct(f(k), For(k, n))",
        "The product of @@f(k)@@ taken over all positive integers @@k@@ dividing the integer @@n@@."),
    ("DivisorProduct(f(k), For(k, n), P(k))",
        "The product of @@f(k)@@ taken over all positive integers @@k@@ dividing the integer @@n@@ and satisfying the predicate @@P(k)@@."),
    ])

documentify(Zeros,
    examples=[
    ("Zeros(f(x), ForElement(x, S))",
        "The set of values @@Element(x, S)@@ satisfying @@Equal(f(x), 0)@@."),
    ("Zeros(f(x), ForElement(x, S), P(x))",
        "The set of values @@Element(x, S)@@ satisfying @@P(x)@@ and @@Equal(f(x), 0)@@."),
    ],
    evaluation_examples=[
    ("Zeros(x**4 - 4*x**2 + 2, ForElement(x, CC), Greater(Re(x), 0))",),
    ])

documentify(UniqueZero,
    examples=[
    ("UniqueZero(f(x), ForElement(x, S))",
        "The unique value @@Element(x, S)@@ satisfying @@Equal(f(x), 0)@@. The result is @Undefined@ if such a value does not exist or is not unique."),
    ("UniqueZero(f(x), ForElement(x, S), P(x))",
        "The unique value @@Element(x, S)@@ satisfying @@P(x)@@ and @@Equal(f(x), 0)@@. The result is @Undefined@ if such a value does not exist or is not unique."),
    ])

documentify(Solutions,
    examples=[
    ("Solutions(Q(x), ForElement(x, S))",
        "The set of values @@Element(x, S)@@ satisfying @@Q(x)@@."),
    ("Solutions(Q(x), ForElement(x, S), P(x))",
        "The set of values @@Element(x, S)@@ satisfying @@P(x)@@ and @@Q(x)@@."),
    ])

documentify(UniqueSolution,
    examples=[
    ("UniqueSolution(Q(x), ForElement(x, S))",
        "The unique value @@Element(x, S)@@ satisfying @@Q(x)@@. The result is undefined if such a value does not exist or is not unique."),
    ("UniqueSolution(Q(x), ForElement(x, S), P(x))",
        "The unique value @@Element(x, S)@@ satisfying @@P(x)@@ and @@Q(x)@@. The result is undefined if such a value does not exist or is not unique."),
    ])

documentify(Supremum,
    examples=[
    ("Supremum(f(x), ForElement(x, S))",
        "Supremum of the set @@Set(f(x), ForElement(x, S))@@."),
    ("Supremum(f(x), ForElement(x, S), P(x))",
        "Supremum of the set @@Set(f(x), ForElement(x, S), P(x))@@."),
    ])

documentify(Infimum,
    examples=[
    ("Infimum(f(x), ForElement(x, S))",
        "Infimum of the set @@Set(f(x), ForElement(x, S))@@."),
    ("Infimum(f(x), ForElement(x, S), P(x))",
        "Infimum of the set @@Set(f(x), ForElement(x, S), P(x))@@."),
    ])

documentify(Minimum,
    examples=[
    ("Minimum(f(x), ForElement(x, S))",
        "Minimum of the set @@Set(f(x), ForElement(x, S))@@. The result is @@Undefined@@ if the set does not have a mimumum value."),
    ("Minimum(f(x), ForElement(x, S), P(x))",
        "Minimum of the set @@Set(f(x), ForElement(x, S), P(x))@@."),
    ])

documentify(Maximum,
    examples=[
    ("Maximum(f(x), ForElement(x, S))",
        "Maximum of the set @@Set(f(x), ForElement(x, S))@@. The result is @@Undefined@@ if the set does not have a mimumum value."),
    ("Maximum(f(x), ForElement(x, S), P(x))",
        "Maximum of the set @@Set(f(x), ForElement(x, S), P(x))@@."),
    ])

documentify(ArgMin,
    examples=[
    ("ArgMin(f(x), ForElement(x, S))",
        "Gives the set of @@x@@ such that @@Equal(f(x), Minimum(f(t), ForElement(t, S)))@@."),
    ("ArgMin(f(x), ForElement(x, S), P(x))",
        "Gives the set of @@x@@ such that @@Equal(f(x), Minimum(f(t), ForElement(t, S), P(t)))@@."),
    ])

documentify(ArgMax,
    examples=[
    ("ArgMax(f(x), ForElement(x, S))",
        "Gives the set of @@x@@ such that @@Equal(f(x), Maximum(f(t), ForElement(t, S)))@@."),
    ("ArgMax(f(x), ForElement(x, S), P(x))",
        "Gives the set of @@x@@ such that @@Equal(f(x), Maximum(f(t), ForElement(t, S), P(t)))@@."),
    ])

documentify(ArgMinUnique,
    examples=[
    ("ArgMinUnique(f(x), ForElement(x, S))",
        "Gives the unique @@Element(x, S)@@ such that @@Equal(f(x), Minimum(f(t), ForElement(t, S)))@@. The result is @@Undefined@@ if such a value does not exist or is not unique."),
    ("ArgMinUnique(f(x), ForElement(x, S), P(x))",
        "Gives the unique @@Element(x, S)@@ such that @@Equal(f(x), Minimum(f(t), ForElement(t, S), P(t)))@@. The result is @@Undefined@@ if such a value does not exist or is not unique."),
    ])

documentify(ArgMaxUnique,
    examples=[
    ("ArgMaxUnique(f(x), ForElement(x, S))",
        "Gives the unique @@Element(x, S)@@ such that @@Equal(f(x), Maximum(f(t), ForElement(t, S)))@@. The result is @@Undefined@@ if such a value does not exist or is not unique."),
    ("ArgMaxUnique(f(x), ForElement(x, S), P(x))",
        "Gives the unique @@Element(x, S)@@ such that @@Equal(f(x), Maximum(f(t), ForElement(t, S), P(t)))@@. The result is @@Undefined@@ if such a value does not exist or is not unique."),
    ])

documentify(Limit,
    examples=[
    ("Limit(f(x), For(x, a), P(x))",
        """The limiting value of @@f(x)@@ for every sequence of @@x@@ satisfying @@P(x)@@ and approaching the limit point @@a@@. 
           If the predicate @@P(x)@@ is omitted, the expression renders correctly to LaTeX,
           but this form should be avoided since it is ambiguous whether it denotes a sequence limit,
           real limit or complex limit (or some other kind of limit). It is better to use
           @SequenceLimit@, @RealLimit@, @LeftLimit@, @RightLimit@ or @ComplexLimit@ depending on the purpose.
           The limit is always a deleted limit. That is, the value of @@f(a)@@ does not need to be equal to the limit and does not even need to be defined.
           The expression @@f(x)@@ is not required to be defined for all @@x@@ satisfying @@P(x)@@;
           it only needs to be defined for all @@x@@ in some neighborhood of the limit point and also satisfying @@P(x)@@."""),
    ])

documentify(SequenceLimit,
    examples=[
    ("SequenceLimit(f(n), For(n, a))",
        "Limiting value of sequence. Equivalent to @Limit(f(n), For(n, a), Element(n, ZZ))@."),
    ("SequenceLimit(f(n), For(n, a), P(n))",
        "Equivalent to @Limit(f(n), For(n, a), And(Element(n, ZZ), P(n))@."),
    ])

documentify(RealLimit,
    examples=[
    ("RealLimit(f(x), For(x, a))",
        "Limiting value, real variable. Equivalent to @Limit(f(x), For(x, a), Element(x, RR))@."),
    ("RealLimit(f(x), For(x, a), P(x))",
        "Equivalent to @Limit(f(x), For(x, a), And(Element(x, RR), P(x))@."),
    ])

documentify(LeftLimit,
    examples=[
    ("LeftLimit(f(x), For(x, a))",
        "Limiting value, from the left. Equivalent to @Limit(f(x), For(x, a), Element(x, OpenInterval(-Infinity,a)))@."),
    ("LeftLimit(f(x), For(x, a), P(x))",
        "Limiting value, from the left. Equivalent to @Limit(f(x), For(x, a), And(Element(x, OpenInterval(-Infinity,a)), P(x)))@."),
    ])

documentify(RightLimit,
    examples=[
    ("RightLimit(f(x), For(x, a))",
        "Limiting value, from the right. Equivalent to @Limit(f(x), For(x, a), Element(x, OpenInterval(a, Infinity)))@."),
    ("RightLimit(f(x), For(x, a), P(x))",
        "Limiting value, from the right. Equivalent to @Limit(f(x), For(x, a), And(Element(x, OpenInterval(a, Infinity)), P(x)))@."),
    ])

documentify(ComplexLimit,
    examples=[
    ("RealLimit(f(z), For(z, a))",
        "Limiting value, complex variable. Equivalent to @Limit(f(z), For(z, a), Element(z, CC))@."),
    ("RealLimit(f(z), For(z, a), P(z))",
        "Equivalent to @Limit(f(z), For(z, a), And(Element(z, CC), P(z))@."),
    ])

documentify(MeromorphicLimit,
    examples=[
    ("MeromorphicLimit(f(z), For(z, a))",
        "Limiting value, allowing poles. This operator is equivalent to @ComplexLimit@, except that whereas @ComplexLimit@ in general is undefined when @a@ is a pole (because the direction of the resulting infinity depends on the direction of approach), @MeromorphicLimit@ is taken to give @UnsignedInfinity@ when @a@ is a pole."),
    ])

documentify(SequenceLimitInferior,
    examples=[
    ("SequenceLimitInferior(f(n), For(n, a))",
        "Limit inferior of sequence."),
    ])

documentify(SequenceLimitSuperior,
    examples=[
    ("SequenceLimitSuperior(f(n), For(n, a))",
        "Limit superior of sequence."),
    ])

documentify(Derivative,
    examples=[
    ("Derivative(f(z), For(z, a))",
        """The derivative of @@f(z)@@ evaluated at @@Equal(z, a)@@.
        This operator is ambiguous since the intended meaning could be a real derivative, a complex derivative, or some other form of derivative.
        It is better to use @RealDerivative@, @ComplexDerivative@, @ComplexBranchDerivative@ or @MeromorphicDerivative@ depending on the purpose."""),
    ("Derivative(f(z), For(z, a, n))",
        "The @@n@@-th derivative of @@f(z)@@ evaluated at @@Equal(z, a)@@."),
    ("Derivative(1/f(z), For(z, a))",
        "The rendering is affected by whether the target expression is a simple function call."),
    ("Derivative(1/f(z), For(z, a, n))",
        "The rendering is affected by whether the target expression is a simple function call."),
    ("Derivative(f(z), For(z, z))",
        "Valid (but potentially confusing): @z@ becomes a bound variable for the expression @f(z)@, but the resulting derivative is evaluated at the value of @z@ defined in the surrounding scope."),
    ])

documentify(RealDerivative,
    examples=[
    ("RealDerivative(f(x), For(x, a))",
        "Real derivative. See @Derivative@ for further information about the call syntax."),
    ("RealDerivative(f(x), For(x, a, n))",
        "Real @@n@@-th derivative. See @Derivative@ for further information about the call syntax."),
    ("Equal(RealDerivative(f(x), For(x, x)), RealLimit((f(x+h)-f(x))/h, For(h, 0)))",
        "Real means that the limit is taken with respect to a real variable."),
    ])

documentify(ComplexDerivative,
    examples=[
    ("ComplexDerivative(f(x), For(x, a))",
        "Complex derivative. See @Derivative@ for further information about the call syntax."),
    ("ComplexDerivative(f(x), For(x, a, n))",
        "Complex @@n@@-th derivative. See @Derivative@ for further information about the call syntax."),
    ("Equal(ComplexDerivative(f(z), For(z, z)), ComplexLimit((f(z+h)-f(z))/h, For(h, 0)))",
        "Complex means that the limit is taken with respect to a complex variable."),
    ])

documentify(ComplexBranchDerivative,
    examples=[
    ("ComplexBranchDerivative(f(z), For(z, z))",
        """Complex derivative, allowing branch cuts. This operator is equivalent to @ComplexDerivative@,
         except that whereas @ComplexDerivative@ is undefined on a branch cut (where the function is not complex differentiable),
         @ComplexBranchDerivative@ gives the complex derivative of the analytically continued function across the branch cut."""),
    ])

documentify(MeromorphicDerivative,
    examples=[
    ("MeromorphicDerivative(f(z), For(z, z))",
        """Complex derivative, allowing poles. This operator is equivalent to @ComplexDerivative@,
         except that whereas @ComplexDerivative@ is undefined at a pole (where the function is not complex differentiable),
         @MeromorphicDerivative@ gives @UnsignedInfinity@ at a pole."""),
    ])

documentify(Integral,
    examples=[
    ("Integral(f(x), For(x, a, b))",
        "The integral of @@f(x)@@ from @@a@@ to @@b@@. The order is significant: @@Equal(Integral(f(x), For(x, a, b)), Neg(Integral(f(x), For(x, b, a))))@@. The precise class of integrals allowed by this operator is yet to be defined, but should normally encompass Lebesgue integrals. The integrand is allowed to be undefined on a subset of measure of zero."),
    ("Integral(f(x), ForElement(x, S))",
        "The integral of @@f(x)@@ over the set @@S@@ (not a directional integral)."),
    ])

documentify(IndefiniteIntegralEqual,
    examples=[
    ("IndefiniteIntegralEqual(f(x), g(x), x)",
        "Indefinite integral"),
    ])

documentify(RealIndefiniteIntegralEqual,
    examples=[
    ("RealIndefiniteIntegralEqual(f(x), g(x), x)",
        "Indefinite integral, real derivative"),
    ])

documentify(ComplexIndefiniteIntegralEqual,
    examples=[
    ("ComplexIndefiniteIntegralEqual(f(x), g(x), x)",
        "Indefinite integral, complex derivative"),
    ])

documentify(IsHolomorphic,
    examples=[
    ("IsHolomorphic(f(z), For(z, c))",
        "Represents the predicate that @@f(z)@@ is holomorphic in some open neighborhood of the point @@c@@."),
    ("IsHolomorphic(f(z), ForElement(z, S))",
        "Represents the predicate that @@f(z)@@ is holomorphic in some open neighborhood of every point in the set @@S@@."),
    ("IsHolomorphic(f(z), For(z, UnsignedInfinity))",
        "Represents the predicate that @@f(1/z)@@ is holomorphic at 0."),
    ("IsHolomorphic(f(z), For(z, ConstI*Infinity))",
        "Represents the predicate that @f(z)@ is a periodic function on the upper half plane that is holomorphic at infinity (in the sense of modular function theory)."),
    ])

documentify(IsMeromorphic,
    examples=[
    ("IsMeromorphic(f(z), For(z, c))",
        "Represents the predicate that @@f(z)@@ is meromorphic in some open neighborhood of the point @@c@@."),
    ("IsMeromorphic(f(z), ForElement(z, S))",
        "Represents the predicate that @@f(z)@@ is meromorphic in some open neighborhood of every point in the set @@S@@."),
    ("IsMeromorphic(f(z), For(z, UnsignedInfinity))",
        "Represents the predicate that @@f(1/z)@@ is meromorphic at 0."),
    ("IsMeromorphic(f(z), For(z, ConstI*Infinity))",
        "Represents the predicate that @@f(z)@@ is a periodic function on the upper half plane that is meromorphic at infinity (in the sense of modular function theory)."),
    ])

documentify(ComplexZeroMultiplicity,
    examples=[
    ("ComplexZeroMultiplicity(f(z), For(z, c))",
        """Gives the root multiplicity (order of vanishing) of @@f(z)@@ at the point @@Equal(z, c)@@.
        For a pole, returns the negated order of the pole. In the special case where @@Equal(f(z), 0)@@
        identically in a neighborhood of @@c@@, the order is @@Infinity@@. If @@f(z)@@ is not meromorphic at @@c@@, the result is @@Undefined@@."""),
    ])

documentify(Residue,
    examples=[
    ("Residue(f(z), For(z, c))",
        "Residue of @@f(z)@@ at the point @@c@@."),
    ])


documentify(Path,
    examples=[
    ("Path(a, b, c)",
        """Represents the path formed by connecting the given points or paths by line segments.
        A path is a formal object, semantically different from a set of points: for a path object, the direction is significant,
        and it is undefined whether a path segment corresponds to an open interval or a closed interval between the points.,
        The typical application is to represent a path of integration."""),
    ("Path(1, -1)", "Represents the path going left from 1 to -1."),
    ("Path(a, Path(b, c))", "Equivalent to @Path(a, b, c))@."),
    ("Path(1, ConstI, -1, -ConstI, 1)",
        "Represents a diamond-shaped loop around the origin in the counterclockwise direction."),
    ("Path(-(ConstI*Infinity), ConstI*Infinity)",
        "Represents the imaginary axis traversed upwards."),
    ("Path(1, Exp(Pi*ConstI/4)*Infinity)",
        "Represents the ray from 1 to infinity along a 45 degree angle."),
    ("Path(Tuple(2, 1), Tuple(0, 0))",
        "Represents the line segment from @@Tuple(2, 1)@@ to the origin in @@CartesianPower(RR, 2)@@."),
    ])

documentify(CurvePath,
    examples=[
    ("CurvePath(f(t), For(t, a, b))",
        "Represents the path traced by @@f(t)@@ as @@t@@ follows the path @@Path(a, b)@@."),
    ("CurvePath(R*Exp(ConstI*t), For(t, 0, 2*Pi))",
        "Represents the circular path counterclockwise around the origin, starting at @@R@@."),
    ("CurvePath(R*Exp(ConstI*t), For(t, 0, -(2*Pi)))",
        "Represents the circular path clockwise around the origin, starting at @@R@@."),
    ("Path(+Infinity, CurvePath(Exp(ConstI*t), For(t, Pi/2, 3*Pi/2)), +Infinity)",
        """Represents the Hankel contour starting at @@+Infinity@@, moving along a straight line above the real axis to @@ConstI@@,
        moving in a half-circle around the origin to @@-ConstI@@,
        and returning to @@+Infinity@@ along a straight line below the real axis."""),
    ])

documentify(AnalyticContinuation,
    examples=[
    ("AnalyticContinuation(f(z), For(z, a, b))",
        """Analytic continuation.
        Represents the value (or limiting value) @@g(b)@@ where @@g(z)@@ is the unique analytic continuation along the path from @@a@@ to @@b@@
        for the function initially represented by @@f(z)@@.
        It is assumed that the expression @@f(z)@@ represents a holomorphic function of @@z@@ in a neighborhood of the initial point @@a@@.
        More generally, @@a@@ is allowed to be a pole, branch point or even an essential singularity as long as @@f(z)@@ is holomorphic locally in a cone around
        the path radiating from @@a@@.
        Infinite endpoints are allowed, with the obvious interpretation.
        Analytic continuation paths are allowed to pass through (isolated) poles of the analytically continued function.
        The path is not allowed to pass through intermediate branch points, but may end at a branch point."""),
    ("AnalyticContinuation(f(z), For(z, a, b))",
        "Represents the analytic continuation of @@f(z)@@ along the straight-line path from @@a@@ to @@b@@."),
    ("AnalyticContinuation(f(z), For(z, P))",
        "Represents the analytic continuation of @@f(z)@@ along the path object @@P@@."),
    ("AnalyticContinuation(f(z), For(z, Path(a, b, c)))",
        "Represents the analytic continuation of @@f(z)@@ along the straight-line path @@Path(a, b, c)@@."),
    ("AnalyticContinuation(f(z), For(z, CurvePath(Exp(ConstI*t), For(t, 0, theta))))",
        "Represents the analytic continuation of @@f(z)@@ along the circular path starting at @@Equal(z, 1)@@ and rotating counterclockwise by the phase @@theta@@."),
    ])

documentify(Sign,
    examples=[
    ("Sign(z)",
        "Sign function."),
    ])

documentify(Abs,
    examples=[
    ("Abs(z)",
        "Absolute value."),
    ])

documentify(Arg,
    examples=[
    ("Arg(z)",
        "Complex argument."),
    ])

documentify(Re,
    examples=[
    ("Re(z)",
        "Real part."),
    ])

documentify(Im,
    examples=[
    ("Im(z)",
        "Imaginary part."),
    ])

documentify(Conjugate,
    examples=[
    ("Conjugate(z)",
        "Complex conjugate."),
    ])

documentify(Csgn,
    examples=[
    ("Csgn(z)",
        "Real-valued sign function for complex numbers."),
    ])

documentify(RealAbs,
    examples=[
    ("RealAbs(z)",
        "Real-valued extension of absolute value."),
    ])

documentify(Max,
    examples=[
    ("Max(x, y)",
        "Maximum value."),
    ("Max(x_(1), Ellipsis, x_(n))",
        "Maximum out of several values. See also @Maximum@."),
    ])

documentify(Min,
    examples=[
    ("Min(x, y)",
        "Minimum value."),
    ("Min(x_(1), Ellipsis, x_(n))",
        "Minimum out of several values. See also @Minimum@."),
    ])

documentify(Floor,
    examples=[
    ("Floor(x)",
        "Floor function."),
    ])

documentify(Ceil,
    examples=[
    ("Ceil(x)",
        "Ceiling function."),
    ])

documentify(ConstGamma,
    examples=[
    ("ConstGamma",
        "The constant gamma (0.577...)."),
    ],
    numerical_examples=[
        ("ConstGamma",),
    ])

documentify(Pi,
    examples=[
    ("Pi",
        "The constant pi (3.14...)."),
    ],
    numerical_examples=[
        ("Pi",),
    ])

documentify(GoldenRatio,
    examples=[
    ("GoldenRatio",
        "The golden ratio (1.618...)."),
    ],
    numerical_examples=[
        ("GoldenRatio",),
    ])

documentify(ConstI,
    examples=[
    ("ConstI",
        "The imaginary unit."),
    ],
    numerical_examples=[
        ("ConstI",),
    ])

documentify(Exp,
    examples=[
    ("Exp(z)",
        "Exponential function"),
    ])

documentify(ConstE,
    examples=[
    ("ConstE",
        "The constant e (2.718...)."),
    ],
    numerical_examples=[
        ("ConstE",),
    ])

documentify(Sin,
    examples=[
    ("Sin(z)",
        "Sine."),
    ])

documentify(Cos,
    examples=[
    ("Cos(z)",
        "Cosine."),
    ])

documentify(Tan,
    examples=[
    ("Tan(z)",
        "Tangent."),
    ])

documentify(Cot,
    examples=[
    ("Cot(z)",
        "Cotangent."),
    ])

documentify(Sec,
    examples=[
    ("Sec(z)",
        "Secant."),
    ])

documentify(Csc,
    examples=[
    ("Csc(z)",
        "Cosecant."),
    ])

documentify(Sinh,
    examples=[
    ("Sinh(z)",
        "Hyperbolic sine."),
    ])

documentify(Cosh,
    examples=[
    ("Cosh(z)",
        "Hyperbolic cosine."),
    ])

documentify(Tanh,
    examples=[
    ("Tanh(z)",
        "Hyperbolic tangent."),
    ])

documentify(Coth,
    examples=[
    ("Coth(z)",
        "Hyperbolic cotangent."),
    ])

documentify(Sech,
    examples=[
    ("Sech(z)",
        "Hyperbolic secant."),
    ])

documentify(Csch,
    examples=[
    ("Csch(z)",
        "Hyperbolic cosecant."),
    ])

documentify(Asin,
    examples=[
    ("Asin(z)",
        "Inverse sine."),
    ])

documentify(Acos,
    examples=[
    ("Acos(z)",
        "Inverse cosine."),
    ])

documentify(Atan,
    examples=[
    ("Atan(z)",
        "Inverse tangent."),
    ])

documentify(Acot,
    examples=[
    ("Acot(z)",
        "Inverse cotangent."),
    ])

documentify(Asec,
    examples=[
    ("Asec(z)",
        "Inverse secant."),
    ])

documentify(Acsc,
    examples=[
    ("Acsc(z)",
        "Inverse cosecant."),
    ])

documentify(Asinh,
    examples=[
    ("Asinh(z)",
        "Inverse hyperbolic sine."),
    ])

documentify(Acosh,
    examples=[
    ("Acosh(z)",
        "Inverse hyperbolic cosine."),
    ])

documentify(Atanh,
    examples=[
    ("Atanh(z)",
        "Inverse hyperbolic tangent."),
    ])

documentify(Acoth,
    examples=[
    ("Acoth(z)",
        "Inverse hyperbolic cotangent."),
    ])

documentify(Asech,
    examples=[
    ("Asech(z)",
        "Inverse hyperbolic secant."),
    ])

documentify(Acsch,
    examples=[
    ("Acsch(z)",
        "Inverse hyperbolic cosecant."),
    ])

documentify(Sinc,
    examples=[
    ("Sinc(z)",
        "Sinc function."),
    ])

documentify(Atan2,
    examples=[
    ("Atan2(y, x)",
        "Two-argument inverse tangent."),
    ])

documentify(LambertW,
    examples=[
    ("LambertW(k, z)",
        "Lambert W-function."),
    ])

documentify(LambertWPuiseuxCoefficient,
    examples=[
    ("LambertWPuiseuxCoefficient(k)",
        "Coefficient in scaled Puiseux expansion of Lambert W-function."),
    ])

documentify(Odd,
    examples=[
    ("Odd(n)",
        "Odd predicate."),
    ])

documentify(Even,
    examples=[
    ("Even(n)",
        "Even predicate."),
    ])

documentify(CongruentMod,
    examples=[
    ("CongruentMod(a, b, m)",
        "Congruence predicate."),
    ])

documentify(Divides,
    examples=[
    ("Divides(d, n)",
        "Divisibility predicate."),
    ])

documentify(LegendreSymbol,
    examples=[
    ("LegendreSymbol(n,k)",
        "Legendre symbol."),
    ])

documentify(JacobiSymbol,
    examples=[
    ("JacobiSymbol(n,k)",
        "Jacobi symbol."),
    ])

documentify(KroneckerSymbol,
    examples=[
    ("KroneckerSymbol(n,k)",
        "Kronecker symbol."),
    ])

documentify(GCD,
    examples=[
    ("GCD(a, b)",
        "Greatest common divisor."),
    ])

documentify(LCM,
    examples=[
    ("LCM(a, b)",
        "Least common multiple."),
    ])

documentify(XGCD,
    examples=[
    ("XGCD(a, b)",
        "Extended greatest common divisor."),
    ])

documentify(Factorial,
    examples=[
    ("Factorial(n)",
        "Factorial."),
    ])

documentify(Binomial,
    examples=[
    ("Binomial(n, k)",
        "Binomial coefficient."),
    ])

documentify(RisingFactorial,
    examples=[
    ("RisingFactorial(z, k)",
        "Rising factorial."),
    ])

documentify(FallingFactorial,
    examples=[
    ("FallingFactorial(z, k)",
        "Falling factorial."),
    ])

documentify(Fibonacci,
    examples=[
    ("Fibonacci(n)",
        "Fibonacci number."),
    ])

documentify(Gamma,
    examples=[
    ("Gamma(z)",
        "Gamma function."),
    ],
    evaluation_examples=[
        ("Gamma(Div(17,2))",),
    ],
    numerical_examples=[
        ("Gamma(1+ConstI)",),
    ])

documentify(LogGamma,
    examples=[
    ("LogGamma(z)",
        "Logarithmic gamma function."),
    ])

documentify(DoubleFactorial,
    examples=[
    ("DoubleFactorial(n)",
        "Double factorial."),
    ])

documentify(HarmonicNumber,
    examples=[
    ("HarmonicNumber(n)",
        "Harmonic number."),
    ])

documentify(StirlingSeriesRemainder,
    examples=[
    ("StirlingSeriesRemainder(n, z)",
        "Remainder term in the Stirling series for the logarithmic gamma function"),
    ])

documentify(ChebyshevT,
    examples=[
    ("ChebyshevT(n, x)",
        "Chebyshev polynomial of the first kind."),
    ])

documentify(ChebyshevU,
    examples=[
    ("ChebyshevU(n, x)",
        "Chebyshev polynomial of the second kind."),
    ])

documentify(Log,
    examples=[
    ("Log(z)",
        "Natural logarithm."),
    ])

documentify(PartitionsP,
    examples=[
    ("PartitionsP(n)",
        "Integer partition function."),
    ])

documentify(HardyRamanujanA,
    examples=[
    ("HardyRamanujanA(n, k)",
        "Exponential sum in the Hardy-Ramanujan-Rademacher formula."),
    ])

documentify(RiemannZeta,
    examples=[
    ("RiemannZeta(s)",
        "Riemann zeta function."),
    ("RiemannZeta(s, 1)",
        "Differentiated Riemann zeta function."),
    ("RiemannZeta(s, r)",
        "Riemann zeta function differentiated to order @@r@@."),
    ],
    evaluation_examples=[
        ("RiemannZeta(4)",),
        ("RiemannZeta(0, 1)",),
    ],
    numerical_examples=[
        ("RiemannZeta(3)",),
    ])

documentify(RiemannZetaZero,
    examples=[
    ("RiemannZetaZero(n)",
        "Nontrivial zero of the Riemann zeta function."),
    ],
    numerical_examples=[
        ("RiemannZetaZero(10**3)",),
    ])

documentify(RiemannHypothesis,
    examples=[
    ("RiemannHypothesis",
        "The Riemann hypothesis. Semantically, @@Element(RiemannHypothesis, Set(True, False))@@."),
    ])

documentify(DeBruijnNewmanLambda,
    examples=[
    ("DeBruijnNewmanLambda",
        "De Bruijn-Newman constant."),
    ])

documentify(KeiperLiLambda,
    examples=[
    ("KeiperLiLambda(n)",
        "Keiper-Li coefficient."),
    ])

documentify(StieltjesGamma,
    examples=[
    ("StieltjesGamma(n, a)",
        "Stieltjes constant."),
    ])

documentify(AiryAi,
    examples=[
    ("AiryAi(z)",
        "Airy function of the first kind."),
    ("AiryAi(z, 1)",
        "Differentiated Airy function of the first kind."),
    ("AiryAi(z, r)",
        "Airy function of the first kind differentiated to order @@r@@."),
    ])

documentify(AiryBi,
    examples=[
    ("AiryBi(z)",
        "Airy function of the second kind."),
    ("AiryBi(z, 1)",
        "Differentiated Airy function of the second kind."),
    ("AiryBi(z, r)",
        "Airy function of the second kind differentiated to order @@r@@."),
    ])

documentify(AiryAiZero,
    examples=[
    ("AiryAiZero(n)",
        "The @@n@@-th real zero of @@AiryAi(x)@@ (@AiryAi@)."),
    ("AiryAiZero(n, 1)",
        "The @@n@@-th real zero of @@AiryAi(x,1)@@."),
    ("AiryAiZero(n, r)",
        "The @@n@@-th real zero of @@AiryAi(x,r)@@."),
    ])

documentify(AiryBiZero,
    examples=[
    ("AiryBiZero(n)",
        "The @@n@@-th real zero of @@AiryBi(x)@@ (@AiryBi@)."),
    ("AiryBiZero(n, 1)",
        "The @@n@@-th real zero of @@AiryBi(x,1)@@."),
    ("AiryBiZero(n, r)",
        "The @@n@@-th real zero of @@AiryBi(x,r)@@."),
    ])


documentify(BesselJ,
    examples=[
    ("BesselJ(nu, z)",
        "Bessel function of the first kind."),
    ("BesselJ(nu, z, 1)",
        "Differentiated Bessel function of the first kind."),
    ("BesselJ(nu, z, r)",
        "Bessel function of the first kind differentiated to order @@r@@."),
    ])

documentify(BesselY,
    examples=[
    ("BesselY(nu, z)",
        "Bessel function of the second kind."),
    ("BesselY(nu, z, 1)",
        "Differentiated Bessel function of the second kind."),
    ("BesselY(nu, z, r)",
        "Bessel function of the second kind differentiated to order @@r@@."),
    ])

documentify(BesselI,
    examples=[
    ("BesselI(nu, z)",
        "Modified Bessel function of the first kind."),
    ("BesselI(nu, z, 1)",
        "Differentiated modified Bessel function of the first kind."),
    ("BesselI(nu, z, r)",
        "Modified Bessel function of the first kind differentiated to order @@r@@."),
    ])

documentify(BesselK,
    examples=[
    ("BesselK(nu, z)",
        "Modified Bessel function of the second kind."),
    ("BesselK(nu, z, 1)",
        "Differentiated modified Bessel function of the second kind."),
    ("BesselK(nu, z, r)",
        "Modified Bessel function of the second kind differentiated to order @@r@@."),
    ])

documentify(HankelH1,
    examples=[
    ("HankelH1(nu, z)",
        "Hankel function of the first kind."),
    ])

documentify(HankelH2,
    examples=[
    ("HankelH2(nu, z)",
        "Hankel function of the second kind."),
    ])

documentify(BesselJZero,
    examples=[
    ("BesselJZero(nu, n)",
        "The @@n@@-th real zero of @@BesselJ(nu, x)@@ (@BesselJ@)."),
    ("BesselJZero(nu, n, 1)",
        "The @@n@@-th real zero of @@BesselJ(nu, x, 1)@@."),
    ("BesselJZero(nu, n, r)",
        "The @@n@@-th real zero of @@BesselJ(nu, x, r)@@."),
    ])

documentify(BesselYZero,
    examples=[
    ("BesselYZero(nu, n)",
        "The @@n@@-th real zero of @@BesselY(nu, x)@@ (@BesselY@)."),
    ("BesselYZero(nu, n, 1)",
        "The @@n@@-th real zero of @@BesselY(nu, x, 1)@@."),
    ("BesselYZero(nu, n, r)",
        "The @@n@@-th real zero of @@BesselY(nu, x, r)@@."),
    ])

documentify(CoulombF,
    examples=[
    ("CoulombF(ell, eta, z)",
        "Regular Coulomb wave function."),
    ])

documentify(CoulombG,
    examples=[
    ("CoulombG(ell, eta, z)",
        "Irregular Coulomb wave function."),
    ])

documentify(CoulombH,
    examples=[
    ("CoulombH(omega, ell, eta, z)",
        "Outgoing or ingoing Coulomb wave function."),
    ])

documentify(CoulombC,
    examples=[
    ("CoulombC(ell, eta)",
        "Coulomb wave function Gamow factor."),
    ])

documentify(CoulombSigma,
    examples=[
    ("CoulombSigma(ell, eta)",
        "Coulomb wave function phase shift."),
    ])

documentify(BernoulliB,
    examples=[
    ("BernoulliB(n)",
        "Bernoulli number."),
    ])

documentify(EulerE,
    examples=[
    ("EulerE(n)",
        "Euler number."),
    ])

documentify(BernoulliPolynomial,
    examples=[
    ("BernoulliPolynomial(n, z)",
        "Bernoulli polynomial."),
    ])

documentify(EulerPolynomial,
    examples=[
    ("EulerPolynomial(n)",
        "Euler polynomial."),
    ])

documentify(StirlingCycle,
    examples=[
    ("StirlingCycle(n, k)",
        "Unsigned Stirling number of the first kind."),
    ])

documentify(StirlingS1,
    examples=[
    ("StirlingS1(n, k)",
        "Signed Stirling number of the first kind."),
    ])

documentify(StirlingS2,
    examples=[
    ("StirlingS2(n, k)",
        "Stirling number of the second kind."),
    ])

documentify(HH,
    examples=[
    ("HH",
        "Upper complex half-plane."),
    ])

documentify(Hypergeometric2F1,
    examples=[
    ("Hypergeometric2F1(a, b, c, z)",
        "Gauss hypergeometric function."),
    ],
    numerical_examples=[
        ("Hypergeometric2F1(2, 3, 4, -5)",),
    ])

documentify(Hypergeometric2F1Regularized,
    examples=[
    ("Hypergeometric2F1Regularized(a, b, c, z)",
        "Regularized Gauss hypergeometric function."),
    ],
    numerical_examples=[
        ("Hypergeometric2F1Regularized(2, 3, 4, -5)",),
    ])

documentify(Hypergeometric3F2,
    examples=[
    ("Hypergeometric3F2(a, b, c, d, e, z)",
        "A generalized hypergeometric function."),
    ])

documentify(Hypergeometric3F2Regularized,
    examples=[
    ("Hypergeometric3F2Regularized(a, b, c, d, e, z)",
        "A regularized generalized hypergeometric function."),
    ])

documentify(Hypergeometric0F1,
    examples=[
    ("Hypergeometric0F1(a, z)",
        "Confluent hypergeometric limit function."),
    ],
    numerical_examples=[
        ("Hypergeometric0F1(3, 4)",),
    ])

documentify(Hypergeometric0F1Regularized,
    examples=[
    ("Hypergeometric0F1Regularized(a, z)",
        "Regularized confluent hypergeometric limit function."),
    ],
    numerical_examples=[
        ("Hypergeometric0F1Regularized(3, 4)",),
    ])

documentify(Hypergeometric1F1,
    examples=[
    ("Hypergeometric1F1(a, b, z)",
        "Kummer confluent hypergeometric function."),
    ],
    numerical_examples=[
        ("Hypergeometric1F1(2, 3, 4)",),
    ])

documentify(Hypergeometric1F1Regularized,
    examples=[
    ("Hypergeometric1F1Regularized(a, b, z)",
        "Regularized Kummer confluent hypergeometric function."),
    ],
    numerical_examples=[
        ("Hypergeometric1F1Regularized(2, 3, 4)",),
    ])

documentify(HypergeometricU,
    examples=[
    ("HypergeometricU(a, b, z)",
        "Tricomi confluent hypergeometric function."),
    ],
    numerical_examples=[
        ("HypergeometricU(1, 3, 6)",),
    ])

documentify(HypergeometricUStar,
    examples=[
    ("HypergeometricUStar(a, b, z)",
        "Scaled Tricomi confluent hypergeometric function."),
    ],
    numerical_examples=[
        ("HypergeometricUStar(1, 3, 6)",),
    ])

documentify(Hypergeometric2F0,
    examples=[
    ("Hypergeometric2F0(a, b, z)",
        "A version of the Tricomi confluent hypergeometric function."),
    ],
    numerical_examples=[
        ("Hypergeometric2F0(3, 4, 5)",),
    ])

documentify(HypergeometricUStarRemainder,
    examples=[
    ("HypergeometricUStarRemainder(n, a, b, z)",
        "Error term in the asymptotic expansion of the Tricomi confluent hypergeometric function."),
    ])

documentify(Erf,
    examples=[
    ("Erf(z)",
        "Error function."),
    ])

documentify(Erfc,
    examples=[
    ("Erfc(z)",
        "Complementary error function."),
    ])

documentify(Erfi,
    examples=[
    ("Erfi(z)",
        "Imaginary error function."),
    ])

documentify(UpperGamma,
    examples=[
    ("UpperGamma(s,z)",
        "Upper incomplete gamma function."),
    ])

documentify(LowerGamma,
    examples=[
    ("LowerGamma(s,z)",
        "Lower incomplete gamma function."),
    ])

documentify(SinIntegral,
    examples=[
    ("SinIntegral(z)",
        "Sine integral."),
    ])


documentify(JacobiTheta,
    examples=[
    ("JacobiTheta(j, z, tau)",
        "Jacobi theta function."),
    ("JacobiTheta(j, z, tau, 1)",
        "Jacobi theta function, differentiated with respect to @@z@@."),
    ("JacobiTheta(j, z, tau, r)",
        "Jacobi theta function, differentiated @@r@@ times with respect to @@z@@."),
    ])

documentify(JacobiThetaPermutation,
    examples=[
    ("JacobiThetaPermutation(j, a, b, c, d)",
        "Index permutation in modular transformation of Jacobi theta functions."),
    ])

documentify(JacobiThetaEpsilon,
    examples=[
    ("JacobiThetaEpsilon(j, a, b, c, d)",
        "Root of unity in modular transformation of Jacobi theta functions."),
    ])

documentify(WeierstrassP,
    examples=[
    ("WeierstrassP(z, tau)",
        "Weierstrass elliptic function."),
    ])

documentify(WeierstrassZeta,
    examples=[
    ("WeierstrassZeta(z, tau)",
        "Weierstrass zeta function."),
    ])

documentify(WeierstrassSigma,
    examples=[
    ("WeierstrassSigma(z, tau)",
        "Weierstrass sigma function."),
    ])

documentify(Lattice,
    examples=[
    ("Lattice(a, b)",
        "Complex lattice with periods @@a@@, @@b@@."),
    ])

documentify(PP,
    examples=[
    ("PP",
        "The set of prime numbers."),
    ])

documentify(PrimeNumber,
    examples=[
    ("PrimeNumber(n)",
        "The @@n@@-th prime number."),
    ])

documentify(PrimePi,
    examples=[
    ("PrimePi(x)",
        "Prime counting function."),
    ])

documentify(PSL2Z,
    examples=[
    ("PSL2Z",
        "Modular group (canonical representatives)."),
    ])

documentify(ModularGroupAction,
    examples=[
    ("ModularGroupAction(gamma, tau)",
        "Action of the modular group."),
    ])

documentify(ModularGroupFundamentalDomain,
    examples=[
    ("ModularGroupFundamentalDomain",
        "Fundamental domain for action of the modular group."),
    ])

documentify(ModularJ,
    examples=[
    ("ModularJ(tau)",
        "Modular @@j@@-invariant."),
    ],
    numerical_examples=[
        ("ModularJ(ConstI)",),
    ])

documentify(PrimitiveReducedPositiveIntegralBinaryQuadraticForms,
    examples=[
    ("PrimitiveReducedPositiveIntegralBinaryQuadraticForms(D)",
        "Primitive reduced positive integral binary quadratic forms."),
    ])

documentify(HilbertClassPolynomial,
    examples=[
    ("HilbertClassPolynomial(D, x)",
        "Hilbert class polynomial."),
    ])

documentify(DedekindEta,
    examples=[
    ("DedekindEta(tau)",
        "Dedekind eta function."),
    ],
    numerical_examples=[
        ("DedekindEta(ConstI)",),
    ])

documentify(EulerQSeries,
    examples=[
    ("EulerQSeries(q)",
        "Euler's q-series."),
    ])

documentify(DedekindEtaEpsilon,
    examples=[
    ("DedekindEtaEpsilon(a, b, c, d)",
        "Root of unity in the functional equation of the Dedekind eta function."),
    ])

documentify(DedekindSum,
    examples=[
    ("DedekindSum(n, k)",
        "Dedekind sum."),
    ])

documentify(EisensteinG,
    examples=[
    ("EisensteinG(k, tau)",
        "Eisenstein series."),
    ])

documentify(EisensteinE,
    examples=[
    ("EisensteinE(k, tau)",
        "Normalized Eisenstein series."),
    ])

documentify(ModularLambda,
    examples=[
    ("ModularLambda(tau)",
        "Modular lambda function."),
    ])

documentify(ModularLambdaFundamentalDomain,
    examples=[
    ("ModularLambdaFundamentalDomain",
        "Fundamental domain of the modular lambda function (@ModularLambda@)."),
    ])

documentify(DirichletGroup,
    examples=[
    ("DirichletGroup(q)",
        "Dirichlet characters with given modulus."),
    ])

documentify(PrimitiveDirichletCharacters,
    examples=[
    ("PrimitiveDirichletCharacters(q)",
        "Primitive Dirichlet characters with given modulus."),
    ])

documentify(DirichletCharacter,
    examples=[
    ("DirichletCharacter(q, ell)",
        "Dirichlet character with Conrey label @@(q, ell)@@. The Conrey label consists of integers @@Element(q, ZZGreaterEqual(1))@@ and @@Element(ell, Range(1, Sub(Max(q, 2), 1)))@@ such that @@Equal(GCD(ell, q), 1)@@."),
    ("DirichletCharacter(q, ell, n)",
        "Evaluation of a Dirichlet character at the integer @@n@@."),
    ("Where(chi(n), Def(chi, DirichletCharacter(q, ell)))",
        "Evaluation of a Dirichlet character at the integer @@n@@."),
    ])

documentify(ConreyGenerator,
    examples=[
    ("ConreyGenerator(p)",
        "Conrey generator."),
    ])

documentify(DiscreteLog,
    examples=[
    ("DiscreteLog(x, b, m)",
        "Discrete logarithm."),
    ])

documentify(DirichletL,
    examples=[
    ("DirichletL(s, chi)",
        "Dirichlet L-function."),
    ],
    numerical_examples=[
        ("DirichletL(2, DirichletCharacter(4, 3))",),
    ])

documentify(GeneralizedBernoulliB,
    examples=[
    ("GeneralizedBernoulliB(n, chi)",
        "Generalized Bernoulli number."),
    ])

documentify(DirichletLZero,
    examples=[
    ("DirichletLZero(n, chi)",
        "Nontrivial zero of Dirichlet L-function."),
    ])

documentify(GeneralizedRiemannHypothesis,
    examples=[
    ("GeneralizedRiemannHypothesis",
        "Generalized Riemann hypothesis. Semantically, @@Element(GeneralizedRiemannHypothesis, Set(True, False))@@."),
    ])

documentify(DirichletLambda,
    examples=[
    ("DirichletLambda(s, chi)",
        "Completed Dirichlet L-function."),
    ])

documentify(GaussSum,
    examples=[
    ("GaussSum(q, chi)",
        "Gauss sum."),
    ])

documentify(BetaFunction,
    examples=[
    ("BetaFunction(a, b)",
        "Beta function."),
    ])

documentify(IncompleteBeta,
    examples=[
    ("IncompleteBeta(x, a, b)",
        "Incomplete beta function."),
    ])

documentify(IncompleteBetaRegularized,
    examples=[
    ("IncompleteBetaRegularized(x, a, b)",
        "Regularized incomplete beta function."),
    ])

documentify(Totient,
    examples=[
    ("Totient(n)",
        "Euler totient function."),
    ])

documentify(LandauG,
    examples=[
    ("LandauG(n)",
        "Landau's function."),
    ])

documentify(ConstCatalan,
    examples=[
    ("ConstCatalan",
        "Catalan's constant."),
    ],
    numerical_examples=[
        ("ConstCatalan",),
    ])

documentify(DigammaFunction,
    examples=[
    ("DigammaFunction(z)",
        "Digamma function."),
    ("DigammaFunction(z, 1)",
        "Differentiated digamma function (trigamma function)."),
    ("DigammaFunction(z, n)",
        "Polygamma function (@@n@@-times differentiated digamma function)."),
    ])

documentify(DigammaFunctionZero,
    examples=[
    ("DigammaFunctionZero(n)",
        "Zero of the digamma function."),
    ])

documentify(SloaneA,
    examples=[
    ("SloaneA(X, n)",
        "Sequence X in Sloane's OEIS."),
    ])

documentify(MultiZetaValue,
    examples=[
    ("MultiZetaValue(s_(1), Ellipsis, s_(n))",
        "Multiple zeta value (MZV) of @@n@@ variables."),
    ])

documentify(BellNumber,
    examples=[
    ("BellNumber(n)",
        "Bell number."),
    ])

documentify(BarnesG,
    examples=[
    ("BarnesG(z)",
        "Barnes G-function."),
    ])

documentify(LogBarnesG,
    examples=[
    ("LogBarnesG(z)",
        "Logarithmic Barnes G-function."),
    ])

documentify(LogBarnesGRemainder,
    examples=[
    ("LogBarnesGRemainder(N, z)",
        "Remainder term in the asymptotic expansion of the logarithmic Barnes G-function."),
    ])

documentify(HalphenConstant,
    examples=[
    ("HalphenConstant",
        "Halphen's constant (one-ninth constant) 0.10765..."),
    ])

documentify(EllipticK,
    examples=[
    ("EllipticK(m)",
        "Legendre complete elliptic integral of the first kind."),
    ])

documentify(EllipticE,
    examples=[
    ("EllipticE(m)",
        "Legendre complete elliptic integral of the second kind."),
    ])

documentify(EllipticPi,
    examples=[
    ("EllipticPi(n, m)",
        "Legendre complete elliptic integral of the third kind."),
    ])

documentify(EllipticPi,
    examples=[
    ("EllipticPi(n, m)",
        "Legendre complete elliptic integral of the third kind."),
    ])

documentify(IncompleteEllipticF,
    examples=[
    ("IncompleteEllipticF(phi, m)",
        "Legendre incomplete elliptic integral of the first kind."),
    ])

documentify(IncompleteEllipticE,
    examples=[
    ("IncompleteEllipticE(phi, m)",
        "Legendre incomplete elliptic integral of the second kind."),
    ])

documentify(IncompleteEllipticPi,
    examples=[
    ("IncompleteEllipticPi(n, phi, m)",
        "Legendre incomplete elliptic integral of the third kind."),
    ])

documentify(CarlsonRF,
    examples=[
    ("CarlsonRF(x, y, z)",
        "Carlson symmetric elliptic integral of the first kind."),
    ])

documentify(CarlsonRG,
    examples=[
    ("CarlsonRG(x, y, z)",
        "Carlson symmetric elliptic integral of the second kind."),
    ])

documentify(CarlsonRJ,
    examples=[
    ("CarlsonRJ(x, y, z, w)",
        "Carlson symmetric elliptic integral of the third kind."),
    ])

documentify(CarlsonRD,
    examples=[
    ("CarlsonRD(x, y, z)",
        "Special case of the Carlson symmetric elliptic integral of the third kind."),
    ])

documentify(CarlsonRC,
    examples=[
    ("CarlsonRC(x)",
        "Special case of the Carlson symmetric elliptic integral of the third kind."),
    ])

documentify(AGM,
    examples=[
    ("AGM(x, y)",
        "Arithmetic-geometric mean."),
    ],
    evaluation_examples=[
        ("AGM(1, 3 + 2*Sqrt(2))",),
    ])


documentify(SquaresR,
    examples=[
    ("SquaresR(k, n)",
        "Sum of squares function."),
    ])

documentify(LiouvilleLambda,
    examples=[
    ("LiouvilleLambda(n)",
        "Liouville function."),
    ])

documentify(DivisorSigma,
    examples=[
    ("DivisorSigma(k, n)",
        "Sum of divisors function."),
    ])

documentify(MoebiusMu,
    examples=[
    ("MoebiusMu(n)",
        "Möbius function."),
    ])

documentify(KroneckerDelta,
    examples=[
    ("KroneckerDelta(x, y)",
        "Kronecker delta."),
    ])

documentify(LegendrePolynomial,
    examples=[
    ("LegendrePolynomial(n, z)",
        "Legendre polynomial."),
    ])

documentify(LegendrePolynomialZero,
    examples=[
    ("LegendrePolynomialZero(n, k)",
        "Legendre polynomial zero."),
    ])

documentify(GaussLegendreWeight,
    examples=[
    ("GaussLegendreWeight(n, k)",
        "Gauss-Legendre quadrature weight."),
    ])

documentify(HermitePolynomial,
    examples=[
    ("HermitePolynomial(n, z)",
        "Hermite polynomial."),
    ])

documentify(BernsteinEllipse,
    examples=[
    ("BernsteinEllipse(rho)",
        "Bernstein ellipse with foci -1, +1 and semi-axis sum @@rho@@."),
    ])

documentify(UnitCircle,
    examples=[
    ("UnitCircle",
        "The complex unit circle."),
    ])

documentify(LogIntegral,
    examples=[
    ("LogIntegral(z)",
        "Logarithmic integral."),
    ])

documentify(RiemannXi,
    examples=[
    ("RiemannXi(s)",
        "Riemann xi-function."),
    ])

documentify(List,
    examples=[
    ("List(Ellipsis)",
        "List with given elements. A @List@ and a @Tuple@ are actually the same object and indistinguishable semantically; the only difference is in the printing of the expression with an explicit @Tuple@ or @List@ head."),
    ])

documentify(Tuple,
    examples=[
    ("Tuple(Ellipsis)",
        "Tuple with given elements."),
    ("Tuple(a, b)",
        "Tuple with two elements."),
    ("Tuple(a)",
        "Tuple with a single element. The 1-tuple is not equal to @a@."),
    ("Tuple()",
        "The empty tuple."),
    ("Tuple(c_(i), For(i, 0, n))",
        "Tuple constructed by a generator expression."),
    ])

documentify(Cyclotomic,
    examples=[
    ("Cyclotomic(n, z)",
        "Cyclotomic polynomial."),
    ])

documentify(SymmetricPolynomial,
    examples=[
    ("SymmetricPolynomial(n, X_(1), Ellipsis, X_(k))",
        "Elementary symmetric polynomial of degree @@n@@ in @@k@@ variables."),
    ("Equal(SymmetricPolynomial(2, X, Y, Z), X*Y + X*Z + Y*Z)",
        "An elementary symmetric polynomial in three variables."),
    ])

documentify(Pos,
    examples=[
    ("Pos(x)",
        "Represents the identity function for numerical values."),
    ("+x",
        "Using Python syntax."),
    ])

documentify(Neg,
    examples=[
    ("Neg(x)",
        "Negation."),
    ("-x",
        "Negation written using Python syntax."),
    ])

documentify(Add,
    examples=[
    ("Add(x, y)",
        "Addition."),
    ("Add(x, y, z)",
        "Addition of multiple terms."),
    ("x + y",
        "Addition written using infix syntax in Python."),
    ])

documentify(Sub,
    examples=[
    ("Sub(x, y)",
        "Subtraction."),
    ("x - y",
        "Subtraction written using infix syntax in Python."),
    ])

documentify(Mul,
    examples=[
    ("Mul(x, y)",
        "Multiplication."),
    ("Mul(x, y, z)",
        "Multiplication of multiple factors."),
    ("x * y",
        "Multiplication written using infix syntax in Python."),
    ])

documentify(Div,
    examples=[
    ("Div(x, y)",
        "Division."),
    ("x / y",
        "Division written using infix syntax in Python."),
    ])

documentify(Pow,
    examples=[
    ("Pow(x, y)",
        "Exponentiation."),
    ("x ** y",
        "Exponentiation written using infix syntax in Python."),
    ])

documentify(Sqrt,
    examples=[
    ("Sqrt(x)",
        "Principal square root."),
    ],
    evaluation_examples=[
        ("Sqrt(-4)",),
    ]
)

documentify(LessEqual,
    examples=[
    ("LessEqual(x, y)",
        "Inequality."),
    ("LessEqual(x, y, z)",
        "Chain of inequalities."),
    ])

documentify(Less,
    examples=[
    ("Less(x, y)",
        "Inequality."),
    ("Less(x, y, z)",
        "Chain of inequalities."),
    ])

documentify(GreaterEqual,
    examples=[
    ("GreaterEqual(x, y)",
        "Inequality."),
    ("GreaterEqual(x, y, z)",
        "Chain of inequalities."),
    ])

documentify(Greater,
    examples=[
    ("Greater(x, y)",
        "Inequality."),
    ("Greater(x, y, z)",
        "Chain of inequalities."),
    ])


'''
import pygrim.formulas
from pygrim.expr import descriptions

ss = ""
for symb in descriptions:
    if symb not in documentified:
        example, _, _, desc = descriptions[symb]
        #documentify(symb, examples=[(str(example), desc)])
        ss += """documentify(%s,
    examples=[
    ("%s",
        "%s"),
    ])

""" % (str(symb), str(example), str(desc))

print(ss)
'''

indexed.close()

