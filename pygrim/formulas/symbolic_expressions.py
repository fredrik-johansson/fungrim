# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Symbolic expressions"),
    Section("Introduction"),
    Description("""
Formulas in Fungrim are represented using symbolic expressions
that encode mathematical objects and operations in a semantic way.
The symbolic expression language is called Grim ("GRIM Represents Intelligible Mathematics").
The LaTeX output rendered on the Fungrim website is
produced automatically from the symbolic Grim expressions."""),
    Description("""This topic page documents fundamental constructions
used in Grim expressions. The language is still a work in progress and the
details are subject to change.
"""),
    Section("Markup for Fungrim entries"),
    Entries(
        "6db9b2",
        "0d9952",
        "c2fb41",
        "f37520",
        "3c8d31",
        "8af90e",
        "b976df",
    ),
    Section("Variable-generating expressions"),
    Entries(
        "43cc72",
        "978576",
    ),
    Section("Sequence-generating expressions"),
    Entries(
        "82c978",
        "73f5e7",
    ),
    Section("Cosmetic markup"),
    Entries(
        "ecfe08",
        "d14265",
        "ca1edc",
    ),
)

#

make_entry(ID("6db9b2"),
    SymbolDefinition(Entry, Ellipsis, "Entry"))

make_entry(ID("0d9952"),
    SymbolDefinition(ID, Ellipsis, "Entry ID"))

make_entry(ID("c2fb41"),
    SymbolDefinition(Formula, Ellipsis, "Formula"))

make_entry(ID("f37520"),
    SymbolDefinition(Variables, Ellipsis, "Declaration of variables"))

make_entry(ID("3c8d31"),
    SymbolDefinition(Assumptions, Ellipsis, "Assumptions (domain declaration) for the variables"))

make_entry(ID("8af90e"),
    SymbolDefinition(References, Ellipsis, "References"))

make_entry(ID("b976df"),
    SymbolDefinition(Description, Ellipsis, "Text description"))

# Local variable generators

make_entry(ID("43cc72"),
    SymbolDefinition(For, Ellipsis, "General-purpose generator"),
    Description(SourceForm(For(x)),
    """declares the given symbol as locally bound variable in the
    scope of the parent call. For example,""",
        SourceForm(f(a, For(x), b)),
    "declares", x, "as a locally bound variable that may be used within the expressions ",
    a, """and""", b, """. The interpretation of the variable is left to the
    parent operator""", f, "."),

    Description("""Called with a tuple of symbols,""",
        SourceForm(For(Tuple(x, y, z))), """, each symbol
    becomes a locally bound variable."""),

    Description("""
    Called with several arguments, for example """,
    SourceForm(For(x, a, b, c)), ", the additional parameters", a, b, c,
    "specify information about the range of", x, ".",
    """The interpretation of the parameters is up to the parent operator""",
    f, """. Most operators recognize """,
    SourceForm(For()), """with two additional parameters as
    specifying an iteration range: for example, """,
        SourceForm(Sum(Factorial(n), For(n, 2, 10))),
    """gives""",
        Sum(Factorial(n), For(n, 2, 10)), ".",
    "(When", SourceForm(For(n, a, b)), " is used in this sense, the endpoints",
    a, "and", b, "must be integers or possibly", Equal(a, -Infinity),
    "and/or", Equal(b, Infinity), "where an infinite sequence makes sense. ",
    "The iteration sequence is empty if", Less(b, a), ".)"),

    Description("""
    There are various exceptions. For example,""", SourceForm(Integral),
    """understands two
    parameters as representing the endpoints (not necessarily integers)
    of a directed line segment to integrate over: """,
        SourceForm(Integral(Cos(x), For(x, -ConstPi, ConstPi))),
    "becomes",
        Integral(Cos(x), For(x, -ConstPi, ConstPi)), ". ",
    SourceForm(Derivative), "takes one or two parameters",
        "denoting the evaluation point and optionally the order of differentiation:",
            SourceForm(Derivative(Sin(x), For(x, y))),
        "becomes",
            Derivative(Sin(x), For(x, y)),
        "and",
            SourceForm(Derivative(Sin(x), For(x, y, 2))),
        "becomes",
            Derivative(Sin(x), For(x, y, 2)),
    ),
)

# todo: document iteration over cartsian products

'''
A subtle point is that the symbol declared in For() overrides any
meaning of the same symbol from the surrounding context, but *not* in the
evaluation of param1, param2, .... For example,

    ( ... For(x), ... Derivative(Sin(x), For(x, x)))

is equivalent to

    ( ... For(x), ... Derivative(Sin(x_), For(x_, x))).
'''


make_entry(ID("978576"),
    SymbolDefinition(ForElement, Ellipsis, "Generator for all the elements of a set"),
    Description(
        SourceForm(ForElement(x, S)), "declares the variable", SourceForm(x),
        "just like", SourceForm(For(x)), "and additionally tells the parent operator",
        "that", x, "is to range over the elements of the set", S, ". ",
        "Examples: ",
        SourceForm(Set(2*n, ForElement(n, ZZ))), "becomes",
        Set(2*n, ForElement(n, ZZ)), ". ",
        SourceForm(Sum(1/n**2, ForElement(n, SetMinus(ZZ, Set(0))))), "becomes",
        Sum(1/n**2, ForElement(n, SetMinus(ZZ, Set(0)))), ". "),
)

# Variable-length sequences

make_entry(ID("82c978"),
    SymbolDefinition(Repeat, Repeat(x, n), "Repeating sequence"),
    Description("Represents the first arguments repeated the number of times ",
        "specified by the last argument. This expression does not represent ",
        "a mathematical object: it only exists at the expression level, and ",
        "injects the sequence between surrounding arguments. ",
        "To construct a mathematical object, we must pass the generator expression ",
        "to a function such as", SourceForm(Tuple), ". Example: ",
        SourceForm(Formula(Tuple(Repeat(1, N), 0, Repeat(1, 2, 3, M), 1, 2))),
        "renders as ",
        Tuple(Repeat(1, N), 0, Repeat(1, 2, 3, M), 1, 2),
        "."))

make_entry(ID("73f5e7"),
    SymbolDefinition(Step, Step(f(n), For(n, a, b)), "Enumerated sequence"),
    Description(SourceForm(Step(f(n), For(n, a, b))),
        " represents the sequence of values ", f(n), "for ", n, "between ",
        "the integers", a, "and", b, ". ",
        "The sequence is empty if ", Less(b, a), ". ",
        "This expression does not represent ",
        "a mathematical object: it only exists at the expression level, and ",
        "injects the sequence between a surrounding arguments. ",
        "To construct a mathematical object, we must pass the generator expression ",
        "to a function such as", SourceForm(Tuple), ". Examples: "),
    Description(SourceForm(f(Step(k**2, For(k, 1, 10))))),
    Description(f(Step(k**2, For(k, 1, 10)))),
    Description(SourceForm(Tuple(Step(Repeat(n, n), For(n, 0, N))))),
    Description(Tuple(Step(Repeat(n, n), For(n, 0, N)))),
    Description(SourceForm(Tuple(1, 2, 2, Step(Repeat(n, n), For(n, 3, N))))),
    Description(Tuple(1, 2, 2, Step(Repeat(n, n), For(n, 3, N)))))

# Cosmetic markup

make_entry(ID("ecfe08"),
    SymbolDefinition(Parentheses, Parentheses(Ellipsis), "Parentheses"),
    Description("Hints that the enclosed expression should be rendered surrounded by parentheses. ",
        "Semantically represents the identity function: ",
        SourceForm(Parentheses(x)), " is equivalent to ", SourceForm(x), "."))

make_entry(ID("d14265"),
    SymbolDefinition(Brackets, Brackets(Ellipsis), "Square brackets"),
    Description("Hints that the enclosed expression should be rendered surrounded by square brackets. ",
        "Semantically represents the identity function: ",
        SourceForm(Brackets(x)), " is equivalent to ", SourceForm(x), "."))

make_entry(ID("ca1edc"),
    SymbolDefinition(Braces, Braces(Ellipsis), "Curly braces"),
    Description("Hints that the enclosed expression should be rendered surrounded by curly braces. ",
        "Semantically represents the identity function: ",
        SourceForm(Braces(x)), " is equivalent to ", SourceForm(x), "."))



"""





38c8cd
496f7f
152e0d
dd40c1
7f4dea
edb4b6
c2703b
d819d0
bfd7ba
e614e6
"""
