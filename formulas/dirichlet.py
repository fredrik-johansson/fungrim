# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Dirichlet characters"),
    Section("Definitions"),
    Entries(
        "e810d8",
        "c7e2fb",
    ),
    Section("Fundamental properties"),
    Subsection("Character group"),
    Entries(
        "47d430",
        "62f7d5",
    ),
    Subsection("Character evaluation"),
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
    Section("Conrey numbering"),
    Subsection("Multiplicativity"),
    Entries
    (
        "2a48bd",
    ),
    Subsection("Principal character"),
    Entries(
        "d8c6d1",
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
    ),
    Section("Related topics"),
    SeeTopics("Dirichlet L-functions"),
)

make_entry(ID("e810d8"),
    SymbolDefinition(DirichletGroup, DirichletGroup(q), "Dirichlet characters with given modulus"),
    Description("Represents the set of Dirichlet characters modulo", q, "."))

make_entry(ID("c7e2fb"),
    SymbolDefinition(DirichletCharacter, DirichletCharacter(q,ell), "Dirichlet character"),
    Description(SourceForm(DirichletCharacter(q,ell)), ", rendered as",
        DirichletCharacter(q,ell), ", represents the Dirichlet character with Conrey label", Tuple(q, ell), "."),
    Description(
        "A character represents an object", chi, " that can be called (", chi(n), ") as a function from", ZZ, "to", CC, "."),
    Description(SourceForm(DirichletCharacter(q,ell,n)), ", rendered as",
        DirichletCharacter(q,ell,n), ", represents the Dirichlet character with Conrey label", Tuple(q, ell), "evaluated at the integer", n, "."),
    References("http://www.lmfdb.org/Character/Labels"),
    )

ellrange = Element(ell, ZZBetween(1, Max(q,2)-1))

# Fundamental properties

make_entry(ID("47d430"),
    Formula(Equal(DirichletGroup(q), SetBuilder(DirichletCharacter(q,ell), ell, And(ellrange, Equal(GCD(ell,q), 1))))),
    Variables(q),
    Assumptions(Element(q, ZZGreaterEqual(1))))

make_entry(ID("62f7d5"),
    Formula(Equal(Cardinality(DirichletGroup(q)), Totient(q))),
    Variables(q),
    Assumptions(Element(q, ZZGreaterEqual(1))))

make_entry(ID("d9a187"),
    Formula(Where(Equal(chi(n), DirichletCharacter(q,ell,n)), Equal(chi, DirichletCharacter(q,ell)))),
    Description("This is simply a syntactical definition of character evaluation."),
    Variables(q,ell,n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), ellrange, Equal(GCD(ell,q), 1), Element(n, ZZ))))

make_entry(ID("57d31a"),
    Formula(Where(Element(chi(n), Union(SetBuilder(Exp(2*ConstPi*ConstI*k/r), k, Element(k, ZZBetween(0,r-1))), Set(0))), Equal(r, Totient(q)))),
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

make_entry(ID("d8c6d1"),
    Formula(Equal(DirichletCharacter(q, 1, n), 1)),
    Variables(q,n),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(n, ZZ), Equal(GCD(n,q), 1))))

make_entry(ID("4cf4e4"),
    Formula(Where(Equal(DirichletCharacter(q, ell, n), Exp(2*ConstPi*ConstI*a*b/Totient(q))),
        Equal(q, p**e), Equal(g, ConreyGenerator(p)), Equal(a, DiscreteLog(ell, g, q)), Equal(b, DiscreteLog(n, g, q)))),
    Variables(p, e, ell, n),
    Assumptions(And(Element(p, PP), GreaterEqual(p, 3), Element(e, ZZGreaterEqual(1)),
        Element(ell, ZZBetween(1, p**e-1)), Element(n, ZZ), Equal(GCD(ell, p**e), GCD(n, p**e), 1))))

make_entry(ID("fc4f6a"),
    Formula(Equal(DirichletCharacter(4, 3, n), (-1)**Floor(n/2))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), Equal(GCD(n,2), 1))))

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
    Section("Specific values"),
    Subsection("Generalized Bernoulli numbers"),
    Entries(
        "cb5d51",
        "e44796",
        "3e0817",
        "f7a866",
        "d69b41",
        "f5c3c5",
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

make_entry(ID("c31c10"),
    Formula(Equal(DirichletL(s, chi), (1/q**s) * Sum(chi(k) * HurwitzZeta(s, k/q), Tuple(k, 1, q)))),
    Variables(q, chi, s),
    Assumptions(And(Element(q, ZZGreaterEqual(1)), Element(chi, DirichletGroup(q)), Element(s, SetMinus(CC, Set(1))))))

make_entry(ID("4c3678"),
    Formula(Equal(HurwitzZeta(s, k/q), (q**s / Totient(q)) * Sum(Conjugate(chi(k)) * DirichletL(s, chi), chi, Element(chi, DirichletGroup(q))))),
    Variables(q, k, s),
    Assumptions(And(Element(q, ZZGreaterEqual(2)), Element(k, ZZBetween(1,q-1)), Equal(GCD(k,q), 1), Element(s, SetMinus(CC, Set(1))))))

# Specific values

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

