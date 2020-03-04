# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Greatest common divisor"),
    Section("Definitions"),
    Entries(
        "287e28",
        "c03ed9",
        "5daceb",
    ),
    Section("Tables"),
    Entries(
        "8b2743",
        "a0d13f",
        "99dc4a",
    ),
    Section("Divisibility"),
    Entries(
        "6880d0",
        "805c7a",
        "7638c5",
        "3605cc",
        "5d03d2",
        "a9c81e",
        "272bc8",
        "67978f",
        "4f1441",
        "65cfe5",
        "b60924",
        "1277f6",
        "e3392b",
        "663d9c",
    ),
    Section("Bézout identity"),
    Entries(
        "be5fcd",
        "965ac0",
        "e922c4",
        "f20503",
    ),
    Section("Connection formulas"),
    Entries(
        "4d3127",
        "6572c5",
        "927e6e",
        "126f3e",
    ),
    Section("Specific values"),
    Entries(
        "19ceaa",
        "af512f",
        "554b2e",
        "34378a",
        "c40be0",
        "0a7aff",
        "720766",
        "8d90e9",
        "0f26cc",
        "c6631e",
        "5fb5e2",
        "157c33",
        "c70178",
        "e19e40",
        "80f20f",
        "7a1799",
    ),
    Subsection("Canonical Bézout coefficients"),
    Entries(
        "e352ca",
        "6fd925",
        "13ed5e",
        "bf877e",
        "945be9",
        "0bb73e",
        "b66d1e",
        "1b47db",
        "a5ef5f",
        "633265",
        "4e5aad",
        "da7d00",
        "569278",
    ),
    Section("Functional equations"),
    Subsection("Symmetry"),
    Entries(
        "258fc7",
        "14b96c",
        "f1817f",
        "dc0823",
    ),
    Subsection("Addition and multiplication formulas"),
    Entries(
        "e65763",
        "b36dba",
        "07ac4a",
        "959a25",
        "d4852c",
        "9500d3",
        "5781de",
        "e74d86",
        "1bbdaf",
        "646745",
        "cb9f61",
    ),
    Subsection("Distributivity"),
    Entries(
        "4366b2",
        "1cde02",
        "8dc1c9",
        "c4a892",
        "1d1653",
        "7009cc",
    ),
    Section("Factorization"),
    Subsection("Coprime factors"),
    Entries(
        "8621f6",
        "fbe121",
    ),
    Subsection("Coprime arguments"),
    Entries(
        "5aad5c",
        "250a45",
    ),
    Subsection("Prime factorization"),
    Entries(
        "062423",
        "499cfc",
        "25986e",
        "6cefd7",
    ),
    Section("Special sequences"),
    Entries(
        "fdae67",
        "da45c0",
    ),
    Section("Summation and counting"),
    Entries(
        "7b27cd",
        "4099d2",
        "aaef97",
        "c24323",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "125606",
        "56acd6",
        "f91d1c",
        "b43dac",
        "10ed14",
    ),
)

# todo: define ExtendedGCD/XGCD
# todo: express variadic signature

make_entry(ID("287e28"),
    SymbolDefinition(GCD, GCD(a,b), "Greatest common divisor"),
    Description("The greatest common divisor function can be called either with with an arbitrary number of integer arguments or with a single finite set of integers as the argument. The current entries only deal with the case of two arguments."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(a, ZZ), Element(b, ZZ)), Element(GCD(a,b), ZZGreaterEqual(0))),
        Tuple(And(Element(S, PowerSet(ZZ)), Less(Cardinality(S), Cardinality(ZZ))), Element(GCD(S), ZZGreaterEqual(0))),
      )))

make_entry(ID("c03ed9"),
    SymbolDefinition(LCM, LCM(a,b), "Least common multiple"),
    Description("The least common multiple function can be called either with with an arbitrary number of integer arguments or with a single finite set of integers as the argument. The current entries only deal with the case of two arguments."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(a, ZZ), Element(b, ZZ)), Element(LCM(a,b), ZZGreaterEqual(0))),
        Tuple(And(Element(S, PowerSet(ZZ)), Less(Cardinality(S), Cardinality(ZZ))), Element(LCM(S), ZZGreaterEqual(0))),
      )))

make_entry(ID("5daceb"),
    SymbolDefinition(XGCD, XGCD(a,b), "Extended greatest common divisor"),
    #Description(""),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(a, ZZ), Element(b, ZZ)),
            Where(And(Element(d, ZZGreaterEqual(0)), Element(u, ZZ), Element(v, ZZ)), Equal(Tuple(d, u, v), XGCD(a, b)))),
      )))

# Tables

make_entry(ID("8b2743"),
    Description("Table of", GCD(n, k), "for", LessEqual(0, n, 15), "and", LessEqual(0, k, 15)),
    Table(TableRelation(Tuple(n, k, y), Equal(GCD(n, k), y)),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
        List(
        Tuple(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
        Tuple(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        Tuple(2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1),
        Tuple(3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3),
        Tuple(4, 1, 2, 1, 4, 1, 2, 1, 4, 1, 2, 1, 4, 1, 2, 1),
        Tuple(5, 1, 1, 1, 1, 5, 1, 1, 1, 1, 5, 1, 1, 1, 1, 5),
        Tuple(6, 1, 2, 3, 2, 1, 6, 1, 2, 3, 2, 1, 6, 1, 2, 3),
        Tuple(7, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1, 1, 7, 1),
        Tuple(8, 1, 2, 1, 4, 1, 2, 1, 8, 1, 2, 1, 4, 1, 2, 1),
        Tuple(9, 1, 1, 3, 1, 1, 3, 1, 1, 9, 1, 1, 3, 1, 1, 3),
        Tuple(10, 1, 2, 1, 2, 5, 2, 1, 2, 1, 10, 1, 2, 1, 2, 5),
        Tuple(11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1),
        Tuple(12, 1, 2, 3, 4, 1, 6, 1, 4, 3, 2, 1, 12, 1, 2, 3),
        Tuple(13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1),
        Tuple(14, 1, 2, 1, 2, 1, 2, 7, 2, 1, 2, 1, 2, 1, 14, 1),
        Tuple(15, 1, 1, 3, 1, 5, 3, 1, 1, 3, 5, 1, 3, 1, 1, 15),
    )))

make_entry(ID("a0d13f"),
    Description("Table of", LCM(n, k), "for", LessEqual(0, n, 15), "and", LessEqual(0, k, 15)),
    Table(TableRelation(Tuple(n, k, y), Equal(LCM(n, k), y)),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
        List(
        Tuple(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
        Tuple(0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30),
        Tuple(0, 3, 6, 3, 12, 15, 6, 21, 24, 9, 30, 33, 12, 39, 42, 15),
        Tuple(0, 4, 4, 12, 4, 20, 12, 28, 8, 36, 20, 44, 12, 52, 28, 60),
        Tuple(0, 5, 10, 15, 20, 5, 30, 35, 40, 45, 10, 55, 60, 65, 70, 15),
        Tuple(0, 6, 6, 6, 12, 30, 6, 42, 24, 18, 30, 66, 12, 78, 42, 30),
        Tuple(0, 7, 14, 21, 28, 35, 42, 7, 56, 63, 70, 77, 84, 91, 14, 105),
        Tuple(0, 8, 8, 24, 8, 40, 24, 56, 8, 72, 40, 88, 24, 104, 56, 120),
        Tuple(0, 9, 18, 9, 36, 45, 18, 63, 72, 9, 90, 99, 36, 117, 126, 45),
        Tuple(0, 10, 10, 30, 20, 10, 30, 70, 40, 90, 10, 110, 60, 130, 70, 30),
        Tuple(0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 11, 132, 143, 154, 165),
        Tuple(0, 12, 12, 12, 12, 60, 12, 84, 24, 36, 60, 132, 12, 156, 84, 60),
        Tuple(0, 13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 13, 182, 195),
        Tuple(0, 14, 14, 42, 28, 70, 42, 14, 56, 126, 70, 154, 84, 182, 14, 210),
        Tuple(0, 15, 30, 15, 60, 15, 30, 105, 120, 45, 30, 165, 60, 195, 210, 15),
    )))

make_entry(ID("99dc4a"),
    Description("Table of", XGCD(n, k), "for", LessEqual(0, n, 10), "and", LessEqual(0, k, 10)),
    Table(TableRelation(Tuple(n, k, Tuple(d, u, v)), Equal(XGCD(n, k), Tuple(d, u, v))),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        List(
    Tuple(Tuple(0,0,0), Tuple(1,0,1), Tuple(2,0,1), Tuple(3,0,1), Tuple(4,0,1), Tuple(5,0,1), Tuple(6,0,1), Tuple(7,0,1), Tuple(8,0,1), Tuple(9,0,1), Tuple(10,0,1)),
    Tuple(Tuple(1,1,0), Tuple(1,0,1), Tuple(1,1,0), Tuple(1,1,0), Tuple(1,1,0), Tuple(1,1,0), Tuple(1,1,0), Tuple(1,1,0), Tuple(1,1,0), Tuple(1,1,0), Tuple(1,1,0)),
    Tuple(Tuple(2,1,0), Tuple(1,0,1), Tuple(2,0,1), Tuple(1,-1,1), Tuple(2,1,0), Tuple(1,-2,1), Tuple(2,1,0), Tuple(1,-3,1), Tuple(2,1,0), Tuple(1,-4,1), Tuple(2,1,0)),
    Tuple(Tuple(3,1,0), Tuple(1,0,1), Tuple(1,1,-1), Tuple(3,0,1), Tuple(1,-1,1), Tuple(1,2,-1), Tuple(3,1,0), Tuple(1,-2,1), Tuple(1,3,-1), Tuple(3,1,0), Tuple(1,-3,1)),
    Tuple(Tuple(4,1,0), Tuple(1,0,1), Tuple(2,0,1), Tuple(1,1,-1), Tuple(4,0,1), Tuple(1,-1,1), Tuple(2,-1,1), Tuple(1,2,-1), Tuple(4,1,0), Tuple(1,-2,1), Tuple(2,-2,1)),
    Tuple(Tuple(5,1,0), Tuple(1,0,1), Tuple(1,1,-2), Tuple(1,-1,2), Tuple(1,1,-1), Tuple(5,0,1), Tuple(1,-1,1), Tuple(1,3,-2), Tuple(1,-3,2), Tuple(1,2,-1), Tuple(5,1,0)),
    Tuple(Tuple(6,1,0), Tuple(1,0,1), Tuple(2,0,1), Tuple(3,0,1), Tuple(2,1,-1), Tuple(1,1,-1), Tuple(6,0,1), Tuple(1,-1,1), Tuple(2,-1,1), Tuple(3,-1,1), Tuple(2,2,-1)),
    Tuple(Tuple(7,1,0), Tuple(1,0,1), Tuple(1,1,-3), Tuple(1,1,-2), Tuple(1,-1,2), Tuple(1,-2,3), Tuple(1,1,-1), Tuple(7,0,1), Tuple(1,-1,1), Tuple(1,4,-3), Tuple(1,3,-2)),
    Tuple(Tuple(8,1,0), Tuple(1,0,1), Tuple(2,0,1), Tuple(1,-1,3), Tuple(4,0,1), Tuple(1,2,-3), Tuple(2,1,-1), Tuple(1,1,-1), Tuple(8,0,1), Tuple(1,-1,1), Tuple(2,-1,1)),
    Tuple(Tuple(9,1,0), Tuple(1,0,1), Tuple(1,1,-4), Tuple(3,0,1), Tuple(1,1,-2), Tuple(1,-1,2), Tuple(3,1,-1), Tuple(1,-3,4), Tuple(1,1,-1), Tuple(9,0,1), Tuple(1,-1,1)),
    Tuple(Tuple(10,1,0), Tuple(1,0,1), Tuple(2,0,1), Tuple(1,1,-3), Tuple(2,1,-2), Tuple(5,0,1), Tuple(2,-1,2), Tuple(1,-2,3), Tuple(2,1,-1), Tuple(1,1,-1), Tuple(10,0,1)),
    )))

# Divisibility

make_entry(ID("6880d0"),
    Formula(Equal(GCD(a,b), Maximum(Set(d, For(d), And(Element(d, ZZGreaterEqual(1)), Divides(d, a), Divides(d, b)))))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("805c7a"),
    Formula(Equal(LCM(a,b), Minimum(Set(m, For(m), And(Element(m, ZZGreaterEqual(1)), Divides(a, m), Divides(b, m)))))),
    Variables(a,b),
    Assumptions(And(Element(a,SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

make_entry(ID("7638c5"),
    Formula(Implies(And(Divides(d,a), Divides(d,b)), Divides(d, GCD(a,b)))),
    Variables(a,b,d),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Element(d, ZZ))))

make_entry(ID("3605cc"),
    Formula(Implies(And(Divides(a,m), Divides(b,m)), Divides(LCM(a,b), m))),
    Variables(a,b,m),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Element(m, ZZ))))

make_entry(ID("5d03d2"),
    Formula(Implies(Or(Divides(d,a), Divides(d,b)), Divides(d, LCM(a,b)))),
    Variables(a,b,d),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Element(d, ZZ))))

make_entry(ID("a9c81e"),
    Formula(Divides(GCD(a, b), a)),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("272bc8"),
    Formula(Divides(GCD(a, b), b)),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("67978f"),
    Formula(Divides(a, LCM(a, b))),
    Variables(a,b),
    Assumptions(And(Element(a,SetMinus(ZZ, Set(0))), Element(b, ZZ))))

make_entry(ID("4f1441"),
    Formula(Divides(b, LCM(a, b))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, SetMinus(ZZ, Set(0))))))

make_entry(ID("65cfe5"),
    Formula(Divides(LCM(a, b), a*b)),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), And(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("b60924"),
    Formula(Divides(GCD(a, b), a*b)),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("1277f6"),
    Formula(Divides(GCD(a, b), LCM(a, b))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), And(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("e3392b"),
    Formula(Divides(GCD(a, b), a+b)),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("663d9c"),
    Formula(Divides(GCD(a, b), a*x+b*y)),
    Variables(a,b,x,y),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Element(x, ZZ), Element(y, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

# Bézout identity

make_entry(ID("be5fcd"),
    Formula(Where(Equal(GCD(a,b), d, a*u + b*v), Equal(Tuple(d, u, v), XGCD(a, b)))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ))))

make_entry(ID("965ac0"),
    Formula(Where(Equal(Set(a*x+b*y, For(Tuple(x,y)), And(Element(x, ZZ), Element(y, ZZ))),
        Set(n*d, ForElement(n, ZZ))), Equal(d, GCD(a,b)))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ))))

make_entry(ID("e922c4"),
    Formula(Equal(GCD(a,b), Minimum(Set(a*x + b*y, For(Tuple(x, y)), And(Element(x, ZZ), Element(y, ZZ), GreaterEqual(a*x + b*y, 1)))))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("f20503"),
    Formula(Where(Equal(d, a*x + b*y), Equal(Tuple(d, u, v), XGCD(a, b)), Equal(Tuple(x, y), Tuple(u+k*b/d, v-k*a/d)))),
    Variables(a,b,k),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Element(k, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

# Connection formulas

make_entry(ID("4d3127"),
    Formula(Equal(GCD(a,b)*LCM(a,b), Abs(a*b))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ))))

make_entry(ID("6572c5"),
    Formula(Equal(GCD(a,b), Abs(a*b) / LCM(a,b))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), NotEqual(a, 0), NotEqual(b, 0))))

make_entry(ID("927e6e"),
    Formula(Equal(LCM(a,b), Abs(a*b) / GCD(a,b))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ), Or(NotEqual(a, 0), NotEqual(b, 0)))))

make_entry(ID("126f3e"),
    Formula(Equal(GCD(a,b), Where(d, Equal(Tuple(d, u, v), XGCD(a, b))))),
    Variables(a,b),
    Assumptions(And(Element(a,ZZ), Element(b, ZZ))))

# Specific values

make_entry(ID("19ceaa"),
    Formula(Equal(GCD(0,0), 0)))

make_entry(ID("af512f"),
    Formula(Equal(LCM(0,0), 0)))

make_entry(ID("554b2e"),
    Formula(Equal(GCD(1,1), 1)))

make_entry(ID("34378a"),
    Formula(Equal(LCM(1,1), 1)))

make_entry(ID("c40be0"),
    Formula(Equal(GCD(a,0), Abs(a))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("0a7aff"),
    Formula(Equal(LCM(a,0), 0)),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("720766"),
    Formula(Equal(GCD(a,1), 1)),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("8d90e9"),
    Formula(Equal(LCM(a,1), Abs(a))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("0f26cc"),
    Formula(Equal(GCD(a, a), Abs(a))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("c6631e"),
    Formula(Equal(LCM(a, a), Abs(a))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("5fb5e2"),
    Formula(Equal(GCD(a, 2), 1 + (1 + (-1)**a)/2)),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("157c33"),
    Formula(Equal(LCM(a, 2), Abs(a) * (1 + (1 - (-1)**a)/2))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("c70178"),
    Formula(Equal(GCD(a, a-1), 1)),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("e19e40"),
    Formula(Equal(LCM(a, a-1), a*(a-1))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("80f20f"),
    Formula(Equal(GCD(a, a - 2), 1 + (1 + (-1)**a)/2)),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("7a1799"),
    Formula(Equal(LCM(a, a-2), (Abs(a*(a-2))/2) * (1 + (1 - (-1)**a)/2))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

# Canonical Bézout coefficients

make_entry(ID("e352ca"),
    Formula(Equal(XGCD(a,0), Tuple(Abs(a), Sign(a), 0))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("6fd925"),
    Formula(Equal(XGCD(0,b), Tuple(Abs(b), 0, Sign(b)))),
    Variables(b),
    Assumptions(Element(b, ZZ)))

make_entry(ID("13ed5e"),
    Formula(Equal(XGCD(a,1), Tuple(1, 0, 1))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("bf877e"),
    Formula(Equal(XGCD(1,b), Tuple(1, Abs(Sign((b-1)*(b+1))), Sign(b)*(Sign(b+1)-Sign(b-1))))),
    Variables(b),
    Assumptions(Element(b, ZZ)))

make_entry(ID("945be9"),
    Formula(Equal(XGCD(a,a), Tuple(Abs(a), 0, Sign(a)))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("0bb73e"),
    Formula(Equal(XGCD(a,-a), Tuple(Abs(a), 0, -Sign(a)))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("b66d1e"),
    Formula(Equal(XGCD(a,-1), Tuple(1, 0, -1))),
    Variables(a),
    Assumptions(Element(a, ZZ)))

make_entry(ID("1b47db"),
    Formula(Equal(XGCD(-1,b), Tuple(1, -Abs(Sign((b-1)*(b+1))), Sign(b)*(Sign(b+1)-Sign(b-1))))),
    Variables(b),
    Assumptions(Element(b, ZZ)))

make_entry(ID("a5ef5f"),
    Formula(Where(Implies(Equal(Abs(a), Abs(b)), Equal(Tuple(u, v), Tuple(0, Sign(b)))), Equal(Tuple(d, u, v), XGCD(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

make_entry(ID("633265"),
    Formula(Where(Implies(And(NotEqual(Abs(a), Abs(b)), NotEqual(Abs(a), Abs(2*d))), Less(2*d*Abs(v), Abs(a))), Equal(Tuple(d, u, v), XGCD(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

make_entry(ID("4e5aad"),
    Formula(Where(Implies(And(NotEqual(Abs(a), Abs(b)), Equal(Abs(a), Abs(2*d))), Equal(v, Sign(b))), Equal(Tuple(d, u, v), XGCD(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

make_entry(ID("da7d00"),
    Formula(Where(Implies(And(NotEqual(Abs(a), Abs(b)), NotEqual(Abs(b), Abs(2*d))), Less(2*d*Abs(u), Abs(b))), Equal(Tuple(d, u, v), XGCD(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

make_entry(ID("569278"),
    Formula(Where(Implies(And(NotEqual(Abs(a), Abs(b)), Equal(Abs(b), Abs(2*d))), Equal(u, Sign(a))), Equal(Tuple(d, u, v), XGCD(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

# Functional equations

# Symmetry

make_entry(ID("258fc7"),
    Formula(Equal(GCD(a, b), GCD(b, a))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

make_entry(ID("14b96c"),
    Formula(Equal(LCM(a, b), LCM(b, a))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

make_entry(ID("f1817f"),
    Formula(Equal(GCD(a, b), GCD(-a, b), GCD(a, -b), GCD(-a, -b))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

make_entry(ID("dc0823"),
    Formula(Equal(LCM(a, b), LCM(-a, b), LCM(a, -b), LCM(-a, -b))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

# Addition and multiplication formulas

make_entry(ID("e65763"),
    Formula(Equal(GCD(a+b, b), GCD(a, b))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

make_entry(ID("b36dba"),
    Formula(Equal(GCD(a-b, b), GCD(a, b))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

make_entry(ID("07ac4a"),
    Formula(Equal(GCD(a+n*b, b), GCD(a, b))),
    Variables(a, b, n),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(n, ZZ))))

make_entry(ID("959a25"),
    Formula(Equal(GCD(Mod(a,b), b), GCD(a, b))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), NotEqual(b, 0))))

make_entry(ID("d4852c"),
    Formula(Equal(GCD(n*a, n*b), Abs(n)*GCD(a, b))),
    Variables(a, b, n),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(n, ZZ))))

make_entry(ID("9500d3"),
    Formula(Equal(LCM(n*a, n*b), Abs(n)*LCM(a, b))),
    Variables(a, b, n),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(n, ZZ))))

make_entry(ID("5781de"),
    Formula(Equal(LCM(a+b, b), Abs(a+b) * LCM(a,b) / Abs(a))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, ZZ))))

make_entry(ID("e74d86"),
    Formula(Equal(LCM(a-b, b), Abs(a-b) * LCM(a,b) / Abs(a))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, ZZ))))

make_entry(ID("1bbdaf"),
    Formula(Equal(LCM(a+n*b, b), Abs(a+n*b) * LCM(a,b) / Abs(a))),
    Variables(a, b, n),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, ZZ), Element(n, ZZ))))

make_entry(ID("646745"),
    Formula(Equal(GCD(a/d, b/d), GCD(a,b)/Abs(d))),
    Variables(a, b, d),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(d, ZZ), Divides(d, a), Divides(d, b))))

make_entry(ID("cb9f61"),
    Formula(Equal(LCM(a/d, b/d), LCM(a,b)/Abs(d))),
    Variables(a, b, d),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(d, ZZ), Divides(d, a), Divides(d, b))))

# Distributivity

make_entry(ID("4366b2"),
    Formula(Equal(GCD(a, GCD(b, c)), GCD(GCD(a, b), c))),
    Variables(a, b, c),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(c, ZZ))))

make_entry(ID("1cde02"),
    Formula(Equal(LCM(a, LCM(b, c)), LCM(LCM(a, b), c))),
    Variables(a, b, c),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(c, ZZ))))

make_entry(ID("8dc1c9"),
    Formula(Equal(GCD(a, LCM(b, c)), LCM(GCD(a, b), GCD(a, c)))),
    Variables(a, b, c),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(c, ZZ))))

make_entry(ID("c4a892"),
    Formula(Equal(LCM(a, GCD(b, c)), GCD(LCM(a, b), LCM(a, c)))),
    Variables(a, b, c),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(c, ZZ))))

make_entry(ID("1d1653"),
    Formula(Equal(GCD(a, LCM(a, b)), Abs(a))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

make_entry(ID("7009cc"),
    Formula(Equal(LCM(a, GCD(a, b)), Abs(a))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

# Factorization

# Coprime arguments

make_entry(ID("8621f6"),
    Formula(Equal(GCD(r*s, c), GCD(r,c)*GCD(s,c))),
    Variables(r, s, c),
    Assumptions(And(Element(r, ZZ), Element(s, ZZ), Element(c, ZZ), Equal(GCD(r,s), 1))))

make_entry(ID("fbe121"),
    Formula(Equal(LCM(r*s, c), LCM(r,c)*LCM(s,c)/Abs(c))),
    Variables(r, s, c),
    Assumptions(And(Element(r, ZZ), Element(s, ZZ), Element(c, ZZ), Equal(GCD(r,s), 1), NotEqual(c, 0))))

make_entry(ID("5aad5c"),
    Formula(Equal(GCD(r**m, s**n), 1)),
    Variables(r, s, m, n),
    Assumptions(And(Element(r, ZZ), Element(s, ZZ), Equal(GCD(r, s), 1), Element(m, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("250a45"),
    Formula(Equal(LCM(r, s), Abs(r*s))),
    Variables(r, s),
    Assumptions(And(Element(r, ZZ), Element(s, ZZ), Equal(GCD(r, s), 1))))

# Prime factorization

make_entry(ID("062423"),
    Formula(Equal(GCD(p, q), 1)),
    Variables(p, q),
    Assumptions(And(Element(p, PP), Element(q, PP), NotEqual(p, q))))

make_entry(ID("499cfc"),
    Formula(Equal(GCD(p**m, q**n), 1)),
    Variables(p, q, m, n),
    Assumptions(And(Element(p, PP), Element(q, PP), NotEqual(p, q), Element(m, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("25986e"),
    Formula(Equal(GCD(Product(PrimeNumber(k)**Subscript(e,k), For(k, 1, m)),
                      Product(PrimeNumber(k)**Subscript(f,k), For(k, 1, m))),
                Product(PrimeNumber(k)**Min(Subscript(e,k), Subscript(f,k)), For(k, 1, m)))),
    Variables(e, f, m),
    Assumptions(And(Element(Subscript(e, k), ZZGreaterEqual(0)),
                    Element(Subscript(f, k), ZZGreaterEqual(0)),
                    Element(m, ZZGreaterEqual(0)))))

make_entry(ID("6cefd7"),
    Formula(Equal(LCM(Product(PrimeNumber(k)**Subscript(e,k), For(k, 1, m)),
                      Product(PrimeNumber(k)**Subscript(f,k), For(k, 1, m))),
                Product(PrimeNumber(k)**Max(Subscript(e,k), Subscript(f,k)), For(k, 1, m)))),
    Variables(e, f, m),
    Assumptions(And(Element(Subscript(e, k), ZZGreaterEqual(0)),
                    Element(Subscript(f, k), ZZGreaterEqual(0)),
                    Element(m, ZZGreaterEqual(0)))))

# Special sequences

make_entry(ID("fdae67"),
    Formula(Equal(GCD(n**a-1, n**b-1), n**GCD(a,b)-1)),
    Variables(a, b, n),
    Assumptions(And(Element(a, ZZGreaterEqual(0)), Element(b, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("da45c0"),
    Formula(Equal(GCD(Fibonacci(m), Fibonacci(n)), Fibonacci(GCD(m, n)))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZ), Element(n, ZZ))))

# Summation and counting

make_entry(ID("7b27cd"),
    Formula(Equal(Cardinality(Set(k, For(k), And(Element(k, Range(1, n)), Equal(GCD(n,k), 1)))), Totient(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

# fixme: should be CartesianPower, not Pow
make_entry(ID("4099d2"),
    Formula(Equal(SequenceLimit(
        (1/N**n) * Cardinality(Set(T, For(T), And(Element(T, Pow(Range(1, N), n)), Equal(GCD(T), 1)))),
        For(N, Infinity)), 1/RiemannZeta(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(2))))

# todo: more formulas? generating functions?
make_entry(ID("aaef97"),
    Formula(Equal(Sum(GCD(n,k), For(k,1,n)), DivisorSum(d*Totient(n/d), For(d, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("c24323"),
    Formula(Equal(Sum(LCM(n,k), For(k,1,n)), (n/2)*(1+DivisorSum(d*Totient(d), For(d, n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Bounds and inequalities

make_entry(ID("125606"),
    Formula(LessEqual(LCM(a,b), Abs(a*b))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

make_entry(ID("56acd6"),
    Formula(LessEqual(GCD(a,b), Max(Abs(a), Abs(b)))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ))))

make_entry(ID("f91d1c"),
    Formula(LessEqual(GCD(a,b), Min(Abs(a), Abs(b)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

make_entry(ID("b43dac"),
    Formula(Where(LessEqual(Abs(u), Abs(b)/d), Equal(Tuple(d, u, v), XGCD(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

make_entry(ID("10ed14"),
    Formula(Where(LessEqual(Abs(v), Abs(a)/d), Equal(Tuple(d, u, v), XGCD(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(ZZ, Set(0))), Element(b, SetMinus(ZZ, Set(0))))))

