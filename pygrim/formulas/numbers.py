# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Numbers and infinities"),
    Section("Numbers"),
    Subsection("Standard number domains"),
    Entries(
        "298e9e",
        "7be5dc",
        "bfe358",
        "0deea6",
        "4fd123",
    ),
    Subsection("Rational numbers"),
    Entries(
        "c01d22",
        "81c491",
        "0c838a",
    ),
    Subsection("Complex numbers"),
    Description("Related topics: ", TopicReference("Imaginary unit"), ", ", TopicReference("Complex plane")),
    Entries(
        "88ad6f",
        "72cef9",
        "a08fb9",
        "77ef0c",  # construction of C, see complex_plane (move here?)
    ),
    Subsection("Algebraic numbers"),
    Entries(
        "be9c83",
        "aa6b07",
        "e5a04c",
        "24c179",
        "cd8a07",
        "155575",
    ),
    Section("Infinities"),
    Entries(
        "b738b1",
        "486ab2",
    ),
    Section("Ranges and intervals"),
    Entries(
        "03fbae",
        "2a52af",
        "00b82b",
        "12d5ab",
        "3fe68f",
        "b2162a",
        "ed302a",
    ),

)

make_entry(ID("298e9e"),
    SymbolDefinition(ZZ, ZZ, "Integers"),
    Description("Represents the set of integers."))

make_entry(ID("7be5dc"),
    SymbolDefinition(QQ, QQ, "Rational numbers"),
    Description("Represents the set of rational numbers."))

make_entry(ID("bfe358"),
    SymbolDefinition(RR, RR, "Real numbers"),
    Description("Represents the set of real numbers."))

make_entry(ID("0deea6"),
    SymbolDefinition(CC, CC, "Complex numbers"),
    Description("Represents the set of complex numbers."))

make_entry(ID("c01d22"),
    Formula(Equal(QQ, Set(p/q, For(Tuple(p, q)), And(Element(p, ZZ), Element(q, SetMinus(ZZ, Set(0))))))))

make_entry(ID("81c491"),
    Formula(NotElement(Sqrt(2), QQ)))

make_entry(ID("4fd123"),
    Formula(Subset(ZZ, QQ, RR, CC)))


make_entry(ID("be9c83"),
    SymbolDefinition(AlgebraicNumbers, AlgebraicNumbers, "Algebraic numbers"),
    Description("Represents the set of algebraic numbers."))

make_entry(ID("e5a04c"),
    Formula(Subset(ZZ, QQ, AlgebraicNumbers, CC)))

make_entry(ID("aa6b07"),
    Formula(Equal(AlgebraicNumbers, Set(z, ForElement(z, CC), Parentheses(Exists(Equal(EvaluateIndeterminate(P, x, z), 0), ForElement(P, SetMinus(Polynomials(ZZ, x), Set(0)))))))),
    Variables(x),
    Assumptions(Equal(x, XX(1))))

make_entry(ID("24c179"),
    Formula(Element(Sqrt(2), AlgebraicNumbers)))

make_entry(ID("b738b1"),
    SymbolDefinition(Infinity, Infinity, "Positive infinity"),
    Description("This formal symbol represents a quantity larger than any real number. We define", Equal(+Infinity, Infinity), "."),
    Description("Multiplication of", Infinity, "by a nonzero complex number represents an infinite limit with the given direction in the complex plane.",
        "In particular,", -Infinity, ",", ConstI*Infinity, "and", -ConstI*Infinity, "are frequently used."),
    Description("The set", Union(RR, Set(Infinity, -Infinity)), "is known as the extended real line."))

make_entry(ID("486ab2"),
    SymbolDefinition(UnsignedInfinity, UnsignedInfinity, "Unsigned infinity"),
    Description("This formal symbol represents a quantity with infinite magnitude and undefined sign."),
    Description("It is typically used to represent the value of meromorphic functions at poles."),
    Description("The set", Union(CC, Set(UnsignedInfinity)), "represents the complex Riemann sphere."))


make_entry(ID("03fbae"),
    SymbolDefinition(ZZGreaterEqual, ZZGreaterEqual(n), "Integers greater than or equal to n"))

make_entry(ID("2a52af"),
    SymbolDefinition(ZZLessEqual, ZZLessEqual(n), "Integers less than or equal to n"),
    Description("This symbol may be rendered differently when", n, "is a concrete value, for example: ", ZZLessEqual(-3)))

make_entry(ID("00b82b"),
    SymbolDefinition(Range, Range(a, b), "Integers between given endpoints"),
    CodeExample(Range(a, b), "Given", Element(a, ZZ), "and", Element(b, ZZ), ", represents", Set(n, ForElement(n, ZZ), LessEqual(a, n, b)), "."),
    CodeExample(Range(a, b), "Given", Element(a, ZZ), "and", Element(b, ZZ), ", is equivalent to", SourceForm(Set(n, For(n, a, b))), "."),
    CodeExample(Range(3, 3), "Represents the singleton set", Set(3), ".", " Note: potentially confusing rendering."),
    CodeExample(Range(3, 2), "Represents the empty set.", " Note: potentially confusing rendering."))


make_entry(ID("12d5ab"),
    SymbolDefinition(ClosedInterval, ClosedInterval(a, b), "Closed interval"),
    CodeExample(ClosedInterval(a, b), "Represents", Set(x, ForElement(x, Union(RR, Set(-Infinity, Infinity))), LessEqual(a, x, b)), "."),
    CodeExample(ClosedInterval(0, 1), "Represents the closed unit interval."),
    CodeExample(ClosedInterval(1, 1), "Represents the singleton set", Set(1), "."),
    CodeExample(ClosedInterval(-Infinity, 0), "Represents half the extended real line (including minus infinity and zero)."),
    CodeExample(ClosedInterval(1, -1), "Represents the empty set.", " Note: potentially confusing rendering."),
    CodeExample(1 + ClosedInterval(0, 1) * ConstI, "Represents a set of points in the complex plane. ",
        SourceForm(ClosedInterval(a, b)), "should only be used with extended real number", a, "and", b,
        "as endpoints, but line segments in the complex plane can be constructed by applying arithmetic operations to a set of real numbers (acting pointwise)."),
    CodeExample(ClosedInterval(1, 4) + ClosedInterval(0, 1) * ConstI, "Represents a rectangle in the complex plane. "))

make_entry(ID("3fe68f"),
    SymbolDefinition(OpenInterval, OpenInterval(a, b), "Open interval"),
    CodeExample(OpenInterval(a, b), "Represents", Set(x, ForElement(x, Union(RR, Set(-Infinity, Infinity))), Less(a, x, b)), "."),
    CodeExample(OpenInterval(0, 1), "Represents the open unit interval."),
    CodeExample(OpenInterval(1, 1), "Represents the empty set."),
    CodeExample(OpenInterval(-Infinity, 0), "Represents half the extended real line (excluding minus infinity and zero)."),
    CodeExample(OpenInterval(1, -1), "Represents the empty set.", " Note: potentially confusing rendering."),
    CodeExample(1 + OpenInterval(0, 1) * ConstI, "Represents a set of points in the complex plane. ",
        SourceForm(OpenInterval(a, b)), "should only be used with extended real number", a, "and", b,
        "as endpoints, but line segments in the complex plane can be constructed by applying arithmetic operations to a set of real numbers (acting pointwise)."),
    CodeExample(OpenInterval(1, 4) + OpenInterval(0, 1) * ConstI, "Represents a rectangle in the complex plane. "))

make_entry(ID("b2162a"),
    SymbolDefinition(ClosedOpenInterval, ClosedOpenInterval(a, b), "Closed-open interval"),
    CodeExample(ClosedOpenInterval(a, b), "Represents", Set(x, ForElement(x, Union(RR, Set(-Infinity, Infinity))), And(LessEqual(a, x), Less(x, b))), "."),
    CodeExample(ClosedOpenInterval(0, 1), "Represents the unit interval (including 0, excluding 1)."),
    CodeExample(ClosedOpenInterval(1, 1), "Represents the empty set."),
    CodeExample(ClosedOpenInterval(-Infinity, 0), "Represents half the extended real line (including minus infinity, excluding zero)."),
    CodeExample(ClosedOpenInterval(1, -1), "Represents the empty set.", " Note: potentially confusing rendering."),
    CodeExample(1 + ClosedOpenInterval(0, 1) * ConstI, "Represents a set of points in the complex plane. ",
        SourceForm(ClosedOpenInterval(a, b)), "should only be used with extended real number", a, "and", b,
        "as endpoints, but line segments in the complex plane can be constructed by applying arithmetic operations to a set of real numbers (acting pointwise)."),
    CodeExample(ClosedOpenInterval(1, 4) + ClosedOpenInterval(0, 1) * ConstI, "Represents a rectangle in the complex plane. "))

make_entry(ID("ed302a"),
    SymbolDefinition(OpenClosedInterval, OpenClosedInterval(a, b), "Open-closed interval"),
    CodeExample(OpenClosedInterval(a, b), "Represents", Set(x, ForElement(x, Union(RR, Set(-Infinity, Infinity))), And(Less(a, x), LessEqual(x, b))), "."),
    CodeExample(OpenClosedInterval(0, 1), "Represents the unit interval (excluding 0, including 1)."),
    CodeExample(OpenClosedInterval(1, 1), "Represents the empty set."),
    CodeExample(OpenClosedInterval(-Infinity, 0), "Represents half the extended real line (excluding minus infinity, including zero)."),
    CodeExample(OpenClosedInterval(1, -1), "Represents the empty set.", " Note: potentially confusing rendering."),
    CodeExample(1 + OpenClosedInterval(0, 1) * ConstI, "Represents a set of points in the complex plane. ",
        SourceForm(OpenClosedInterval(a, b)), "should only be used with extended real number", a, "and", b,
        "as endpoints, but line segments in the complex plane can be constructed by applying arithmetic operations to a set of real numbers (acting pointwise)."),
    CodeExample(OpenClosedInterval(1, 4) + OpenClosedInterval(0, 1) * ConstI, "Represents a rectangle in the complex plane. "))

