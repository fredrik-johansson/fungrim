# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Partition function"),
    Entries(
        "f5e153",
    ),
    Section("Specific values"),
    Entries(
        "856db2",
        "cebe1b",
        "e84642",
        "b2583f",
        "7ef291",
        "6018a4",
        "cd3013",
        "9933df",
    ),
    Section("Generating functions"),
    Entries(
        "599417",
    ),
    Section("Sums and recurrence relations"),
    Entries(
        "acdce8",
        "4d2e45",
    ),
    Section("Congruences"),
    Entries(
        "d8e37d",
        "89260d",
        "dacd74",
    ),
    Section("Inequalities"),
    Entries(
        "f7407a",
        "df3c07",
        "d72123",
        "e1f15b",
    ),
    Section("Asymptotic expansions"),
    Entries(
        "7697af",
    ),
    Section("Hardy-Ramanujan-Rademacher formula"),
    Entries(
        "fb7a63",
        "3eae25",
        "5adbc3",
        "afd27a",
    ),
)

make_entry(ID("f5e153"),
    SymbolDefinition(PartitionsP, PartitionsP(n), "Integer partition function"),
    Description(PartitionsP(n), "denotes the number of ways the integer", n, "can be written as a sum of positive integers."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(n, ZZ), Element(PartitionsP(n), ZZGreaterEqual(0))),
        Tuple(Element(n, ZZGreaterEqual(0)), Element(PartitionsP(n), ZZGreaterEqual(1))),
      )),
    )

make_entry(ID("3eae25"),
    SymbolDefinition(HardyRamanujanA, HardyRamanujanA(n,k), "Exponential sum in the Hardy-Ramanujan-Rademacher formula"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(1))), Element(HardyRamanujanA(n,k), RR)),
      )),
    )

make_entry(ID("856db2"),
    Description("Table of", PartitionsP(n), "for", LessEqual(0, n, 200)),
    Table(TableRelation(Tuple(n, y), Equal(PartitionsP(n), y)),
      TableHeadings(n, PartitionsP(n)), TableSplit(4),
      List(
Tuple(0, 1), Tuple(1, 1), Tuple(2, 2), Tuple(3, 3), Tuple(4, 5),
Tuple(5, 7), Tuple(6, 11), Tuple(7, 15), Tuple(8, 22), Tuple(9, 30),
Tuple(10, 42), Tuple(11, 56), Tuple(12, 77), Tuple(13, 101), Tuple(14, 135),
Tuple(15, 176), Tuple(16, 231), Tuple(17, 297), Tuple(18, 385), Tuple(19, 490),
Tuple(20, 627), Tuple(21, 792), Tuple(22, 1002), Tuple(23, 1255), Tuple(24, 1575),
Tuple(25, 1958), Tuple(26, 2436), Tuple(27, 3010), Tuple(28, 3718), Tuple(29, 4565),
Tuple(30, 5604), Tuple(31, 6842), Tuple(32, 8349), Tuple(33, 10143), Tuple(34, 12310),
Tuple(35, 14883), Tuple(36, 17977), Tuple(37, 21637), Tuple(38, 26015), Tuple(39, 31185),
Tuple(40, 37338), Tuple(41, 44583), Tuple(42, 53174), Tuple(43, 63261), Tuple(44, 75175),
Tuple(45, 89134), Tuple(46, 105558), Tuple(47, 124754), Tuple(48, 147273), Tuple(49, 173525),
Tuple(50, 204226), Tuple(51, 239943), Tuple(52, 281589), Tuple(53, 329931), Tuple(54, 386155),
Tuple(55, 451276), Tuple(56, 526823), Tuple(57, 614154), Tuple(58, 715220), Tuple(59, 831820),
Tuple(60, 966467), Tuple(61, 1121505), Tuple(62, 1300156), Tuple(63, 1505499), Tuple(64, 1741630),
Tuple(65, 2012558), Tuple(66, 2323520), Tuple(67, 2679689), Tuple(68, 3087735), Tuple(69, 3554345),
Tuple(70, 4087968), Tuple(71, 4697205), Tuple(72, 5392783), Tuple(73, 6185689), Tuple(74, 7089500),
Tuple(75, 8118264), Tuple(76, 9289091), Tuple(77, 10619863), Tuple(78, 12132164), Tuple(79, 13848650),
Tuple(80, 15796476), Tuple(81, 18004327), Tuple(82, 20506255), Tuple(83, 23338469), Tuple(84, 26543660),
Tuple(85, 30167357), Tuple(86, 34262962), Tuple(87, 38887673), Tuple(88, 44108109), Tuple(89, 49995925),
Tuple(90, 56634173), Tuple(91, 64112359), Tuple(92, 72533807), Tuple(93, 82010177), Tuple(94, 92669720),
Tuple(95, 104651419), Tuple(96, 118114304), Tuple(97, 133230930), Tuple(98, 150198136), Tuple(99, 169229875),
Tuple(100, 190569292), Tuple(101, 214481126), Tuple(102, 241265379), Tuple(103, 271248950), Tuple(104, 304801365),
Tuple(105, 342325709), Tuple(106, 384276336), Tuple(107, 431149389), Tuple(108, 483502844), Tuple(109, 541946240),
Tuple(110, 607163746), Tuple(111, 679903203), Tuple(112, 761002156), Tuple(113, 851376628), Tuple(114, 952050665),
Tuple(115, 1064144451), Tuple(116, 1188908248), Tuple(117, 1327710076), Tuple(118, 1482074143), Tuple(119, 1653668665),
Tuple(120, 1844349560), Tuple(121, 2056148051), Tuple(122, 2291320912), Tuple(123, 2552338241), Tuple(124, 2841940500),
Tuple(125, 3163127352), Tuple(126, 3519222692), Tuple(127, 3913864295), Tuple(128, 4351078600), Tuple(129, 4835271870),
Tuple(130, 5371315400), Tuple(131, 5964539504), Tuple(132, 6620830889), Tuple(133, 7346629512), Tuple(134, 8149040695),
Tuple(135, 9035836076), Tuple(136, 10015581680), Tuple(137, 11097645016), Tuple(138, 12292341831), Tuple(139, 13610949895),
Tuple(140, 15065878135), Tuple(141, 16670689208), Tuple(142, 18440293320), Tuple(143, 20390982757), Tuple(144, 22540654445),
Tuple(145, 24908858009), Tuple(146, 27517052599), Tuple(147, 30388671978), Tuple(148, 33549419497), Tuple(149, 37027355200),
Tuple(150, 40853235313), Tuple(151, 45060624582), Tuple(152, 49686288421), Tuple(153, 54770336324), Tuple(154, 60356673280),
Tuple(155, 66493182097), Tuple(156, 73232243759), Tuple(157, 80630964769), Tuple(158, 88751778802), Tuple(159, 97662728555),
Tuple(160, 107438159466), Tuple(161, 118159068427), Tuple(162, 129913904637), Tuple(163, 142798995930), Tuple(164, 156919475295),
Tuple(165, 172389800255), Tuple(166, 189334822579), Tuple(167, 207890420102), Tuple(168, 228204732751), Tuple(169, 250438925115),
Tuple(170, 274768617130), Tuple(171, 301384802048), Tuple(172, 330495499613), Tuple(173, 362326859895), Tuple(174, 397125074750),
Tuple(175, 435157697830), Tuple(176, 476715857290), Tuple(177, 522115831195), Tuple(178, 571701605655), Tuple(179, 625846753120),
Tuple(180, 684957390936), Tuple(181, 749474411781), Tuple(182, 819876908323), Tuple(183, 896684817527), Tuple(184, 980462880430),
Tuple(185, 1071823774337), Tuple(186, 1171432692373), Tuple(187, 1280011042268), Tuple(188, 1398341745571), Tuple(189, 1527273599625),
Tuple(190, 1667727404093), Tuple(191, 1820701100652), Tuple(192, 1987276856363), Tuple(193, 2168627105469), Tuple(194, 2366022741845),
Tuple(195, 2580840212973), Tuple(196, 2814570987591), Tuple(197, 3068829878530), Tuple(198, 3345365983698), Tuple(199, 3646072432125),
Tuple(200, 3972999029388),
    )))

make_entry(ID("9933df"),
    Description("Table of", PartitionsP(10**n), "to 50 digits for", LessEqual(0, n, 30)),
    Table(TableRelation(Tuple(n, y), Equal(NearestDecimal(PartitionsP(10**n), 50), y)),
      TableHeadings(n, PartitionsP(10**n)), TableSplit(1),
      List(
        Tuple(0, Decimal("1")),
        Tuple(1, Decimal("42")),
        Tuple(2, Decimal("190569292")),
        Tuple(3, Decimal("24061467864032622473692149727991")),
        Tuple(4, Decimal("3.6167251325636293988820471890953695495016030339316e+106")),
        Tuple(5, Decimal("2.7493510569775696512677516320986352688173429315980e+346")),
        Tuple(6, Decimal("1.4716849863582233986310047606098959434840304844391e+1107")),
        Tuple(7, Decimal("9.2027175502604546685596278166825605430729405281024e+3514")),
        Tuple(8, Decimal("1.7605170459462491413603738946791352040098537975109e+11131")),
        Tuple(9, Decimal("1.6045350842809668832728039026391874671468439447108e+35218")),
        Tuple(10, Decimal("1.0523943461106485297281294178237273482933553642403e+111390")),
        Tuple(11, Decimal("4.1604280503811938572793734321866528100080985902856e+352268")),
        Tuple(12, Decimal("6.1290009628366844179973253747618396500221302871150e+1113995")),
        Tuple(13, Decimal("5.7144146870758614917950406422638086360770375255550e+3522790")),
        Tuple(14, Decimal("2.7509605970815655120620992887934278296645559629575e+11140071")),
        Tuple(15, Decimal("1.3655377298964220782966300424326842827176530525453e+35228030")),
        Tuple(16, Decimal("9.1291313906814503700935608040674225211147823841734e+111400845")),
        Tuple(17, Decimal("8.2913007910135095775713801190603101231989771169282e+352280441")),
        Tuple(18, Decimal("1.4787003107715742179708592460012268624667759844895e+1114008609")),
        Tuple(19, Decimal("5.6469284039962075996762611156427010823552403269436e+3522804577")),
        Tuple(20, Decimal("1.8381765083448826436460575151963949703661288601871e+11140086259")),
        Tuple(21, Decimal("1.2125743672403400786494500161173864623062685147724e+35228045954")),
        Tuple(22, Decimal("1.6197861609669294695161189248758019106925992523025e+111400862778")),
        Tuple(23, Decimal("2.5273733524499047268270064364643395566828146205663e+352280459735")),
        Tuple(24, Decimal("4.5725915523567534123265286016382336070839930153380e+1114008627985")),
        Tuple(25, Decimal("3.9109259209775087194782941921388925892278301362731e+3522804597566")),
        Tuple(26, Decimal("1.4696356043302577340385578467919062215335762286639e+11140086280078")),
        Tuple(27, Decimal("3.0787999182688279161294058462619983591578972390067e+35228045975896")),
        Tuple(28, Decimal("1.7285510783890260357320054674456196730673005602418e+111400862801021")),
        Tuple(29, Decimal("2.8144933818546523144681227969465158737560857425620e+352280459759213")),
        Tuple(30, Decimal("8.7580564911459301179252748158578897130776558175089e+1114008628010469")))))



make_entry(ID("cebe1b"),
    Formula(Equal(PartitionsP(0), Cardinality(Set(List())), 1)))

make_entry(ID("e84642"),
    Formula(Equal(PartitionsP(1), Cardinality(Set(List(1))), 1)))

make_entry(ID("b2583f"),
    Formula(Equal(PartitionsP(2), Cardinality(Set(List(2), List(1,1))), 2)))

make_entry(ID("7ef291"),
    Formula(Equal(PartitionsP(3), Cardinality(Set(List(3), List(2,1), List(1,1,1))), 3)))

make_entry(ID("6018a4"),
    Formula(Equal(PartitionsP(4), Cardinality(Set(List(4), List(3,1), List(2,2), List(2,1,1), List(1,1,1,1))), 5)))

make_entry(ID("cd3013"),
    Formula(Equal(PartitionsP(-n), 0)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("599417"),
    Formula(Equal(Sum(PartitionsP(n) * q**n, Tuple(n, 0, Infinity)),
        1/EulerQSeries(q))),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("acdce8"),
    Formula(Equal(PartitionsP(n), Sum((-1)**(k+1) * (PartitionsP(n - k*(3*k-1)/2) + PartitionsP(n - k*(3*k+1)/2)), Tuple(k, 1, n+1)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("4d2e45"),
    Formula(Equal(PartitionsP(n), Div(1,n) * Sum(DivisorSigma(n-k) * PartitionsP(k), Tuple(k, 0, n-1)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("d8e37d"),
    Formula(Equal(Mod(PartitionsP(5*n+4), 5), 0)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("89260d"),
    Formula(Equal(Mod(PartitionsP(7*n+5), 7), 0)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("dacd74"),
    Formula(Equal(Mod(PartitionsP(11*n+6), 11), 0)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("f7407a"),
    Formula(LessEqual(PartitionsP(n), PartitionsP(n+1))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("df3c07"),
    Formula(Less(PartitionsP(n), PartitionsP(n+1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("d72123"),
    Formula(GreaterEqual(PartitionsP(n), n)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("e1f15b"),
    Formula(LessEqual(PartitionsP(n), 2**n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("7697af"),
    Formula(AsymptoticTo(PartitionsP(n), Exp(ConstPi*Sqrt(2*n/3)) / (4 * n * Sqrt(3)), n, Infinity)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# todo: fix bessel subscript printing
hrr_term = Div(HardyRamanujanA(n,k), k) * BesselI(Div(3,2), (ConstPi/k) * Sqrt(Div(2,3) * (n - Div(1,24))))

make_entry(ID("fb7a63"),
    Formula(Equal(PartitionsP(n), ((2*ConstPi) / Pow(24*n-1, Div(3,4))) * Sum(hrr_term, Tuple(k, 1, Infinity)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("5adbc3"),
    Formula(Equal(HardyRamanujanA(n,k), Sum(KroneckerDelta(GCD(r,k), 1) * Exp(ConstPi*ConstI*(DedekindSum(r,k) - 2*n*r/k)), Tuple(r, 0, k-1)))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(k, ZZGreaterEqual(1)))))

make_entry(ID("afd27a"),
    Formula(LessEqual(Abs(PartitionsP(n) - ((2*ConstPi) / Pow(24*n-1, Div(3,4))) * Sum(hrr_term, Tuple(k, 1, N))),
        (44*ConstPi**2/(225*Sqrt(3*N))) + (ConstPi * Sqrt(2) / 75) * Sqrt(N / (n - 1)) * Sinh((ConstPi/N) * Sqrt(2*n/3)))),
    Variables(n, N),
    Assumptions(And(Element(n, ZZGreaterEqual(2)), Element(N, ZZGreaterEqual(1)))))

