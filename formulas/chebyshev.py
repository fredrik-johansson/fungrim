# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Chebyshev polynomials"),
    Section("Definitions"),
    Entries(
        "1a0c43",
        "d4e9aa",
    ),
    Section("Tables"),
    Entries(
        "85e42e",
        "fd8310",
    ),
    Section("Specific values"),
    Entries(
        "c76e72",
        "be5652",
        "48765b",
        "75eacb",
        "9001e6",
        "fc5d42",
        "2760e7",
        "a46d91",
        "42102c",
        "e03fa4",
        "be9a45",
        "2a5337",
        "7d111e",
    ),
    Section("Zeros and extrema"),
    Entries(
        "7a7d1d",
        "ce39ac",
        "3d25dd",
        "b5a25e",
        "db2b0a",
    ),
    Section("Symmetries"),
    Entries(
        "6a24ab",
        "88aeb6",
        "9093a3",
        "78f5bb",
    ),
    Section("Orthogonality"),
    Entries(
        "2c26a1",
        "473c36",
    ),
    Section("Differential equations"),
    Entries(
        "0ed026",
        "30b67b",
    ),
    Section("Recurrence relations"),
    Entries(
        "faeed9",
        "d1ef91",
        "8a785a",
        "303204",
        "7b2c26",
        "ce5e03",
        "0649c9",
        "844561",
    ),
    Section("Order transformations"),
    Entries(
        "7e882c",
        "ed5222",
        "4b83c6",
        "de0968",
        "82288c",
        "5f09f4",
    ),
    Section("Trigonometric formulas"),
    Entries(
        "fda800",
        "2fc479",
        "b8fdcd",
        "f4b3fa",
        "4c7aeb",
        "9789ee",
    ),
    Section("Power formulas"),
    Entries(
        "0cbe75",
        "61375f",
        "fdf80d",
        "42eb01",
        "5bd0ec",
    ),
#    Section("Sum representations"),
#    Entries(
#    ),
    Section("Product representations"),
    Entries(
        "305a29",
        "f5fa23",
    ),
    Section("Hypergeometric representations"),
    Entries(
        "382679",
        "ce9a39",
    ),
    Section("Generating functions"),
    Entries(
        "685d1a",
        "b5049d",
        "27b2bb",
        "9d7c61",
        "fff8ff",
    ),
    Section("Derivatives"),
    Entries(
        "1a0d11",
        "05fe07",
        "35e13b",
        "6582c4",
        "e1797b",
        "12ce84",
        "a68f0e",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "15dd69",
        "3c662e",
        "c718ea",
        "0b3fd6",
        "443759",
        "2a4b9d",
    ),
)

# Definitions

make_entry(ID("1a0c43"),
    SymbolDefinition(ChebyshevT, ChebyshevT(n,x), "Chebyshev polynomial of the first kind"))

make_entry(ID("d4e9aa"),
    SymbolDefinition(ChebyshevU, ChebyshevU(n,x), "Chebyshev polynomial of the second kind"))

# Tables

make_entry(ID("85e42e"),
    Description("Table of", ChebyshevT(n,x), "for", LessEqual(0, n, 15)),
    Table(TableRelation(Tuple(n, p), Equal(ChebyshevT(n,x), p)),
      TableHeadings(n, ChebyshevT(n,x)), TableSplit(1),
      List(
Tuple(0, 1),
Tuple(1, x),
Tuple(2, 2*x**2 - 1),
Tuple(3, 4*x**3 - 3*x),
Tuple(4, 8*x**4 - 8*x**2 + 1),
Tuple(5, 16*x**5 - 20*x**3 + 5*x),
Tuple(6, 32*x**6 - 48*x**4 + 18*x**2 - 1),
Tuple(7, 64*x**7 - 112*x**5 + 56*x**3 - 7*x),
Tuple(8, 128*x**8 - 256*x**6 + 160*x**4 - 32*x**2 + 1),
Tuple(9, 256*x**9 - 576*x**7 + 432*x**5 - 120*x**3 + 9*x),
Tuple(10, 512*x**10 - 1280*x**8 + 1120*x**6 - 400*x**4 + 50*x**2 - 1),
Tuple(11, 1024*x**11 - 2816*x**9 + 2816*x**7 - 1232*x**5 + 220*x**3 - 11*x),
Tuple(12, 2048*x**12 - 6144*x**10 + 6912*x**8 - 3584*x**6 + 840*x**4 - 72*x**2 + 1),
Tuple(13, 4096*x**13 - 13312*x**11 + 16640*x**9 - 9984*x**7 + 2912*x**5 - 364*x**3 + 13*x),
Tuple(14, 8192*x**14 - 28672*x**12 + 39424*x**10 - 26880*x**8 + 9408*x**6 - 1568*x**4 + 98*x**2 - 1),
Tuple(15, 16384*x**15 - 61440*x**13 + 92160*x**11 - 70400*x**9 + 28800*x**7 - 6048*x**5 + 560*x**3 - 15*x))),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("fd8310"),
    Description("Table of", ChebyshevU(n,x), "for", LessEqual(0, n, 15)),
    Table(TableRelation(Tuple(n, p), Equal(ChebyshevU(n,x), p)),
      TableHeadings(n, ChebyshevU(n,x)), TableSplit(1),
      List(
Tuple(0, 1),
Tuple(1, 2*x),
Tuple(2, 4*x**2 - 1),
Tuple(3, 8*x**3 - 4*x),
Tuple(4, 16*x**4 - 12*x**2 + 1),
Tuple(5, 32*x**5 - 32*x**3 + 6*x),
Tuple(6, 64*x**6 - 80*x**4 + 24*x**2 - 1),
Tuple(7, 128*x**7 - 192*x**5 + 80*x**3 - 8*x),
Tuple(8, 256*x**8 - 448*x**6 + 240*x**4 - 40*x**2 + 1),
Tuple(9, 512*x**9 - 1024*x**7 + 672*x**5 - 160*x**3 + 10*x),
Tuple(10, 1024*x**10 - 2304*x**8 + 1792*x**6 - 560*x**4 + 60*x**2 - 1),
Tuple(11, 2048*x**11 - 5120*x**9 + 4608*x**7 - 1792*x**5 + 280*x**3 - 12*x),
Tuple(12, 4096*x**12 - 11264*x**10 + 11520*x**8 - 5376*x**6 + 1120*x**4 - 84*x**2 + 1),
Tuple(13, 8192*x**13 - 24576*x**11 + 28160*x**9 - 15360*x**7 + 4032*x**5 - 448*x**3 + 14*x),
Tuple(14, 16384*x**14 - 53248*x**12 + 67584*x**10 - 42240*x**8 + 13440*x**6 - 2016*x**4 + 112*x**2 - 1),
Tuple(15, 32768*x**15 - 114688*x**13 + 159744*x**11 - 112640*x**9 + 42240*x**7 - 8064*x**5 + 672*x**3 - 16*x))),
    Variables(x),
    Assumptions(Element(x, CC)))

# Specific values

make_entry(ID("c76e72"),
    Formula(Equal(ChebyshevT(0,x), 1)),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("be5652"),
    Formula(Equal(ChebyshevT(1,x), x)),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("48765b"),
    Formula(Equal(ChebyshevU(0,x), 1)),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("75eacb"),
    Formula(Equal(ChebyshevU(1,x), 2*x)),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("9001e6"),
    Formula(Equal(ChebyshevU(-1,x), 0)),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("fc5d42"),
    Formula(Equal(ChebyshevT(n,1), 1)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("2760e7"),
    Formula(Equal(ChebyshevT(n,-1), (-1)**n)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("a46d91"),
    Formula(Equal(ChebyshevT(2*n,0), (-1)**n)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("42102c"),
    Formula(Equal(ChebyshevT(2*n+1,0), 0)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("e03fa4"),
    Formula(Equal(ChebyshevU(n,1), n+1)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("be9a45"),
    Formula(Equal(ChebyshevU(n,-1), (-1)**n * (n+1))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("2a5337"),
    Formula(Equal(ChebyshevU(2*n,0), (-1)**n)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("7d111e"),
    Formula(Equal(ChebyshevU(2*n+1,0), 0)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# Zeros and extrema

make_entry(ID("7a7d1d"),
    Formula(Equal(Zeros(ChebyshevT(n,x), x, Element(x, CC)), SetBuilder(Cos(((2*k-1)/(2*n))*ConstPi), k, Element(k, ZZBetween(1, n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("ce39ac"),
    Formula(Equal(Zeros(ChebyshevU(n,x), x, Element(x, CC)), SetBuilder(Cos((k/(n+1))*ConstPi), k, Element(k, ZZBetween(1, n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("3d25dd"),
    Formula(Equal(Solutions(Brackets(Element(ChebyshevT(n,x), Set(-1,1))), x, Element(x, CC)), SetBuilder(Cos((k/n)*ConstPi), k, Element(k, ZZBetween(0, n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("b5a25e"),
    Formula(Equal(Solutions(Brackets(Equal(ChebyshevT(n,x), 1)), x, Element(x, CC)), SetBuilder(Cos((2*k/n)*ConstPi), k, Element(k, ZZBetween(0, Floor(n/2)))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("db2b0a"),
    Formula(Equal(Solutions(Brackets(Equal(ChebyshevT(n,x), -1)), x, Element(x, CC)), SetBuilder(Cos(((2*k-1)/n)*ConstPi), k, Element(k, ZZBetween(1, Floor((n+1)/2)))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

# Symmetries

make_entry(ID("6a24ab"),
    Formula(Equal(ChebyshevT(n,-x), (-1)**n * ChebyshevT(n,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("88aeb6"),
    Formula(Equal(ChebyshevU(n,-x), (-1)**n * ChebyshevU(n,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("9093a3"),
    Formula(Equal(ChebyshevT(-n,x), ChebyshevT(n,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("78f5bb"),
    Formula(Equal(ChebyshevU(-n,x), -ChebyshevU(n-2,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

# Orthogonality

make_entry(ID("2c26a1"),
    Formula(Equal(Integral((ChebyshevT(n,x)*ChebyshevT(m,x)) * (1/Sqrt(1-x**2)), Tuple(x,-1,1)),
        Cases(Tuple(0, Unequal(n, m)), Tuple(ConstPi, Equal(n, m, 0)), Tuple(ConstPi/2, And(Equal(n, m), Unequal(n, 0)))))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)))))

make_entry(ID("473c36"),
    Formula(Equal(Integral((ChebyshevU(n,x)*ChebyshevU(m,x)) * Sqrt(1-x**2), Tuple(x,-1,1)), Cases(Tuple(0, Unequal(n, m)), Tuple(ConstPi/2, Equal(n, m))))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)))))

# Differential equations

c1 = Subscript(c,1)
c2 = Subscript(c,2)

make_entry(ID("0ed026"),
    Formula(Where(Equal((1-x**2) * Derivative(y(x), Tuple(x, x, 2)) - x * Derivative(y(x), Tuple(x, x, 1)) + n**2 * y(x), 0),
        Equal(y(x), c1 * ChebyshevT(n,x) + c2 * ChebyshevU(n-1,x) * Sqrt(1-x**2)))),
    Variables(n, x, c1, c2),
    Assumptions(And(Element(n, ZZ), Element(x, CC), Element(c1, CC), Element(c2, CC),
        Or(Equal(c2, 0), NotElement(x, Union(OpenClosedInterval(-Infinity,1), ClosedOpenInterval(1,Infinity)))))))

# todo: x = +-1 doesn't work because 0 * inf is undefined; what is a clean way to fix this?
make_entry(ID("30b67b"),
    Formula(Where(Equal((1-x**2) * Derivative(y(x), Tuple(x, x, 2)) - 3 * x * Derivative(y(x), Tuple(x, x, 1)) + n * (n+2) * y(x), 0),
        Equal(y(x), c1 * ChebyshevU(n,x) + c2 * (ChebyshevT(n+1,x) / Sqrt(1-x**2))))),
    Variables(n, x, c1, c2),
    Assumptions(And(Element(n, ZZ), Element(x, CC), Element(c1, CC), Element(c2, CC),
        Or(Equal(c2, 0), NotElement(x, Union(OpenClosedInterval(-Infinity,1), ClosedOpenInterval(1,Infinity)))),
            NotElement(x, Set(-1, 1)))))

# Recurrence relations

make_entry(ID("faeed9"),
    Formula(Equal(ChebyshevT(n,x), 2*x*ChebyshevT(n-1,x) - ChebyshevT(n-2,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("d1ef91"),
    Formula(Equal(ChebyshevU(n,x), 2*x*ChebyshevU(n-1,x) - ChebyshevU(n-2,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("8a785a"),
    Formula(Equal(ChebyshevT(n,x), 2*x*ChebyshevT(n+1,x) - ChebyshevT(n+2,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("303204"),
    Formula(Equal(ChebyshevU(n,x), 2*x*ChebyshevU(n+1,x) - ChebyshevU(n+2,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("7b2c26"),
    Formula(Equal(ChebyshevT(n,x), x*ChebyshevT(n-1,x) - (1-x**2)*ChebyshevU(n-2,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("ce5e03"),
    Formula(Equal(ChebyshevU(n,x), x*ChebyshevU(n-1,x) + ChebyshevT(n,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("0649c9"),
    Formula(Equal(ChebyshevT(n,x), (ChebyshevU(n,x) - ChebyshevU(n-2,x))/2)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("844561"),
    Formula(Equal(ChebyshevT(n,x), ChebyshevU(n,x) - x*ChebyshevU(n-1,x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

# Order transformations

make_entry(ID("7e882c"),
    Formula(Equal(ChebyshevT(m,ChebyshevT(n,x)), ChebyshevT(m*n, x))),
    Variables(m, n, x),
    Assumptions(And(Element(m, ZZ), Element(n, ZZ), Element(x, CC))))

make_entry(ID("ed5222"),
    Formula(Equal(ChebyshevT(m,x)*ChebyshevT(n,x), (ChebyshevT(m+n, x) + ChebyshevT(Abs(m-n), x))/2)),
    Variables(m, n, x),
    Assumptions(And(Element(m, ZZ), Element(n, ZZ), Element(x, CC))))

make_entry(ID("4b83c6"),
    Formula(Equal(ChebyshevT(2*n,x), 2*ChebyshevT(n,x)**2-1)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("de0968"),
    Formula(Equal(ChebyshevT(2*n+1,x), 2*ChebyshevT(n+1,x)*ChebyshevT(n,x) - x)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("82288c"),
    Formula(Equal(ChebyshevT(2*n,x), ChebyshevT(n,2*x**2-1))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("5f09f4"),
    Formula(Equal(ChebyshevU(2*n,x), ChebyshevT(n,2*x**2-1) + ChebyshevU(n-1,2*x**2-1))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

# Trigonometric formulas

make_entry(ID("fda800"),
    Formula(Equal(ChebyshevT(n,x), Cos(n*Acos(x)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("2fc479"),
    Formula(Equal(ChebyshevT(n,x), Cosh(n*Acosh(x)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("b8fdcd"),
    Formula(Equal(ChebyshevU(n-1,x) * Sqrt(1-x**2), Sin(n*Acos(x)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("f4b3fa"),
    Formula(Equal(ChebyshevT(n,Cos(x)), Cos(n*x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("4c7aeb"),
    Formula(Equal(ChebyshevU(n,Cos(x))*Sin(x), Sin(n*x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("9789ee"),
    Formula(Equal(ChebyshevT(2*n+1,Sin(x)), (-1)**n * Sin((2*n+1)*x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

# Power formulas

make_entry(ID("0cbe75"),
    Formula(Equal(ChebyshevT(n,x), Div(1,2)*((x+Sqrt(x**2-1))**n + (x-Sqrt(x**2-1))**n))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("61375f"),
    Formula(Equal(ChebyshevU(n-1,x)*Sqrt(x**2-1), Div(1,2)*((x+Sqrt(x**2-1))**n - (x-Sqrt(x**2-1))**n))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("fdf80d"),
    Formula(Equal(ChebyshevT(n,x) + ChebyshevU(n-1,x)*Sqrt(x**2-1), (x+Sqrt(x**2-1))**n)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("42eb01"),
    Formula(Equal(ChebyshevT(n,x)**2 + (x**2-1)*ChebyshevU(n-1,x)**2, 1)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("5bd0ec"),
    Formula(Equal(ChebyshevT(n,(x + x**-1)/2), (x**n + x**(-n))/2)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, SetMinus(CC, Set(0))))))

# Product representations

make_entry(ID("305a29"),
    Formula(Equal(ChebyshevT(n,x), 2**(n-1) * Product(Parentheses(x-Cos((2*k-1)/(2*n) * ConstPi)), Tuple(k,1,n)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(x, CC))))

make_entry(ID("f5fa23"),
    Formula(Equal(ChebyshevU(n,x), 2**n * Product(Parentheses(x-Cos(k/(n+1) * ConstPi)), Tuple(k,1,n)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, CC))))

# Hypergeometric representations

make_entry(ID("382679"),
    Formula(Equal(ChebyshevT(n,x), Hypergeometric2F1(-n,n,Div(1,2),(1-x)/2))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("ce9a39"),
    Formula(Equal(ChebyshevU(n,x), (n+1) * Hypergeometric2F1(-n,n+2,Div(3,2),(1-x)/2))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

# Generating functions

make_entry(ID("685d1a"),
    Formula(Equal(Sum(ChebyshevT(n,x) * z**n, Tuple(n, 0, Infinity)), (1-x*z)/(1-2*x*z+z**2))),
    Variables(x, z),
    Assumptions(And(Element(x, ClosedInterval(-1,1)), Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("b5049d"),
    Formula(Equal(Sum(ChebyshevU(n,x) * z**n, Tuple(n, 0, Infinity)), 1/(1-2*x*z+z**2))),
    Variables(x, z),
    Assumptions(And(Element(x, ClosedInterval(-1,1)), Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("27b2bb"),
    Formula(Equal(Sum(ChebyshevT(n,x) * (z**n / n), Tuple(n, 1, Infinity)), -Div(1,2)*Log(1-2*x*z+z**2))),
    Variables(x, z),
    Assumptions(And(Element(x, ClosedInterval(-1,1)), Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("9d7c61"),
    Formula(Equal(Sum(ChebyshevT(n,x) * (z**n / Factorial(n)), Tuple(n, 0, Infinity)), Exp(z*x) * Cosh(z * Sqrt(x**2-1)))),
    Variables(x, z),
    Assumptions(And(Element(x, CC), Element(z, CC))))

make_entry(ID("fff8ff"),
    Formula(Equal(Sum(ChebyshevU(n,x) * (z**n / Factorial(n)), Tuple(n, 0, Infinity)), Exp(z*x) * (Cosh(z * Sqrt(x**2-1)) + z*x*Sinc(ConstI*z*Sqrt(x**2-1))))),
    Variables(x, z),
    Assumptions(And(Element(x, CC), Element(z, CC))))

# Derivatives

make_entry(ID("1a0d11"),
    Formula(Equal(ComplexDerivative(ChebyshevT(n, x), x, x), n * ChebyshevU(n-1, x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, CC))))

make_entry(ID("05fe07"),
    Formula(Equal(ComplexDerivative(ChebyshevT(n, x), x, x, 2), (n * (n * ChebyshevT(n, x) - x * ChebyshevU(n-1, x))) / (x**2-1))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, SetMinus(CC, Set(-1, 1))))))

make_entry(ID("35e13b"),
    Formula(Equal(ComplexDerivative(ChebyshevU(n, x), x, x), ((n+1)*ChebyshevT(n+1, x) - x * ChebyshevU(n,x)) / (x**2-1))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZ), Element(x, SetMinus(CC, Set(-1, 1))))))

make_entry(ID("6582c4"),
    Formula(Equal(ComplexDerivative(ChebyshevT(n, x), x, x, r),
        (Sqrt(ConstPi) / (x-1)**r) * Hypergeometric3F2Regularized(1, -n, n, Div(1,2), 1-r, (1-x)/2))),
    Variables(n, r, x),
    Assumptions(And(Element(n, ZZ), Element(r, ZZGreaterEqual(0)), Element(x, SetMinus(CC, Set(-1, 1))))),
    References("http://functions.wolfram.com/Polynomials/ChebyshevT/20/02/01/0002/"))

make_entry(ID("e1797b"),
    Formula(Equal(ComplexDerivative(ChebyshevU(n, x), x, x, r),
        ((Sqrt(ConstPi) * (n+1)) / (2 * (x-1)**r)) * Hypergeometric3F2Regularized(1, -n, n+2, Div(3,2), 1-r, (1-x)/2))),
    Variables(n, r, x),
    Assumptions(And(Element(n, ZZ), Element(r, ZZGreaterEqual(0)), Element(x, SetMinus(CC, Set(-1, 1))))),
    References("http://functions.wolfram.com/Polynomials/ChebyshevU/20/02/01/0002/"))

make_entry(ID("12ce84"),
    Formula(Equal(ComplexDerivative(ChebyshevT(n, x), x, x, r),
        (RisingFactorial(n,r) * RisingFactorial(n-r+1,r) / DoubleFactorial(2*r-1)) * Hypergeometric2F1(r+n, r-n, Div(1,2)+r, (1-x)/2))),
    Variables(n, r, x),
    Assumptions(And(Element(n, ZZ), Element(r, ZZGreaterEqual(0)), Element(x, SetMinus(CC, Set(-1))))))

make_entry(ID("a68f0e"),
    Formula(Equal(ComplexDerivative(ChebyshevT(n, x), x, 1, r),
        (RisingFactorial(n,r) * RisingFactorial(n-r+1,r) / DoubleFactorial(2*r-1)))),
    Variables(n, r),
    Assumptions(And(Element(n, ZZ), Element(r, ZZGreaterEqual(0)))))


# Bounds and inequalities

make_entry(ID("15dd69"),
    Formula(LessEqual(Abs(ChebyshevT(n,x)), 1)),
    Variables(n,x),
    Assumptions(And(Element(n, ZZ), Element(x, ClosedInterval(-1,1)))))

make_entry(ID("3c662e"),
    Formula(LessEqual(Abs(ChebyshevU(n,x)), Abs(n+1))),
    Variables(n,x),
    Assumptions(And(Element(n, ZZ), Element(x, ClosedInterval(-1,1)))))

make_entry(ID("c718ea"),
    Formula(LessEqual(Abs(ChebyshevT(n,z)), Abs(ChebyshevT(n,ConstI*Abs(z))))),
    Variables(n,z),
    Assumptions(And(Element(n, ZZ), Element(z, CC))))

make_entry(ID("0b3fd6"),
    Formula(LessEqual(Abs(ChebyshevU(n,z)), Abs(ChebyshevU(n,ConstI*Abs(z))))),
    Variables(n,z),
    Assumptions(And(Element(n, ZZ), Element(z, CC))))

make_entry(ID("443759"),
    Formula(LessEqual(Abs(ChebyshevT(n,z)), (Abs(z) + Sqrt(Abs(z)**2+1))**n)),
    Variables(n,z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

make_entry(ID("2a4b9d"),
    Formula(LessEqual(Abs(ChebyshevU(n,z)), (Abs(z) + Sqrt(Abs(z)**2+1))**n)),
    Variables(n,z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

