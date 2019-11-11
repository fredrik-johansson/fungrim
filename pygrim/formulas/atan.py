# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Inverse tangent"),
    Section("Definitions"),
    Entries(
        "b120b9",
        "ce3a8e",
    ),
    Section("Illustrations"),
    Entries(
        "8bb3d8",
    ),
    Section("Transcendental equations"),
    Entries(
        "1f026d",
        "d4b0b6",
        "0b829e",
        "f516e3",
        "cbce7f",
        "a2af66",
    ),
    Section("Differential equations"),
    Entries(
        "61d8f3",
    ),
    Section("Integral representations"),
    Entries(
        "90a864",
    ),
    Section("Specific values"),
    Entries(
        "645e30",
        "d418d3",
        "7295b5",
        "a2d208",
        "9b0994",
        "157c6c",
        "706783",
        "3c1021",
        "a9ecff",
        "c6c92a",
        "7dd050",
        "b0049f",
    ),
    Section("Analytic properties"),
    Entries(
        "a6cd13",
        "30ba67",
        "48031d",
        "26c47c",
        "3b11d3",
        "718a9b",
    ),
    Section("Cases for atan2"),
    Entries(
        "a6776b",
        "77e519",
        "22fb4a",
    ),
    Section("Argument transformations"),
    Subsection("Symmetries"),
    Entries(
        "0ee626",
        "632063",
        "e3d274",
        "073e1a",
        "bfc13f",
    ),
    Subsection("Addition and multiplication formulas"),
    Entries(
        "072166",
        "268c9e",
        "14f8c2",
    ),
    Subsection("Algebraic transformations"),
    Entries(
        "67c0be",
    ),
    Section("Sums and products"),
    Entries(
        "cf64b3",
        "00e608",
        "3ea11b",
        "503d4d",
        "a020e9",
        "1d730a",
    ),
    Section("Representations through other functions"),
    Subsection("Logarithms"),
    Entries(
        "a18b77",
        "500c0a",
        "12765e",
        "9dec3e",
        "eca4ce",
    ),
    Subsection("Inverse trigonometric functions"),
    Entries(
        "c580f4",
        "7954ad",
        "ec7f2d",
    ),
    Subsection("Hypergeometric functions"),
    Entries(
        "34ff28",
    ),
    Section("Complex parts"),
    Entries(
        "df52fc",
        "b65d19",
    ),
    Section("Derivatives and integrals"),
    Entries(
        "8fbf69",
        "a4eb86",
        "90631b",
        "36171f",
        "6b8963",
        "1d3fd7",
    ),
    Section("Series expansions"),
    Entries(
        "4e5947",
    ),
    Section("Bounds and inequalities"),
    Subsection("Real arguments"),
    Entries(
        "b63481",
        "e7a9b1",
        "5d6f74",
        "466095",
        "3478af",
        "1eeccf",
        "efebb8",
        "a42212",
        "3fe47b",
        "f5d28c",
        "b0a4e9",
        "d04a5b",
        "b971fe",
    ),
    Subsection("Complex arguments"),
    Entries(
        "7272a8",
        "fa9b71",
    ),
    Subsection("Perturbations"),
    Entries(
        "47331d",
        "96289e",
        "fa30c7",
        "4d2168",
    ),
)

make_entry(ID("b120b9"),
    SymbolDefinition(Atan, Atan(z), "Inverse tangent"),
    Description("The inverse tangent function", Atan(z),
        "(denoted by", SourceForm(Atan(z)), "in the Fungrim formula language)",
         "is a function of a single variable.",
        "The following table lists conditions such that", SourceForm(Atan(z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, RR), Element(Atan(z), OpenInterval(-(Pi/2), Pi/2))),
        Tuple(Element(z, SetMinus(CC, Set(-ConstI, +ConstI))), Element(Atan(z), CC)),
        TableSection("Infinities"),
        Tuple(Element(z, Set(-Infinity, Infinity)), Element(Atan(z), Set(-(Pi/2), Pi/2))),
        Tuple(Element(z, Set(-ConstI, +ConstI)), Element(Atan(z), Set(-ConstI*Infinity, +ConstI*Infinity))),
        TableSection("Formal power series"),
        Tuple(Element(z, FormalPowerSeries(RR, x)), Element(Atan(z), FormalPowerSeries(RR, x))),
        Tuple(And(Element(z, FormalPowerSeries(CC, x)), NotElement(SeriesCoefficient(z, x, 0), Set(-ConstI, +ConstI))), Element(Atan(z), FormalPowerSeries(CC, x))),
      )))

make_entry(ID("ce3a8e"),
    SymbolDefinition(Atan2, Atan2(y, x), "Two-argument inverse tangent"),
    Description("The inverse tangent function", Atan2(y, x),
        "(denoted by", SourceForm(Atan2(y, x)), "in the Fungrim formula language)",
         "is a function of two variables.",
        "The following table lists conditions such that", SourceForm(Atan2(y, x)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(y, RR), Element(x, RR)), Element(Atan2(y, x), OpenClosedInterval(-Pi, Pi))),
      )))

make_entry(ID("8bb3d8"),
    Image(Description("X-ray of", Atan(z), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_atan")),
    description_xray,
    )

# Transcendental equations

make_entry(ID("1f026d"),
    Formula(Equal(Tan(Atan(z)), z)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("d4b0b6"),
    Formula(Equal(Sin(Atan(z)), z/Sqrt(1+z**2))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(-ConstI, ConstI)))))

make_entry(ID("0b829e"),
    Formula(Equal(Cos(Atan(z)), 1/Sqrt(1+z**2))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(-ConstI, ConstI)))))

make_entry(ID("f516e3"),
    Formula(Equal(Atan(Tan(theta)), theta)),
    Variables(theta),
    Assumptions(And(Element(theta, CC), Less(-(Pi/2), Re(theta), Pi/2))))

make_entry(ID("cbce7f"),
    Formula(Equal(Solutions(Brackets(Equal(Tan(w), z)), ForElement(w, CC)), Set(Atan(z) + Pi*n, ForElement(n, ZZ)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(-ConstI, ConstI)))))

make_entry(ID("a2af66"),
    Formula(Equal(Atan2(y, x), UniqueSolution(Brackets(Where(
        Equal(Tuple(x,y), Tuple(r*Cos(theta), r*Sin(theta))),
            Equal(r, Sqrt(x**2+y**2)))), ForElement(theta, OpenClosedInterval(-Pi, Pi))))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR), Or(Unequal(x, 0), Unequal(y, 0)))))


# Differential equations

C_1 = Subscript(c, 1)
C_2 = Subscript(c, 2)

# todo: complex ray instead of interval?
make_entry(ID("61d8f3"),
    Formula(Where(Equal((1+z**2) * ComplexDerivative(y(z), For(z, z, 2)) + 2 * z * ComplexDerivative(y(z), For(z, z, 1)), 0), Equal(y(z), C_1 + C_2 * Atan(z)))),
    Variables(z, C_1, C_2),
    Assumptions(And(Element(z, CC), Element(C_1, CC), Element(C_2, CC),
        NotElement(ConstI*z, Union(OpenClosedInterval(-Infinity, -1), ClosedOpenInterval(1, Infinity))))))

# Integral representations

make_entry(ID("90a864"),
    Formula(Equal(Atan(z), Integral(1/(1+t**2), For(t, 0, z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(ConstI*z, Union(OpenClosedInterval(-Infinity,-1), ClosedOpenInterval(1,Infinity))))))

# Specific values

make_entry(ID("645e30"),
    Formula(Equal(Atan(0), 0)))

make_entry(ID("d418d3"),
    Formula(Equal(Atan(+Infinity), Pi/2)))

make_entry(ID("7295b5"),
    Formula(Equal(Atan(-Infinity), -(Pi/2))))

make_entry(ID("a2d208"),
    Formula(Equal(Atan(+ConstI), +ConstI*Infinity)))

make_entry(ID("9b0994"),
    Formula(Equal(Atan(-ConstI), -ConstI*Infinity)))

make_entry(ID("157c6c"),
    Formula(Equal(Atan(1), Pi/4)))

make_entry(ID("706783"),
    Formula(Equal(Atan(Sqrt(3)), Pi/3)))

make_entry(ID("3c1021"),
    Formula(Equal(Atan(1/Sqrt(3)), Pi/6)))

make_entry(ID("a9ecff"),
    Formula(Equal(Atan(Sqrt(2)-1), Pi/8)))

make_entry(ID("c6c92a"),
    Formula(Equal(Atan(Sqrt(2)+1), 3*Pi/8)))

make_entry(ID("7dd050"),
    Formula(Equal(Atan(2-Sqrt(3)), Pi/12)))

make_entry(ID("b0049f"),
    Formula(Equal(Atan(2+Sqrt(3)), 5*Pi/12)))

# Analytic properties

make_entry(ID("a6cd13"),
    Formula(Equal(IsHolomorphic(Atan(z), ForElement(z, 
        SetMinus(CC, Parentheses(Union(OpenClosedInterval(-Infinity,-1)*ConstI, ClosedOpenInterval(1,Infinity)*ConstI))))))))

make_entry(ID("30ba67"),
    Formula(Equal(EssentialSingularities(Atan(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("48031d"),
    Formula(Equal(Poles(Atan(z), ForElement(z, Union(CC, Set(UnsignedInfinity)))), Set())))

make_entry(ID("26c47c"),
    Formula(Equal(BranchPoints(Atan(z), z, Union(CC, Set(UnsignedInfinity))), Set(-ConstI, ConstI, UnsignedInfinity))))

make_entry(ID("3b11d3"),
    Formula(Equal(BranchCuts(Atan(z), z, CC),
        Set(OpenClosedInterval(-Infinity,-1)*ConstI, ClosedOpenInterval(1,Infinity)*ConstI))))

make_entry(ID("718a9b"),
    Formula(Equal(Zeros(Atan(z), ForElement(z, CC)), Set(0))))

# Cases for atan2

make_entry(ID("a6776b"),
    Formula(Equal(Atan2(0,x), Cases(Tuple(0, GreaterEqual(x, 0)), Tuple(Pi, Less(x, 0))))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("77e519"),
    Formula(Equal(Atan2(y,0), (Pi/2) * Sign(y))),
    Variables(y),
    Assumptions(Element(y, RR)))

make_entry(ID("22fb4a"),
    Formula(Equal(Atan2(y,x), Cases(
        Tuple(0, Equal(x, y, 0)),
        Tuple(Atan(y/x), Greater(x, 0)),
        Tuple(Parentheses(Pi/2) * Sign(y) - Atan(x/y), Unequal(y, 0)),
        Tuple(Pi, And(Equal(y, 0), Less(x, 0))),
        ))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

# Argument transformations

make_entry(ID("0ee626"),
    Formula(Equal(Atan(-z), -Atan(z))),
    Variables(z),
    Assumptions(Element(z, Union(CC, Set(-Infinity, Infinity)))))

make_entry(ID("632063"),
    Formula(Equal(Atan(Conjugate(z)), Conjugate(Atan(z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(ConstI*z, Union(OpenInterval(-Infinity,-1), OpenInterval(1,Infinity))))))

make_entry(ID("e3d274"),
    Formula(Equal(Atan(1/z), Pi/2 - Atan(z))),
    Variables(z),
    Assumptions(And(Element(z, CC), Or(Greater(Re(z), 0),
        And(Equal(Re(z), 0), Element(Im(z), Union(OpenInterval(-1,0), OpenInterval(1, Infinity))))))))

make_entry(ID("073e1a"),
    Formula(Equal(Atan(1/z), -(Pi/2) - Atan(z))),
    Variables(z),
    Assumptions(And(Element(z, CC), Or(Less(Re(z), 0),
        And(Equal(Re(z), 0), Element(Im(z), Union(OpenInterval(-Infinity,-1), OpenInterval(0, 1))))))))

make_entry(ID("bfc13f"),
    Formula(Equal(Atan(1/z), (Pi/2)*Csgn(1/z) - Atan(z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(ConstI*z, Union(Set(0), OpenClosedInterval(-Infinity, -1), ClosedOpenInterval(1, Infinity))))))

# Addition and multiplication formulas

make_entry(ID("072166"),
    Formula(Equal(Atan(ConstI*z), ConstI*Atanh(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("268c9e"),
    Formula(Equal(Atan(x+y), Atan(x) + Atan(y/(1+x*(x+y))))),
    Variables(x, y),
    Assumptions(And(Element(x, CC), Element(y, CC), Less(Abs(x+y), 1), Less(Abs(x), 1)),
                And(Element(x, RR), Element(y, RR), Greater(x*(x+y), -1))))

make_entry(ID("14f8c2"),
    Formula(Equal(Atan(2*z), Atan(z) + Atan(z/(1+2*z**2)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Not(And(Equal(Re(z), 0), Element(Abs(Im(z)), ClosedInterval(Sqrt(2)/2, 1)))))))

# Algebraic transformations

make_entry(ID("67c0be"),
    Formula(Equal(Atan(z), 2*Atan(z/(1+Sqrt(1+z**2))))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Sums and products

make_entry(ID("cf64b3"),
    Formula(Equal(Atan(x)+Atan(y), Atan2(x+y, 1-x*y))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("00e608"),
    Formula(Equal(Atan(x)-Atan(y), Atan2(x-y, 1+x*y))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("3ea11b"),
    Formula(Equal(Atan(x)+Atan(y), Atan((x+y)/(1-x*y)))),
    Variables(x, y),
    Assumptions(And(Element(x, CC), Element(y, CC), Less(Abs(x), 1), Less(Abs(y), 1)),
                And(Element(x, RR), Element(y, RR), Less(x*y, 1))))

make_entry(ID("503d4d"),
    Formula(Equal(Atan(x)-Atan(y), Atan((x-y)/(1+x*y)))),
    Variables(x, y),
    Assumptions(And(Element(x, CC), Element(y, CC), Less(Abs(x), 1), Less(Abs(y), 1)),
                And(Element(x, RR), Element(y, RR), Greater(x*y, -1))))


y1 = Subscript(y,1)
y2 = Subscript(y,2)
x1 = Subscript(x,1)
x2 = Subscript(x,2)

make_entry(ID("a020e9"),
    Formula(Equal(Atan2(y1,x1)+Atan2(y2,x2), Atan2(y1*x2+y2*x1, x1*x2-y1*y2))),
    Variables(x, y),
    Assumptions(And(Element(x1, RR), Element(x2, RR), Element(y1, RR), Element(y2, RR),
        Element(Atan2(y1,x1)+Atan2(y2,x2), OpenClosedInterval(-Pi, Pi)),
        Not(Equal(x1,y1,0)), Not(Equal(x2,y2,0)))))

make_entry(ID("1d730a"),
    Formula(Equal(Atan2(y1,x1)-Atan2(y2,x2), Atan2(y1*x2-y2*x1, x1*x2+y1*y2))),
    Variables(x, y),
    Assumptions(And(Element(x1, RR), Element(x2, RR), Element(y1, RR), Element(y2, RR),
        Element(Atan2(y1,x1)-Atan2(y2,x2), OpenClosedInterval(-Pi, Pi)),
        Not(Equal(x1,y1,0)), Not(Equal(x2,y2,0)))))

# Representations through other functions

make_entry(ID("a18b77"),
    Formula(Equal(Atan(z), (ConstI/2)*(Log(1-ConstI*z) - Log(1 + ConstI*z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("500c0a"),
    Formula(Equal(Atan(z), (ConstI/2)*(Log((1-ConstI*z)/(1+ConstI*z))))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(-z*ConstI, ClosedOpenInterval(1, Infinity)))))

make_entry(ID("12765e"),
    Formula(Equal(Atan(z), -(ConstI/2)*(Log((1+ConstI*z)/(1-ConstI*z))))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z*ConstI, ClosedOpenInterval(1, Infinity)))))

make_entry(ID("9dec3e"),
    Formula(Equal(Atan2(y,x), -ConstI*Log(Sign(x+y*ConstI)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR), Unequal(x+y*ConstI, 0))))

make_entry(ID("eca4ce"),
    Formula(Equal(Atan2(y,x), Im(Log(x+y*ConstI)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR), Unequal(x+y*ConstI, 0))))

make_entry(ID("c580f4"),
    Formula(Equal(Atan(z), Acot(1/z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("7954ad"),
    Formula(Equal(Atan(z), Asin(z/Sqrt(1+z**2)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(ConstI*z, Union(OpenClosedInterval(-Infinity,-1), ClosedOpenInterval(1,Infinity))))))

make_entry(ID("ec7f2d"),
    Formula(Equal(Atan(z), Csgn(z) * Acos(1/Sqrt(1+z**2)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(-ConstI, ConstI)))))

# todo: works at branch points with the right infinity of 2F1 at 1?
make_entry(ID("34ff28"),
    Formula(Equal(Atan(z), z * Hypergeometric2F1(1, Div(1,2), Div(3,2), -z**2))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(-ConstI, ConstI)))))

# Complex parts

make_entry(ID("df52fc"),
    Formula(Equal(Re(Atan(x+y*ConstI)), Div(1,2)*Atan2(2*x, 1-x**2-y**2))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR), Not(And(Equal(x, 0), Element(y, Union(OpenClosedInterval(-Infinity, -1), Set(1))))))))

make_entry(ID("b65d19"),
    Formula(Equal(Im(Atan(x+y*ConstI)), Div(1,4)*Log((x**2+(1+y)**2)/(x**2+(1-y)**2)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR), NotElement(x+y*ConstI, Set(-ConstI, ConstI)))))


# Derivatives and integrals

make_entry(ID("8fbf69"),
    Formula(Equal(ComplexDerivative(Atan(z), For(z, z, 1)), 1/(1+z**2))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(ConstI*z, Union(OpenClosedInterval(-Infinity,-1), ClosedOpenInterval(1,Infinity))))))

make_entry(ID("a4eb86"),
    Formula(Equal(ComplexDerivative(Atan(z), For(z, z, 2)), -((2*z)/(1+z**2)**2))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(ConstI*z, Union(OpenClosedInterval(-Infinity,-1), ClosedOpenInterval(1,Infinity))))))

make_entry(ID("90631b"),
    Formula(Equal(ComplexDerivative(Atan(z), For(z, z, n)),
        Factorial(n-1) / (1+z**2)**((n+1)/2) * ChebyshevU(n-1, -(z/Sqrt(1+z**2))))),
    Variables(z, n),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(z, CC), NotElement(ConstI*z, Union(OpenClosedInterval(-Infinity,-1), ClosedOpenInterval(1,Infinity))))),
    References("M. A. Boutiche and M. Rahmani (2017), On the higher derivatives of the inverse tangent function, https://arxiv.org/abs/1712.03521, Theorem 9"))

make_entry(ID("36171f"),
    Formula(Equal(ComplexDerivative(Atan(z), For(z, z, n)),
        (((-1)**n * Factorial(n-1)) / (2 * ConstI)) * (1/(z+ConstI)**n - 1/(z-ConstI)**n))),
    Variables(z, n),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(z, CC), NotElement(ConstI*z, Union(OpenClosedInterval(-Infinity,-1), ClosedOpenInterval(1,Infinity))))))

make_entry(ID("6b8963"),
    Formula(Equal(RealDerivative(Atan2(y, x), For(x, x, 1)), -(y/(x**2+y**2)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR), Or(Greater(x, 0), Unequal(y, 0)))))

make_entry(ID("1d3fd7"),
    Formula(Equal(RealDerivative(Atan2(y, x), For(y, y, 1)), x/(x**2+y**2))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR), Or(Greater(x, 0), Unequal(y, 0)))))

# Series expansions

make_entry(ID("4e5947"),
    Formula(Equal(Atan(z), Sum((-1)**k * z**(2*k+1) / (2*k+1), For(k, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 1)))),

# Bounds and inequalities

## Real arguments

make_entry(ID("b63481"),
    Formula(LessEqual(Abs(Atan2(y,x)), Pi)),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("e7a9b1"),
    Formula(Less(Abs(Atan(x)), Pi/2)),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("5d6f74"),
    Formula(LessEqual(Abs(Atan(x)), Pi/2)),
    Variables(x),
    Assumptions(Element(x, Union(RR, Set(-Infinity, Infinity)))))

make_entry(ID("466095"),
    Formula(LessEqual(Abs(Atan(x)), Abs(x))),
    Variables(x),
    Assumptions(Element(x, Union(RR, Set(-Infinity, Infinity)))))

make_entry(ID("3478af"),
    Formula(LessEqual(Atan(x), Sum((-1)**k * x**(2*k+1) / (2*k+1), For(k, 0, 2*N)))),
    Variables(x, N),
    Assumptions(And(Element(x, ClosedOpenInterval(0, Infinity)), Element(N, ZZGreaterEqual(0)))))

make_entry(ID("1eeccf"),
    Formula(GreaterEqual(Atan(x), Sum((-1)**k * x**(2*k+1) / (2*k+1), For(k, 0, 2*N+1)))),
    Variables(x, N),
    Assumptions(And(Element(x, ClosedOpenInterval(0, Infinity)), Element(N, ZZGreaterEqual(0)))))

make_entry(ID("efebb8"),
    Formula(LessEqual(Atan(x), (Pi/2)**2 * (x / (1 + (Pi/2) * x)))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(0, Infinity))))

make_entry(ID("a42212"),
    Formula(GreaterEqual(Atan(x), x/(1+x))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(0, Infinity))))

make_entry(ID("3fe47b"),
    Formula(GreaterEqual(Atan(x), (Pi * x) / (Pi + 2*x))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(0, Infinity))))

make_entry(ID("f5d28c"),
    Formula(LessEqual(Atan(x), (Pi/2) * (x / Sqrt(1 + x**2)))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(0, Infinity))))

make_entry(ID("b0a4e9"),
    Formula(GreaterEqual(Atan(x), (x / Sqrt(1 + x**2)))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(0, Infinity))))

make_entry(ID("d04a5b"),
    Formula(LessEqual(Atan(x), (Pi/2) * Tanh(x))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(0, Infinity))))

make_entry(ID("b971fe"),
    Formula(GreaterEqual(Atan(x), Tanh(x))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(0, Infinity))))

## Complex arguments

make_entry(ID("7272a8"),
    Formula(LessEqual(Abs(Atan(z)), Abs(Atanh(Abs(z))))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("fa9b71"),
    Formula(LessEqual(Abs(Atan(z)), -Log(1-Abs(z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), LessEqual(Abs(z), 1))))

## Perturbations

make_entry(ID("47331d"),
    Formula(Equal(Abs(Atan(x+y)-Atan(x)), Atan2(Abs(y), 1+x*(x+y)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("96289e"),
    Formula(LessEqual(Abs(Atan(x+y)-Atan(x)), Abs(y))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("fa30c7"),
    Formula(LessEqual(Abs(Atan(x+y)-Atan(x)), Abs(y)/(1 + Max(0, Abs(x)-Abs(y))**2))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("4d2168"),
    Formula(Less(Abs(Atan(x+y)-Atan(x)), Pi)),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

