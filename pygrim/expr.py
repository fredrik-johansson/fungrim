# -*- coding: utf-8 -*-

int_types = (int, type(1<<128))

katex_function = []

int_cache = {}

def escape_title(name):
    # paren = name.find("(")
    # if paren >= 0:
    #     name = name[:paren].rstrip(" ")
    return name.replace(" ", "_")

class Expr(object):
    """
    Represents a symbolic expression.

    A symbolic expression is either an atom (symbol, integer or text)
    or a non-atomic expression representing a function application
    f(a, b, ...) where f and a, b, ... are symbolic expressions.

    The methods .is_atom(), and specifically .is_symbol(), .is_integer(),
    .is_text() are useful to check for atoms.

    For a non-atomic expression expr, expr.head() returns f and
    expr.args() returns (a, b, ...) as a Python tuple.
    For a non-atomic expression, these methods both return None.

    Expr objects are immutable and instances may be cached silently.

    Most arithmetic operators are overloaded to permit constructing
    expressions in natural syntax, but the == and != operators
    perform structural comparison.
    """

    def __new__(self, arg=None, symbol_name=None, call=None):
        """
        Expr(expr) creates a copy of expr (this may actually return
        the same object).

        Expr(5) creates an Integer atom with the value 5.
        Expr("text") creates a Text atom with the value "text".
        Expr(symbol_name="x") creates a Symbol atom with the label "x".

        Expr(call=(f, a, b)) creates the non-atomic expression f(a, b).
        """
        if isinstance(arg, Expr):
            return arg
        self = object.__new__(Expr)
        self._hash = None
        self._symbol = None
        self._integer = None
        self._text = None
        self._args = None
        if symbol_name is not None:
            self._symbol = symbol_name
        elif isinstance(arg, str):
            self._text = arg
        elif isinstance(arg, int_types):
            self._integer = int(arg)
        elif call is not None:
            self._args = tuple(Expr(obj) for obj in call)
            assert len(self._args) >= 1
        return self

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if hash(self) != hash(other):
            return False
        if self._args is not None:
            if other._args is not None:
                return self._args == other._args
            return False
        if self._symbol is not None:
            if other._symbol is not None:
                return self._symbol == other._symbol
            return False
        if self._integer is not None:
            if other._integer is not None:
                return self._integer == other._integer
            return False
        if self._text is not None:
            if other._text is not None:
                return self._text == other._text
            return False
        return False

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        if self._hash is None:
            if self._symbol is not None:
                self._hash = hash(self._symbol)
            elif self._integer is not None:
                self._hash = hash(self._integer)
            elif self._text is not None:
                self._hash = hash(self._text)
            else:
                self._hash = hash(self._args)
        return self._hash

    def __int__(self):
        return int(self._integer)

    def is_atom(self):
        """Returns True if self is an atom (symbol, integer or text),
        False otherwise."""
        return self._args is None

    def is_symbol(self):
        return self._symbol is not None

    def is_integer(self):
        return self._integer is not None

    def is_text(self):
        return self._text is not None

    def head(self):
        if self._args is None:
            return None
        return self._args[0]

    def args(self):
        if self._args is None:
            return None
        return self._args[1:]

    def __call__(self, *args):
        return Expr(call=((self,) + args))

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
            if self._args[0] == Entry:
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

    def atoms(self, unique=False):
        """
        Generate all atoms in this expression. With unique=True, avoids
        repetitions.
        """
        if self.is_atom():
            yield self
        else:
            if unique:
                seen = set()
                for arg in self._args:
                    for atom in arg.atoms():
                        if atom not in seen:
                            yield atom
                            seen.add(atom)
            else:
                for arg in self._args:
                    for atom in arg.atoms():
                        yield atom

    def symbols(self, unique=False):
        """
        Generate all symbols in this expression. With unique=True, avoids
        repetitions.
        """
        if self.is_symbol():
            yield self
        elif not self.is_atom():
            if unique:
                seen = set()
                for arg in self._args:
                    for symbol in arg.symbols():
                        if symbol not in seen:
                            yield symbol
                            seen.add(symbol)
            else:
                for arg in self._args:
                    for symbol in arg.symbols():
                        yield symbol

    def subexpressions(self, unique=False):
        """
        Generate all subexpressions of this expression (including the
        root expression). With unique=True, avoids repetitions.
        """
        yield self
        if not self.is_atom():
            if unique:
                seen = set()
                for arg in self._args:
                    for expr in arg.subexpressions():
                        if expr not in seen:
                            yield expr
                            seen.add(expr)
            else:
                for arg in self._args:
                    for expr in arg.subexpressions():
                        yield expr

    def replace(self, rules):
        """
        Replace subexpressions of self with exact matches in the given
        dictionary. Warning: does not treat locally bound variables specially.
        """
        if self in rules:
            return rules[self]
        if self.is_atom():
            return self
        return Expr(call=(arg.replace(rules) for arg in self._args))

    # needs work
    def need_parens_in_mul(self):
        if self.is_atom():
            if self.is_integer() and self._integer < 0:
                return True
            return False
        # if self._args[0] in (Pos, Neg):
        #     return True
        if self._args[0] in (Add, Sub):
            return True
        return False

    # needs work
    def show_exponential_as_power(self, allow_div=True):
        if self.is_atom():
            return True
        head = self._args[0]
        if head == Div:
            if not self._args[-1].is_atom():
                return False
            allow_div = False
        if head not in (Pos, Neg, Add, Sub, Mul, Div, Pow, Abs, Sqrt):
            return False
        for arg in self._args[1:]:
            if not arg.show_exponential_as_power(allow_div=allow_div):
                return False
        return True

    def latex(self, in_small=False):
        from .latex import latex
        return latex(self, in_small=in_small)

    def _can_render_html(self):
        if self.is_integer():
            return True
        if self.head() == Decimal:
            return True
        if self.head() == Div and self.args()[0].is_integer() and self.args()[1].is_integer():
            return True
        if self.head() == Tuple:
            return all(arg._can_render_html() for arg in self.args())
        if self.head() == Set:
            return all(arg._can_render_html() for arg in self.args())
        return False

    def html(self, display=False, avoid_latex=False, single=False):
        katex = katex_function[0]
        if self.is_atom():
            if avoid_latex and self.is_integer():
                return str(self._integer)
            return katex(self.latex(), display=display)
        if self.head() == Decimal and avoid_latex:
            text = self.args()[0]._text
            if "e" in text:
                mant, expo = text.split("e")
                expo = expo.lstrip("+")
                text = mant + " &middot; 10<sup>" + expo + "</sup>"
            return text
        if self.head() == Div and avoid_latex and self.args()[0].is_integer() and self.args()[1].is_integer():
            p, q = self.args()
            return "%s/%s" % (str(self.args()[0]._integer), str(self.args()[1]._integer))
        if self.head() == Neg and avoid_latex and self.args()[0]._can_render_html():
            return "-" + self.args()[0].html(display=display, avoid_latex=True)
        if self.head() == Tuple and avoid_latex and self._can_render_html():
            return "(" + ", ".join(a.html(display=display, avoid_latex=True) for a in self.args()) + ")"
        if self.head() == Set and avoid_latex and self._can_render_html():
            return "{" + ", ".join(a.html(display=display, avoid_latex=True) for a in self.args()) + "}"
        if self.head() == Table:
            return self.html_Table()
        if self.head() == Formula:
            return katex(self._args[1].latex())
        if self.head() == References:
            return self.html_References()
        if self.head() == Assumptions:
            return self.html_Assumptions()
        if self.head() == Description:
            return self.html_Description(display=display)
        if self.head() == SymbolDefinition:
            return self.html_SymbolDefinition()
        if self.head() == Image:
            return self.html_Image(single=single)
        return katex(self.latex(), display=display)

    def html_Image(self, single=False):
        description, image = self.args()
        path = image.args()[0]._text
        s = ""
        s += """<div style="text-align:center; margin:0.6em 0.4em 0.0em 0.2em">"""
        s += """<span style="font-size:85%; color:#888">Image:</span> """
        s += description.html()

        imgid = path

        # hack: duplicated constants in html head
        thumb_size = "140px"
        full_size = "400px"

        if single and 0:
            s += """<div style="text-align:center; padding-right:1em">"""
            s += """<img id="%s", src="../../img/%s.svg" style="height:%s; margin-top:0.3em; margin-bottom:0px"/>""" % (imgid, path, full_size)
            s += """</div>"""
        else:
            s += """<button style="margin:0 0 0 0.3em" onclick="toggleBig('%s', '../../img/%s_small.svg', '../../img/%s.svg')">Big &#x1F50D;</button>""" % (imgid, path, path)
            s += """<div style="text-align:center; padding-right:1em;">"""
            s += """<img id="%s", src="../../img/%s_small.svg" style="width:%s; max-width:100%%; margin-top:0.3em; margin-bottom:0px"/>""" % (imgid, path, thumb_size)
            s += """</div>"""

        s += """</div>"""
        return s


    def html_Table(self):
        rel = self.get_arg_with_head(TableRelation)
        heads = self.get_arg_with_head(TableHeadings)
        if heads is None:
            heads = self.get_arg_with_head(TableValueHeadings)
        data = self.get_arg_with_head(List)
        split = self.get_arg_with_head(TableSplit)
        colheads = self.get_arg_with_head(TableColumnHeadings)
        headrows = []
        if split is None:
            split = 1
        else:
            split = split.args()[0]._integer
        if heads is None:
            cols = len(data.args()[0].args())
        else:
            cols = len(heads.args())
        num = len(data.args())
        innum = num // split
        s = """<div style="overflow-x:auto;">"""
        s += """<table align="center" style="border:0; background-color:#fff;">"""
        s += """<tr style="border:0; background-color:#fff">"""
        j = 0
        for outer in range(split):
            s += """<td style="border:0; background-color:#fff; vertical-align:top;">"""
            s += """<table style="float: left; margin-right: 1em;">"""
            if heads is not None:
                s += "<tr>"
                for col in heads.args():
                    # the nowrap is a hack to avoid "n \ k" breaking
                    s += """<th style="white-space:nowrap;">""" + col.html(display=False, avoid_latex=True) + "</th>"
                s += "</tr>"
            if outer == split-1:
                end = num
            else:
                end = innum*(outer+1)
            for row in data.args()[innum*outer : end]:
                s += "<tr>"
                if row.head() == TableSection:
                    s += """<td colspan="%i" style="text-align:center; font-weight: bold">%s</td>""" % (cols, row.args()[0]._text)
                else:
                    if colheads is not None:
                        col = colheads.args()[j]
                        s += "<th>" + col.html(display=False, avoid_latex=True) + "</th>"
                    for i, col in enumerate(row.args()):
                        s += "<td>" + col.html(display=False, avoid_latex=True) + "</td>"
                s += "</tr>"
                j += 1
            s += """</table>"""
            s += "</td>"
        s += "</tr></table></div>"
        if rel is not None:
            s += """<div style="text-align:center; margin-top: 0.5em">"""
            s += Description("Table data:", rel.args()[0], " such that ", rel.args()[1]).html(display=True)
            s += """</div>"""
        return s

    def html_References(self):
        s = ""
        s += """<div class="entrysubhead">References:</div>"""
        s += "<ul>"
        for ref in self._args[1:]:
            s += "<li>%s</li>" % ref._text
        s += "</ul>"
        return s

    def html_Assumptions(self):
        s = ""
        #s += """<div class="entrysubhead">Assumptions:</div>"""

        #for arg in self.args():
        #    s += arg.html(display=True)
        #return s
        num = 1
        for arg in self.args():
            s += """<div style="text-align:center; margin:0.8em">"""
            if num == 1:
                strcond = "Assumptions"
            else:
                strcond = "Alternative assumptions"
            s += """<span style="font-size:85%; color:#888; margin-right:0.8em">""" + strcond + """:</span>"""
            s += arg.html(display=False)
            s += """</div>"""
            num += 1
        return s

    def html_Description(self, display=False):
        s = ""
        if display:
            s += """<div style="text-align:center; margin:0.6em">"""
        for arg in self.args():
            if arg.is_text():
                if arg._text and arg._text[0] in (",", ".", ";"):
                    s = s.rstrip()
                s += arg._text
            elif (not arg.is_atom()) and arg.head() == SourceForm:
                s += "<tt>%s</tt>" % str(arg.args()[0])
            elif (not arg.is_atom()) and arg.head() == EntryReference:
                id = arg.args()[0]._text
                s += """<a href="../../entry/%s/">%s</a>""" % (id, id)
            elif (not arg.is_atom()) and arg.head() == TopicReference:
                title = arg.args()[0]._text
                s += """<a href="../../topic/%s/">%s</a>""" % (escape_title(title), title)
            else:
                s += arg.html(avoid_latex=True)
            s += " "
        if display:
            s += """</div>"""
        return s

    def html_SymbolDefinition(self):
        symbol, example, description = self.args()
        s = ""
        s += """<div style="text-align:center; margin:0.6em">"""
        s += """<span style="font-size:85%; color:#888">Symbol:</span> """
        s += """<tt><a href="../../symbol/%s/">%s</a></tt>""" % (symbol._symbol, symbol._symbol)
        s += """ <span style="color:#888">&mdash;</span> """
        s += example.html()
        s += """ <span style="color:#888">&mdash;</span> """
        s += description._text
        s += """</div>"""
        return s

    def get_arg_with_head(self, head):
        for arg in self.args():
            if not arg.is_atom() and (arg.head() == head):
                return arg
        return None

    def id(self):
        id = self.get_arg_with_head(ID)
        return id._args[1]._text

    def title(self):
        title = self.get_arg_with_head(Title)
        return title._args[1]._text

    def entry_html(self, single=False, entry_dir="../../entry/", symbol_dir="../../symbol/", default_visible=False):
        id = self.id()
        all_tex = []
        image_downloads = []
        s = ""
        s += """<div class="entry">"""
        if single:
            s += """<div style="padding-top:0.4em">"""
        else:
            s += """<div style="float:left; margin-top:0.0em; margin-right:0.3em">"""
            s += """<a href="%s%s/" style="margin-left:3pt; font-size:85%%">%s</a> <span></span><br/>""" % (entry_dir, id, id)
            s += """<button style="margin-top:0.2em; margin-bottom: 0.1em;" onclick="toggleVisible('%s:info')">Details</button>""" % id
            s += """</div>"""
            s += """<div>"""

        args = self.args()
        args = [arg for arg in args if arg.head() not in (ID, Variables)]

        for arg in args:
            if arg.head() == Image:
                src = arg.get_arg_with_head(ImageSource).args()[0]._text
                image_downloads.append(src)

        # First item is always visible
        s += args[0].html(display=True, single=single)
        s += "</div>"

        # Remaining items may be hidden beneath the fold
        if single:
            s += """<div id="%s:info" style="padding: 1em; clear:both">""" % id
        else:
            if default_visible:
                s += """<div id="%s:info" style="display:visible; padding: 1em; clear:both">""" % id
            else:
                s += """<div id="%s:info" style="display:none; padding: 1em; clear:both">""" % id

        if image_downloads:
            src = image_downloads[0]
            s += """<div style="text-align:center; margin-top:0; margin-bottom:1.1em">"""
            s += """<span style="font-size:85%; color:#888">Download:</span> """
            s += """<a href="../../img/%s_small.png">png (small)</a>""" % src
            s += """ <span style="color:#888">&mdash;</span> """
            s += """<a href="../../img/%s_medium.png">png (medium)</a>""" % src
            s += """ <span style="color:#888">&mdash;</span> """
            s += """<a href="../../img/%s_large.png">png (large)</a>""" % src
            s += """ <span style="color:#888">&mdash;</span> """
            s += """<a href="../../img/%s_small.pdf">pdf (small)</a>""" % src
            s += """ <span style="color:#888">&mdash;</span> """
            s += """<a href="../../img/%s.pdf">pdf (medium/large)</a>""" % src
            s += """ <span style="color:#888">&mdash;</span> """
            s += """<a href="../../img/%s_small.svg">svg (small)</a>""" % src
            s += """ <span style="color:#888">&mdash;</span> """
            s += """<a href="../../img/%s.svg">svg (medium/large)</a>""" % src
            s += """</div>"""

        # Remaining items
        for arg in args[1:]:
            s += arg.html(display=True)
            s += "\n\n"

        # Generate TeX listing
        for arg in self.args():
            if arg.head() in (Formula, Assumptions):
                for arg2 in arg.args():
                    all_tex.append(arg2.latex())

        if all_tex:
            s += """<div class="entrysubhead">TeX:</div>"""
            s += "<pre>"
            s += "\n\n".join(all_tex)
            s += "</pre>"

        # Generate symbol table
        symbols = self.symbols(unique=True)
        symbols = [sym for sym in symbols if sym not in exclude_symbols]
        s += """<div class="entrysubhead">Definitions:</div>"""
        s += Expr.definitions_table_html(symbols, center=True, symbol_dir=symbol_dir)

        s += """<div class="entrysubhead">Source code for this entry:</div>"""
        s += "<pre>"
        s += self.str()
        s += "</pre>"

        s += "</div></div>\n"

        return s

    @staticmethod
    def definitions_table_html(symbols, center=False, entry_dir="../../entry/", symbol_dir="../../symbol/"):
        katex = katex_function[0]
        s = ""
        if center:
            s += """<table style="margin: 0 auto">"""
        else:
            s += """<table>"""
        # s += """<tr><th>Fungrim symbol</th> <th>Notation</th> <th>Domain</th> <th>Codomain</th> <th>Description</th></tr>"""
        s += """<tr><th>Fungrim symbol</th> <th>Notation</th> <th>Short description</th></tr>"""
        for symbol in symbols:
            if symbol in descriptions:
                example, domain, codomain, description = descriptions[symbol]
                s += """<tr><td><tt><a href="%s%s/">%s</a></tt>""" % (symbol_dir, symbol.str(), symbol.str())
                s += """<td>%s</td>""" % katex(example.latex(), False)
                # domstr = ",\, ".join(dom.latex() for dom in domain)
                # s += """<td>%s</td>""" % katex(domstr, False)
                # if codomain is None:
                #     s += """<td></td>"""
                # else:
                #     s += """<td>%s</td>""" % katex(codomain.latex(), False)
                s += """<td>%s</td></tr>""" % description
        s += """</table>"""
        return s

    def n(self, digits=20, **kwargs):
        from .numeric import neval
        return neval(self, digits, **kwargs)

all_builtins = []

def inject_builtin(string):
    for sym in string.split():
        globals()[sym] = Expr(symbol_name=sym)
        all_builtins.append(sym)

variable_names = set()

def inject_vars(string):
    for sym in string.split():
        e = Expr(symbol_name=sym)
        globals()[sym] = e
        variable_names.add(sym)

inject_builtin("""
True_ False_
Parentheses Brackets Braces
Ellipsis Call Subscript
Unknown Undefined
Where
Set List Tuple
SetBuilder
PowerSet
Union Intersection SetMinus Not And Or Equivalent Implies
Cardinality
Element NotElement Subset SubsetEqual
ForAll Exists
EqualAndElement
Rings CommutativeRings Fields
PP ZZ QQ RR CC HH AlgebraicNumbers
ZZGreaterEqual ZZLessEqual ZZBetween
ClosedInterval OpenInterval ClosedOpenInterval OpenClosedInterval
RealBall
UnitCircle
OpenDisk ClosedDisk BernsteinEllipse
InteriorClosure Interior
Decimal
Equal Unequal Greater GreaterEqual Less LessEqual
Pos Neg Add Sub Mul Div Mod Inv Pow
CongruentMod Odd Even
Max Min Sign Csgn Abs Floor Ceil Arg Re Im Conjugate
NearestDecimal
Minimum Maximum ArgMin ArgMax ArgMinUnique ArgMaxUnique
Solutions UniqueSolution
Supremum Infimum
Limit SequenceLimit RealLimit LeftLimit RightLimit ComplexLimit MeromorphicLimit
SequenceLimitInferior SequenceLimitSuperior
Derivative RealDerivative ComplexDerivative ComplexBranchDerivative MeromorphicDerivative
Sum Product
PrimeSum DivisorSum PrimeProduct DivisorProduct
Integral
IndefiniteIntegralEqual RealIndefiniteIntegralEqual ComplexIndefiniteIntegralEqual
AsymptoticTo
FormalGenerator
FormalPowerSeries FormalLaurentSeries SeriesCoefficient
HolomorphicDomain Poles BranchPoints BranchCuts EssentialSingularities Zeros UniqueZero AnalyticContinuation
ComplexZeroMultiplicity
Residue
Infinity UnsignedInfinity
Sqrt NthRoot Log LogBase Exp
Sin Cos Tan Sec Cot Csc
Asin Acos Atan Atan2 Asec Acot Acsc
Sinh Cosh Tanh Sech Coth Csch
Asinh Acosh Atanh Asech Acoth Acsch
Sinc LambertW LambertWPuiseuxCoefficient
ConstPi ConstE ConstGamma ConstI GoldenRatio ConstCatalan
Binomial Factorial DoubleFactorial GammaFunction LogGamma DigammaFunction PolyGamma RisingFactorial FallingFactorial HarmonicNumber StirlingSeriesRemainder
Erf Erfc Erfi
UpperGamma LowerGamma
BernoulliB BernoulliPolynomial EulerE EulerPolynomial
StirlingCycle StirlingS1 StirlingS2 BellNumber
RiemannZeta RiemannZetaZero
BesselJ BesselI BesselY BesselK HankelH1 HankelH2
CoulombF CoulombG CoulombH CoulombC CoulombSigma
Hypergeometric0F1 Hypergeometric1F1 Hypergeometric2F1 Hypergeometric2F0 Hypergeometric3F2
HypergeometricU HypergeometricUStar
Hypergeometric0F1Regularized Hypergeometric1F1Regularized Hypergeometric2F1Regularized Hypergeometric2F0Regularized Hypergeometric3F2Regularized
HypergeometricUStarRemainder
AiryAi AiryBi
LegendrePolynomial LegendrePolynomialZero GaussLegendreWeight
HermitePolynomial
ChebyshevT ChebyshevU
DedekindEta EulerQSeries DedekindEtaEpsilon DedekindSum
JacobiTheta JacobiThetaEpsilon JacobiThetaPermutation
Divides
GCD LCM XGCD DivisorSigma MoebiusMu Totient SquaresR LiouvilleLambda
LegendreSymbol JacobiSymbol KroneckerSymbol
Fibonacci
PartitionsP HardyRamanujanA
KroneckerDelta
Lattice
WeierstrassP WeierstrassZeta WeierstrassSigma
PrimeNumber PrimePi
RiemannHypothesis
LogIntegral LandauG
Matrix2x2 Matrix2x1
Spectrum Det
SL2Z PSL2Z ModularGroupAction ModularGroupFundamentalDomain
ModularLambdaFundamentalDomain
ModularJ ModularLambda
PrimitiveReducedPositiveIntegralBinaryQuadraticForms
HilbertClassPolynomial
DirichletCharacter DirichletGroup PrimitiveDirichletCharacters
ConreyGenerator
DiscreteLog
Cases Otherwise
HurwitzZeta DirichletL GeneralizedBernoulliB LerchPhi PolyLog
RiemannXi StieltjesGamma KeiperLiLambda DeBruijnNewmanLambda
DirichletLZero
GeneralizedRiemannHypothesis
DirichletLambda GaussSum JacobiSum
EisensteinG EisensteinE
EllipticK EllipticE
QSeriesCoefficient EqualQSeriesEllipsis
BetaFunction IncompleteBeta IncompleteBetaRegularized
""")


inject_builtin("""
Var
Entry Formula ID Assumptions References Variables DomainCodomain
Description Table TableRelation TableValueHeadings TableHeadings TableColumnHeadings TableSplit TableSection
Topic Title DefinitionsTable Section Subsection SeeTopics Entries EntryReference TopicReference
SourceForm SymbolDefinition
Image ImageSource
""")

# symbols we don't want to show in entry definition listings
exclude_symbols = set([Set, List, Tuple, And, Or, Implies, Equivalent, Not, Element, NotElement, Union, Intersection, SetMinus, Subset, SubsetEqual])

inject_vars("""a b c d e f g h i j k l m n o p q r s t u v w x y z""")
inject_vars("""A B C D E F G H I J K L M N O P Q R S T U V W X Y Z""")
inject_vars("""alpha beta gamma delta epsilon zeta eta theta iota kappa mu nu xi pi rho sigma tau phi chi psi omega ell""")
inject_vars("""Alpha Beta Gamma Delta Epsilon Zeta Eta Theta Iota Kappa Mu Nu Xi Pi Rho Sigma Tau Phi Chi Psi Omega""")

described_symbols = []
descriptions = {}
long_descriptions = {}
domain_tables = {}

def describe(symbol, example, domain, codomain, description):
    described_symbols.append(symbol)
    descriptions[symbol] = (example, domain, codomain, description)

def describe2(symbol, example, description, domain_table=None, long_description=None):
    described_symbols.append(symbol)
    descriptions[symbol] = (example, None, None, description)
    if long_description is not None:
        long_descriptions[symbol] = long_description
    if domain_table is not None:
        domain_tables[symbol] = domain_table



description_x_predicate = Description("The expression", SourceForm(Var(x)),
    "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator. ",
    "The corresponding predicate", P(x), "must define the domain of", x, "unambiguously; that is, it must include a statement such as",
    Element(x, S), "where", S, "is a known set.",
    "More generally,", SourceForm(Var(x, y, Ellipsis)), "defines a collection of variables", Tuple(x, y, Ellipsis),
    "all of which become locally bound, with a corresponding predicate", P(x, y, Ellipsis), ".")

description_xray = Description("An X-ray plot illustrates the geometry of a complex analytic function", f(z), ".",
    "Thick black curves show where", Equal(Im(f(z)), 0), "(the function is pure real).",
    "Thick red curves show where", Equal(Re(f(z)), 0), "(the function is pure imaginary).",
    "Points where black and red curves intersect are zeros or poles.",
    "Magnitude level curves", Equal(Abs(f(z)), C), "are rendered as thin gray curves, with brighter shades corresponding to larger", C, ".",
    "Blue lines show branch cuts.",
    "The value of the function is continuous with the branch cut on the side indicated with a solid line, and discontinuous on the side indicated with a dashed line.",
    "Yellow is used to highlight important regions.")


all_entries = []
all_topics = []

def def_Topic(*args):
    topic = Topic(*args)
    all_topics.append(topic)

def make_entry(*args):
    entry = Entry(*args)
    symd = entry.get_arg_with_head(SymbolDefinition)
    if symd is not None:
        id = entry.get_arg_with_head(ID)
        symbol, example, description = symd.args()
        described_symbols.append(symbol)
        descriptions[symbol] = (example, None, None, description._text)
        domain_tables[symbol] = id.args()[0]._text
    all_entries.append(entry)

