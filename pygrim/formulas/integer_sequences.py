# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Integer sequences"),
    Section("Definitions"),
    Entries(
        "aac67f",
        "963387",
    ),
    Section("Core sequences"),
    Description("Main topic: ", TopicReference("Prime numbers")),
    Entries(
        "9d0839",
    ),
    Description("Main topic: ", TopicReference("Partition function")),
    Entries(
        "8eed2c",
    ),
    Description("Main topic: ", TopicReference("Fibonacci numbers")),
    Entries(
        "373aa1",
    ),
    Description("Bell numbers - Main topic: ", TopicReference("Stirling numbers")),
    Entries(
        "60dc3e",
    ),
    Description("Main topic: ", TopicReference("Factorials and binomial coefficients")),
    Entries(
        "d12aa0",
    ),
    Description("Prime counting function - Main topic: ", TopicReference("Prime numbers")),
    Entries(
        "4fa169",
    ),
    Description("Main topic: ", TopicReference("Landau's function")),
    Entries(
        "6af603",
    ),
    Description("Main topic: ", TopicReference("Pi")),
    Entries(
        "483547",
    ),
    Description("Main topic: ", TopicReference("Bernoulli numbers and polynomials")),
    Entries(
        "b6111c",
    ),
)

make_entry(ID("aac67f"),
    SymbolDefinition(SloaneA, SloaneA(X, n), "Sequence X in Sloane's OEIS"),
    Description(SourceForm(SloaneA(X, n)), ", rendered as", SloaneA(X, n),
        "gives the integer at position", n, "in sequence number", X,
        "in Sloane's On-Line Encyclopedia of Integer Sequences (OEIS). ",
        "The identifier", X, "can be specified as an integer (e.g. 55) or a text (e.g. \"A000055\")"),
    Description("Semantically, this function represents the intended infinite extension of each (non-finite) ",
        "OEIS sequence although the OEIS database itself of course only lists a finite number of terms."))

make_entry(ID("963387"),
    Formula(Implies(And(Element(X, ZZGreaterEqual(1)), Element(n, ZZ)), Element(SloaneA(X, n), Union(ZZ, Set(Undefined))))),
    Variables(X, n))

# Core sequences

make_entry(ID("9d0839"),
    Formula(Equal(PrimeNumber(n), SloaneA("A000040", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("8eed2c"),
    Formula(Equal(PartitionsP(n), SloaneA("A000041", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("373aa1"),
    Formula(Equal(Fibonacci(n), SloaneA("A000045", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("60dc3e"),
    Formula(Equal(BellNumber(n), SloaneA("A000110", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("d12aa0"),
    Formula(Equal(Factorial(n), SloaneA("A000142", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("4fa169"),
    Formula(Equal(PrimePi(n), SloaneA("A000720", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("6af603"),
    Formula(Equal(LandauG(n), SloaneA("A000793", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("483547"),
    Formula(Equal(ConstPi, Sum(SloaneA("A000796", n) * 10**(1-n), For(n, 1, Infinity)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("b6111c"),
    Formula(Equal(BernoulliB(n), SloaneA("A027641", n) / SloaneA("A027642", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

