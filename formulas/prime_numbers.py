# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Prime numbers"),
    Entries(
        "38f111",
        "0b643d",
        "6c22c8",
        "c03de4",
    ),
    Section("Basic formulas"),
    Entries(
        "3fc797",
        "04427b",
    ),
    Section("Numerical values"),
    Entries(
        "a3035f",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "d1ec2d",
        "69fd4b",
        "8c52de",
        "6f3cf7",
        "d898b9",
        "5258c0",
        "375afe",
    ),
)

make_entry(ID("38f111"),
    SymbolDefinition(PP, PP, "Prime numbers"),
    Description("The set of prime numbers."))

make_entry(ID("0b643d"),
    SymbolDefinition(PrimeNumber, PrimeNumber(n), "nth prime number"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(n, ZZGreaterEqual(1)), Element(PrimeNumber(n), PP)),
      )))

make_entry(ID("6c22c8"),
    SymbolDefinition(PrimePi, PrimePi(x), "Prime counting function"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(x, RR), Element(PrimePi(x), ZZGreaterEqual(0))),
        Tuple(Element(x, Set(Infinity)), Element(PrimePi(x), Set(Infinity))))
      ))

make_entry(ID("c03de4"),
    SymbolDefinition(RiemannHypothesis, RiemannHypothesis, "Riemann hypothesis"),
    Description("Used as a symbol in logical formulas, represents the assertion that the Riemann hypothesis is true."))

make_entry(ID("3fc797"),
    Formula(Equal(PP, SetBuilder(PrimeNumber(n), Element(n, ZZGreaterEqual(1))))))

make_entry(ID("04427b"),
    Formula(Equal(PrimePi(x), Cardinality(SetBuilder(p, And(Element(p, PP), LessEqual(p, x)))))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("d1ec2d"),
    Formula(Less(PrimeNumber(n+1), 2*PrimeNumber(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("69fd4b"),
    Formula(GreaterEqual(PrimePi(2*x) - PrimePi(x), 1)),
    Variables(x),
    Assumptions(And(Element(x, RR), GreaterEqual(x, 1))))

make_entry(ID("375afe"),
    Formula(Less(Abs(PrimePi(x)-LogIntegral(x)), Sqrt(x)*Log(x)/(8*ConstPi))),
    Variables(x),
    Assumptions(And(Element(x, RR), GreaterEqual(x, 2657), RiemannHypothesis)),
    References("L. Schoenfeld (1976). Sharper bounds for the Chebyshev functions θ(x) and ψ(x). II. Mathematics of Computation. 30 (134): 337-360. DOI: 10.2307/2005976"))

make_entry(ID("d898b9"),
    Formula(Greater(PrimePi(x), x/Log(x))),
    Variables(x),
    Assumptions(And(Element(x, RR), GreaterEqual(x, 17))))

make_entry(ID("5258c0"),
    Formula(Less(PrimePi(x), Decimal("1.25506") * x/Log(x))),
    Variables(x),
    Assumptions(And(Element(x, RR), Greater(x, 1))))

make_entry(ID("8c52de"),
    Formula(Greater(PrimeNumber(n), n*(Log(n*Log(n))-1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(2))))

make_entry(ID("6f3cf7"),
    Formula(Less(PrimeNumber(n), n*Log(n*Log(n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(6))))

make_entry(ID("a3035f"),
    Description("Table of", PrimeNumber(n), "for", LessEqual(1, n, 200)),
    Table(TableRelation(Tuple(n, y), Equal(PrimeNumber(n), y)),
      TableHeadings(n, PrimeNumber(n)), TableSplit(4),
      List(
Tuple(1, 2), Tuple(2, 3), Tuple(3, 5), Tuple(4, 7), Tuple(5, 11),
Tuple(6, 13), Tuple(7, 17), Tuple(8, 19), Tuple(9, 23), Tuple(10, 29),
Tuple(11, 31), Tuple(12, 37), Tuple(13, 41), Tuple(14, 43), Tuple(15, 47),
Tuple(16, 53), Tuple(17, 59), Tuple(18, 61), Tuple(19, 67), Tuple(20, 71),
Tuple(21, 73), Tuple(22, 79), Tuple(23, 83), Tuple(24, 89), Tuple(25, 97),
Tuple(26, 101), Tuple(27, 103), Tuple(28, 107), Tuple(29, 109), Tuple(30, 113),
Tuple(31, 127), Tuple(32, 131), Tuple(33, 137), Tuple(34, 139), Tuple(35, 149),
Tuple(36, 151), Tuple(37, 157), Tuple(38, 163), Tuple(39, 167), Tuple(40, 173),
Tuple(41, 179), Tuple(42, 181), Tuple(43, 191), Tuple(44, 193), Tuple(45, 197),
Tuple(46, 199), Tuple(47, 211), Tuple(48, 223), Tuple(49, 227), Tuple(50, 229),
Tuple(51, 233), Tuple(52, 239), Tuple(53, 241), Tuple(54, 251), Tuple(55, 257),
Tuple(56, 263), Tuple(57, 269), Tuple(58, 271), Tuple(59, 277), Tuple(60, 281),
Tuple(61, 283), Tuple(62, 293), Tuple(63, 307), Tuple(64, 311), Tuple(65, 313),
Tuple(66, 317), Tuple(67, 331), Tuple(68, 337), Tuple(69, 347), Tuple(70, 349),
Tuple(71, 353), Tuple(72, 359), Tuple(73, 367), Tuple(74, 373), Tuple(75, 379),
Tuple(76, 383), Tuple(77, 389), Tuple(78, 397), Tuple(79, 401), Tuple(80, 409),
Tuple(81, 419), Tuple(82, 421), Tuple(83, 431), Tuple(84, 433), Tuple(85, 439),
Tuple(86, 443), Tuple(87, 449), Tuple(88, 457), Tuple(89, 461), Tuple(90, 463),
Tuple(91, 467), Tuple(92, 479), Tuple(93, 487), Tuple(94, 491), Tuple(95, 499),
Tuple(96, 503), Tuple(97, 509), Tuple(98, 521), Tuple(99, 523), Tuple(100, 541),
Tuple(101, 547), Tuple(102, 557), Tuple(103, 563), Tuple(104, 569), Tuple(105, 571),
Tuple(106, 577), Tuple(107, 587), Tuple(108, 593), Tuple(109, 599), Tuple(110, 601),
Tuple(111, 607), Tuple(112, 613), Tuple(113, 617), Tuple(114, 619), Tuple(115, 631),
Tuple(116, 641), Tuple(117, 643), Tuple(118, 647), Tuple(119, 653), Tuple(120, 659),
Tuple(121, 661), Tuple(122, 673), Tuple(123, 677), Tuple(124, 683), Tuple(125, 691),
Tuple(126, 701), Tuple(127, 709), Tuple(128, 719), Tuple(129, 727), Tuple(130, 733),
Tuple(131, 739), Tuple(132, 743), Tuple(133, 751), Tuple(134, 757), Tuple(135, 761),
Tuple(136, 769), Tuple(137, 773), Tuple(138, 787), Tuple(139, 797), Tuple(140, 809),
Tuple(141, 811), Tuple(142, 821), Tuple(143, 823), Tuple(144, 827), Tuple(145, 829),
Tuple(146, 839), Tuple(147, 853), Tuple(148, 857), Tuple(149, 859), Tuple(150, 863),
Tuple(151, 877), Tuple(152, 881), Tuple(153, 883), Tuple(154, 887), Tuple(155, 907),
Tuple(156, 911), Tuple(157, 919), Tuple(158, 929), Tuple(159, 937), Tuple(160, 941),
Tuple(161, 947), Tuple(162, 953), Tuple(163, 967), Tuple(164, 971), Tuple(165, 977),
Tuple(166, 983), Tuple(167, 991), Tuple(168, 997), Tuple(169, 1009), Tuple(170, 1013),
Tuple(171, 1019), Tuple(172, 1021), Tuple(173, 1031), Tuple(174, 1033), Tuple(175, 1039),
Tuple(176, 1049), Tuple(177, 1051), Tuple(178, 1061), Tuple(179, 1063), Tuple(180, 1069),
Tuple(181, 1087), Tuple(182, 1091), Tuple(183, 1093), Tuple(184, 1097), Tuple(185, 1103),
Tuple(186, 1109), Tuple(187, 1117), Tuple(188, 1123), Tuple(189, 1129), Tuple(190, 1151),
Tuple(191, 1153), Tuple(192, 1163), Tuple(193, 1171), Tuple(194, 1181), Tuple(195, 1187),
Tuple(196, 1193), Tuple(197, 1201), Tuple(198, 1213), Tuple(199, 1217), Tuple(200, 1223),
    )))

