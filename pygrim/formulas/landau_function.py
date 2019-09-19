# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Landau's function"),
    Section("Definitions"),
    Entries(
        "32e430",
    ),
    Section("Tables"),
    Entries(
        "177218",
    ),
    Section("Arithmetic representations"),
    Entries(
        "7932c3",
    ),
    Section("Asymptotics"),
    Entries(
        "a3ab2a",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "9697b8",
        "3d5019",
        "87d19b",
    ),
    Section("Riemann hypothesis"),
    Entries(
        "65fa9f",
    ),
)

make_entry(ID("32e430"),
    SymbolDefinition(LandauG, LandauG(n), "Landau's function"),
    Description("Landau's function", LandauG(n), "gives the largest order of an element of the symmetric group", Subscript(S, n), "."),
    Description("It can be defined arithmetically as the maximum least common multiple of the partitions of", n, ", as in", EntryReference("7932c3"), "."),
    Description("The following table lists conditions such that", SourceForm(LandauG(n)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(n, ZZGreaterEqual(0)), Element(LandauG(n), ZZGreaterEqual(1))))),
    References("https://oeis.org/A000793"))

# Tables

make_entry(ID("177218"),
    Description("Table of", LandauG(n), "for", LessEqual(0, n, 100)),
    Table(
      Var(n),
      TableValueHeadings(n, LandauG(n)),
      TableSplit(4),
      List(
    Tuple(0, 1),
    Tuple(1, 1),
    Tuple(2, 2),
    Tuple(3, 3),
    Tuple(4, 4),
    Tuple(5, 6),
    Tuple(6, 6),
    Tuple(7, 12),
    Tuple(8, 15),
    Tuple(9, 20),
    Tuple(10, 30),
    Tuple(11, 30),
    Tuple(12, 60),
    Tuple(13, 60),
    Tuple(14, 84),
    Tuple(15, 105),
    Tuple(16, 140),
    Tuple(17, 210),
    Tuple(18, 210),
    Tuple(19, 420),
    Tuple(20, 420),
    Tuple(21, 420),
    Tuple(22, 420),
    Tuple(23, 840),
    Tuple(24, 840),
    Tuple(25, 1260),
    Tuple(26, 1260),
    Tuple(27, 1540),
    Tuple(28, 2310),
    Tuple(29, 2520),
    Tuple(30, 4620),
    Tuple(31, 4620),
    Tuple(32, 5460),
    Tuple(33, 5460),
    Tuple(34, 9240),
    Tuple(35, 9240),
    Tuple(36, 13860),
    Tuple(37, 13860),
    Tuple(38, 16380),
    Tuple(39, 16380),
    Tuple(40, 27720),
    Tuple(41, 30030),
    Tuple(42, 32760),
    Tuple(43, 60060),
    Tuple(44, 60060),
    Tuple(45, 60060),
    Tuple(46, 60060),
    Tuple(47, 120120),
    Tuple(48, 120120),
    Tuple(49, 180180),
    Tuple(50, 180180),
    Tuple(51, 180180),
    Tuple(52, 180180),
    Tuple(53, 360360),
    Tuple(54, 360360),
    Tuple(55, 360360),
    Tuple(56, 360360),
    Tuple(57, 471240),
    Tuple(58, 510510),
    Tuple(59, 556920),
    Tuple(60, 1021020),
    Tuple(61, 1021020),
    Tuple(62, 1141140),
    Tuple(63, 1141140),
    Tuple(64, 2042040),
    Tuple(65, 2042040),
    Tuple(66, 3063060),
    Tuple(67, 3063060),
    Tuple(68, 3423420),
    Tuple(69, 3423420),
    Tuple(70, 6126120),
    Tuple(71, 6126120),
    Tuple(72, 6846840),
    Tuple(73, 6846840),
    Tuple(74, 6846840),
    Tuple(75, 6846840),
    Tuple(76, 8953560),
    Tuple(77, 9699690),
    Tuple(78, 12252240),
    Tuple(79, 19399380),
    Tuple(80, 19399380),
    Tuple(81, 19399380),
    Tuple(82, 19399380),
    Tuple(83, 38798760),
    Tuple(84, 38798760),
    Tuple(85, 58198140),
    Tuple(86, 58198140),
    Tuple(87, 58198140),
    Tuple(88, 58198140),
    Tuple(89, 116396280),
    Tuple(90, 116396280),
    Tuple(91, 116396280),
    Tuple(92, 116396280),
    Tuple(93, 140900760),
    Tuple(94, 140900760),
    Tuple(95, 157477320),
    Tuple(96, 157477320),
    Tuple(97, 232792560),
    Tuple(98, 232792560),
    Tuple(99, 232792560),
    Tuple(100, 232792560),
    )))

# Arithmetic representations

# todo: semantic markup for variable-length tuples (or better, partitions?)
make_entry(ID("7932c3"),
    Formula(Equal(LandauG(n),
        Maximum(SetBuilder(LCM(Subscript(s, 1), Ellipsis, Subscript(s, k)), Tuple(k, Subscript(s, i)),
            And(Element(k, ZZGreaterEqual(0)), Element(Subscript(s, i), ZZGreaterEqual(1)), Equal(Sum(Subscript(s, i), Tuple(i, 1, k)), n)))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

# Asymptotics

make_entry(ID("a3ab2a"),
    Formula(Equal(SequenceLimit(Log(LandauG(n)) / Sqrt(n * Log(n)), Var(n), Infinity), 1)))

# Bounds and inequalities

make_entry(ID("9697b8"),
    Formula(LessEqual(Log(LandauG(n)), Sqrt(n*Log(n)) * (1 + (Log(Log(n))-Decimal("0.975"))/(2*Log(n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(4))),
    References("Jean-Pierre Massias, Jean-Louis Nicolas and Guy Robin (1989), Effective bounds for the maximal order of an element in the symmetric group, Mathematics of Computation, 53, 118, 665--665, https://doi.org/10.1090/s0025-5718-1989-0979940-4"))

make_entry(ID("3d5019"),
    Formula(GreaterEqual(Log(LandauG(n)), Sqrt(n*Log(n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(906))),
    References("Jean-Pierre Massias, Jean-Louis Nicolas and Guy Robin (1989), Effective bounds for the maximal order of an element in the symmetric group, Mathematics of Computation, 53, 118, pp. 665-665, https://doi.org/10.1090/s0025-5718-1989-0979940-4"))

make_entry(ID("87d19b"),
    Formula(LessEqual(Maximum(SetBuilder(p, p, And(Element(p, PP), Divides(p, LandauG(n))))), Decimal("1.328") * Sqrt(n*Log(n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(5))),
    References("Jon Grantham (1995), The largest prime dividing the maximal order of an element of S_n, 64, 209, pp. 407--210, https://doi.org/10.2307/2153344"))

# Riemann hypothesis

make_entry(ID("65fa9f"),
    Formula(Equivalent(RiemannHypothesis,
        ForAll(n, Element(n, ZZGreaterEqual(1)),
            Less(Log(LandauG(n)), Where(Sqrt(f(n)), Equal(f(y), UniqueSolution(Brackets(Equal(LogIntegral(x), y)), Var(x), Element(x, OpenInterval(1, Infinity))))))))),
    References("Marc Deleglise, Jean-Louis Nicolas, The Landau function and the Riemann Hypothesis, https://arxiv.org/abs/1907.07664"))

