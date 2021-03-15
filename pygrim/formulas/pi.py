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
        "483547", # OEIS
    ),
    Section("Euler's identity"),
    Entries(
        "271314",
    ),
    Section("Elementary function representations"),
    Entries(
        "0c9939",
        "3ff35f",
        "722241",
        "b89166",
        "590136",
        "030560",
    ),
    Subsection("Machin-type formulas"),
    Entries(
        "f8d280",
        "cbf396",
        "b1357b",
        "0644b6",
        "5278da",
        "7ce79e",
        "8332d8",
    ),
    Section("Integral representations"),
    Entries(
        "464961",
        "fc8149",
        "04cd99",
        "dae4a7",
        "81f500",
        "bd3faa",
        "9a3503",
        "8107d6",
        "5033c7",
        "6ed553",
        "859856",
        "d8cb3e",
        "e00d9e",
    ),
    Section("Series representations"),
    Entries(
        "f617c0",
        "93831d",
        "419b45",
        "fddfe6",
        "6b9f81",
        "57fcaf",
        "0479f5",
        "338055",
        "fbc53d",
        "11302a",
        "9bf21b",
        "8dff72",
        "31eecc",
        "bad5d9",
        "54c80d",
        "f78fa0",
        "dbdf08",
        "a2e6f9",
    ),
    Section("Product representations"),
    Entries(
        "69fe63",
        "490cf4",
        "a91200",
        "6fce07",
    ),
    Section("Limit representations"),
    Entries(
        "dea83d",
        "e1e106",
        "420007",
        "220e8d",
        "6d9ceb",    # from agm
    ),
    Section("Special function representations"),
    Entries(
        "8fab22",
        "2371b9",
        "63ba30",
        "67bb53",
        "591d64",
        "033c51",
        "dabb47",
        "ce5423",
        "07e35f",
        "9206a3",
        "1448e3",
        "a7095f",
        "c6c108",
        "2a0316",
        "f55b36",
        "769f6e",
        "488a30",
        "826257",
        "3d276b",
        "2806fd",
        "68b73d",
        "42d727",
        "8ee7c9",
        "f56273",
    ),
    Section("Approximations"),
    Entries(
        "2516c2",
        "1e3a25",
        "fdc3a3",
        "4c0698",
        "13c539",  # from agm
    ),
)


make_entry(ID("b5d706"),
    SymbolDefinition(Pi, Pi, "The constant pi (3.14...)"),
    Description("The real number giving the ratio of a circle's circumference to its diameter."))

# Numerical value

make_entry(ID("6505a9"),
    Formula(Element(Pi,
        RealBall(Decimal("3.1415926535897932384626433832795028841971693993751"), Decimal("5.83e-51")))))

make_entry(ID("47acde"),
    Description("Table of simple expressions involving", Pi, "to 50 digits"),
    Table(
      Var(x),
      TableValueHeadings(x, NearestDecimal(x, 50)),
      TableSplit(1),
      List(
    Tuple(Pi, Decimal("3.1415926535897932384626433832795028841971693993751")),
    Tuple(2*Pi, Decimal("6.2831853071795864769252867665590057683943387987502")),
    Tuple(3*Pi, Decimal("9.4247779607693797153879301498385086525915081981253")),
    Tuple(4*Pi, Decimal("12.566370614359172953850573533118011536788677597500")),
    Tuple(Pi/2, Decimal("1.5707963267948966192313216916397514420985846996876")),
    Tuple(3*Pi/2, Decimal("4.7123889803846898576939650749192543262957540990627")),
    Tuple(Pi/3, Decimal("1.0471975511965977461542144610931676280657231331250")),
    Tuple(2*Pi/3, Decimal("2.0943951023931954923084289221863352561314462662501")),
    Tuple(Pi/4, Decimal("0.78539816339744830961566084581987572104929234984378")),
    Tuple(3*Pi/4, Decimal("2.3561944901923449288469825374596271631478770495313")),
    Tuple(Pi/5, Decimal("0.62831853071795864769252867665590057683943387987502")),
    Tuple(2*Pi/5, Decimal("1.2566370614359172953850573533118011536788677597500")),
    Tuple(3*Pi/5, Decimal("1.8849555921538759430775860299677017305183016396251")),
    Tuple(4*Pi/5, Decimal("2.5132741228718345907701147066236023073577355195001")),
    Tuple(Pi/6, Decimal("0.52359877559829887307710723054658381403286156656252")),
    Tuple(5*Pi/6, Decimal("2.6179938779914943653855361527329190701643078328126")),
    Tuple(1/Pi, Decimal("0.31830988618379067153776752674502872406891929148091")),
    Tuple(2/Pi, Decimal("0.63661977236758134307553505349005744813783858296183")),
    Tuple(1/(2*Pi), Decimal("0.15915494309189533576888376337251436203445964574046")),
    Tuple(Pi**2, Decimal("9.8696044010893586188344909998761511353136994072408")),
    Tuple((2*Pi)**2, Decimal("39.478417604357434475337963999504604541254797628963")),
    Tuple(Pi**2/2, Decimal("4.9348022005446793094172454999380755676568497036204")),
    Tuple(Pi**2/4, Decimal("2.4674011002723396547086227499690377838284248518102")),
    Tuple(Pi**2/6, Decimal("1.6449340668482264364724151666460251892189499012068")),
    Tuple(1/Pi**2, Decimal("0.10132118364233777144387946320972763890435877467225")),
    Tuple(1/(2*Pi)**2, Decimal("0.025330295910584442860969865802431909726089693668062")),
    Tuple(Pi**3, Decimal("31.006276680299820175476315067101395202225288565885")),
    Tuple(Pi**4, Decimal("97.409091034002437236440332688705111249727585672685")),
    Tuple(Sqrt(Pi), Decimal("1.7724538509055160272981674833411451827975494561224")),
    Tuple(Sqrt(2*Pi), Decimal("2.5066282746310005024157652848110452530069867406099")),
    Tuple(1/Sqrt(Pi), Decimal("0.56418958354775628694807945156077258584405062932900")),
    Tuple(1/Sqrt(2*Pi), Decimal("0.39894228040143267793994605993438186847585863116493")),
    Tuple(Log(Pi), Decimal("1.1447298858494001741434273513530587116472948129153")),
    Tuple(Log(2*Pi), Decimal("1.8378770664093454835606594728112352797227949472756")),
    Tuple(Div(1,2)*Log(2*Pi), Decimal("0.91893853320467274178032973640561763986139747363778")),
    Tuple(Exp(Pi), Decimal("23.140692632779269005729086367948547380266106242600")),
    Tuple(Exp(Pi/2), Decimal("4.8104773809653516554730356667038331263901708746645")),
    Tuple(Exp(2*Pi), Decimal("535.49165552476473650304932958904718147780579760329")),
    Tuple(Exp(-Pi), Decimal("0.043213918263772249774417737171728011275728109810633")),
    Tuple(Exp(-(Pi/2)), Decimal("0.20787957635076190854695561983497877003387784163177")),
    Tuple(Exp(-(2*Pi)), Decimal("0.0018674427317079888144302129348270303934228050024753")),
    Tuple(Exp(Pi) - Pi, Decimal("19.999099979189475767266442984669044496068936843225")),
)))


make_entry(ID("0c838a"),
    Formula(NotElement(Pi, QQ)))

make_entry(ID("155575"),
    Formula(NotElement(Pi, AlgebraicNumbers)))

# Euler's identity

make_entry(ID("271314"),
    Formula(Equal(Exp(Pi*ConstI) + 1, 0)))

# Elementary function representations

make_entry(ID("0c9939"),
    Formula(Equal(Pi, 4*Atan(1))))

make_entry(ID("3ff35f"),
    Formula(Equal(Pi, 2*Acos(0))))

make_entry(ID("722241"),
    Formula(Equal(Pi, 2*Asin(1))))

make_entry(ID("b89166"),
    Formula(Equal(Pi, UniqueZero(Sin(x), ForElement(x, ClosedInterval(3, 4))))))

make_entry(ID("590136"),
    Formula(Equal(Pi, -(ConstI * Log(-1)))))

make_entry(ID("030560"),
    Formula(Equal(Pi, 10*Asin(1/(2*GoldenRatio)))))


make_entry(ID("f8d280"),
    Formula(Equal(Pi, 16*Atan(Div(1,5)) - 4*Atan(Div(1,239)))))

make_entry(ID("cbf396"),
    Formula(Equal(Pi, 4*Atan(Div(1,2)) + 4*Atan(Div(1,3)))))

make_entry(ID("b1357b"),
    Formula(Equal(Pi, 8*Atan(Div(1,2)) - 4*Atan(Div(1,7)))))

make_entry(ID("0644b6"),
    Formula(Equal(Pi, 8*Atan(Div(1,3)) + 4*Atan(Div(1,7)))))

make_entry(ID("5278da"),
    Formula(Equal(Pi, 4*Atan(Div(1,2)) + 4*Atan(Div(1,5)) + 4*Atan(Div(1,8)))))

make_entry(ID("7ce79e"),
    Formula(Equal(Pi, 4*Atan(Div(1,3)) + 4*Atan(Div(1,4)) + 4*Atan(Div(1,7)) + 4*Atan(Div(1,13)))))

make_entry(ID("8332d8"),
    Formula(Equal(Pi, 48*Atan(Div(1,49))+128*Atan(Div(1,57))-20*Atan(Div(1,239))+48*Atan(Div(1,110443)))))




# Integral representations

make_entry(ID("464961"),
    Formula(Equal(Pi, 2 * Integral(Sqrt(1-x**2), For(x, -1, 1)))))

make_entry(ID("fc8149"),
    Formula(Equal(Pi, Integral(1/Sqrt(1-x**2), For(x, -1, 1)))))

make_entry(ID("04cd99"),
    Formula(Equal(Pi, Integral(1/(x**2+1), For(x, -Infinity, Infinity)))))

make_entry(ID("dae4a7"),
    Formula(Equal(Pi, Integral(Exp(-x**2), For(x, -Infinity, Infinity))**2)))

make_entry(ID("81f500"),
    Formula(Equal(Pi, Div(22,7) - Integral(x**4*(1-x)**4/(1+x**2), For(x, 0, 1)))))

make_entry(ID("bd3faa"),
    Formula(Equal(Pi, Div(355,113) - Div(1,3164) * Integral(x**8*(1-x)**8*(25+816*x**2)/(1+x**2), For(x, 0, 1)))),
    References("https://mathworld.wolfram.com/PiFormulas.html"))

make_entry(ID("9a3503"),
    Formula(Equal(Pi, Integral(Sinc(x), For(x, -Infinity, Infinity)))))

make_entry(ID("8107d6"),
    Formula(Equal(Pi, Integral(Sinc(x)**2, For(x, -Infinity, Infinity)))))

make_entry(ID("5033c7"),
    Formula(Equal(Pi, 2 * ConstE * Integral(Cos(x) / (x**2+1), For(x, 0, Infinity)))))

make_entry(ID("6ed553"),
    Formula(Equal(Pi, 8 * Integral(Sin(x**2), For(x, 0, Infinity))**2)))

make_entry(ID("859856"),
    Formula(Equal(Pi, 8 * Integral(Cos(x**2), For(x, 0, Infinity))**2)))

make_entry(ID("d8cb3e"),
    Formula(Equal(Pi, Integral(JacobiTheta(2,0,ConstI*t), For(t, 0, Infinity)))))

make_entry(ID("e00d9e"),
    Formula(Equal(Pi, 3 * Integral(Parentheses(JacobiTheta(3,0,ConstI*t)-1), For(t, 0, Infinity)))))


# Series representations

make_entry(ID("f617c0"),
    Formula(Equal(Pi, 4*Sum((-1)**n / (2*n+1), For(n, 0, Infinity)))))

make_entry(ID("93831d"),
    Formula(Equal(Pi, Sum((2**(n+1) * Factorial(n)**2) / Factorial(2*n+1), For(n, 0, Infinity)))))

make_entry(ID("419b45"),
    Formula(Equal(Pi, Sum(Factorial(n) / DoubleFactorial(2*n+1), For(n, 0, Infinity)))))

make_entry(ID("fddfe6"),
    Formula(Equal(Pi, Sum((1 / 16**n) * (4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(8*n+6)), For(n, 0, Infinity)))),
    References("D. H. Bailey and P. B. Borwein and S. Plouffe (1997). On the rapid computation of various polylogarithmic constants. Mathematics of Computation. vol 66, no 218, p. 903–913. DOI:10.1090/S0025-5718-97-00856-9"))

make_entry(ID("6b9f81"),
    Formula(Equal(1/Pi,
        (2*Sqrt(2))/9801 * Sum((Factorial(4*n) * (1103+26390*n))/(Factorial(n)**4 * 396**(4*n)), For(n, 0, Infinity)))))

make_entry(ID("57fcaf"),
    Formula(Equal(1/Pi,
        12*Sum((-1)**n*Factorial(6*n)*(13591409+545140134*n)/(Factorial(3*n)*Factorial(n)**3*640320**(3*n+Div(3,2))),
            For(n, 0, Infinity)))))

make_entry(ID("0479f5"),
    Formula(Equal(Pi, 72*Sum(1/(n*(Exp(Pi*n)-1)), For(n, 1, Infinity)) - 96*Sum(1/(n*(Exp(2*Pi*n)-1)), For(n, 1, Infinity)) + 24*Sum(1/(n*(Exp(4*Pi*n)-1)), For(n, 1, Infinity)))),
    References("http://www.lacim.uqam.ca/~plouffe/inspired2.pdf"))

make_entry(ID("338055"),
    Formula(Equal(Pi, 8 * Sum(1/((4*n+1)*(4*n+3)), For(n, 0, Infinity)))))

make_entry(ID("fbc53d"),
    Formula(Equal(Pi**2 / 6, Sum(1/n**2, For(n, 1, Infinity)))))

make_entry(ID("11302a"),
    Formula(Equal(Pi**2 / 12, Sum((-1)**(n+1)/n**2, For(n, 1, Infinity)))))

make_entry(ID("9bf21b"),
    Formula(Equal(Pi**4 / 90, Sum(1/n**4, For(n, 1, Infinity)))))

make_entry(ID("8dff72"),
    Formula(Equal(Pi, 2 * Sum(Atan(1/(n**2+n+1)), For(n, 0, Infinity)))))

make_entry(ID("31eecc"),
    Formula(Equal(Pi, 2 * Sum(Atan(1/Fibonacci(2*n+1)), For(n, 0, Infinity)))))

make_entry(ID("bad5d9"),
    Formula(Equal(Pi, Sqrt(3) * (3 * Sum((-1)**n / (3*n+1), For(n, 0, Infinity)) - Log(2)))))

make_entry(ID("54c80d"),
    Formula(Equal(Pi, 4*Sqrt(2) * Sum((-1)**n / (4*n+1), For(n, 0, Infinity)) - 2*Log(1+Sqrt(2)))))

make_entry(ID("f78fa0"),
    Formula(Equal(Pi, Sqrt(3) * (Div(9,2) * Sum(1/Binomial(2*n,n), For(n, 0, Infinity)) - 6))))

make_entry(ID("dbdf08"),
    Formula(Equal(Pi, Sqrt(3) * (Div(9,2) * Sum(n/Binomial(2*n,n), For(n, 1, Infinity)) - 3))))

make_entry(ID("a2e6f9"),
    Formula(Equal(Pi, Sum((3**n-1)*RiemannZeta(n+1) / 4**n, For(n, 1, Infinity)))))


# Product representations

make_entry(ID("69fe63"),
    Formula(Equal(Pi, 2*Product((4*n**2)/(4*n**2-1), For(n, 1, Infinity)))))

make_entry(ID("490cf4"),
    Formula(Equal(Pi, 2*Product(Sec(Pi/2**n), For(n, 2, Infinity)))))

make_entry(ID("a91200"),
    Formula(Equal(Pi**2/6, PrimeProduct((1-1/p**2)**(-1), For(p)))))

# todo: semantic representation of recurrence
make_entry(ID("6fce07"),
    Formula(Equal(2 / Pi, Where(Product(a_(n) / 2, For(n, 1, Infinity)), Def(a_(1), Sqrt(2)), Def(a_(n), Sqrt(2 + a_(n-1)))))))

# Limit representations

make_entry(ID("dea83d"),
    Formula(Equal(Pi, SequenceLimit((4/n**2) * Sum(Sqrt(n**2-k**2), For(k, 0, n)), For(n, Infinity)))))

make_entry(ID("e1e106"),
    Formula(Equal(Pi, SequenceLimit(16**n/(n*Binomial(2*n,n)**2), For(n, Infinity)))))

make_entry(ID("420007"),
    Formula(Equal(Pi, SequenceLimit(Div(1,2) * ((-1)**(n+1) * (Factorial(2*n) / BernoulliB(2*n)))**(1/Parentheses(2*n)), For(n, Infinity)))))

make_entry(ID("220e8d"),
    Formula(Equal(3/Pi**2, SequenceLimit(Mul(Div(1, Pow(N, 2)), Sum(Totient(n), For(n, 1, N))), For(N, Infinity)))))

# Special function representations

make_entry(ID("8fab22"),
    Formula(Equal(Pi, Gamma(Div(1, 2))**2)))

make_entry(ID("2371b9"),
    Formula(Equal(Pi, (Sqrt(3) / 2) * (Gamma(Div(1,3)) * Gamma(Div(2,3))))))

make_entry(ID("63ba30"),
    Formula(Equal(Pi, (1 / Sqrt(2)) * (Gamma(Div(1,4)) * Gamma(Div(3,4))))))

make_entry(ID("67bb53"),
    Formula(Equal(Pi, Sqrt(6 * RiemannZeta(2)))))

make_entry(ID("591d64"),
    Formula(Equal(Pi, BetaFunction(Div(1,2), Div(1,2)))))

make_entry(ID("033c51"),
    Formula(Equal(Pi, EisensteinG(2, ConstI))))

make_entry(ID("dabb47"),
    Formula(Equal(Pi, Div(1,2) * Gamma(Div(1,4))**Div(4,3) * AGM(1, Sqrt(2))**Div(2,3))))

make_entry(ID("ce5423"),
    Formula(Equal(Pi, 2 * EllipticK(0))))

make_entry(ID("07e35f"),
    Formula(Equal(Pi, 2 * EllipticE(0))))

make_entry(ID("9206a3"),
    Formula(Equal(Pi, Sqrt(6 * PolyLog(2, 1)))))

make_entry(ID("1448e3"),
    Formula(Equal(Pi, 2 * Hypergeometric2F1(Div(1,2), Div(1,2), Div(3,2), 1))))

make_entry(ID("a7095f"),
    Formula(Equal(1 / Pi, Div(1,2) * Hypergeometric2F1(Div(1,2),-Div(1,2),1,1))))

make_entry(ID("c6c108"),
    Formula(Equal(1 / Pi, Div(1,4) * Hypergeometric2F1(-Div(1,2),-Div(1,2),1,1))))

make_entry(ID("2a0316"),
    Formula(Equal(Pi, 2 * Hypergeometric2F1(-Div(1,2),-Div(1,2),Div(1,2),1))))

make_entry(ID("f55b36"),
    Formula(Equal(Pi, 4 * (Hypergeometric2F1(-Div(1,2),1,Div(1,2),-1)-1))))

make_entry(ID("769f6e"),
    Formula(Equal(Pi, 2 * Hypergeometric2F1(1,1,Div(1,2),Div(1,2))-4)))

make_entry(ID("488a30"),
    Formula(Equal(Pi, 4*(Sqrt(2)*Hypergeometric2F1(-Div(1,2),-Div(1,2),Div(1,2),Div(1,2))-1))))

make_entry(ID("826257"),
    Formula(Equal(Pi, Sqrt(3)*(Div(9,2) * Hypergeometric2F1(1,1,Div(1,2),Div(1,4)) - 6))))

make_entry(ID("3d276b"),
    Formula(Equal(Pi, 12 * Hypergeometric2F1(-Div(1,2),-Div(1,2),Div(1,2),Div(1,4)) - 6*Sqrt(3))))

make_entry(ID("2806fd"),
    Formula(Equal(Pi, (9/(2*Sqrt(3)) *Hypergeometric2F1(1, 1, Div(3,2), 1/4)))))

make_entry(ID("68b73d"),
    Formula(Equal(1/Pi, (2*Sqrt(3))/9 * Hypergeometric2F1(-Div(1,3),Div(1,3),1,1))))

make_entry(ID("42d727"),
    Formula(Equal(Pi, (5 * Sqrt(GoldenRatio + 2)) / (2 * GoldenRatio) * Hypergeometric2F1(1, 1, Div(3,2), 1/(2*GoldenRatio)**2))))


make_entry(ID("8ee7c9"),
    Formula(Equal(Pi, Sqrt(DigammaFunction(Div(1,4), 1) - 8*ConstCatalan))))

# todo: 2*catalan/dirichlet(-1,[0,1,0,-1],1)
make_entry(ID("f56273"),
    Formula(Equal(Pi, (4 * DirichletL(1, DirichletCharacter(4,3))))))


# Approximations

make_entry(ID("2516c2"),
    Formula(Less(Abs(Pi - Div(22,7)), Decimal("0.00127"))))

make_entry(ID("1e3a25"),
    Formula(Less(Abs(Pi - Div(355,113)), Decimal("2.67e-7"))))

make_entry(ID("fdc3a3"),
    Formula(Less(Abs(Pi - Log(Pow(640320,3)+744)/Sqrt(163)), Decimal("2.24e-31"))))

make_entry(ID("4c0698"),
    Formula(Less(Abs(1/Pi -
        Parentheses(12*Sum((-1)**n*Factorial(6*n)*(13591409+545140134*n)/(Factorial(3*n)*Factorial(n)**3*640320**(3*n+Div(3,2))),
            For(n, 0, N-1)))), Div(1,151931373056000**N))),
    Variables(N),
    Assumptions(Element(N, ZZGreaterEqual(0))))

