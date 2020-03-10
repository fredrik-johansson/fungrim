# -*- coding: utf-8 -*-

from ..expr import *

# todo: Espinosa-Moll balanced polygamma function?

def_Topic(
    Title("Digamma function"),
    Section("Definitions"),
    Entries(
        "f1527d",
        "8bdd03",
    ),
    Section("Illustrations"),
    Entries(
        "cf93bc",
        "a20761",
    ),
    Section("Domain and singularities"),
    Subsection("Digamma function"),
    Entries(
        "03d70f",
        "a0845d",
        "e7aef3",
        "f29019",
        "453c11",
    ),
    Subsection("Polygamma functions"),
    Entries(
        "9ee737",
        "d0bba3",
        "a8ab81",
        "394cdc",
        "d9403e",
        "86333d",
    ),
    Section("Specific values"),
    Description("Main topic: ", TopicReference("Specific values of the digamma function")),
    Subsection("Zeros"),
    Entries(
        "950e5a",
        "3f15eb",
    ),
    Subsection("Values at integers and simple fractions"),
    Entries(
        "ea2482",
        "ada157",
        "00c02a",
        "89bed3",
        "98f642",
        "7ec4f0",
        "3fe553",
    ),
    Subsection("Values of polygamma functions at integers and simple fractions"),
    Entries(
        "babd3c",
        "90b26f",
        "5ce30b",
        "807c7d",
    ),
    Section("Zeros"),
    Entries(
        "d0b65a",
        "6000d0",
        "233814",
        "fb9942",
    ),
    Section("Derivatives and differential equations"),
    Description("Related topic:", TopicReference("Gamma function")),
    Entries(
        "8415c7",
        "4b6ccb",
        "f1e02b",
        "6db9fc",
        "21f4f9",
    ),
    Section("Series representations"),
    Subsection("Series of rational functions"),
    Entries(
        "686524",
        "dfb55b",
    ),
    Subsection("Taylor series"),
    Entries(
        "c76eaf",
    ),
    Subsection("Laurent series"),
    Entries(
        "a2675b",
        "b4825b",
        "ddc7e1",
    ),
    Subsection("Asymptotic expansions"),
    Entries(
        "cf5355",
        "24c9e9",
    ),
    Subsection("Weierstrass product"),
    Entries(
        "bf533f",
    ),
    Section("Representation by other functions"),
    Entries(
        "bba4ec",
        "d6fbc8",
        "ee3dc5",
        "a6bdf5",
    ),
    Section("Functional equations"),
    Subsection("Recurrence relations"),
    Entries(
        "11dfd2",
        "9f32fe",
        "554ac2",
        "039051",
        "34fafa",
        "c687d6",
    ),
    Subsection("Reflection formula"),
    Entries(
        "adf5e2",
        "361f61",
    ),
    Subsection("Multiplication theorem"),
    Entries(
        "eec21a",
        "7b724b",
    ),
    Subsection("Conjugate symmetry"),
    Entries(
        "aa47cd",
        "5db5f2",
    ),
    Section("Integral representations"),
    Entries(
        "62b81d",
        "e1e71f",
        "a4cc3b",
        "f946a5",
        "cfb999",
        "d9c818",
        "4f5575",
        "c89abc",
        "547fcd",
    ),
    Section("Generating functions"),
    Entries(
        "4e3853",
        "88e89f",
    ),
    Section("Finite sums"),
    Entries(
        "1e47db",
        "458a97",
        "739819",
        "bb9eb6",
    ),
    Section("Bounds and inequalities"),
    Subsection("Real range and signs"),
    Entries(
        "4fdf65",
        "3c4f5f",
        "d4bdf8",
        "c86ca1",
        "15d56a",
        "0e5d90",
    ),
    Subsection("Real upper and lower bounds"),
    Entries(
        "24d810",
        "94a81f",
        "e63fe8",
        "8671a4",
        "5a3c4a",
    ),
    Subsection("Monotonicity"),
    Entries(
        "6cabb7",
        "b16177",
    ),
    Section("Summation of rational functions"),
    Subsection("Infinite series"),
    Entries(
        "7212ea",
        "f42042",
        "d02cf9",
        "21e21a",
        "b7f13b",
    ),
    Subsection("Finite sums"),
    Entries(
        "19e67f",
    ),
)

def_Topic(
    Title("Specific values of the digamma function"),
    Description("Related topic: ", TopicReference("Digamma function")),
    Section("Zeros"),
    Entries(
        "950e5a",
        "3f15eb",
    ),
    Section("Values at integers"),
    Entries(
        "ea2482",
        "ada157",
        "75f9bf",
        "00c02a",
    ),
    Section("Values at simple fractions"),
    Entries(
        "89bed3",
        "98f642",
        "45a969",
        "7ec4f0",
        "f93bae",
        "177de7",
        "967bbb",
        "8c368f",
    ),
    Section("Values at general fractions"),
    Entries(
        "3fe553",
    ),
    Section("Values of polygamma functions at integers and simple fractions"),
    Entries(
        "babd3c",
        "4a30f1",
        "a62320",
        "fa0292",
        "90b26f",
        "595f46",
        "b31fd2",
        "2251c6",
        "5ce30b",
        "807c7d",
        "d2f9fb",
        "03aca0",
        "e83059",
        "bb88c8",
        "921d61",
    ),
    Section("Specific complex parts"),
    Entries(
        "03e2a6",
        "22a9cd",
        "6f3fec",
    ),
    Section("Limits at singularities"),
    Entries(
        "42c1f5",
        "78c19c",
        "1cbe83",
        "dce62c",
    ),
    Section("Infinite sums over zeros"),
    Entries(
        "1165fc",
        "39ce44",
        "a4f9c9",
        "6547da",
    ),
)


# Definitions

make_entry(ID("f1527d"),
    SymbolDefinition(DigammaFunction, DigammaFunction(z), "Digamma function"),
    Description(SourceForm(DigammaFunction(z)), ", rendered as", DigammaFunction(z), ", represents the digamma function of argument", z, "."),
    Description(SourceForm(DigammaFunction(z, m)), ", rendered as", DigammaFunction(z, m), ", represents the order", m,
        "derivative of the digamma function of argument", z, ". ",
        "This is also known as the polygamma function of order", m, "and argument", z, ". ",
        "The case", Equal(m, 1), "(rendered as ", DigammaFunction(z,1), ") is sometimes called the trigamma function, ", Equal(m, 2), "the tetragamma function, etc."),
)

make_entry(ID("8bdd03"),
    SymbolDefinition(DigammaFunctionZero, DigammaFunctionZero(n), "Zero of the digamma function"))

# Illustrations

make_entry(ID("cf93bc"),
    Image(Description("X-ray of", DigammaFunction(z), "on", Element(z, ClosedInterval(-5,5) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_digamma")),
    description_xray,
    )

make_entry(ID("a20761"),
    Image(Description("X-ray of", DigammaFunction(z,1), "on", Element(z, ClosedInterval(-5,5) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_trigamma")),
    description_xray,
    )

# Domain and singularities

## Digamma function

make_entry(ID("03d70f"),
    Formula(Implies(Element(x, SetMinus(RR, ZZLessEqual(0))), Element(DigammaFunction(x), RR))),
    Variables(x))

make_entry(ID("a0845d"),
    Formula(Implies(Element(z, SetMinus(CC, ZZLessEqual(0))), Element(DigammaFunction(z), CC))),
    Variables(z))

make_entry(ID("e7aef3"),
    Formula(IsHolomorphic(DigammaFunction(z), ForElement(z, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("f29019"),
    Formula(IsMeromorphic(DigammaFunction(z), ForElement(z, CC))))

make_entry(ID("453c11"),
    Formula(Equal(Poles(DigammaFunction(z), ForElement(z, CC)), ZZLessEqual(0))))

## Polygamma functions

make_entry(ID("9ee737"),
    Formula(Equal(DigammaFunction(z,0), DigammaFunction(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("d0bba3"),
    Formula(Implies(And(Element(m, ZZGreaterEqual(0)), Element(x, SetMinus(RR, ZZLessEqual(0)))), Element(DigammaFunction(x, m), RR))),
    Variables(x, m))

make_entry(ID("a8ab81"),
    Formula(Implies(And(Element(m, ZZGreaterEqual(0)), Element(z, SetMinus(CC, ZZLessEqual(0)))), Element(DigammaFunction(z, m), CC))),
    Variables(z, m))

make_entry(ID("394cdc"),
    Formula(IsHolomorphic(DigammaFunction(z, m), ForElement(z, SetMinus(CC, ZZLessEqual(0))))),
    Variables(m),
    Assumptions(Element(m, ZZGreaterEqual(0))))

make_entry(ID("d9403e"),
    Formula(IsMeromorphic(DigammaFunction(z, m), ForElement(z, CC))),
    Variables(m),
    Assumptions(Element(m, ZZGreaterEqual(0))))

make_entry(ID("86333d"),
    Formula(Equal(Poles(DigammaFunction(z, m), ForElement(z, CC)), ZZLessEqual(0))),
    Variables(m),
    Assumptions(Element(m, ZZGreaterEqual(0))))

# Derivatives and differential equations

make_entry(ID("8415c7"),
    Formula(Equal(DigammaFunction(z), ComplexDerivative(Gamma(z), For(z, z)) / Gamma(z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("4b6ccb"),
    Formula(Equal(DigammaFunction(z), ComplexBranchDerivative(Brackets(LogGamma(z)), For(z, z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("f1e02b"),
    Formula(Equal(DigammaFunction(z, m), ComplexBranchDerivative(Brackets(LogGamma(z)), For(z, z, m + 1)))),
    Variables(m, z),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("6db9fc"),
    Formula(Equal(ComplexDerivative(Brackets(DigammaFunction(z)), For(z, z, n)), DigammaFunction(z, n))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("21f4f9"),
    Formula(Equal(ComplexDerivative(Brackets(DigammaFunction(z, m)), For(z, z, n)), DigammaFunction(z, m+n))),
    Variables(n, m, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)), Element(z, CC), NotElement(z, ZZLessEqual(0)))))

# Series representations

make_entry(ID("686524"),
    Formula(Equal(DigammaFunction(z), -ConstGamma + Sum(Parentheses(1/(n+1) - 1/(n+z)), For(n, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("dfb55b"),
    Formula(Equal(DigammaFunction(z, m), (-1)**(m+1) * Factorial(m) * Sum(1/(n+z)**(m+1), For(n, 0, Infinity)))),
    Variables(m, z),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(z, CC), NotElement(z, ZZLessEqual(0)))))

## Taylor series

make_entry(ID("c76eaf"),
    Formula(Equal(DigammaFunction(1+z), -ConstGamma + Sum((-1)**(n+1) * RiemannZeta(n+1) * z**n, For(n, 1, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 1))))

## Laurent series

make_entry(ID("a2675b"),
    Formula(Equal(DigammaFunction(z), -(1/z) - ConstGamma + Sum((-1)**(n+1) * RiemannZeta(n+1) * z**n, For(n, 1, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("b4825b"),
    Formula(Equal(DigammaFunction(-n+z), -(1/z) + DigammaFunction(n+1) + Sum(((-1)**(k+1) * RiemannZeta(k+1) + Sum(1/j**(k+1), For(j, 1, n))) * z**k, For(k, 1, Infinity)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("ddc7e1"),
    Formula(Equal(DigammaFunction(-n+z, m), (-1)**(m+1)*Factorial(m)/z**(m+1) + Sum(RisingFactorial(k+1,m) * ((-1)**(m+k+1)*RiemannZeta(m+k+1) + Sum(1/j**(k+m+1), For(j, 1, n))) * z**k, For(k, 0, Infinity)))),
    Variables(n, m, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(1)), Element(z, CC), Less(Abs(z), 1))))

## Asymptotic expansions

make_entry(ID("cf5355"),
    Formula(Equal(DigammaFunction(z), Log(z) - 1/(2*z) - Sum(BernoulliB(2*n)/(2*n*z**(2*n)), For(n, 1, N-1)) + Derivative(StirlingSeriesRemainder(N, z), For(z, z)))),
    Variables(z, N),
    Assumptions(And(Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))), Element(N, ZZGreaterEqual(0)))))

make_entry(ID("24c9e9"),
    Formula(Equal(DigammaFunction(z, m),
        ((-1)**(m+1) / Factorial(m)) * (1 / (m*z**m) + 1/(2*z**(m+1)) + 
            Sum((RisingFactorial(m+1,2*n-1)/Factorial(2*n)) * (BernoulliB(2*n) / z**(m+2*n)), For(n, 1, N-1)))
            + Derivative(StirlingSeriesRemainder(N, z), For(z, z, m+1)))),
    Variables(m, z, N),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))), Element(N, ZZGreaterEqual(0)))))

# todo: valid everywhere when removing the poles!
make_entry(ID("bf533f"),
    Formula(Equal(DigammaFunction(z)/Gamma(z),
        -(Exp(2*ConstGamma*z)*Product((1-z/DigammaFunctionZero(n)) * Exp(z/DigammaFunctionZero(n)), For(n, 0, Infinity))))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))),
    References("https://doi.org/10.1080%2F10652469.2017.1376193"))

# Representation by other functions

make_entry(ID("bba4ec"),
    Formula(Equal(DigammaFunction(z, m), (-1)**(m+1) * Factorial(m) * HurwitzZeta(m+1, z))),
    Variables(m, z),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("d6fbc8"),
    Formula(Equal(DigammaFunction(z, m), (-1)**(m+1) * Factorial(m) * LerchPhi(1, m+1, z))),
    Variables(m, z),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("ee3dc5"),
    Formula(Equal(DigammaFunction(z), (z-1) * Hypergeometric3F2(1, 1, 2-z, 2, 2, 1) - ConstGamma)),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))),
    References("http://functions.wolfram.com/GammaBetaErf/PolyGamma/26/01/01/0001/"))

make_entry(ID("a6bdf5"),
    Formula(Equal(DigammaFunction(z), -StieltjesGamma(0, z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

# Zeros

make_entry(ID("d0b65a"),
    Formula(Implies(Element(n, ZZGreaterEqual(0)), Element(DigammaFunctionZero(n), RR))))

make_entry(ID("6000d0"),
    Formula(Equal(Zeros(DigammaFunction(z), ForElement(z, CC)), Set(DigammaFunctionZero(n), ForElement(n, ZZGreaterEqual(0))))))

make_entry(ID("233814"),
    Formula(Equal(DigammaFunctionZero(n),
        Where(UniqueZero(DigammaFunction(x), ForElement(x, S)),
            Equal(S,
                Cases(Tuple(OpenInterval(0, Infinity), Equal(n, 0)),
                      Tuple(OpenInterval(-n,-n+1), Less(n, 0))))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("950e5a"),
    Description("Table of", DigammaFunctionZero(n), "to 50 digits for", LessEqual(0, n, 10)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(DigammaFunctionZero(n), 50)),
      TableSplit(1),
      List(
    Tuple(0, Decimal("1.4616321449683623412626595423257213284681962040064")),
    Tuple(1, Decimal("-0.50408300826445540925826930453330249895538518236858")),
    Tuple(2, Decimal("-1.5734984731623904587782860436904346126550408591168")),
    Tuple(3, Decimal("-2.6107208684441446500015377157187242079510740108735")),
    Tuple(4, Decimal("-3.6352933664369010978391815669460177139484238611935")),
    Tuple(5, Decimal("-4.6532377617431424417145981511482073637190694161339")),
    Tuple(6, Decimal("-5.6671624415568855358494741745181554247117957876948")),
    Tuple(7, Decimal("-6.6784182130734267428298558886022000992046860101508")),
    Tuple(8, Decimal("-7.6877883250316260374400988918437049536838217978826")),
    Tuple(9, Decimal("-8.6957641638164012664887761608046458202724380849667")),
    Tuple(10, Decimal("-9.7026725400018637360844267648942153185775505998219")),
    )))

make_entry(ID("fb9942"),
    Formula(AsymptoticTo(DigammaFunctionZero(n), -n + (1/Pi)*Atan(Pi/Log(n)), n, Infinity)))

# Specific values

## Zeros and poles

make_entry(ID("3f15eb"),
    Formula(Equal(DigammaFunction(DigammaFunctionZero(n)), 0)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("42c1f5"),
    Formula(Equal(DigammaFunction(-n), UnsignedInfinity)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("78c19c"),
    Formula(Equal(DigammaFunction(-n, m), UnsignedInfinity)),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)))))

make_entry(ID("1cbe83"),
    Formula(Equal(DigammaFunction(Infinity, m), RealLimit(DigammaFunction(x), For(x, Infinity)),
        Cases(Tuple(Infinity, Equal(m, 0)), Tuple(0, Greater(m, 0))))),
    Variables(m),
    Assumptions(Element(m, ZZGreaterEqual(0))))

make_entry(ID("dce62c"),
    Formula(Equal(RightLimit(DigammaFunction(x), For(x, 0)), (-1)**(m+1) * Infinity)),
    Variables(m),
    Assumptions(Element(m, ZZGreaterEqual(0))))

## Values at integers

make_entry(ID("ea2482"),
    Formula(Equal(DigammaFunction(1), -ConstGamma)))

make_entry(ID("ada157"),
    Formula(Equal(DigammaFunction(2), 1-ConstGamma)))

make_entry(ID("75f9bf"),
    Formula(Equal(DigammaFunction(3), Div(3,2)-ConstGamma)))

make_entry(ID("00c02a"),
    Formula(Equal(DigammaFunction(n), HarmonicNumber(n-1)-ConstGamma)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

## Values at simple fractions

make_entry(ID("89bed3"),
    Formula(Equal(DigammaFunction(Div(1,2)), -(2*Log(2))-ConstGamma)))

make_entry(ID("98f642"),
    Formula(Equal(DigammaFunction(Div(1,3)), -(Sqrt(3)*Pi/6) - ConstGamma - 3*Log(3)/2)))

make_entry(ID("45a969"),
    Formula(Equal(DigammaFunction(Div(2,3)), Sqrt(3)*Pi/6 - ConstGamma - 3*Log(3)/2)))

make_entry(ID("7ec4f0"),
    Formula(Equal(DigammaFunction(Div(1,4)), -(Pi/2) - ConstGamma - 3*Log(2))))

make_entry(ID("f93bae"),
    Formula(Equal(DigammaFunction(Div(3,4)), Pi/2 - ConstGamma - 3*Log(2))))

make_entry(ID("177de7"),
    Formula(Equal(DigammaFunction(Div(1,6)), -(Sqrt(3)*Pi/2) - ConstGamma - 2*Log(2) - 3*Log(3)/2)))

make_entry(ID("967bbb"),
    Formula(Equal(DigammaFunction(Div(5,6)), Sqrt(3)*Pi/2 - ConstGamma - 2*Log(2) - 3*Log(3)/2)))

make_entry(ID("8c368f"),
    Formula(Equal(DigammaFunction(Div(1,8)), -(Pi/2*(Sqrt(2)+1)) - ConstGamma - 4*Log(2) - (Log(2+Sqrt(2))-Log(2-Sqrt(2)))/Sqrt(2))))

## Values at general fractions

make_entry(ID("3fe553"),
    Formula(Equal(DigammaFunction(Div(p,q)),
        -ConstGamma - Log(2*q) - Pi/2 * Cot(Pi * p / q) + 2 * Sum(Cos((2*Pi*k*p)/q) * Log(Sin(Pi*k/q)), For(k, 1, Floor((q-1)/2))))),
    Variables(p, q),
    Assumptions(And(Element(q, ZZGreaterEqual(2)), Element(p, Range(1, q-1)))))

## Polygamma functions at integers and simple fractions

make_entry(ID("babd3c"),
    Formula(Equal(DigammaFunction(1, 1), Pi**2 / 6)))

make_entry(ID("fa0292"),
    Formula(Equal(DigammaFunction(2, 1), Pi**2 / 6 - 1)))

make_entry(ID("4a30f1"),
    Formula(Equal(DigammaFunction(1, 2), -(2*RiemannZeta(3)))))

make_entry(ID("a62320"),
    Formula(Equal(DigammaFunction(1, m), (-1)**(m+1) * Factorial(m) * RiemannZeta(m+1))),
    Variables(m),
    Assumptions(Element(m, ZZGreaterEqual(1))))

make_entry(ID("90b26f"),
    Formula(Equal(DigammaFunction(n, m), (-1)**(m+1) * Factorial(m) * HurwitzZeta(m+1, n))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(m, ZZGreaterEqual(1)))))

make_entry(ID("595f46"),
    Formula(Equal(DigammaFunction(Div(1,2), 1), Pi**2 / 2)))

make_entry(ID("5ce30b"),
    Formula(Equal(DigammaFunction(Div(1,2), m), (-1)**(m+1) * (2**(m+1)-1) * Factorial(m) * RiemannZeta(m+1))),
    Variables(m),
    Assumptions(Element(m, ZZGreaterEqual(1))))

make_entry(ID("807c7d"),
    Formula(Equal(DigammaFunction(Div(1,4), 1), Pi**2 + 8*ConstCatalan)))

make_entry(ID("d2f9fb"),
    Formula(Equal(DigammaFunction(Div(3,4), 1), Pi**2 - 8*ConstCatalan)))

make_entry(ID("03aca0"),
    Formula(Equal(DigammaFunction(Div(1,4), 2), -(2*Pi**3) - 56*RiemannZeta(3))))

make_entry(ID("e83059"),
    Formula(Equal(DigammaFunction(Div(3,4), 2), 2*Pi**3 - 56*RiemannZeta(3))))

make_entry(ID("b31fd2"),
    Formula(Equal(DigammaFunction(Div(1,2), 2), -(14*RiemannZeta(3)))))

make_entry(ID("2251c6"),
    Formula(Equal(DigammaFunction(Div(1,2), 3), Pi**4)))

make_entry(ID("bb88c8"),
    Formula(Equal(DigammaFunction(Div(1,6), 2), -(182*RiemannZeta(3)) - 4*Sqrt(3)*Pi**3)))

make_entry(ID("921d61"),
    Formula(Equal(DigammaFunction(Div(5,6), 2), -(182*RiemannZeta(3)) + 4*Sqrt(3)*Pi**3)))

## Special complex parts

make_entry(ID("03e2a6"),
    Formula(Equal(Im(DigammaFunction(ConstI*y)), (Pi/2) * Coth(Pi*y) + 1/(2*y))),
    Variables(y),
    Assumptions(And(Element(y, RR), NotEqual(y, 0))))

make_entry(ID("22a9cd"),
    Formula(Equal(Im(DigammaFunction(1+ConstI*y)), (Pi/2) * Coth(Pi*y) - 1/(2*y))),
    Variables(y),
    Assumptions(And(Element(y, RR), NotEqual(y, 0))))

make_entry(ID("6f3fec"),
    Formula(Equal(Im(DigammaFunction(Div(1,2)+ConstI*y)), (Pi/2) * Tanh(Pi*y))),
    Variables(y),
    Assumptions(And(Element(y, RR), NotEqual(y, 0))))

# Functional equations

## Recurrence relations

make_entry(ID("11dfd2"),
    Formula(Equal(DigammaFunction(z+1), DigammaFunction(z) + 1/z)),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("9f32fe"),
    Formula(Equal(DigammaFunction(z+n), DigammaFunction(z) + Sum(1/(z+k), For(k, 0, n-1)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("554ac2"),
    Formula(Equal(DigammaFunction(z-n), DigammaFunction(z) - Sum(1/(z-k), For(k, 1, n)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(0)), NotElement(z-n, ZZLessEqual(0)))))


make_entry(ID("039051"),
    Formula(Equal(DigammaFunction(z+1, m), DigammaFunction(z, m) + ((-1)**m * Factorial(m))/z**(m+1))),
    Variables(m, z),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("34fafa"),
    Formula(Equal(DigammaFunction(z+n, m), DigammaFunction(z, m) + (-1)**m * Factorial(m) * Sum(1/(z+k)**(m+1), For(k, 0, n-1)))),
    Variables(m, z, n),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(z, CC), NotElement(z, ZZLessEqual(0)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("c687d6"),
    Formula(Equal(DigammaFunction(z-n, m), DigammaFunction(z, m) - (-1)**m * Factorial(m) * Sum(1/(z-k)**(m+1), For(k, 1, n)))),
    Variables(m, z, n),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(z, CC), Element(n, ZZGreaterEqual(0)), NotElement(z-n, ZZLessEqual(0)))))

## Reflection formula

make_entry(ID("adf5e2"),
    Formula(Equal(DigammaFunction(1-z), DigammaFunction(z) + Pi*Cot(Pi*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZ))))

make_entry(ID("361f61"),
    Formula(Equal(DigammaFunction(1-z, m), (-1)**m * (DigammaFunction(z, m) + Pi * ComplexDerivative(Cot(Pi*z), For(z, z, m))))),
    Variables(m, z),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(z, CC), NotElement(z, ZZ))))

## Multiplication theorem

make_entry(ID("eec21a"),
    Formula(Equal(DigammaFunction(n*z), Log(n) + Div(1,n) * Sum(DigammaFunction(z+k/n), For(k, 0, n-1)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(z, CC), NotElement(Mul(n, z), ZZLessEqual(0)))))

make_entry(ID("7b724b"),
    Formula(Equal(DigammaFunction(n*z, m), Div(1,n**(m+1)) * Sum(DigammaFunction(z+k/n, m), For(k, 0, n-1)))),
    Variables(m, n, z),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(n, ZZGreaterEqual(1)), Element(z, CC), NotElement(Mul(n, z), ZZLessEqual(0)))))

## Conjugate symmetry

make_entry(ID("aa47cd"),
    Formula(Equal(DigammaFunction(Conjugate(z)), Conjugate(DigammaFunction(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("5db5f2"),
    Formula(Equal(DigammaFunction(Conjugate(z), m), Conjugate(DigammaFunction(z, m)))),
    Variables(m, z),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(z, CC))))

# Integral representations

make_entry(ID("62b81d"),
    Formula(Equal(DigammaFunction(z), Integral(Parentheses(Exp(-t)/t - Exp(-(z*t))/(1-Exp(-t))), For(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("e1e71f"),
    Formula(Equal(DigammaFunction(z), Integral(Parentheses(Exp(-t) - 1/(1+t)**z) * Div(1,t), For(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("a4cc3b"),
    Formula(Equal(DigammaFunction(z), -ConstGamma + Integral((1-t**(z-1))/(1-t), For(t, 0, 1)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("f946a5"),
    Formula(Equal(DigammaFunction(z), -ConstGamma + Integral((Exp(-t)-Exp(-(z*t)))/(1-Exp(-t)), For(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("cfb999"),
    Formula(Equal(DigammaFunction(z), Log(z) + Integral(Exp(-(z*t)) * Parentheses(1/t - 1/(1-Exp(-t))), For(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("d9c818"),
    Formula(Equal(DigammaFunction(z), Log(z) - 1/(2*z) - 2*Integral(t/((t**2+z**2)*(Exp(2*Pi*t)-1)), For(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("4f5575"),
    Formula(Equal(DigammaFunction(z), Log(z) - 1/(2*z) - Integral(Exp(-(z*t))*Parentheses(Div(1,2) - 1/t + 1/(Exp(t)-1)), For(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("c89abc"),
    Formula(Equal(DigammaFunction(z, m), (-1)**(m+1) * Integral(((t**m * Exp(-(z*t))) / (1 - Exp(-t))), For(t, 0, Infinity)))),
    Variables(z, m),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0), Element(m, ZZGreaterEqual(1)))))

make_entry(ID("547fcd"),
    Formula(Equal(DigammaFunction(z, m), -Integral(t**(z-1) / (1-t) * Log(t)**m, For(t, 0, 1)))),
    Variables(z, m),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0), Element(m, ZZGreaterEqual(1)))))

# Generating functions

make_entry(ID("4e3853"),
    Formula(Equal(Sum(DigammaFunction(n) * z**n, For(n, 1, Infinity)), (z * (ConstGamma + Log(1-z))) / (z - 1))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("88e89f"),
    Formula(Equal(Sum(DigammaFunction(n) * (z**n / Factorial(n)), For(n, 1, Infinity)),
        z * ComplexDerivative(Hypergeometric1F1(a,2,z), For(a, 1)) - ConstGamma * (Exp(z) - 1))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Summation

## Finite sums

make_entry(ID("1e47db"),
    Formula(Equal(Sum(DigammaFunction(k), For(k, 1, n)), n * (DigammaFunction(n+1) - 1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("458a97"),
    Formula(Equal(Sum(DigammaFunction(k/n) * Exp(2*Pi*r*k*ConstI/n), For(k, 1, n)), n*Log(1-Exp(2*Pi*r*ConstI/n)))),
    Variables(r, n),
    Assumptions(And(Element(n, ZZGreaterEqual(2)), Element(r, Range(1, n-1)))))

make_entry(ID("739819"),
    Formula(Equal(Sum(DigammaFunction(k/n) * Cos(2*Pi*r*k/n), For(k, 1, n)), n*Log(2*Sin(Pi*r/n)))),
    Variables(r, n),
    Assumptions(And(Element(n, ZZGreaterEqual(2)), Element(r, Range(1, n-1)))))

make_entry(ID("bb9eb6"),
    Formula(Equal(Sum(DigammaFunction(k/n) * Sin(2*Pi*r*k/n), For(k, 1, n)), Pi*(r-n/2))),
    Variables(r, n),
    Assumptions(And(Element(n, ZZGreaterEqual(2)), Element(r, Range(1, n-1)))))

## Infinite sums over zeros

make_entry(ID("1165fc"),
    Formula(Equal(Sum(1/DigammaFunctionZero(n)**2, For(n, 0, Infinity)), 
        ConstGamma**2 + Pi**2/2)))

make_entry(ID("39ce44"),
    Formula(Equal(Sum(1/DigammaFunctionZero(n)**3, For(n, 0, Infinity)), 
        -ConstGamma**3 - ConstGamma*Pi**2/2 - 4*RiemannZeta(3))))

make_entry(ID("a4f9c9"),
    Formula(Equal(Sum(1/DigammaFunctionZero(n)**4, For(n, 0, Infinity)), 
        ConstGamma**4 + Pi**4/9 + 2*ConstGamma**2*Pi**2/3 + 4*(ConstGamma*RiemannZeta(3)))))

make_entry(ID("6547da"),
    Formula(Equal(Sum(1/DigammaFunctionZero(n)**(r+1), For(n, 0, Infinity)), 
        Where(ComplexDerivative(f(z), For(z, 0, r)) / Factorial(r),
            Equal(f(z), ComplexLimit(Parentheses(DigammaFunction(t) - DigammaFunction(t,1)/DigammaFunction(t)), For(t, z)))))),
    Variables(r),
    Assumptions(Element(r, ZZGreaterEqual(1))),
    References("https://doi.org/10.1080%2F10652469.2017.1376193"))

# Bounds and inequalities

## Real range and signs

make_entry(ID("4fdf65"),
    Formula(Implies(Element(x, OpenInterval(DigammaFunctionZero(0), Infinity)), Element(DigammaFunction(x), OpenInterval(0, Infinity)))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("3c4f5f"),
    Formula(Implies(Element(x, OpenInterval(0, DigammaFunctionZero(0))), Element(DigammaFunction(x), OpenInterval(-Infinity, 0)))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("d4bdf8"),
    Formula(Implies(Element(x, OpenInterval(-n, DigammaFunctionZero(n))), Element(DigammaFunction(x), OpenInterval(-Infinity, 0)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(x, RR))))

make_entry(ID("c86ca1"),
    Formula(Implies(Element(x, OpenInterval(DigammaFunctionZero(n), -n+1)), Element(DigammaFunction(x), OpenInterval(0, Infinity)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(x, RR))))

make_entry(ID("15d56a"),
    Formula(Implies(And(Element(x, OpenInterval(0, Infinity)), Element(m, ZZGreaterEqual(1))),
        Element(DigammaFunction(x, m), Cases(Tuple(OpenInterval(0, Infinity), Odd(m)), Tuple(OpenInterval(-Infinity, 0), Even(m)))))),
    Variables(x, m),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(x, RR))))

make_entry(ID("0e5d90"),
    Formula(Implies(And(Element(m, ZZGreaterEqual(1)), Odd(m), Element(x, SetMinus(RR, ZZLessEqual(0)))), Element(DigammaFunction(x, m), OpenInterval(0, Infinity)))),
    Variables(x, m),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(x, RR))))

## Real upper and lower bounds

make_entry(ID("24d810"),
    Formula(Less(DigammaFunction(x), Log(x))),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0, Infinity))))

make_entry(ID("94a81f"),
    Formula(Less(DigammaFunction(x), Log(x) - 1/(2*x))),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0, Infinity))))

make_entry(ID("e63fe8"),
    Formula(Greater(DigammaFunction(x), Log(x) - 1/x)),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0, Infinity))))

make_entry(ID("8671a4"),
    Formula(Less((-1)**(m+1) * DigammaFunction(x, m), Factorial(m-1) / x**m + Factorial(m) / x**(m+1))),
    Variables(m, x),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(x, OpenInterval(0, Infinity)))))

make_entry(ID("5a3c4a"),
    Formula(Greater((-1)**(m+1) * DigammaFunction(x, m), Factorial(m-1) / x**m + Factorial(m) / (2 * x**(m+1)))),
    Variables(m, x),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(x, OpenInterval(0, Infinity)))))

## Monotonicity

make_entry(ID("6cabb7"),
    Formula(Greater(DigammaFunction(x + y), DigammaFunction(x))),
    Variables(x, y),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(y, OpenInterval(0, Infinity)))))

make_entry(ID("b16177"),
    Formula(Cases(
        Tuple(Greater(DigammaFunction(x + y, m), DigammaFunction(x)), Even(m)),
        Tuple(Less(DigammaFunction(x + y, m), DigammaFunction(x)), Odd(m)))),
    Variables(x, y, m),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(x, OpenInterval(0, Infinity)), Element(y, OpenInterval(0, Infinity)))))

# Summation of rational functions

# Infinite series

make_entry(ID("7212ea"),
    Formula(Equal(Sum((-1)**n / (n+a), For(n, 0, Infinity)), Div(1,2) * (DigammaFunction((a+1)/2) - DigammaFunction(a/2)))),
    Variables(a),
    Assumptions(And(Element(a, CC), NotElement(a, ZZLessEqual(0)))))

make_entry(ID("f42042"),
    Formula(Equal(Sum(1 / (n+a)**r, For(n, 0, Infinity)), ((-1)**r / Factorial(r-1)) * DigammaFunction(a, r-1))),
    Variables(r, a),
    Assumptions(And(Element(r, ZZGreaterEqual(2)), Element(a, CC), NotElement(a, ZZLessEqual(0)))))

make_entry(ID("d02cf9"),
    Formula(Equal(Sum((-1)**n / (n+a)**r, For(n, 0, Infinity)), ((-1)**r / (2**r * Factorial(r-1))) * (DigammaFunction(a/2, r-1) - DigammaFunction((a+1)/2, r-1)))),
    Variables(r, a),
    Assumptions(And(Element(r, ZZGreaterEqual(2)), Element(a, CC), NotElement(a, ZZLessEqual(0)))))

make_entry(ID("21e21a"),
    Formula(Equal(Sum(1 / ((n+a)*(n+b)), For(n, 0, Infinity)),
        Cases(Tuple(1/(a-b) * (DigammaFunction(a) - DigammaFunction(b)), NotEqual(a, b)),
              Tuple(DigammaFunction(a, 1), Equal(a, b))))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), NotElement(a, ZZLessEqual(0)), NotElement(b, ZZLessEqual(0)))))

make_entry(ID("b7f13b"),
    Formula(Equal(Sum((-1)**n / ((n+a)*(n+b)), For(n, 0, Infinity)),
        Cases(Tuple(1/(2*(a-b)) * (DigammaFunction(a/2) + DigammaFunction((b+1)/2) - DigammaFunction(b/2) - DigammaFunction((a+1)/2)), NotEqual(a, b)),
              Tuple(Div(1,4) * (DigammaFunction(a/2, 1) - DigammaFunction((a+1)/2, 1)), Equal(a, b))))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), NotElement(a, ZZLessEqual(0)), NotElement(b, ZZLessEqual(0)))))

# Finite series
# todo: add more?

make_entry(ID("19e67f"),
    Formula(Equal(Sum(1 / (n+a), For(n, A, B)), DigammaFunction(a+B+1) - DigammaFunction(a+A))),
    Variables(a, A, B),
    Assumptions(And(Element(a, CC), Element(A, ZZ), Element(B, ZZ), LessEqual(A,B), NotElement(-a, Range(A,B)))))

