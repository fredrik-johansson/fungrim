# -*- coding: utf-8 -*-

from ..expr import *

# todo:
# analytic properties
# rationalizing denominators
# identities to a separate page
# cleaner series expansion markup

def_Topic(
    Title("Square roots"),
    Section("Definitions"),
    Entries(
        "21d9b8",
    ),
    Section("Illustrations"),
    Entries(
        "af984e",
    ),
    Section("Elementary functions"),
    Entries(
        "627c9c",
        "97b736",
    ),
    Section("Specific values"),
    Entries(
        "9d5b81",
        "61480c",
        "2eb54a",
        "0ad836",
        "31a8ca",
        "9dec73",
        "f9f31d",
    ),
    Section("Quadratic equations"),
    Entries(
        "08d275",
        "e0ac95",
        "fc2582",
    ),
    Section("Functional equations"),
    Entries(
        "0984ef",
        "d8791e",
        "3cc884",
        "57af50",
        "08bd37",
        "616bcb",
        "73b76c",
        "d0a331",
        "0d8e03",
        "1232f7",
        "99c0b3",
        "d40229",
        "6f63dd",
        "185efc",
    ),
    Section("Complex parts"),
    Entries(
        "ac54c7",
        "22e0be",
        "8c1ee5",
        "4ed6a8",
        "e722ca",
        "c58f46",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "ac54c7",
        "02751f",
        "14cbeb",
        "34136c",
    ),
    Section("Derivatives and integrals"),
    Entries(
        "2a11ab",
        "3e71f4",
        "83abff",
        "6ddbf4",
    ),
    Section("Series expansions"),
    Entries(
        "b14da0",
        "3c2557",
        "6202cb",
        "5ff181",
    ),
)

Log_branch_cut = OpenClosedInterval(-Infinity, 0)
Log_holomorphic_domain = SetMinus(CC, Log_branch_cut)

make_entry(ID("21d9b8"),
    SymbolDefinition(Sqrt, Sqrt(z), "Principal square root"),
    Description("The principal square root", Sqrt(z), "is a function of one complex variable", z, ".",),
    Description("It has a branch point singularity at", Equal(z, 0),
        "and a branch cut on", OpenClosedInterval(-Infinity, 0), "where the value on",
            OpenInterval(-Infinity, 0), "is taken to be continuous with the upper half plane."),
    Description("The following table lists all conditions such that", SourceForm(Sqrt(z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, ClosedOpenInterval(0,Infinity)), Element(Sqrt(z), ClosedOpenInterval(0,Infinity))),
        Tuple(Element(z, CC), Element(Sqrt(z), CC)),
        TableSection("Infinities"),
        Tuple(Element(z, Set(UnsignedInfinity)), Element(Sqrt(z), Set(UnsignedInfinity))),
        Tuple(Element(z, Set(Exp(ConstI*theta)*Infinity, ForElement(theta, OpenClosedInterval(-Pi,Pi)))),
                Element(Sqrt(z), Set(Exp(ConstI*theta)*Infinity, ForElement(theta, OpenClosedInterval(-Pi/2,Pi/2))))),
        TableSection("Formal power series"),
        Tuple(And(Element(z, PowerSeries(RR, x)), Element(SeriesCoefficient(z, x, 0), OpenInterval(0,Infinity))),
            And(Element(Sqrt(z), PowerSeries(RR, x)))),
        Tuple(And(Element(z, PowerSeries(CC, x)), NotEqual(SeriesCoefficient(z, x, 0), 0)),
            And(Element(Sqrt(z), PowerSeries(CC, x)))),
      )))

make_entry(ID("af984e"),
    Image(Description("X-ray of", Sqrt(z), "on", Element(z, ClosedInterval(-3,3) + ClosedInterval(-3,3)*ConstI)),
        ImageSource("xray_sqrt")),
    description_xray,
    )


# note could be valid at 0 if log(0) = -inf ...
make_entry(ID("627c9c"),
    Formula(Equal(Sqrt(z), Exp(Div(1,2)*Log(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("97b736"),
    Formula(Equal(Sqrt(z), z**Div(1,2))),
    Variables(z),
    Assumptions(Element(z, CC)))



make_entry(ID("9d5b81"),
    Description("Table of", Sqrt(n), "to 50 digits for", LessEqual(0, n, 50)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(Sqrt(n), 50)),
      TableSplit(1),
      List(
    Tuple(0, Decimal("0")),
    Tuple(1, Decimal("1")),
    Tuple(2, Decimal("1.4142135623730950488016887242096980785696718753769")),
    Tuple(3, Decimal("1.7320508075688772935274463415058723669428052538104")),
    Tuple(4, Decimal("2")),
    Tuple(5, Decimal("2.2360679774997896964091736687312762354406183596115")),
    Tuple(6, Decimal("2.4494897427831780981972840747058913919659474806567")),
    Tuple(7, Decimal("2.6457513110645905905016157536392604257102591830825")),
    Tuple(8, Decimal("2.8284271247461900976033774484193961571393437507539")),
    Tuple(9, Decimal("3")),
    Tuple(10, Decimal("3.1622776601683793319988935444327185337195551393252")),
    Tuple(11, Decimal("3.3166247903553998491149327366706866839270885455894")),
    Tuple(12, Decimal("3.4641016151377545870548926830117447338856105076208")),
    Tuple(13, Decimal("3.6055512754639892931192212674704959462512965738452")),
    Tuple(14, Decimal("3.7416573867739413855837487323165493017560198077787")),
    Tuple(15, Decimal("3.8729833462074168851792653997823996108329217052916")),
    Tuple(16, Decimal("4")),
    Tuple(17, Decimal("4.1231056256176605498214098559740770251471992253736")),
    Tuple(18, Decimal("4.2426406871192851464050661726290942357090156261308")),
    Tuple(19, Decimal("4.3588989435406735522369819838596156591370039252324")),
    Tuple(20, Decimal("4.4721359549995793928183473374625524708812367192231")),
    Tuple(21, Decimal("4.5825756949558400065880471937280084889844565767680")),
    Tuple(22, Decimal("4.6904157598234295545656301135444662805882283534117")),
    Tuple(23, Decimal("4.7958315233127195415974380641626939199967070419041")),
    Tuple(24, Decimal("4.8989794855663561963945681494117827839318949613133")),
    Tuple(25, Decimal("5")),
    Tuple(26, Decimal("5.0990195135927848300282241090227819895637709460996")),
    Tuple(27, Decimal("5.1961524227066318805823390245176171008284157614311")),
    Tuple(28, Decimal("5.2915026221291811810032315072785208514205183661649")),
    Tuple(29, Decimal("5.3851648071345040312507104915403295562951201616448")),
    Tuple(30, Decimal("5.4772255750516611345696978280080213395274469499798")),
    Tuple(31, Decimal("5.5677643628300219221194712989185495204763933775704")),
    Tuple(32, Decimal("5.6568542494923801952067548968387923142786875015078")),
    Tuple(33, Decimal("5.7445626465380286598506114682189293182202644579828")),
    Tuple(34, Decimal("5.8309518948453004708741528775455830765213983348860")),
    Tuple(35, Decimal("5.9160797830996160425673282915616170484155012307943")),
    Tuple(36, Decimal("6")),
    Tuple(37, Decimal("6.0827625302982196889996842452020670620849700947864")),
    Tuple(38, Decimal("6.1644140029689764502501923814542442252356240234446")),
    Tuple(39, Decimal("6.2449979983983982058468931209397944610729599779917")),
    Tuple(40, Decimal("6.3245553203367586639977870888654370674391102786504")),
    Tuple(41, Decimal("6.4031242374328486864882176746218132645204201326210")),
    Tuple(42, Decimal("6.4807406984078602309659674360879966577052043070583")),
    Tuple(43, Decimal("6.5574385243020006523441099976360016279269663198838")),
    Tuple(44, Decimal("6.6332495807107996982298654733413733678541770911787")),
    Tuple(45, Decimal("6.7082039324993690892275210061938287063218550788346")),
    Tuple(46, Decimal("6.7823299831252681390645563266259691051957483239233")),
    Tuple(47, Decimal("6.8556546004010441249358714490848489604606434610013")),
    Tuple(48, Decimal("6.9282032302755091741097853660234894677712210152415")),
    Tuple(49, Decimal("7")),
    Tuple(50, Decimal("7.0710678118654752440084436210484903928483593768847")))))

# todo: chain-ops to write EqualEqualElement?
make_entry(ID("61480c"),
    Formula(Where(Element(x, RealBall(Decimal("0.707106781186547524400844362105"), Decimal("1.51e-31"))),
        Equal(x, Sqrt(Div(1,2)), 1/Sqrt(2), Sqrt(2)/2))))

make_entry(ID("2eb54a"),
    Formula(Equal(Sqrt(-1), ConstI)))

make_entry(ID("0ad836"),
    Formula(Equal(Sqrt(ConstI), (1/Sqrt(2)) * (1+ConstI))))

make_entry(ID("31a8ca"),
    Formula(Equal(Sqrt(UnsignedInfinity), UnsignedInfinity)))

make_entry(ID("9dec73"),
    Formula(Equal(Sqrt(Infinity), Infinity)))

make_entry(ID("f9f31d"),
    Formula(Equal(Sqrt(Exp(ConstI*theta) * Infinity), Exp(ConstI*theta/2) * Infinity)),
    Variables(theta),
    Assumptions(Element(theta, OpenClosedInterval(-Pi, Pi))))




make_entry(ID("08d275"),
    Formula(Equal(Zeros(z**2 - c, ForElement(z, CC)), Set(Sqrt(c), -Sqrt(c)))),
    Variables(c),
    Assumptions(Element(c, CC)))

make_entry(ID("e0ac95"),
    Formula(Equal(Zeros(z**2 - c, ForElement(z, CC)), Set(ConstI*Sqrt(-c), -ConstI*Sqrt(-c)))),
    Variables(c),
    Assumptions(Element(c, CC)))

make_entry(ID("fc2582"),
    Formula(Equal(Zeros(a*z**2+b*z+c, ForElement(z, CC)), Set((-b+Sqrt(b**2-4*a*c))/(2*a), (-b-Sqrt(b**2-4*a*c))/(2*a)))),
    Variables(a, b, c),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(c, CC), NotEqual(a, 0))))


make_entry(ID("0984ef"),
    Formula(Equal(Sqrt(z)**2, z)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("d8791e"),
    Formula(Equal(Sqrt(z**2), z)),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(Arg(z), OpenClosedInterval(-Pi/2, Pi/2)))))

make_entry(ID("3cc884"),
    Formula(Equal(Sqrt(x**2), Abs(x))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("57af50"),
    Formula(Equal(Sqrt(-z), ConstI*Sqrt(z))),
    Variables(z),
    Assumptions(Or(Element(z, ClosedOpenInterval(0, Infinity)), And(Element(z, CC), Less(Im(z), 0)))))

make_entry(ID("08bd37"),
    Formula(Equal(Sqrt(-z), -ConstI*Sqrt(z))),
    Variables(z),
    Assumptions(Or(Element(z, OpenClosedInterval(-Infinity, 0)), And(Element(z, CC), Greater(Im(z), 0)))))

make_entry(ID("616bcb"),
    Formula(Equal(Sqrt(z/2), Sqrt(z)/Sqrt(2))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("73b76c"),
    Formula(Equal(Sqrt(a*b), Sqrt(a)*Sqrt(b))),
    Variables(a, b),
    Assumptions(Or(And(Element(a, CC), Element(b, ClosedOpenInterval(0, Infinity))),
                   And(Element(b, CC), Element(a, ClosedOpenInterval(0, Infinity)))),
        And(Element(a, CC), Element(b, CC), Element(Arg(a) + Arg(b), OpenClosedInterval(-Pi, Pi)))))

make_entry(ID("d0a331"),
    Formula(Equal(Sqrt(1/z), 1/Sqrt(z))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))))

make_entry(ID("0d8e03"),
    Formula(Equal(Sqrt(a/b), Sqrt(a)/Sqrt(b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, OpenInterval(0, Infinity))),
        And(Element(a, ClosedOpenInterval(0, Infinity)), Element(b, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))),
        And(Element(a, CC), Element(b, SetMinus(CC, Set(0))), Element(Arg(a) - Arg(b), OpenClosedInterval(-Pi, Pi)))))

make_entry(ID("1232f7"),
    Formula(Equal(Sqrt(r*Exp(ConstI*theta)), Sqrt(r) * Exp(ConstI*theta/2))),
    Variables(r, theta),
    Assumptions(And(Element(r, ClosedOpenInterval(0, Infinity)), Element(theta, OpenClosedInterval(-Pi, Pi)))))

make_entry(ID("99c0b3"),
    Formula(Equal(Sqrt(z-c*z**2), Sqrt(z)*Sqrt(1-c*z))),
    Variables(z, c),
    Assumptions(And(Element(z, CC), Element(c, ClosedOpenInterval(0, Infinity)))))

make_entry(ID("d40229"),
    Formula(Equal(Sqrt(z/(z+c)), Sqrt(z)/Sqrt(z+c))),
    Variables(z, c),
    Assumptions(And(Element(z, CC), Element(c, ClosedOpenInterval(0, Infinity)), NotEqual(z+c, 0))))

make_entry(ID("6f63dd"),
    Formula(Equal(Sqrt(z/(z-c)), Sqrt(-z)/Sqrt(c-z))),
    Variables(z, c),
    Assumptions(And(Element(z, CC), Element(c, ClosedOpenInterval(0, Infinity)), NotEqual(z-c, 0))))

make_entry(ID("185efc"),
    Formula(Equal(Sqrt(z/(c-z)), Sqrt(z)*Sqrt(1/(c-z)))),
    Variables(z, c),
    Assumptions(And(Element(z, CC), Element(c, ClosedOpenInterval(0, Infinity)), NotEqual(c-z, 0))))

make_entry(ID("ac54c7"),
    Formula(Equal(Abs(Sqrt(z)), Sqrt(Abs(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("22e0be"),
    Formula(Equal(Arg(Sqrt(z)), Arg(z)/2)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("8c1ee5"),
    Formula(Equal(Sign(Sqrt(z)), Sqrt(Sign(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("4ed6a8"),
    Formula(Equal(Re(Sqrt(z)), Sqrt((Abs(z)+Re(z))/2))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e722ca"),
    Formula(Equal(Im(Sqrt(z)), Sign(Im(z)) * Sqrt((Abs(z)-Re(z))/2))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("c58f46"),
    Formula(Equal(Sqrt(Conjugate(z)), Conjugate(Sqrt(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, OpenInterval(-Infinity, 0)))))



make_entry(ID("02751f"),
    Formula(LessEqual(Abs(Sqrt(x+a) - Sqrt(x)), Sqrt(x) * (1 - Sqrt(1 - Abs(a)/x)))),
    Variables(x, a),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(a, RR), LessEqual(Abs(a), x))))

make_entry(ID("14cbeb"),
    Formula(LessEqual(Abs(Sqrt(x+a) - Sqrt(x)), (Sqrt(x)/2) * (Abs(a)/x + Abs(a)**2/x**2))),
    Variables(x, a),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(a, RR), LessEqual(Abs(a), x))))

make_entry(ID("34136c"),
    Formula(LessEqual(Abs(1/Sqrt(x+a) - 1/Sqrt(x)), Abs(a) / (2 * (x - Abs(a))**Div(3,2)))),
    Variables(x, a),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(a, RR), Less(Abs(a), x))))

make_entry(ID("2a11ab"),
    Formula(Equal(ComplexDerivative(Sqrt(z), For(z, z, 1)), 1/(2*Sqrt(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))))

make_entry(ID("3e71f4"),
    Formula(Equal(ComplexDerivative(Sqrt(z), For(z, z, 2)), -(1/(4*z**Div(3,2))))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))))

make_entry(ID("83abff"),
    Formula(Equal(ComplexDerivative(Sqrt(z), For(z, z, r)), (-1)**r * RisingFactorial(-Div(1,2), r) * z**(r-Div(1,2)))),
    Variables(z, r),
    Assumptions(And(Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))), Element(r, ZZGreaterEqual(0)))))

# todo: cleaner way to write down condition? will need in many other formulas
no_crossing = Or(And(GreaterEqual(Re(a), 0), GreaterEqual(Re(b), 0)),
                 And(GreaterEqual(Im(a), 0), GreaterEqual(Im(b), 0)),
                 And(Less(Im(a), 0), Less(Im(b), 0)))

no_crossing2 = Equal(Intersection(OpenInterval(a, b), OpenInterval(-Infinity, 0)), Set())

make_entry(ID("6ddbf4"),
    Formula(Equal(Integral(Sqrt(z), For(z, a, b)), Div(2,3) * (b**Div(3,2) - a**Div(3,2)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), no_crossing),
                And(Element(a, CC), Element(b, CC), no_crossing2)))

make_entry(ID("b14da0"),
    Formula(Equal(Sqrt(z+x), Sqrt(z) * Sum(((-1)**k * RisingFactorial(-Div(1,2),k)) / (z**k * Factorial(k)) * x**k, For(k, 0, Infinity)))),
    Variables(z, x),
    Assumptions(And(Element(z, SetMinus(CC, Set(0))), Element(x, CC), And(Less(Abs(x), Abs(z)), Or(Greater(Re(z), 0), Equal(Sign(Im(x)), Sign(Im(z)))))),
        And(Element(z, SetMinus(CC, Set(0))), FormalGenerator(x, PowerSeries(CC, x)))))

make_entry(ID("3c2557"),
    Formula(Equal(1/Sqrt(z+x), (1/Sqrt(z)) * Sum(((-1)**k * RisingFactorial(Div(1,2),k)) / (z**k * Factorial(k)) * x**k, For(k, 0, Infinity)))),
    Variables(z, x),
    Assumptions(And(Element(z, SetMinus(CC, Set(0))), Element(x, CC), And(Less(Abs(x), Abs(z)), Or(Greater(Re(z), 0), Equal(Sign(Im(x)), Sign(Im(z)))))),
        And(Element(z, SetMinus(CC, Set(0))), FormalGenerator(x, PowerSeries(CC, x)))))

make_entry(ID("6202cb"),
    Formula(Where(Equal(Subscript(c, n), 1/(n * Subscript(a, 0)) * Sum((3*k/2-n) * Subscript(a, k) * Subscript(c, n-k), For(k, 1, n))),
        Equal(Subscript(c, n), SeriesCoefficient(Sqrt(A), x, n)), Equal(Subscript(a, n), SeriesCoefficient(A, x, n)))),
    Variables(A, n),
    Assumptions(And(Element(A, PowerSeries(CC, x)), NotEqual(SeriesCoefficient(A, x, 0), 0), Element(n, ZZGreaterEqual(1)))))
    #Formula(Where(Equal(Sqrt(Sum(Subscript(a, n) * x**n, For(n, 0, Infinity))), Sum(Subscript(c, n) * x**n, For(n, 0, Infinity))),
    #    Equal(Subscript(c, 0), Sqrt(Subscript(a, 0))),
    #        Equal(Subscript(c, n), 1/(n * Subscript(a, 0)) * Sum((3*k/2-n) * Subscript(a, k) * Subscript(c, n-k), For(k, 1, n))))))

make_entry(ID("5ff181"),
    Formula(Where(Equal(Subscript(c, n), 1/(n * Subscript(a, 0)) * Sum((k/2-n) * Subscript(a, k) * Subscript(c, n-k), For(k, 1, n))),
        Equal(Subscript(c, n), SeriesCoefficient(1/Sqrt(A), x, n)), Equal(Subscript(a, n), SeriesCoefficient(A, x, n)))),
    Variables(A, n),
    Assumptions(And(Element(A, PowerSeries(CC, x)), NotEqual(SeriesCoefficient(A, x, 0), 0), Element(n, ZZGreaterEqual(1)))))

