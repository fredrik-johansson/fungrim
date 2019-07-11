# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Dirichlet characters"),
    Section("Definitions"),
    Entries(
        "c7e2fb",
        "e810d8",
        "2f52bc",
    ),
    Section("Character evaluation"),
    Entries(
        "d9a187",
        "57d31a",
        "1c3957",
        "0851cf",
        "afd0c5",
        "bdf58d",
        "d29554",
        "458198",
    ),
    Section("Principal characters"),
    Entries(
        "d8c6d1",
    ),
    Section("Character group"),
    Entries(
        "47d430",
        "ed65c8",
        "62f7d5",
        "0ba38f",
        "f88596",
        "3b43b0",
    ),
    Section("Primitive decomposition"),
    Entries(
        "a7d592",
    ),
    Section("Conrey numbering"),
    Subsection("Multiplicativity"),
    Entries
    (
        "2a48bd",
    ),
    Subsection("Odd powers"),
    Entries(
        "166a87",
        "a9847a",
        "75231e",
        "540931",
        "4cf4e4",
    ),
    Subsection("Even powers"),
    Entries(
        "fc4f6a",
        "03fbe8",
    ),
    Section("Orthogonality"),
    Entries(
        "4877d1",
        "3ab92d",
        "a4e947",
        "f4de66",
    ),
    Section("Tables"),
    Subsection("Primitive and non-primitive characters"),
    Entries(
        "338b5c",
    ),
    Subsection("Character values"),
    Entries(
        "c40df4",
        "ef432d",
        "287d9b",
        "5dc1c0",
        "668877",
        "d8cac6",
        "ec0054",
        "fc267b",
        "0c7de4",
        "d8155f",
        "7a56c2",
        "5e1d3b",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "e6deb7",
        "5df909",
    ),
    Section("L-series"),
    SeeTopics("Dirichlet L-functions"),
    Entries(
        "604c7c",
    ),
)

make_entry(ID("e810d8"),
    SymbolDefinition(DirichletGroup, DirichletGroup(q), "Dirichlet characters with given modulus"),
    Description(SourceForm(DirichletGroup(q)), ", rendered as", DirichletGroup(q), ", represents the set of Dirichlet characters modulo", q, ", given", Element(q, ZZGreaterEqual(1)), "."),
    Description("Dirichlet characters can be defined axiomatically as functions from", ZZ, "to", CC,
        "satisfying the properties in formulas", EntryReference("1c3957"), ", ",
            EntryReference("0851cf"), ", and", EntryReference("afd0c5"), "."),
    Description("In this definition, the modulus", q, "is not an attribute of the character; for example",
        "the character giving the sequence", List(0, 1, 0, 1, Ellipsis), "is an element of both", DirichletGroup(2),
        "and", DirichletGroup(4), "."),
    Description("A more explicit construction of the characters is possible using the Conrey numbering scheme, which is implemented by", SourceForm(DirichletCharacter), "."))

make_entry(ID("2f52bc"),
    SymbolDefinition(PrimitiveDirichletCharacters, PrimitiveDirichletCharacters(q), "Primitive Dirichlet characters with given modulus"),
    Description(SourceForm(PrimitiveDirichletCharacters(q)), ", rendered as", PrimitiveDirichletCharacters(q),
        ", represents the set of primitive Dirichlet characters modulo", q, ", given", Element(q, ZZGreaterEqual(1)),
        ". Primitive characters are defined in ", EntryReference("ed65c8"), "."))

ellrange = Element(ell, ZZBetween(1, Max(q,2)-1))

make_entry(ID("c7e2fb"),
    SymbolDefinition(DirichletCharacter, DirichletCharacter(q,ell), "Dirichlet character"),
    Description(SourceForm(DirichletCharacter(q,ell)), ", rendered as",
        DirichletCharacter(q,ell), ", represents the Dirichlet character with Conrey label", Tuple(q, ell), "."),
    Description(
        "A character represents an object", chi, " that can be called (", chi(n), ") as a function from", ZZ, "to", CC, "."),
    Description(SourceForm(DirichletCharacter(q,ell,n)), ", rendered as",
        DirichletCharacter(q,ell,n), ", represents the Dirichlet character with Conrey label", Tuple(q, ell), "evaluated at the integer", n, "."),
    Description("The Conrey label consists of integers", Element(q, ZZGreaterEqual(1)), "and", Element(ell, ZZBetween(1, Max(q,2)-1)),
        "such that", Equal(GCD(ell,q), 1), ". ",
        "In this scheme", DirichletCharacter(q,1), "always represents the trivial/principal character (taking only values 0 and 1) modulo", q, ". ",
        "Non-principal characters are defined by", EntryReference("4cf4e4"), "when", q, "is an odd prime power, by",
            EntryReference("fc4f6a"), "and", EntryReference("03fbe8"), "when", q, "is an even prime power, and in general by factoring", q,
            "into prime powers using", EntryReference("2a48bd"), "."),
    References("http://www.lmfdb.org/Character/Labels"),
    )

# Fundamental properties

make_entry(ID("47d430"),
    Formula(Equal(DirichletGroup(q), SetBuilder(DirichletCharacter(q,ell), ell, And(ellrange, Equal(GCD(ell,q), 1))))),
    Variables(q),
    Assumptions(Element(q, ZZGreaterEqual(1))))

make_entry(ID("ed65c8"),
    Formula(Equal(PrimitiveDirichletCharacters(q),
        SetBuilder(chi, chi, And(Element(chi, DirichletGroup(q)),
            ForAll(d, And(Element(d, ZZBetween(1, q-1)), Divides(d, q)),
                Exists(a, And(Element(a, ZZBetween(0, q-1)), CongruentMod(a, 1, d), Equal(GCD(a,q), 1), Unequal(chi(a), 1)))))))),
    Variables(q),
    Assumptions(Element(q, ZZGreaterEqual(1))),
    References("T. Apostol (1976), Introduction to Analytic Number Theory, Springer. Chapter 8.7."))

make_entry(ID("62f7d5"),
    Formula(Equal(Cardinality(DirichletGroup(q)), Totient(q))),
    Variables(q),
    Assumptions(Element(q, ZZGreaterEqual(1))))

make_entry(ID("0ba38f"),
    Formula(Equal(Cardinality(PrimitiveDirichletCharacters(q)), DivisorSum(Totient(d)*MoebiusMu(q/d), d, q))),
    Variables(q),
    Assumptions(Element(q, ZZGreaterEqual(1))),
    References("http://oeis.org/A007431"))

make_entry(ID("f88596"),
    Formula(Equal(SequenceLimit(Sum(Cardinality(DirichletGroup(q)), Tuple(q, 1, N)) / (Div(1,2) * N**2), N, Infinity), 6/ConstPi**2)))

make_entry(ID("3b43b0"),
    Formula(Equal(SequenceLimit(Sum(Cardinality(PrimitiveDirichletCharacters(q)), Tuple(q, 1, N)) / Sum(Cardinality(DirichletGroup(q)), Tuple(q, 1, N)), N, Infinity), 6/ConstPi**2)),
    References("H. Jager, On the number of Dirichlet characters with modulus not exceeding x, Indagationes Mathematicae, Volume 76, Issue 5, 1973, Pages 452-455, https://doi.org/10.1016/1385-7258(73)90069-3"))

make_entry(ID("d9a187"),
    Formula(Where(Equal(chi(n), DirichletCharacter(q,ell,n)), Equal(chi, DirichletCharacter(q,ell)))),
    Description("This is simply a syntactical definition of character evaluation."),
    Variables(q,ell,n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), ellrange, Equal(GCD(ell,q), 1), Element(n, ZZ))))

make_entry(ID("57d31a"),
    Formula(Where(Element(chi(n), Union(SetBuilder(Exp(2*ConstPi*ConstI*k/r), k, Element(k, ZZ)), Set(0))), Equal(r, Totient(q)))),
    Variables(q,chi,n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(n, ZZ))))

make_entry(ID("1c3957"),
    Formula(Equal(chi(n+q), chi(n))),
    Variables(q,chi,n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(n, ZZ))))

make_entry(ID("0851cf"),
    Formula(Equal(chi(m*n), chi(m)*chi(n))),
    Variables(q,chi,m,n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("afd0c5"),
    Formula(Equivalent(Equal(chi(n), 0), Unequal(GCD(n,q), 1))),
    Variables(q,chi,n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(n, ZZ))))

make_entry(ID("bdf58d"),
    Formula(Equal(chi(1), 1)),
    Variables(q,chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("d29554"),
    Formula(Element(chi(-1), Set(1, -1))),
    Variables(q,chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("458198"),
    Formula(Equal(chi(0), Cases(Tuple(1, Equal(q, 1)), Tuple(0, Unequal(q, 1))))),
    Variables(q,chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

# Principal characters

make_entry(ID("d8c6d1"),
    Formula(Equal(DirichletCharacter(q, 1, n), Cases(Tuple(1, Equal(GCD(n,q), 1)), Tuple(0, Otherwise)))),
    Variables(q,n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(n, ZZ))))

# Primitive decomposition

make_entry(ID("a7d592"),
    Formula(Where(Exists(Tuple(d, Subscript(chi, 0)), And(Element(d, ZZBetween(1, q)), Divides(d, q),
        Element(Subscript(chi, 0), PrimitiveDirichletCharacters(d)), Equal(chi, Subscript(chi, 0) * Subscript(chi, 1)))),
            Equal(Subscript(chi, 1), DirichletCharacter(q, 1)))),
    Variables(q, Subscript(chi, 0)),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

# Conrey numbering

ell1 = Subscript(ell, 1)
ell2 = Subscript(ell, 2)
q1 = Subscript(q, 1)
q2 = Subscript(q, 2)

make_entry(ID("166a87"),
    SymbolDefinition(ConreyGenerator, ConreyGenerator(p), "Conrey generator"),
    Description("For an odd prime", p, ", the Conrey generator is defined as the smallest positive integer", ConreyGenerator(p),
        "that generates the multiplicative group of order", p**e, "for every", GreaterEqual(e, 1), "."))

make_entry(ID("75231e"),
    Formula(Equal(ConreyGenerator(p), Minimum(
        SetBuilder(a, a,
        And(Element(a, ZZGreaterEqual(1)),
            Equal(Cardinality(SetBuilder(Mod(a**k, p), k, Element(k, ZZGreaterEqual(0)))), p-1),
            Equal(Cardinality(SetBuilder(Mod(a**k, p**2), k, Element(k, ZZGreaterEqual(0)))), p*(p-1)))
        )))),
    Variables(p),
    Assumptions(And(Element(p, PP), GreaterEqual(p, 3))))

make_entry(ID("540931"),
    Formula(Where(Equal(ConreyGenerator(p), Cases(Tuple(10, Equal(p, 40487)), Tuple(7, Equal(p, 6692367337)),
            Tuple(Minimum(A), Otherwise))),
        Equal(A, SetBuilder(a, a,
        And(Element(a, ZZGreaterEqual(1)),
            Equal(Cardinality(SetBuilder(Mod(a**k, p), k, Element(k, ZZGreaterEqual(0)))), p-1))
        )))),
    Variables(p),
    Assumptions(And(Element(p, PP), GreaterEqual(p, 3), Less(p, Pow(10, 12)))))

make_entry(ID("a9847a"),
    SymbolDefinition(DiscreteLog, DiscreteLog(x, b, q), "Discrete logarithm"),
    Description(DiscreteLog(x, b, q), "represents the smallest positive integer", y, "such that", CongruentMod(Pow(b, y), x, q)))

make_entry(ID("2a48bd"),
    Formula(Equal(DirichletCharacter(q1 * q2, ell), DirichletCharacter(q1, Mod(ell, q1)) * DirichletCharacter(q2, Mod(ell, q2)))),
    Variables(q1,q2,ell),
    Assumptions(And(Element(q1, ZZGreaterEqual(1)), Element(q2, ZZGreaterEqual(1)),
        Element(ell, ZZBetween(1, Max(q1*q2, 2)-1)), Equal(GCD(ell,q1), GCD(ell,q2), GCD(q1,q2), 1))))

make_entry(ID("4cf4e4"),
    Formula(Where(Equal(DirichletCharacter(q, ell, n), Exp(2*ConstPi*ConstI*a*b/Totient(q))),
        Equal(q, p**e), Equal(g, ConreyGenerator(p)), Equal(a, DiscreteLog(ell, g, q)), Equal(b, DiscreteLog(n, g, q)))),
    Variables(p, e, ell, n),
    Assumptions(And(Element(p, PP), GreaterEqual(p, 3), Element(e, ZZGreaterEqual(1)),
        Element(ell, ZZBetween(1, p**e-1)), Element(n, ZZ), Equal(GCD(ell, p**e), GCD(n, p**e), 1))))

make_entry(ID("fc4f6a"),
    Formula(Equal(DirichletCharacter(4, 3, n), Cases(Tuple(1,CongruentMod(n,1,4)), Tuple(-1,CongruentMod(n,3,4)), Tuple(0, Otherwise)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("03fbe8"),
    Formula(Where(Equal(DirichletCharacter(q, ell, n), Exp(2*ConstPi*ConstI*(((1-x)*(1-y)/8 + a*b/2**(e-2))))),
        Equal(q, 2**e), Equal(L(k),
            Cases(Tuple(
                Tuple(1, DiscreteLog(k, 5, q)), Element(k, SetBuilder(Mod(5**i, q), i, Element(i, ZZGreaterEqual(1))))),
                 Tuple(
                Tuple(-1, DiscreteLog(-k, 5, q)), Element(k, SetBuilder(Mod(-5**i, q), i, Element(i, ZZGreaterEqual(1))))))),
    Equal(Tuple(x, a), L(ell)), Equal(Tuple(y, b), L(n)))),
    Variables(e, ell, n),
    Assumptions(And(Element(e, ZZGreaterEqual(3)), Element(ell, ZZBetween(1, 2**e-1)), Element(n, ZZ), Equal(GCD(ell, 2), GCD(n, 2), 1))))

# Orthogonality

make_entry(ID("4877d1"),
    Formula(Equal(Sum(chi(n), Tuple(n, 0, q-1)), Cases(Tuple(Totient(q), Equal(chi, DirichletCharacter(q, 1))), Tuple(0, Otherwise)))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("3ab92d"),
    Formula(Equal(Sum(chi(n), chi, Element(chi, DirichletGroup(q))), Cases(Tuple(Totient(q), CongruentMod(n, 1, q)), Tuple(0, Otherwise)))),
    Variables(q, n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(n, ZZ))))

chi1 = Subscript(chi, 1)
chi2 = Subscript(chi, 2)

make_entry(ID("a4e947"),
    Formula(Equal(Sum(chi1(n)*Conjugate(chi2(n)), Tuple(n, 0, q-1)), Cases(Tuple(Totient(q), Equal(chi1, chi2)), Tuple(0, Otherwise)))),
    Variables(q, chi1, chi2),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi1, DirichletGroup(q)), Element(chi2, DirichletGroup(q)))))

make_entry(ID("f4de66"),
    Formula(Equal(Sum(chi(m)*Conjugate(chi(n)), chi, Element(chi, DirichletGroup(q))), Cases(Tuple(Totient(q), And(CongruentMod(n, m, q), Equal(GCD(m,q), 1))), Tuple(0, Otherwise)))),
    Variables(q, m, n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(m, ZZ), Element(n, ZZ))))

# Tables

make_entry(ID("338b5c"),
    Description("Table of", PrimitiveDirichletCharacters(q), "and", SetMinus(DirichletGroup(q), PrimitiveDirichletCharacters(q)), "for", LessEqual(1, q, 30)),
    Table(TableRelation(Tuple(q, Cardinality(DirichletGroup(q)), Cardinality(PrimitiveDirichletCharacters(q)), P, N), And(Equal(PrimitiveDirichletCharacters(q), SetBuilder(DirichletCharacter(q,ell), ell, Element(l, P))),
            Equal(SetMinus(DirichletGroup(q), PrimitiveDirichletCharacters(q)), SetBuilder(DirichletCharacter(q,ell), ell, Element(l, N))))),
        TableHeadings(q, Cardinality(DirichletGroup(q)), Cardinality(PrimitiveDirichletCharacters(q)),
            Description(ell, "such that", DirichletCharacter(q,ell), "is primitive"), Description(ell, "such that", DirichletCharacter(q,ell), "is non-primitive")),
        List(
    Tuple(1, 1, 1, Set(1), Set()),
    Tuple(2, 1, 0, Set(), Set(1)),
    Tuple(3, 2, 1, Set(2), Set(1)),
    Tuple(4, 2, 1, Set(3), Set(1)),
    Tuple(5, 4, 3, Set(2, 3, 4), Set(1)),
    Tuple(6, 2, 0, Set(), Set(1, 5)),
    Tuple(7, 6, 5, Set(2, 3, 4, 5, 6), Set(1)),
    Tuple(8, 4, 2, Set(3, 5), Set(1, 7)),
    Tuple(9, 6, 4, Set(2, 4, 5, 7), Set(1, 8)),
    Tuple(10, 4, 0, Set(), Set(1, 3, 7, 9)),
    Tuple(11, 10, 9, Set(2, 3, 4, 5, 6, 7, 8, 9, 10), Set(1)),
    Tuple(12, 4, 1, Set(11), Set(1, 5, 7)),
    Tuple(13, 12, 11, Set(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), Set(1)),
    Tuple(14, 6, 0, Set(), Set(1, 3, 5, 9, 11, 13)),
    Tuple(15, 8, 3, Set(2, 8, 14), Set(1, 4, 7, 11, 13)),
    Tuple(16, 8, 4, Set(3, 5, 11, 13), Set(1, 7, 9, 15)),
    Tuple(17, 16, 15, Set(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), Set(1)),
    Tuple(18, 6, 0, Set(), Set(1, 5, 7, 11, 13, 17)),
    Tuple(19, 18, 17, Set(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18), Set(1)),
    Tuple(20, 8, 3, Set(3, 7, 19), Set(1, 9, 11, 13, 17)),
    Tuple(21, 12, 5, Set(2, 5, 11, 17, 20), Set(1, 4, 8, 10, 13, 16, 19)),
    Tuple(22, 10, 0, Set(), Set(1, 3, 5, 7, 9, 13, 15, 17, 19, 21)),
    Tuple(23, 22, 21, Set(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22), Set(1)),
    Tuple(24, 8, 2, Set(5, 11), Set(1, 7, 13, 17, 19, 23)),
    Tuple(25, 20, 16, Set(2, 3, 4, 6, 8, 9, 11, 12, 13, 14, 16, 17, 19, 21, 22, 23), Set(1, 7, 18, 24)),
    Tuple(26, 12, 0, Set(), Set(1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)),
    Tuple(27, 18, 12, Set(2, 4, 5, 7, 11, 13, 14, 16, 20, 22, 23, 25), Set(1, 8, 10, 17, 19, 26)),
    Tuple(28, 12, 5, Set(3, 11, 19, 23, 27), Set(1, 5, 9, 13, 15, 17, 25)),
    Tuple(29, 28, 27, Set(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28), Set(1)),
    Tuple(30, 8, 0, Set(), Set(1, 7, 11, 13, 17, 19, 23, 29)),
    )))



make_entry(ID("c40df4"),
    Description("Table of", DirichletCharacter(1, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(1, ell)))),
        TableHeadings(Description(ell, "\\", n), 0),
        TableColumnHeadings(1),
        List(
        Tuple(1),
    )))

make_entry(ID("ef432d"),
    Description("Table of", DirichletCharacter(2, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(2, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1),
        TableColumnHeadings(1),
        List(
        Tuple(0, 1),
    )))

make_entry(ID("287d9b"),
    Description("Table of", DirichletCharacter(3, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(3, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2),
        TableColumnHeadings(1, 2),
        List(
        Tuple(0, 1, 1),
        Tuple(0, 1, -1),
    )))

make_entry(ID("5dc1c0"),
    Description("Table of", DirichletCharacter(4, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(4, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3),
        TableColumnHeadings(1, 3),
        List(
        Tuple(0, 1, 0, 1),
        Tuple(0, 1, 0, -1),
    )))

make_entry(ID("668877"),
    Description("Table of", DirichletCharacter(5, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(5, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3, 4),
        TableColumnHeadings(1, 2, 3, 4),
        List(
        Tuple(0, 1, 1, 1, 1),
        Tuple(0, 1, ConstI, -ConstI, -1),
        Tuple(0, 1, -ConstI, ConstI, -1),
        Tuple(0, 1, -1, -1, 1),
    )))

make_entry(ID("d8cac6"),
    Description("Table of", DirichletCharacter(6, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(6, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3, 4, 5),
        TableColumnHeadings(1, 5),
        List(
        Tuple(0, 1, 0, 0, 0, 1),
        Tuple(0, 1, 0, 0, 0, -1),
    )))

make_entry(ID("ec0054"),
    Description("Table of", DirichletCharacter(7, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(7, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3, 4, 5, 6),
        TableColumnHeadings(1, 2, 3, 4, 5, 6),
        List(
        Tuple(0, 1, 1, 1, 1, 1, 1),
        Tuple(0, 1, -Exp(ConstPi*ConstI/3), Exp(2*ConstPi*ConstI/3), Exp(2*ConstPi*ConstI/3), -Exp(ConstPi*ConstI/3), 1),
        Tuple(0, 1, Exp(2*ConstPi*ConstI/3), Exp(ConstPi*ConstI/3), -Exp(ConstPi*ConstI/3), -Exp(2*ConstPi*ConstI/3), -1),
        Tuple(0, 1, Exp(2*ConstPi*ConstI/3), -Exp(ConstPi*ConstI/3), -Exp(ConstPi*ConstI/3), Exp(2*ConstPi*ConstI/3), 1),
        Tuple(0, 1, -Exp(ConstPi*ConstI/3), -Exp(2*ConstPi*ConstI/3), Exp(2*ConstPi*ConstI/3), Exp(ConstPi*ConstI/3), -1),
        Tuple(0, 1, 1, -1, 1, -1, -1),
    )))

make_entry(ID("fc267b"),
    Description("Table of", DirichletCharacter(8, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(8, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3, 4, 5, 6, 7),
        TableColumnHeadings(1, 3, 5, 7),
        List(
        Tuple(0, 1, 0, 1, 0, 1, 0, 1),
        Tuple(0, 1, 0, 1, 0, -1, 0, -1),
        Tuple(0, 1, 0, -1, 0, -1, 0, 1),
        Tuple(0, 1, 0, -1, 0, 1, 0, -1),
    )))

make_entry(ID("0c7de4"),
    Description("Table of", DirichletCharacter(9, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(9, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3, 4, 5, 6, 7, 8),
        TableColumnHeadings(1, 2, 4, 5, 7, 8),
        List(
        Tuple(0, 1, 1, 0, 1, 1, 0, 1, 1),
        Tuple(0, 1, Exp(ConstPi*ConstI/3), 0, Exp(2*ConstPi*ConstI/3), -Exp(2*ConstPi*ConstI/3), 0, -Exp(ConstPi*ConstI/3), -1),
        Tuple(0, 1, Exp(2*ConstPi*ConstI/3), 0, -Exp(ConstPi*ConstI/3), -Exp(ConstPi*ConstI/3), 0, Exp(2*ConstPi*ConstI/3), 1),
        Tuple(0, 1, -Exp(2*ConstPi*ConstI/3), 0, -Exp(ConstPi*ConstI/3), Exp(ConstPi*ConstI/3), 0, Exp(2*ConstPi*ConstI/3), -1),
        Tuple(0, 1, -Exp(ConstPi*ConstI/3), 0, Exp(2*ConstPi*ConstI/3), Exp(2*ConstPi*ConstI/3), 0, -Exp(ConstPi*ConstI/3), 1),
        Tuple(0, 1, -1, 0, 1, -1, 0, 1, -1),
    )))

make_entry(ID("d8155f"),
    Description("Table of", DirichletCharacter(10, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(10, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
        TableColumnHeadings(1, 3, 7, 9),
        List(
        Tuple(0, 1, 0, 1, 0, 0, 0, 1, 0, 1),
        Tuple(0, 1, 0, ConstI, 0, 0, 0, -ConstI, 0, -1),
        Tuple(0, 1, 0, -ConstI, 0, 0, 0, ConstI, 0, -1),
        Tuple(0, 1, 0, -1, 0, 0, 0, -1, 0, 1),
    )))

make_entry(ID("7a56c2"),
    Description("Table of", DirichletCharacter(11, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(11, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        TableColumnHeadings(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        List(
    Tuple(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    Tuple(0, 1, Exp(ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), -Exp(4*ConstPi*ConstI/5), -Exp(2*ConstPi*ConstI/5), Exp(3*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), -1),
    Tuple(0, 1, -Exp(3*ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), 1),
    Tuple(0, 1, Exp(2*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), 1),
    Tuple(0, 1, Exp(4*ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), 1),
    Tuple(0, 1, -Exp(4*ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), Exp(ConstPi*ConstI/5), Exp(3*ConstPi*ConstI/5), -Exp(2*ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), -1),
    Tuple(0, 1, -Exp(2*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), Exp(3*ConstPi*ConstI/5), -Exp(4*ConstPi*ConstI/5), Exp(ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), -1),
    Tuple(0, 1, Exp(3*ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), -Exp(2*ConstPi*ConstI/5), Exp(ConstPi*ConstI/5), -Exp(4*ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), -1),
    Tuple(0, 1, -Exp(ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), Exp(4*ConstPi*ConstI/5), Exp(2*ConstPi*ConstI/5), -Exp(3*ConstPi*ConstI/5), -Exp(ConstPi*ConstI/5), 1),
    Tuple(0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1),
    )))

make_entry(ID("5e1d3b"),
    Description("Table of", DirichletCharacter(12, ell)),
    Table(TableRelation(Tuple(ell, n, y), Where(Equal(chi(n), y), Equal(chi, DirichletCharacter(12, ell)))),
        TableHeadings(Description(ell, "\\", n), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
        TableColumnHeadings(1, 5, 7, 11),
        List(
    Tuple(0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1),
    Tuple(0, 1, 0, 0, 0, -1, 0, 1, 0, 0, 0, -1),
    Tuple(0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0, -1),
    Tuple(0, 1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1),
    )))

# Bounds and inequalities

make_entry(ID("e6deb7"),
    Formula(LessEqual(Abs(Sum(chi(n), Tuple(n, 0, N))), Totient(q))),
    Variables(N),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(N, ZZ), Element(chi, DirichletGroup(q)), Unequal(chi, DirichletCharacter(q, 1)))))

make_entry(ID("5df909"),
    Formula(LessEqual(Abs(Sum(chi(n), Tuple(n, M, N))), Sqrt(q)*Log(q)/(2*Log(2)) + 3*Sqrt(q))),
    Variables(q, chi, M, N),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(M, ZZ), Element(N, ZZ), Element(chi, DirichletGroup(q)), Unequal(chi, DirichletCharacter(q, 1)))),
    Description("Pólya-Vinogradov inequality, explicit form"),
    References("E. Dobrowolski and K. S. Williams, An upper bound for the sum ... for a certain class of functions f, Proceedings of the American Mathematical Society, Vol. 114, No. 1 (Jan., 1992), pp. 29-35, http://doi.org/10.2307/2159779"))





def_Topic(
    Title("Dirichlet L-functions"),
    Section("Definitions"),
    Entries(
        "d5a598",
    ),
    Section("L-series"),
    Entries(
        "604c7c",
        "291569",
    ),
    Section("Euler product"),
    Entries(
        "d088ea",
        "0f96c3",
    ),
    Section("Hurwitz zeta representation"),
    Entries(
        "04217b",
        "c31c10",
        "4c3678",
    ),
    Section("Principal and non-primitive characters"),
    Entries(
        "a9337b",
        "ff8254",
        "629f70",
        "1bd945",
    ),
    Section("Value at 1"),
    Entries(
        "6c3fff",
        "3d5327",
        "23256b",
        "d10029",
        "c2750a",
        "d83109",
        "3b8c97",
        "c9d117",
    ),
    Section("Value at 0"),
    Entries(
        "a07d28",
        "789ca4",
        "fad52f",
    ),
    Section("Values at negative integers"),
    Entries(
        "cb5d51",
        "e44796",
        "3e0817",
        "f7a866",
        "d69b41",
        "f5c3c5",
    ),
    Section("Zeros"),
    Subsection("Nontrivial zeros"),
    Entries(
        "3f96c1",
        "dc593e",
        "982e3b",
        "2a34c3",
        "214a91",
    ),
    Subsection("Trivial zeros"),
    Entries(
        "bc755b",
        "9ba78a",
    ),
    Section("Conjugate symmetry"),
    Entries(
        "7c86d5",
        "50adea",
        "97fe89",
    ),
    Section("Functional equation"),
    Entries(
        "cc6a5a",
        "b788a1",
        "11a763",
        "62f12c",
        "b78a50",
        "288207",
    ),
    Section("Analytic properties"),
    Entries(
        "8533f5",
        "97f631",
        "ea8c55",
        "fe4692",
    ),
    Section("Approximations"),
    Entries(
        "312147",
        "4911bd",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "8ff1ff",
        "9b3fde",
    ),
    Section("Related topics"),
    SeeTopics("Dirichlet characters", "Riemann zeta function", "Bernoulli numbers and polynomials"),
)

make_entry(ID("d5a598"),
    SymbolDefinition(DirichletL, DirichletL(s, chi), "Dirichlet L-function"))

# L-series

make_entry(ID("604c7c"),
    Formula(Equal(DirichletL(s, chi), Sum(chi(n)/n**s, Tuple(n, 1, Infinity)))),
    Variables(q, chi, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("291569"),
    Formula(Equal(1/DirichletL(s, chi), Sum((MoebiusMu(n) * chi(n))/n**s, Tuple(n, 1, Infinity)))),
    Variables(q, chi, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC), Greater(Re(s), 1))))

# Euler product

make_entry(ID("d088ea"),
    Formula(Equal(DirichletL(s, chi), PrimeProduct(1/(1-chi(p)*p**(-s)), p))),
    Variables(q, chi, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("0f96c3"),
    Formula(Equal(1/DirichletL(s, chi), PrimeProduct(Parentheses(1-chi(p)/p**s), p))),
    Variables(q, chi, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC), Greater(Re(s), 1))))

# Hurwitz zeta representation

make_entry(ID("04217b"),
    SymbolDefinition(HurwitzZeta, HurwitzZeta(s, a), "Hurwitz zeta function"))

make_entry(ID("d10029"),
    SymbolDefinition(StieltjesGamma, StieltjesGamma(n, a), "Stieltjes constant"))

make_entry(ID("c31c10"),
    Formula(Equal(DirichletL(s, chi), (1/q**s) * Sum(chi(k) * HurwitzZeta(s, k/q), Tuple(k, 1, q)))),
    Variables(q, chi, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, SetMinus(CC, Set(1))))))

make_entry(ID("4c3678"),
    Formula(Equal(HurwitzZeta(s, k/q), (q**s / Totient(q)) * Sum(Conjugate(chi(k)) * DirichletL(s, chi), chi, Element(chi, DirichletGroup(q))))),
    Variables(q, k, s),
    Assumptions(And(Element(q, ZZGreaterEqual(2)), Element(k, ZZBetween(1,q-1)), Equal(GCD(k,q), 1), Element(s, SetMinus(CC, Set(1))))))

# Principal and non-primitive characters

make_entry(ID("a9337b"),
    Formula(Equal(DirichletL(s, DirichletCharacter(1, 1)), RiemannZeta(s))),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("ff8254"),
    Formula(Equal(DirichletL(s, DirichletCharacter(2**n, 1)), (1-Pow(2,-s)) * RiemannZeta(s))),
    Variables(n, s),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(s, CC))))

make_entry(ID("629f70"),
    Formula(Equal(DirichletL(s, DirichletCharacter(q, 1)), RiemannZeta(s) * PrimeProduct(Parentheses(1 - 1/p**s), p, Divides(p, q)))),
    Variables(q, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(s, CC))))

make_entry(ID("1bd945"),
    Formula(Where(Equal(DirichletL(s,chi), DirichletL(s, Subscript(chi,0)) * PrimeProduct(Parentheses(1-Call(Subscript(chi,0), p)/p**s), p, Divides(p, q))),
        Equal(Subscript(chi, 1), DirichletCharacter(q, 1)), Equal(chi, Subscript(chi, 0) * Subscript(chi, 1)))),
    Variables(q, d, Subscript(chi, 0), s),
    Assumptions(And(
        Element(q, ZZGreaterEqual(1)),
        Element(d, ZZBetween(1,q)),
        Divides(d, q),
        Element(Subscript(chi, 0), PrimitiveDirichletCharacters(d)),
        Element(s, CC))),
    Description("This allows an L-function of a non-primitive character to be expressed in terms of an L-function of a primitive character."))

# Value at 1

make_entry(ID("6c3fff"),
    Formula(Equal(DirichletL(1, chi), Cases(Tuple(UnsignedInfinity, Equal(chi, DirichletCharacter(q, 1))), Tuple(ComplexLimit(DirichletL(s, chi), s, 1), Otherwise)))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("3d5327"),
    Formula(Unequal(DirichletL(1, chi), 0)),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("23256b"),
    Formula(Equal(ComplexLimit((s-1)*DirichletL(1, DirichletCharacter(q, 1)), s, 1), Totient(q)/q)),
    Variables(q),
    Assumptions(Element(q, ZZGreaterEqual(1))))

make_entry(ID("c2750a"),
    Formula(Equal(DirichletL(1,chi), (1/q) * Sum(chi(k) * StieltjesGamma(0,k/q), Tuple(k, 1, q-1)))),
    Variables(q),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Unequal(chi, DirichletCharacter(q, 1)))))

make_entry(ID("d83109"),
    Formula(Equal(DirichletL(1,DirichletCharacter(3,2)), ConstPi/Sqrt(27))))

make_entry(ID("3b8c97"),
    Formula(Equal(DirichletL(1,DirichletCharacter(4,3)), ConstPi/4)))

make_entry(ID("c9d117"),
    Formula(Equal(DirichletL(1,DirichletCharacter(5,4)), 2*Log(GoldenRatio)/Sqrt(5))))

# Value at 0

make_entry(ID("a07d28"),
    Formula(Equal(DirichletL(0,DirichletCharacter(q,1)), Cases(Tuple(-Div(1,2), Equal(q, 1)), Tuple(0, Otherwise)))),
    Variables(q),
    Assumptions(And(Element(q, ZZGreaterEqual(1)))))

make_entry(ID("789ca4"),
    Formula(Equal(DirichletL(0,chi), -Div(1,q) * Sum(k * chi(k), Tuple(k, 1, q)))),
    Variables(q),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Unequal(chi, DirichletCharacter(q, 1)))))

make_entry(ID("fad52f"),
    Formula(Implies(Equal(chi(-1), 1), Equal(DirichletL(0,chi), 0))),
    Variables(q),
    Assumptions(And(Element(q, ZZGreaterEqual(2)), Element(chi, DirichletGroup(q)))))

# Values at negative integers

make_entry(ID("cb5d51"),
    SymbolDefinition(GeneralizedBernoulliB, GeneralizedBernoulliB(n, chi), "Generalized Bernoulli number"))

make_entry(ID("e44796"),
    Formula(Equal(GeneralizedBernoulliB(n, chi), Sum(chi(a) * Sum(Binomial(n,k) * BernoulliB(k) * a**(n-k) * q**(k-1), Tuple(k, 0, n)), Tuple(a, 1, q)))),
    Variables(q, chi, n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("3e0817"),
    Formula(Equal(GeneralizedBernoulliB(n, chi), q**(n-1) * Sum(chi(a) * BernoulliPolynomial(n, a/q), Tuple(a, 1, q)))),
    Variables(q, chi, n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("f7a866"),
    Formula(Equal(GeneralizedBernoulliB(0, chi), Cases(Tuple(Totient(q)/q, Equal(chi, DirichletCharacter(q, 1))), Tuple(0, Otherwise)))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("d69b41"),
    Formula(Equal(Sum(chi(a)* (z*Exp(a*z)/(Exp(q*z)-1)), Tuple(a, 1, q)),
        Sum(GeneralizedBernoulliB(n, chi) * (z**n / Factorial(n)), Tuple(n, 0, Infinity)))),
    Variables(q, chi, z),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(z, CC), Unequal(z, 0), Less(Abs(z), 2*ConstPi / q))))

make_entry(ID("f5c3c5"),
    Formula(Equal(DirichletL(-n, chi), -(GeneralizedBernoulliB(n+1,chi)/(n+1)))),
    Variables(q, chi, n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(n, ZZGreaterEqual(0)))))

# Zeros

make_entry(ID("3f96c1"),
    SymbolDefinition(DirichletLZero, DirichletLZero(n,chi), "Nontrivial zero of Dirichlet L-function"),
    Description("Generalizing", SourceForm(RiemannZetaZero), ", this gives an enumeration of the nontrivial zeros of a given Dirichlet L-function, where eventual repeated zeros are counted separately.",
        "The index", n, "is a nonzero integer such that", Greater(n, 0), "gives zeros with", Greater(Im(DirichletLZero(n,chi)), 0),
        ", ordered by increasing imaginary part, while", Less(n, 0), "gives zeros with", LessEqual(Im(DirichletLZero(n,chi)), 0),
        ", ordered by decreasing imaginary part."))

make_entry(ID("dc593e"),
    SymbolDefinition(GeneralizedRiemannHypothesis, GeneralizedRiemannHypothesis, "Generalized Riemann hypothesis"),
    Description("Used as a symbol in logical formulas, represents the assertion that the generalized Riemann hypothesis is true for all Dirichlet L-functions, "
        "or in other words that", EntryReference("214a91"), "always holds."))

make_entry(ID("982e3b"),
    Formula(Less(0, Re(DirichletLZero(n,chi)), 1)),
    Variables(q,n,chi),
    Assumptions(And(Element(q,ZZGreaterEqual(1)), Element(chi, PrimitiveDirichletCharacters(q)),
        Element(n, ZZ), Unequal(n, 0))))

make_entry(ID("214a91"),
    Formula(Equal(Re(DirichletLZero(n,chi)), Div(1,2))),
    Variables(q,n,chi),
    Assumptions(And(Element(q,ZZGreaterEqual(1)), Element(chi, PrimitiveDirichletCharacters(q)),
        Element(n, ZZ), Unequal(n, 0), Or(And(Less(q, 400000), Less(Abs(Im(DirichletLZero(n,chi))), Pow(10,8)/q)), GeneralizedRiemannHypothesis))),
    References("""D. J. Platt (2013), Numerical computations concerning the GRH. https://arxiv.org/pdf/1305.3087.pdf"""))

make_entry(ID("9ba78a"),
    Formula(Equal(Zeros(DirichletL(s, chi), s, And(Element(s, CC), LessEqual(Re(s), 0))),
        Cases(Tuple(SetBuilder(-(2*n), n, Element(n, ZZGreaterEqual(1))), Equal(q, 1)),
              Tuple(SetBuilder(-(2*n), n, Element(n, ZZGreaterEqual(0))), And(Equal(chi(-1), 1), Unequal(q, 1))),
              Tuple(SetBuilder(-(2*n)-1, n, Element(n, ZZGreaterEqual(0))), Equal(chi(-1), -1))))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, PrimitiveDirichletCharacters(q)))))

make_entry(ID("bc755b"),
    Formula(Equal(Zeros(DirichletL(s, chi), s, Element(s, CC)),
        Union(Parentheses(Zeros(DirichletL(s, chi), s, And(Element(s, CC), LessEqual(Re(s), 0)))),
            SetBuilder(DirichletLZero(n, chi), n, Element(n, SetMinus(ZZ, Set(0))))))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("2a34c3"),
    Formula(Equal(Zeros(DirichletL(s, chi), s, And(Element(s, CC), Less(0, Re(s), 1))),
        SetBuilder(DirichletLZero(n, chi), n, Element(n, SetMinus(ZZ, Set(0)))))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

# todo: document extra trivial zeros for non-primitive characters?

# Conjugate symmetry

make_entry(ID("7c86d5"),
    Formula(Equal(DirichletL(s, Conjugate(chi)), Conjugate(DirichletL(Conjugate(s), chi)))),
    Variables(s, CC),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC))))

make_entry(ID("50adea"),
    Formula(Equal(DirichletL(Conjugate(s), chi), Conjugate(DirichletL(s, Conjugate(chi))))),
    Variables(s, CC),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC))))

make_entry(ID("97fe89"),
    Formula(Equal(DirichletL(Conjugate(s), Conjugate(chi)), Conjugate(DirichletL(s, chi)))),
    Variables(s, CC),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC))))

# Functional equation

make_entry(ID("cc6a5a"),
    SymbolDefinition(DirichletLambda, DirichletLambda(s, chi), "Completed Dirichlet L-function"),
    Description("The completed Dirichlet L-function is an entire function of", s, ".",
        "It is defined by", EntryReference("b788a1"), "and taking the limiting value at the exceptional points", s,
        "where a pole appears in one of the constituent factors."),
    Description("In the literature, this function is sometimes multiplied by a different constant factor (depending on", chi, "but constant with respect to", s, ")."))

make_entry(ID("b788a1"),
    Formula(Equal(DirichletLambda(s, chi), Where(beta * (q / ConstPi)**((s+a)/2) * GammaFunction((s+a)/2) * DirichletL(s,chi),
        Equal(a, (1 - chi(-1))/2), Equal(beta, Cases(Tuple(s*(s-1), Equal(q, 1)), Tuple(1, Otherwise)))))),
    Variables(q, chi, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, PrimitiveDirichletCharacters(q)), Element(s, CC),
        NotElement(s, Cases(Tuple(SetBuilder(-(2*n), n, Element(n, ZZGreaterEqual(0))), Equal(chi(-1), 1)),
                            Tuple(SetBuilder(-(2*n)-1, n, Element(n, ZZGreaterEqual(0))), Equal(chi(-1), -1)))),
        Not(And(Equal(q,1), Equal(s,1))))))

make_entry(ID("11a763"),
    SymbolDefinition(GaussSum, GaussSum(q, chi), "Gauss sum"))

make_entry(ID("62f12c"),
    Formula(Equal(GaussSum(q, chi), Sum(chi(n) * Exp(2*ConstPi*ConstI*n/q), Tuple(n, 1, q)))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("b78a50"),
    Formula(Equal(Abs(GaussSum(q, chi)), Sqrt(q))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, PrimitiveDirichletCharacters(q)))))

make_entry(ID("288207"),
    Formula(Equal(DirichletLambda(s, chi), Where(epsilon * DirichletLambda(1-s, Conjugate(chi)), Equal(a, (1-chi(-1))/2), Equal(epsilon, GaussSum(q, chi) / (ConstI**a * Sqrt(q)))))),
    Variables(q, chi, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, PrimitiveDirichletCharacters(q)), Element(s, CC))))

# Analytic properties

make_entry(ID("8533f5"),
    Formula(Equal(BranchCuts(DirichletL(s,chi), s, Union(CC, Set(UnsignedInfinity))), Set())),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("97f631"),
    Formula(Equal(EssentialSingularities(DirichletL(s,chi), s, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("ea8c55"),
    Formula(Equal(Poles(DirichletL(s,chi), s, Union(CC, Set(UnsignedInfinity))), Cases(Tuple(Set(1), Equal(chi, DirichletCharacter(q, 1))), Tuple(Set(), Otherwise)))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

make_entry(ID("fe4692"),
    Formula(Equal(HolomorphicDomain(DirichletL(s,chi), s, Union(CC, Set(UnsignedInfinity))), Cases(Tuple(SetMinus(CC, Set(1)), Equal(chi, DirichletCharacter(q, 1))), Tuple(CC, Otherwise)))),
    Variables(q, chi),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)))))

# Approximations

make_entry(ID("312147"),
    Formula(LessEqual(Abs(DirichletL(s,chi) - Sum(chi(k) / k**s, Tuple(k, 1, N-1))), HurwitzZeta(Re(s), N))),
    Variables(q, chi, s, N),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC), Greater(Re(s), 1), Element(N, ZZGreaterEqual(1)))))

make_entry(ID("4911bd"),
    Formula(LessEqual(Abs(1/DirichletL(s,chi) - PrimeProduct(Parentheses(1-chi(p) / p**s), p, Less(p, N))), HurwitzZeta(Re(s), N))),
    Variables(q, chi, s, N),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, CC), Greater(Re(s), 1), Element(N, ZZGreaterEqual(1)))))

# Bounds and inequalities

make_entry(ID("8ff1ff"),
    Formula(LessEqual(Abs(DirichletL(s, chi)), RiemannZeta(Re(s)))),
    Variables(q, chi, s),
    Assumptions(
        And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)),
            Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("9b3fde"),
    Formula(LessEqual(Abs(DirichletL(s,chi)), (q*Abs(1+s)/(2*ConstPi))**((1+eta-Re(s))/2) * RiemannZeta(1+eta))),
    Variables(q, chi, s, eta),
    Assumptions(
        And(Element(q, ZZGreaterEqual(2)), Element(chi, PrimitiveDirichletCharacters(q)),
            Element(s, CC), Element(eta, OpenClosedInterval(0, Div(1,2))), LessEqual(-eta, Re(s), 1 + eta))),
    References("H. Rademacher, On the Phragmén-Lindelöf theorem and some applications, Mathematische Zeitschrift, December 1959, Volume 72, Issue 1, pp 192-204. Theorem 3. https://doi.org/10.1007/BF01162949"))

