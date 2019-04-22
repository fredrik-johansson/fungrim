# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Numbers and infinities"),
    Section("Numbers"),
    Entries(
        "298e9e",
        "7be5dc",
        "bfe358",
        "0deea6",
        "851121",
        "c01d22",
        "3e1c20",
        "77ef0c",  # construction of C, see complex_plane (move here?)
        "4fd123",
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

make_entry(ID("851121"),
    SymbolDefinition(ConstI, ConstI, "Imaginary unit"),
    Description("The imaginary unit."))

make_entry(ID("c01d22"),
    Formula(Equal(QQ, SetBuilder(p/q, Tuple(p, q), And(Element(p, ZZ), Element(q, SetMinus(ZZ, Set(0))))))))

make_entry(ID("3e1c20"),
    Formula(Equal(ConstI**2, -1)))

make_entry(ID("4fd123"),
    Formula(Subset(ZZ, QQ, RR, CC)))


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
    SymbolDefinition(ZZBetween, ZZBetween(a, b), "Integers between a and b inclusive"))

make_entry(ID("12d5ab"),
    SymbolDefinition(ClosedInterval, ClosedInterval(a, b), "Closed interval"))

make_entry(ID("3fe68f"),
    SymbolDefinition(OpenInterval, OpenInterval(a, b), "Open interval"))

make_entry(ID("b2162a"),
    SymbolDefinition(ClosedOpenInterval, ClosedOpenInterval(a, b), "Closed-open interval"))

make_entry(ID("ed302a"),
    SymbolDefinition(OpenClosedInterval, OpenClosedInterval(a, b), "Open-closed interval"))


