# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Pi"),
    Section("Definitions"),
    Entries(
        "b5d706",
    ),
    Section("Numerical value"),
    Entries(
        "6505a9",
        "47acde",
        "0c838a",
        "155575",
    ),
    Section("Elementary function representations"),
    Entries(
        "0c9939",
        "3ff35f",
        "722241",
        "b89166",
        "f8d280",
        "590136",
    ),
    Section("Integral representations"),
    Entries(
        "464961",
        "04cd99",
        "dae4a7",
    ),
    Section("Series representations"),
    Entries(
        "f617c0",
        "fddfe6",
    ),
    Section("Product representations"),
    Entries(
        "69fe63",
    ),
    Section("Limit representations"),
    Entries(
        "e1e106",
    ),
    Section("Approximations"),
    Entries(
        "2516c2",
        "1e3a25",
        "fdc3a3",
        "4c0698",
    ),
)

make_entry(ID("b5d706"),
    SymbolDefinition(ConstPi, ConstPi, "The constant pi (3.14...)"),
    Description("The real number giving the ratio of a circle's circumference to its diameter."))

# Numerical value

make_entry(ID("6505a9"),
    Formula(Element(ConstPi,
        RealBall(Decimal("3.1415926535897932384626433832795028841971693993751"), Decimal("5.83e-51")))))

make_entry(ID("47acde"),
    Description("Table of simple expressions involving", ConstPi, "to 50 digits"),
    Table(
      Var(x),
      TableValueHeadings(x, NearestDecimal(x, 50)),
      TableSplit(1),
      List(
    Tuple(ConstPi, Decimal("3.1415926535897932384626433832795028841971693993751")),
    Tuple(2*ConstPi, Decimal("6.2831853071795864769252867665590057683943387987502")),
    Tuple(3*ConstPi, Decimal("9.4247779607693797153879301498385086525915081981253")),
    Tuple(4*ConstPi, Decimal("12.566370614359172953850573533118011536788677597500")),
    Tuple(ConstPi/2, Decimal("1.5707963267948966192313216916397514420985846996876")),
    Tuple(3*ConstPi/2, Decimal("4.7123889803846898576939650749192543262957540990627")),
    Tuple(ConstPi/3, Decimal("1.0471975511965977461542144610931676280657231331250")),
    Tuple(2*ConstPi/3, Decimal("2.0943951023931954923084289221863352561314462662501")),
    Tuple(ConstPi/4, Decimal("0.78539816339744830961566084581987572104929234984378")),
    Tuple(3*ConstPi/4, Decimal("2.3561944901923449288469825374596271631478770495313")),
    Tuple(ConstPi/5, Decimal("0.62831853071795864769252867665590057683943387987502")),
    Tuple(2*ConstPi/5, Decimal("1.2566370614359172953850573533118011536788677597500")),
    Tuple(3*ConstPi/5, Decimal("1.8849555921538759430775860299677017305183016396251")),
    Tuple(4*ConstPi/5, Decimal("2.5132741228718345907701147066236023073577355195001")),
    Tuple(ConstPi/6, Decimal("0.52359877559829887307710723054658381403286156656252")),
    Tuple(5*ConstPi/6, Decimal("2.6179938779914943653855361527329190701643078328126")),
    Tuple(1/ConstPi, Decimal("0.31830988618379067153776752674502872406891929148091")),
    Tuple(2/ConstPi, Decimal("0.63661977236758134307553505349005744813783858296183")),
    Tuple(1/(2*ConstPi), Decimal("0.15915494309189533576888376337251436203445964574046")),
    Tuple(ConstPi**2, Decimal("9.8696044010893586188344909998761511353136994072408")),
    Tuple((2*ConstPi)**2, Decimal("39.478417604357434475337963999504604541254797628963")),
    Tuple(ConstPi**2/2, Decimal("4.9348022005446793094172454999380755676568497036204")),
    Tuple(ConstPi**2/4, Decimal("2.4674011002723396547086227499690377838284248518102")),
    Tuple(ConstPi**2/6, Decimal("1.6449340668482264364724151666460251892189499012068")),
    Tuple(1/ConstPi**2, Decimal("0.10132118364233777144387946320972763890435877467225")),
    Tuple(1/(2*ConstPi)**2, Decimal("0.025330295910584442860969865802431909726089693668062")),
    Tuple(ConstPi**3, Decimal("31.006276680299820175476315067101395202225288565885")),
    Tuple(ConstPi**4, Decimal("97.409091034002437236440332688705111249727585672685")),
    Tuple(Sqrt(ConstPi), Decimal("1.7724538509055160272981674833411451827975494561224")),
    Tuple(Sqrt(2*ConstPi), Decimal("2.5066282746310005024157652848110452530069867406099")),
    Tuple(1/Sqrt(ConstPi), Decimal("0.56418958354775628694807945156077258584405062932900")),
    Tuple(1/Sqrt(2*ConstPi), Decimal("0.39894228040143267793994605993438186847585863116493")),
    Tuple(Log(ConstPi), Decimal("1.1447298858494001741434273513530587116472948129153")),
    Tuple(Log(2*ConstPi), Decimal("1.8378770664093454835606594728112352797227949472756")),
    Tuple(Div(1,2)*Log(2*ConstPi), Decimal("0.91893853320467274178032973640561763986139747363778")),
    Tuple(Exp(ConstPi), Decimal("23.140692632779269005729086367948547380266106242600")),
    Tuple(Exp(ConstPi/2), Decimal("4.8104773809653516554730356667038331263901708746645")),
    Tuple(Exp(2*ConstPi), Decimal("535.49165552476473650304932958904718147780579760329")),
    Tuple(Exp(-ConstPi), Decimal("0.043213918263772249774417737171728011275728109810633")),
    Tuple(Exp(-(ConstPi/2)), Decimal("0.20787957635076190854695561983497877003387784163177")),
    Tuple(Exp(-(2*ConstPi)), Decimal("0.0018674427317079888144302129348270303934228050024753")),
    Tuple(Exp(ConstPi) - ConstPi, Decimal("19.999099979189475767266442984669044496068936843225")),
)))


make_entry(ID("0c838a"),
    Formula(NotElement(ConstPi, QQ)))

make_entry(ID("155575"),
    Formula(NotElement(ConstPi, AlgebraicNumbers)))

# Elementary function representations

make_entry(ID("0c9939"),
    Formula(Equal(ConstPi, 4*Atan(1))))

make_entry(ID("3ff35f"),
    Formula(Equal(ConstPi, 2*Acos(0))))

make_entry(ID("722241"),
    Formula(Equal(ConstPi, 2*Asin(1))))

make_entry(ID("b89166"),
    Formula(Equal(ConstPi, UniqueZero(Sin(x), Var(x), Element(x, ClosedInterval(3, 4))))))

make_entry(ID("f8d280"),
    Formula(Equal(ConstPi, 16*Acot(5) - 4*Acot(239))))

make_entry(ID("590136"),
    Formula(Equal(ConstPi, -(ConstI * Log(-1)))))

# Integral representations

make_entry(ID("464961"),
    Formula(Equal(ConstPi, 2 * Integral(Sqrt(1-x**2), For(x, -1, 1)))))

make_entry(ID("04cd99"),
    Formula(Equal(ConstPi, Integral(1/(x**2+1), For(x, -Infinity, Infinity)))))

make_entry(ID("dae4a7"),
    Formula(Equal(ConstPi, Integral(Exp(-x**2), For(x, -Infinity, Infinity))**2)))

# Series representations

make_entry(ID("f617c0"),
    Formula(Equal(ConstPi, 4*Sum((-1)**k / (2*k+1), For(k, 0, Infinity)))))

make_entry(ID("fddfe6"),
    Formula(Equal(ConstPi, Sum((1 / 16**k) * (4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)), For(k, 0, Infinity)))),
    References("D. H. Bailey and P. B. Borwein and S. Plouffe (1997). On the rapid computation of various polylogarithmic constants. Mathematics of Computation. vol 66, no 218, p. 903–913. DOI:10.1090/S0025-5718-97-00856-9"))

# Product representations

make_entry(ID("69fe63"),
    Formula(Equal(ConstPi, 2*Product((4*k**2)/(4*k**2-1), For(k, 1, Infinity)))))

# Limit representations

make_entry(ID("e1e106"),
    Formula(Equal(ConstPi, SequenceLimit(16**k/(k*Binomial(2*k,k)**2), Var(k), Infinity))))

# Approximations

make_entry(ID("2516c2"),
    Formula(Less(Abs(ConstPi - Div(22,7)), Decimal("0.00127"))))

make_entry(ID("1e3a25"),
    Formula(Less(Abs(ConstPi - Div(355,113)), Decimal("2.67e-7"))))

make_entry(ID("fdc3a3"),
    Formula(Less(Abs(ConstPi - Log(Pow(640320,3)+744)/Sqrt(163)), Decimal("2.24e-31"))))

make_entry(ID("4c0698"),
    Formula(Less(Abs(1/ConstPi -
        Parentheses(12*Sum((-1)**k*Factorial(6*k)*(13591409+545140134*k)/(Factorial(3*k)*Factorial(k)**3*640320**(3*k+Div(3,2))),
            For(k, 0, N-1)))), Div(1,151931373056000**N))),
    Variables(N),
    Assumptions(Element(N, ZZGreaterEqual(0))))

