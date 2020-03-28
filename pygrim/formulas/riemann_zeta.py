# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Riemann zeta function"),
    Section("Definitions"),
    Entries(
        "e0a6a2",
    ),
    Section("Illustrations"),
    Entries(
        "3131df",
    ),
    Section("Dirichlet series"),
    Entries(
        "da2fdb",   # Dirichlet series
        "1d46d4",
    ),
    Section("Euler product"),
    Entries(
        "8f5e66",  # Euler product
    ),
    Section("Laurent series"),
    Description("Related topic:", TopicReference("Stieltjes constants")),
    Entries(
        "b1a2e1",
    ),
    Section("Special values"),
    Entries(
        "a01b6e",  # zeta(2)
        "e84983",  # zeta(3) irrational
        "72ccda",  # zeta(2n)
        "51fd98",  # zeta(-n)
        "7cb17f",  # table of zeta(2n)
        "e50a56",  # table of zeta(-n)
        "e93ca8",  # table of zeta(n) to 50 digits
    ),
    Section("Analytic properties"),
    Entries(
        "8b5ddb",  # holomorphic domain
        "52c4ab",  # poles
        "fdb94b",  # essential singularities
        "36a095",  # branch points
        "9a258f",  # branch cuts
    ),
    Section("Zeros"),
    SeeTopics("Zeros of the Riemann zeta function"),
    Entries(
        "669509",  # RiemannZetaZero
        "c03de4",  # RiemannHypothesis
        "49704a",  # RH formula
        "2e1ff3",  # real zeros
        "a78abc",  # nontrivial zeros
        "692e42",  # complex zeros
        "cbbf16",  # 0 < re < 1
        "e6ff64",  # re = 1/2
        "60c2ec",  # conjugate symmetry
        "71d9d9",  # table of rho_n to 50 digits
    ),
    Section("Complex parts"),
    Entries(
        "69348a",  # conjugate
    ),
    Section("Functional equation"),
    Entries(
        "9ee8bc",  # functional equation
        "1a63af",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "809bc0",  # bound in right plane
        "3a5eb6",  # bound in critical strip
    ),
    Section("Euler-Maclaurin formula"),
    Entries(
        "792f7b",  # Euler-Maclaurin formula
    ),
    Section("Approximations"),
    Entries(
        "d31b04",  # Euler-Maclaurin formula
        "e37535",  # Borwein
    ),
    #Section("Related topics"),
    #SeeTopics("Gamma function", "Bernoulli number"),
)

def_Topic(
    Title("Zeros of the Riemann zeta function"),
    Entries(
        "e0a6a2",
        "669509",
        "c03de4",
    ),
    Section("Main properties"),
    Description("See also: ", TopicReference("Riemann hypothesis")),
    Entries(
        "9fa2a1",  # RH formula
        "49704a",  # RH
        "2e1ff3",  # real zeros
        "a78abc",  # nontrivial zeros
        "692e42",  # complex zeros
        "cbbf16",  # 0 < re < 1
        "e6ff64",  # re = 1/2
        "60c2ec",  # conjugate symmetry
    ),
    Section("Numerical values"),
    Entries(
        "945fa5",  # rho_1 to 50 digits
        "c0ae99",  # rho_2 to 50 digits
        "71d9d9",  # table of rho_n to 50 digits
        "dc558b",  # table of rho_n to 10 digits
        "2e1cc7"   # table of rho_10^n to 50 digits
    ),
    Section("Related topics"),
    SeeTopics("Riemann zeta function"),
)

make_entry(ID("e0a6a2"),
    SymbolDefinition(RiemannZeta, RiemannZeta(s), "Riemann zeta function"),
    Description("The Riemann zeta function", RiemannZeta(s), "is a function of one complex variable", s,
        ". It is a meromorphic function with a pole at", Equal(s, 1), ".",
        "The following table lists all conditions such that", SourceForm(RiemannZeta(s)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(s, OpenInterval(1, Infinity)), Element(RiemannZeta(s), OpenInterval(1, Infinity))),
        Tuple(Element(s, SetMinus(RR, Set(1))), Element(RiemannZeta(s), RR)),
        Tuple(Element(s, SetMinus(CC, Set(1))), Element(RiemannZeta(s), CC)),
        TableSection("Infinities"),
        Tuple(Element(s, Set(1)), Element(RiemannZeta(s), Set(UnsignedInfinity))),
        Tuple(Element(s, Set(Infinity)), Element(RiemannZeta(s), Set(1))),
        TableSection("Formal power series"),
        Tuple(And(Element(s, PowerSeries(RR, x)), NotEqual(SeriesCoefficient(s, x, 0), 1)),
            Element(RiemannZeta(s), PowerSeries(RR, x))),
        Tuple(And(Element(s, PowerSeries(CC, x)), NotEqual(SeriesCoefficient(s, x, 0), 1)),
            Element(RiemannZeta(s), PowerSeries(CC, x))),
        Tuple(And(Element(s, PowerSeries(RR, x)), NotEqual(s, 1)),
            Element(RiemannZeta(s), LaurentSeries(RR, x))),
        Tuple(And(Element(s, PowerSeries(CC, x)), NotEqual(s, 1)),
            Element(RiemannZeta(s), LaurentSeries(CC, x))),
      )),
    )

make_entry(ID("669509"),
    SymbolDefinition(RiemannZetaZero, RiemannZetaZero(n), "Nontrivial zero of the Riemann zeta function"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(n, SetMinus(ZZ, Set(0))), Element(RiemannZetaZero(n), CC))
    )))

make_entry(ID("3131df"),
    Image(Description("X-ray of", RiemannZeta(s), "on", Element(s, ClosedInterval(-22,22) + ClosedInterval(-27,27)*ConstI), "with the critical strip highlighted"),
        ImageSource("xray_zeta")),
    description_xray,
    )

make_entry(ID("da2fdb"),
    Formula(Equal(RiemannZeta(s), Sum(1/k**s, For(k, 1, Infinity)))),
    Variables(s),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("1d46d4"),
    Formula(Equal(1/RiemannZeta(s), Sum(MoebiusMu(k)/k**s, For(k, 1, Infinity)))),
    Variables(s),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("8f5e66"),
    Formula(Equal(RiemannZeta(s), PrimeProduct(1/(1-1/p**s), For(p)))),
    Variables(s),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("a01b6e"),
    Formula(Equal(RiemannZeta(2), Pi**2 / 6)))

make_entry(ID("e84983"),
    Formula(NotElement(RiemannZeta(3), QQ)),
    References("R. Apéry (1979), Irrationalité de ζ(2) et ζ(3), Astérisque, 61: 11-13."))

make_entry(ID("72ccda"),
    Formula(Equal(RiemannZeta(2*n), (-1)**(n+1) * BernoulliB(2*n) * (2*Pi)**(2*n) / (2 * Factorial(2*n)))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), GreaterEqual(n, 1))))

make_entry(ID("51fd98"),
    Formula(Equal(RiemannZeta(-n), (-1)**n * BernoulliB(n+1) / (n+1))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), GreaterEqual(n, 0))))

make_entry(ID("9ee8bc"),
    Formula(Equal(RiemannZeta(s), 2 * (2*Pi)**(s-1) * Sin(Pi*s/2) * Gamma(1-s) * RiemannZeta(1-s))),
    Variables(s),
    Assumptions(
        And(Element(s, CC), NotElement(s, ZZGreaterEqual(0))),
        And(Element(s, PowerSeries(CC, SerX)), NotElement(s, ZZGreaterEqual(0))),
    ))

make_entry(ID("1a63af"),
    Formula(Equal(RiemannZeta(1-s), (2 * Cos(Div(1,2)*Pi*s)) / (2*Pi)**(s) * Gamma(s) * RiemannZeta(s))),
    Variables(s),
    Assumptions(
        And(Element(s, CC), NotElement(s, ZZLessEqual(1))),
        And(Element(s, PowerSeries(CC, SerX)), NotElement(s, ZZLessEqual(1))),
    ))

make_entry(ID("7cb17f"),
    Description("Table of", RiemannZeta(2*n), "for", LessEqual(1, n, 20)),
    Table(
      Var(n),
      # todo: support writing 2n and still parse table?
      TableValueHeadings(n, RiemannZeta(n)),
      TableSplit(2),
      List(
    Tuple(2, Div(1, 6) * Pi**2),
    Tuple(4, Div(1, 90) * Pi**4),
    Tuple(6, Div(1, 945) * Pi**6),
    Tuple(8, Div(1, 9450) * Pi**8),
    Tuple(10, Div(1, 93555) * Pi**10),
    Tuple(12, Div(691, 638512875) * Pi**12),
    Tuple(14, Div(2, 18243225) * Pi**14),
    Tuple(16, Div(3617, 325641566250) * Pi**16),
    Tuple(18, Div(43867, 38979295480125) * Pi**18),
    Tuple(20, Div(174611, 1531329465290625) * Pi**20),
    Tuple(22, Div(155366, 13447856940643125) * Pi**22),
    Tuple(24, Div(236364091, 201919571963756521875) * Pi**24),
    Tuple(26, Div(1315862, 11094481976030578125) * Pi**26),
    Tuple(28, Div(6785560294, 564653660170076273671875) * Pi**28),
    Tuple(30, Div(6892673020804, 5660878804669082674070015625) * Pi**30),
    Tuple(32, Div(7709321041217, 62490220571022341207266406250) * Pi**32),
    Tuple(34, Div(151628697551, 12130454581433748587292890625) * Pi**34),
    Tuple(36, Div(26315271553053477373, 20777977561866588586487628662044921875) * Pi**36),
    Tuple(38, Div(308420411983322, 2403467618492375776343276883984375) * Pi**38),
    Tuple(40, Div(261082718496449122051, 20080431172289638826798401128390556640625) * Pi**40))))

make_entry(ID("e50a56"),
    Description("Table of", RiemannZeta(-n), "for", LessEqual(0, n, 30)),
    Table(
      Var(n),
      # todo: support writing -n and still parse table?
      TableValueHeadings(n, RiemannZeta(n)),
      TableSplit(3),
      List(
    Tuple(0, -Div(1, 2)),
    Tuple(-1, -Div(1, 12)),
    Tuple(-2, 0),
    Tuple(-3, Div(1, 120)),
    Tuple(-4, 0),
    Tuple(-5, -Div(1, 252)),
    Tuple(-6, 0),
    Tuple(-7, Div(1, 240)),
    Tuple(-8, 0),
    Tuple(-9, -Div(1, 132)),
    Tuple(-10, 0),
    Tuple(-11, Div(691, 32760)),
    Tuple(-12, 0),
    Tuple(-13, -Div(1, 12)),
    Tuple(-14, 0),
    Tuple(-15, Div(3617, 8160)),
    Tuple(-16, 0),
    Tuple(-17, -Div(43867, 14364)),
    Tuple(-18, 0),
    Tuple(-19, Div(174611, 6600)),
    Tuple(-20, 0),
    Tuple(-21, -Div(77683, 276)),
    Tuple(-22, 0),
    Tuple(-23, Div(236364091, 65520)),
    Tuple(-24, 0),
    Tuple(-25, -Div(657931, 12)),
    Tuple(-26, 0),
    Tuple(-27, Div(3392780147, 3480)),
    Tuple(-28, 0),
    Tuple(-29, -Div(1723168255201, 85932)),
    Tuple(-30, 0))))

make_entry(ID("e93ca8"),
    Description("Table of", RiemannZeta(n), "to 50 digits for", LessEqual(2, n, 50)),
    Table(
      Var(n),
      # todo: support writing -n and still parse table?
      TableValueHeadings(n, NearestDecimal(RiemannZeta(n), 50)),
      TableSplit(1),
      List(
    Tuple(2, Decimal("1.6449340668482264364724151666460251892189499012068")),
    Tuple(3, Decimal("1.2020569031595942853997381615114499907649862923405")),
    Tuple(4, Decimal("1.0823232337111381915160036965411679027747509519187")),
    Tuple(5, Decimal("1.0369277551433699263313654864570341680570809195019")),
    Tuple(6, Decimal("1.0173430619844491397145179297909205279018174900329")),
    Tuple(7, Decimal("1.0083492773819228268397975498497967595998635605652")),
    Tuple(8, Decimal("1.0040773561979443393786852385086524652589607906499")),
    Tuple(9, Decimal("1.0020083928260822144178527692324120604856058513949")),
    Tuple(10, Decimal("1.0009945751278180853371459589003190170060195315645")),
    Tuple(11, Decimal("1.0004941886041194645587022825264699364686064357582")),
    Tuple(12, Decimal("1.0002460865533080482986379980477396709604160884580")),
    Tuple(13, Decimal("1.0001227133475784891467518365263573957142751058955")),
    Tuple(14, Decimal("1.0000612481350587048292585451051353337474816961692")),
    Tuple(15, Decimal("1.0000305882363070204935517285106450625876279487069")),
    Tuple(16, Decimal("1.0000152822594086518717325714876367220232373889905")),
    Tuple(17, Decimal("1.0000076371976378997622736002935630292130882490903")),
    Tuple(18, Decimal("1.0000038172932649998398564616446219397304546972190")),
    Tuple(19, Decimal("1.0000019082127165539389256569577951013532585711448")),
    Tuple(20, Decimal("1.0000009539620338727961131520386834493459437941874")),
    Tuple(21, Decimal("1.0000004769329867878064631167196043730459664466948")),
    Tuple(22, Decimal("1.0000002384505027277329900036481867529949350418218")),
    Tuple(23, Decimal("1.0000001192199259653110730677887188823263872549978")),
    Tuple(24, Decimal("1.0000000596081890512594796124402079358012275039188")),
    Tuple(25, Decimal("1.0000000298035035146522801860637050693660118447309")),
    Tuple(26, Decimal("1.0000000149015548283650412346585066306986288647882")),
    Tuple(27, Decimal("1.0000000074507117898354294919810041706041194547190")),
    Tuple(28, Decimal("1.0000000037253340247884570548192040184024232328931")),
    Tuple(29, Decimal("1.0000000018626597235130490064039099454169480616653")),
    Tuple(30, Decimal("1.0000000009313274324196681828717647350212198135680")),
    Tuple(31, Decimal("1.0000000004656629065033784072989233251220071062692")),
    Tuple(32, Decimal("1.0000000002328311833676505492001455975940495024830")),
    Tuple(33, Decimal("1.0000000001164155017270051977592973835456309516522")),
    Tuple(34, Decimal("1.0000000000582077208790270088924368598910630541731")),
    Tuple(35, Decimal("1.0000000000291038504449709968692942522788404641070")),
    Tuple(36, Decimal("1.0000000000145519218910419842359296322453184209838")),
    Tuple(37, Decimal("1.0000000000072759598350574810145208690123380592649")),
    Tuple(38, Decimal("1.0000000000036379795473786511902372363558732735126")),
    Tuple(39, Decimal("1.0000000000018189896503070659475848321007300850306")),
    Tuple(40, Decimal("1.0000000000009094947840263889282533118386949087539")),
    Tuple(41, Decimal("1.0000000000004547473783042154026799112029488570339")),
    Tuple(42, Decimal("1.0000000000002273736845824652515226821577978691214")),
    Tuple(43, Decimal("1.0000000000001136868407680227849349104838025906437")),
    Tuple(44, Decimal("1.0000000000000568434198762758560927718296752406855")),
    Tuple(45, Decimal("1.0000000000000284217097688930185545507370494266207")),
    Tuple(46, Decimal("1.0000000000000142108548280316067698343071417395377")),
    Tuple(47, Decimal("1.0000000000000071054273952108527128773544799568000")),
    Tuple(48, Decimal("1.0000000000000035527136913371136732984695340593430")),
    Tuple(49, Decimal("1.0000000000000017763568435791203274733490144002796")),
    Tuple(50, Decimal("1.0000000000000008881784210930815903096091386391386")))))


make_entry(ID("809bc0"),
    Formula(LessEqual(Abs(RiemannZeta(s)), RiemannZeta(Re(s)))),
    Variables(s),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1))))

make_entry(ID("3a5eb6"),
    Formula(Less(Abs(RiemannZeta(s)), 3 * Abs((1+s)/(1-s)) * Abs((1+s)/(2*Pi))**((1+eta-Re(s))/2) * RiemannZeta(1+eta))),
    Variables(s, eta),
    Assumptions(
        And(Element(s, CC), Element(eta, RR), NotEqual(s, 1), Element(eta, OpenClosedInterval(0, Div(1,2))), LessEqual(-eta, Re(s), 1 + eta))),
    References("H. Rademacher, Topics in analytic number theory, Springer, 1973. Equation 43.3."))

make_entry(ID("792f7b"),
    Formula(Equal(RiemannZeta(s),
        Sum(1/k**s, For(k, 1, N-1)) + N**(1-s)/(s-1) + 1/N**s * (Div(1,2) +
            Sum((BernoulliB(2*k) / Factorial(2*k)) * (RisingFactorial(s, 2*k-1) / N**(2*k-1)), For(k, 1, M))) -
                Integral((BernoulliPolynomial(2*M, t - Floor(t)) / Factorial(2 * M)) * (RisingFactorial(s, 2*M) / t**(s+2*M)), For(t, N, Infinity)))),
    Assumptions(And(Element(s, CC), NotEqual(s, 1), Element(N, ZZ), Element(M, ZZ), Greater(Re(s+2*M-1), 0), GreaterEqual(N, 1), GreaterEqual(M, 1))),
    Variables(s, N, M),
    References("""F. Johansson (2015), Rigorous high-precision computation of the Hurwitz zeta function and its derivatives, Numerical Algorithms 69:253, DOI: 10.1007/s11075-014-9893-1""",
        """F. W. J. Olver, Asymptotics and Special Functions, AK Peters, 1997. Chapter 8."""))

make_entry(ID("d31b04"),
    Formula(LessEqual(Abs(RiemannZeta(s) -
        Parentheses(Sum(1/k**s, For(k, 1, N-1)) + N**(1-s)/(s-1) + 1/N**s * (Div(1,2) +
            Sum((BernoulliB(2*k) / Factorial(2*k)) * (RisingFactorial(s, 2*k-1) / N**(2*k-1)), For(k, 1, M))))),
        (4 * Abs(RisingFactorial(s, 2*M)) / (2*Pi)**(2*M)) * (N**(-Parentheses(Re(s)+2*M-1)) / (Re(s)+2*M-1)))),
    Assumptions(And(Element(s, CC), NotEqual(s, 1), Element(N, ZZ), Element(M, ZZ), Greater(Re(s+2*M-1), 0), GreaterEqual(N, 1), GreaterEqual(M, 1))),
    Variables(s, N, M),
    References("""F. Johansson (2015), Rigorous high-precision computation of the Hurwitz zeta function and its derivatives, Numerical Algorithms 69:253, DOI: 10.1007/s11075-014-9893-1""",
        """F. W. J. Olver, Asymptotics and Special Functions, AK Peters, 1997. Chapter 8."""))

make_entry(ID("e37535"),
    Formula(Where(
        LessEqual(Abs((1-2**(1-s))*RiemannZeta(s) - Div(1,d(n)) * Sum(((-1)**k*(d(n)-d(k)))/(k+1)**s, For(k, 0, n-1))),
            (3*(1 + 2*Abs(Im(s)))/(3+Sqrt(8))**n) * Exp(Abs(Im(s))*Pi/2)),
            Equal(d(k), n*Sum(Factorial(n+i-1)*4**i/(Factorial(n-i)*Factorial(2*i)), For(i, 0, k))))),
    Variables(s, n),
    Assumptions(And(Element(s, CC), GreaterEqual(Re(s), Div(1,2)), NotEqual(s, 1), Element(n, ZZGreaterEqual(1)))),
    References("P. Borwein. An efficient algorithm for the Riemann zeta function. Canadian Mathematical Society Conference Proceedings, vol. 27, pp. 29-34. 2000.")
    )

make_entry(ID("69348a"),
    Formula(Equal(RiemannZeta(Conjugate(s)), Conjugate(RiemannZeta(s)))),
    Variables(s),
    Assumptions(And(Element(s, CC), NotEqual(s, 1))))

make_entry(ID("8b5ddb"),
    Formula(IsHolomorphic(RiemannZeta(s), ForElement(s, SetMinus(CC, Set(1))))))

make_entry(ID("52c4ab"),
    Formula(Equal(Poles(RiemannZeta(s), ForElement(s, Union(CC, Set(UnsignedInfinity)))), Set(1))))

make_entry(ID("fdb94b"),
    Formula(Equal(EssentialSingularities(RiemannZeta(s), s, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("36a095"),
    Formula(Equal(BranchPoints(RiemannZeta(s), s, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("9a258f"),
    Formula(Equal(BranchCuts(RiemannZeta(s), s, Union(CC)), Set())))

make_entry(ID("2e1ff3"),
    Formula(Equal(Zeros(RiemannZeta(s), ForElement(s, RR)), Set(-(2*n), ForElement(n, ZZGreaterEqual(1))))))

make_entry(ID("a78abc"),
    Formula(Equal(Zeros(RiemannZeta(s), ForElement(s, CC), LessEqual(0, Re(s), 1)), Set(RiemannZetaZero(n), For(n), And(Element(n, ZZ), NotEqual(n, 0))))))

make_entry(ID("692e42"),
    Formula(Equal(Zeros(RiemannZeta(s), ForElement(s, CC)), Union(Set(-(2*n), ForElement(n, ZZGreaterEqual(1))),
        Set(RiemannZetaZero(n), For(n), And(Element(n, ZZ), NotEqual(n, 0)))))))

make_entry(ID("cbbf16"),
    Formula(Less(0, Re(RiemannZetaZero(n)), 1)),
    Variables(n),
    Assumptions(And(Element(n, ZZ), NotEqual(n, 0))))

make_entry(ID("60c2ec"),
    Formula(Equal(RiemannZetaZero(-n), Conjugate(RiemannZetaZero(n)))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), NotEqual(n, 0))))

make_entry(ID("e6ff64"),
    Formula(Equal(Re(RiemannZetaZero(n)), Div(1,2))),
    Variables(n),
    Assumptions(And(Element(n, ZZ), NotEqual(n, 0), Or(Less(Abs(n), 103800788359), RiemannHypothesis))),
    References("""D. J. Platt (2016), Isolating some non-trivial zeros of zeta, Mathematics of Computation 86(307):1, DOI: 10.1090/mcom/3198"""))

make_entry(ID("945fa5"),
    Formula(Element(RiemannZetaZero(1),
        Div(1,2) + RealBall(Decimal("14.134725141734693790457251983562470270784257115699"), Decimal("2.44e-49")) * ConstI)))

make_entry(ID("c0ae99"),
    Formula(Element(RiemannZetaZero(2),
        Div(1,2) + RealBall(Decimal("21.022039638771554992628479593896902777334340524903"), Decimal("2.19e-49")) * ConstI)))

make_entry(ID("dc558b"),
    Description("Table of", Im(RiemannZetaZero(n)), "to 10 digits for", LessEqual(1, n, 500)),
    Table(TableRelation(Tuple(n, y), And(Equal(Re(RiemannZetaZero(n)), Div(1,2)), Equal(NearestDecimal(Im(RiemannZetaZero(n)), 10), y))),
      TableHeadings(n, Im(RiemannZetaZero(n))), TableSplit(5),
      List(*(
    Tuple(1, Decimal("14.13472514")),
    Tuple(2, Decimal("21.02203964")),
    Tuple(3, Decimal("25.01085758")),
    Tuple(4, Decimal("30.42487613")),
    Tuple(5, Decimal("32.93506159")),
    Tuple(6, Decimal("37.58617816")),
    Tuple(7, Decimal("40.91871901")),
    Tuple(8, Decimal("43.32707328")),
    Tuple(9, Decimal("48.00515088")),
    Tuple(10, Decimal("49.77383248")),
    Tuple(11, Decimal("52.97032148")),
    Tuple(12, Decimal("56.44624770")),
    Tuple(13, Decimal("59.34704400")),
    Tuple(14, Decimal("60.83177852")),
    Tuple(15, Decimal("65.11254405")),
    Tuple(16, Decimal("67.07981053")),
    Tuple(17, Decimal("69.54640171")),
    Tuple(18, Decimal("72.06715767")),
    Tuple(19, Decimal("75.70469070")),
    Tuple(20, Decimal("77.14484007")),
    Tuple(21, Decimal("79.33737502")),
    Tuple(22, Decimal("82.91038085")),
    Tuple(23, Decimal("84.73549298")),
    Tuple(24, Decimal("87.42527461")),
    Tuple(25, Decimal("88.80911121")),
    Tuple(26, Decimal("92.49189927")),
    Tuple(27, Decimal("94.65134404")),
    Tuple(28, Decimal("95.87063423")),
    Tuple(29, Decimal("98.83119422")),
    Tuple(30, Decimal("101.3178510")),
    Tuple(31, Decimal("103.7255380")),
    Tuple(32, Decimal("105.4466231")),
    Tuple(33, Decimal("107.1686112")),
    Tuple(34, Decimal("111.0295355")),
    Tuple(35, Decimal("111.8746592")),
    Tuple(36, Decimal("114.3202209")),
    Tuple(37, Decimal("116.2266803")),
    Tuple(38, Decimal("118.7907829")),
    Tuple(39, Decimal("121.3701250")),
    Tuple(40, Decimal("122.9468293")),
    Tuple(41, Decimal("124.2568186")),
    Tuple(42, Decimal("127.5166839")),
    Tuple(43, Decimal("129.5787042")),
    Tuple(44, Decimal("131.0876885")),
    Tuple(45, Decimal("133.4977372")),
    Tuple(46, Decimal("134.7565098")),
    Tuple(47, Decimal("138.1160421")),
    Tuple(48, Decimal("139.7362090")),
    Tuple(49, Decimal("141.1237074")),
    Tuple(50, Decimal("143.1118458")),
    Tuple(51, Decimal("146.0009825")),
    Tuple(52, Decimal("147.4227653")),
    Tuple(53, Decimal("150.0535204")),
    Tuple(54, Decimal("150.9252576")),
    Tuple(55, Decimal("153.0246938")),
    Tuple(56, Decimal("156.1129093")),
    Tuple(57, Decimal("157.5975918")),
    Tuple(58, Decimal("158.8499882")),
    Tuple(59, Decimal("161.1889641")),
    Tuple(60, Decimal("163.0307097")),
    Tuple(61, Decimal("165.5370692")),
    Tuple(62, Decimal("167.1844400")),
    Tuple(63, Decimal("169.0945154")),
    Tuple(64, Decimal("169.9119765")),
    Tuple(65, Decimal("173.4115365")),
    Tuple(66, Decimal("174.7541915")),
    Tuple(67, Decimal("176.4414343")),
    Tuple(68, Decimal("178.3774078")),
    Tuple(69, Decimal("179.9164840")),
    Tuple(70, Decimal("182.2070785")),
    Tuple(71, Decimal("184.8744678")),
    Tuple(72, Decimal("185.5987837")),
    Tuple(73, Decimal("187.2289226")),
    Tuple(74, Decimal("189.4161587")),
    Tuple(75, Decimal("192.0266564")),
    Tuple(76, Decimal("193.0797266")),
    Tuple(77, Decimal("195.2653967")),
    Tuple(78, Decimal("196.8764818")),
    Tuple(79, Decimal("198.0153097")),
    Tuple(80, Decimal("201.2647519")),
    Tuple(81, Decimal("202.4935945")),
    Tuple(82, Decimal("204.1896718")),
    Tuple(83, Decimal("205.3946972")),
    Tuple(84, Decimal("207.9062589")),
    Tuple(85, Decimal("209.5765097")),
    Tuple(86, Decimal("211.6908626")),
    Tuple(87, Decimal("213.3479194")),
    Tuple(88, Decimal("214.5470448")),
    Tuple(89, Decimal("216.1695385")),
    Tuple(90, Decimal("219.0675963")),
    Tuple(91, Decimal("220.7149188")),
    Tuple(92, Decimal("221.4307056")),
    Tuple(93, Decimal("224.0070003")),
    Tuple(94, Decimal("224.9833247")),
    Tuple(95, Decimal("227.4214443")),
    Tuple(96, Decimal("229.3374133")),
    Tuple(97, Decimal("231.2501887")),
    Tuple(98, Decimal("231.9872353")),
    Tuple(99, Decimal("233.6934042")),
    Tuple(100, Decimal("236.5242297")),
    Tuple(101, Decimal("237.7698205")),
    Tuple(102, Decimal("239.5554776")),
    Tuple(103, Decimal("241.0491578")),
    Tuple(104, Decimal("242.8232719")),
    Tuple(105, Decimal("244.0708985")),
    Tuple(106, Decimal("247.1369901")),
    Tuple(107, Decimal("248.1019901")),
    Tuple(108, Decimal("249.5736896")),
    Tuple(109, Decimal("251.0149478")),
    Tuple(110, Decimal("253.0699867")),
    Tuple(111, Decimal("255.3062565")),
    Tuple(112, Decimal("256.3807137")),
    Tuple(113, Decimal("258.6104395")),
    Tuple(114, Decimal("259.8744070")),
    Tuple(115, Decimal("260.8050845")),
    Tuple(116, Decimal("263.5738939")),
    Tuple(117, Decimal("265.5578518")),
    Tuple(118, Decimal("266.6149738")),
    Tuple(119, Decimal("267.9219151")),
    Tuple(120, Decimal("269.9704490")),
    Tuple(121, Decimal("271.4940556")),
    Tuple(122, Decimal("273.4596092")),
    Tuple(123, Decimal("275.5874926")),
    Tuple(124, Decimal("276.4520495")),
    Tuple(125, Decimal("278.2507435")),
    Tuple(126, Decimal("279.2292509")),
    Tuple(127, Decimal("282.4651148")),
    Tuple(128, Decimal("283.2111857")),
    Tuple(129, Decimal("284.8359640")),
    Tuple(130, Decimal("286.6674454")),
    Tuple(131, Decimal("287.9119205")),
    Tuple(132, Decimal("289.5798549")),
    Tuple(133, Decimal("291.8462913")),
    Tuple(134, Decimal("293.5584341")),
    Tuple(135, Decimal("294.9653696")),
    Tuple(136, Decimal("295.5732549")),
    Tuple(137, Decimal("297.9792771")),
    Tuple(138, Decimal("299.8403261")),
    Tuple(139, Decimal("301.6493255")),
    Tuple(140, Decimal("302.6967496")),
    Tuple(141, Decimal("304.8643713")),
    Tuple(142, Decimal("305.7289126")),
    Tuple(143, Decimal("307.2194961")),
    Tuple(144, Decimal("310.1094631")),
    Tuple(145, Decimal("311.1651415")),
    Tuple(146, Decimal("312.4278012")),
    Tuple(147, Decimal("313.9852857")),
    Tuple(148, Decimal("315.4756161")),
    Tuple(149, Decimal("317.7348059")),
    Tuple(150, Decimal("318.8531043")),
    Tuple(151, Decimal("321.1601343")),
    Tuple(152, Decimal("322.1445587")),
    Tuple(153, Decimal("323.4669696")),
    Tuple(154, Decimal("324.8628661")),
    Tuple(155, Decimal("327.4439013")),
    Tuple(156, Decimal("329.0330717")),
    Tuple(157, Decimal("329.9532397")),
    Tuple(158, Decimal("331.4744676")),
    Tuple(159, Decimal("333.6453785")),
    Tuple(160, Decimal("334.2113548")),
    Tuple(161, Decimal("336.8418504")),
    Tuple(162, Decimal("338.3399929")),
    Tuple(163, Decimal("339.8582167")),
    Tuple(164, Decimal("341.0422611")),
    Tuple(165, Decimal("342.0548775")),
    Tuple(166, Decimal("344.6617029")),
    Tuple(167, Decimal("346.3478706")),
    Tuple(168, Decimal("347.2726776")),
    Tuple(169, Decimal("349.3162609")),
    Tuple(170, Decimal("350.4084193")),
    Tuple(171, Decimal("351.8786490")),
    Tuple(172, Decimal("353.4889005")),
    Tuple(173, Decimal("356.0175750")),
    Tuple(174, Decimal("357.1513023")),
    Tuple(175, Decimal("357.9526851")),
    Tuple(176, Decimal("359.7437550")),
    Tuple(177, Decimal("361.2893617")),
    Tuple(178, Decimal("363.3313306")),
    Tuple(179, Decimal("364.7360241")),
    Tuple(180, Decimal("366.2127103")),
    Tuple(181, Decimal("367.9935755")),
    Tuple(182, Decimal("368.9684381")),
    Tuple(183, Decimal("370.0509192")),
    Tuple(184, Decimal("373.0619284")),
    Tuple(185, Decimal("373.8648739")),
    Tuple(186, Decimal("375.8259128")),
    Tuple(187, Decimal("376.3240922")),
    Tuple(188, Decimal("378.4366802")),
    Tuple(189, Decimal("379.8729753")),
    Tuple(190, Decimal("381.4844686")),
    Tuple(191, Decimal("383.4435294")),
    Tuple(192, Decimal("384.9561168")),
    Tuple(193, Decimal("385.8613008")),
    Tuple(194, Decimal("387.2228902")),
    Tuple(195, Decimal("388.8461284")),
    Tuple(196, Decimal("391.4560836")),
    Tuple(197, Decimal("392.2450833")),
    Tuple(198, Decimal("393.4277438")),
    Tuple(199, Decimal("395.5828700")),
    Tuple(200, Decimal("396.3818542")),
    Tuple(201, Decimal("397.9187362")),
    Tuple(202, Decimal("399.9851199")),
    Tuple(203, Decimal("401.8392286")),
    Tuple(204, Decimal("402.8619178")),
    Tuple(205, Decimal("404.2364418")),
    Tuple(206, Decimal("405.1343875")),
    Tuple(207, Decimal("407.5814604")),
    Tuple(208, Decimal("408.9472455")),
    Tuple(209, Decimal("410.5138692")),
    Tuple(210, Decimal("411.9722678")),
    Tuple(211, Decimal("413.2627361")),
    Tuple(212, Decimal("415.0188098")),
    Tuple(213, Decimal("415.4552150")),
    Tuple(214, Decimal("418.3877058")),
    Tuple(215, Decimal("419.8613648")),
    Tuple(216, Decimal("420.6438276")),
    Tuple(217, Decimal("422.0767101")),
    Tuple(218, Decimal("423.7165796")),
    Tuple(219, Decimal("425.0698825")),
    Tuple(220, Decimal("427.2088251")),
    Tuple(221, Decimal("428.1279141")),
    Tuple(222, Decimal("430.3287454")),
    Tuple(223, Decimal("431.3013069")),
    Tuple(224, Decimal("432.1386417")),
    Tuple(225, Decimal("433.8892185")),
    Tuple(226, Decimal("436.1610064")),
    Tuple(227, Decimal("437.5816982")),
    Tuple(228, Decimal("438.6217387")),
    Tuple(229, Decimal("439.9184422")),
    Tuple(230, Decimal("441.6831992")),
    Tuple(231, Decimal("442.9045463")),
    Tuple(232, Decimal("444.3193363")),
    Tuple(233, Decimal("446.8606227")),
    Tuple(234, Decimal("447.4417042")),
    Tuple(235, Decimal("449.1485457")),
    Tuple(236, Decimal("450.1269458")),
    Tuple(237, Decimal("451.4033084")),
    Tuple(238, Decimal("453.9867378")),
    Tuple(239, Decimal("454.9746838")),
    Tuple(240, Decimal("456.3284267")),
    Tuple(241, Decimal("457.9038931")),
    Tuple(242, Decimal("459.5134153")),
    Tuple(243, Decimal("460.0879444")),
    Tuple(244, Decimal("462.0653673")),
    Tuple(245, Decimal("464.0572869")),
    Tuple(246, Decimal("465.6715392")),
    Tuple(247, Decimal("466.5702869")),
    Tuple(248, Decimal("467.4390462")),
    Tuple(249, Decimal("469.5360046")),
    Tuple(250, Decimal("470.7736555")),
    Tuple(251, Decimal("472.7991747")),
    Tuple(252, Decimal("473.8352323")),
    Tuple(253, Decimal("475.6003394")),
    Tuple(254, Decimal("476.7690152")),
    Tuple(255, Decimal("478.0752638")),
    Tuple(256, Decimal("478.9421815")),
    Tuple(257, Decimal("481.8303394")),
    Tuple(258, Decimal("482.8347828")),
    Tuple(259, Decimal("483.8514272")),
    Tuple(260, Decimal("485.5391481")),
    Tuple(261, Decimal("486.5287183")),
    Tuple(262, Decimal("488.3805671")),
    Tuple(263, Decimal("489.6617616")),
    Tuple(264, Decimal("491.3988216")),
    Tuple(265, Decimal("493.3144416")),
    Tuple(266, Decimal("493.9579978")),
    Tuple(267, Decimal("495.3588288")),
    Tuple(268, Decimal("496.4296962")),
    Tuple(269, Decimal("498.5807824")),
    Tuple(270, Decimal("500.3090849")),
    Tuple(271, Decimal("501.6044470")),
    Tuple(272, Decimal("502.2762703")),
    Tuple(273, Decimal("504.4997733")),
    Tuple(274, Decimal("505.4152317")),
    Tuple(275, Decimal("506.4641527")),
    Tuple(276, Decimal("508.8007003")),
    Tuple(277, Decimal("510.2642279")),
    Tuple(278, Decimal("511.5622897")),
    Tuple(279, Decimal("512.6231445")),
    Tuple(280, Decimal("513.6689856")),
    Tuple(281, Decimal("515.4350572")),
    Tuple(282, Decimal("517.5896686")),
    Tuple(283, Decimal("518.2342231")),
    Tuple(284, Decimal("520.1063104")),
    Tuple(285, Decimal("521.5251934")),
    Tuple(286, Decimal("522.4566962")),
    Tuple(287, Decimal("523.9605309")),
    Tuple(288, Decimal("525.0773857")),
    Tuple(289, Decimal("527.9036416")),
    Tuple(290, Decimal("528.4062139")),
    Tuple(291, Decimal("529.8062263")),
    Tuple(292, Decimal("530.8669179")),
    Tuple(293, Decimal("532.6881830")),
    Tuple(294, Decimal("533.7796308")),
    Tuple(295, Decimal("535.6643141")),
    Tuple(296, Decimal("537.0697591")),
    Tuple(297, Decimal("538.4285262")),
    Tuple(298, Decimal("540.2131664")),
    Tuple(299, Decimal("540.6313902")),
    Tuple(300, Decimal("541.8474371")),
    Tuple(301, Decimal("544.3238901")),
    Tuple(302, Decimal("545.6368332")),
    Tuple(303, Decimal("547.0109121")),
    Tuple(304, Decimal("547.9316134")),
    Tuple(305, Decimal("549.4975676")),
    Tuple(306, Decimal("550.9700100")),
    Tuple(307, Decimal("552.0495722")),
    Tuple(308, Decimal("553.7649721")),
    Tuple(309, Decimal("555.7920206")),
    Tuple(310, Decimal("556.8994764")),
    Tuple(311, Decimal("557.5646592")),
    Tuple(312, Decimal("559.3162370")),
    Tuple(313, Decimal("560.2408075")),
    Tuple(314, Decimal("562.5592076")),
    Tuple(315, Decimal("564.1608791")),
    Tuple(316, Decimal("564.5060559")),
    Tuple(317, Decimal("566.6987877")),
    Tuple(318, Decimal("567.7317579")),
    Tuple(319, Decimal("568.9239552")),
    Tuple(320, Decimal("570.0511148")),
    Tuple(321, Decimal("572.4199841")),
    Tuple(322, Decimal("573.6146105")),
    Tuple(323, Decimal("575.0938860")),
    Tuple(324, Decimal("575.8072471")),
    Tuple(325, Decimal("577.0390035")),
    Tuple(326, Decimal("579.0988347")),
    Tuple(327, Decimal("580.1369594")),
    Tuple(328, Decimal("581.9465763")),
    Tuple(329, Decimal("583.2360882")),
    Tuple(330, Decimal("584.5617059")),
    Tuple(331, Decimal("585.9845632")),
    Tuple(332, Decimal("586.7427719")),
    Tuple(333, Decimal("588.1396633")),
    Tuple(334, Decimal("590.6603975")),
    Tuple(335, Decimal("591.7258581")),
    Tuple(336, Decimal("592.5713583")),
    Tuple(337, Decimal("593.9747147")),
    Tuple(338, Decimal("595.7281537")),
    Tuple(339, Decimal("596.3627683")),
    Tuple(340, Decimal("598.4930773")),
    Tuple(341, Decimal("599.5456404")),
    Tuple(342, Decimal("601.6021367")),
    Tuple(343, Decimal("602.5791679")),
    Tuple(344, Decimal("603.6256189")),
    Tuple(345, Decimal("604.6162185")),
    Tuple(346, Decimal("606.3834604")),
    Tuple(347, Decimal("608.4132173")),
    Tuple(348, Decimal("609.3895752")),
    Tuple(349, Decimal("610.8391629")),
    Tuple(350, Decimal("611.7742096")),
    Tuple(351, Decimal("613.5997787")),
    Tuple(352, Decimal("614.6462379")),
    Tuple(353, Decimal("615.5385634")),
    Tuple(354, Decimal("618.1128314")),
    Tuple(355, Decimal("619.1844826")),
    Tuple(356, Decimal("620.2728937")),
    Tuple(357, Decimal("621.7092945")),
    Tuple(358, Decimal("622.3750027")),
    Tuple(359, Decimal("624.2699000")),
    Tuple(360, Decimal("626.0192834")),
    Tuple(361, Decimal("627.2683969")),
    Tuple(362, Decimal("628.3258624")),
    Tuple(363, Decimal("630.4738874")),
    Tuple(364, Decimal("630.8057809")),
    Tuple(365, Decimal("632.2251412")),
    Tuple(366, Decimal("633.5468583")),
    Tuple(367, Decimal("635.5238003")),
    Tuple(368, Decimal("637.3971932")),
    Tuple(369, Decimal("637.9255140")),
    Tuple(370, Decimal("638.9279383")),
    Tuple(371, Decimal("640.6947947")),
    Tuple(372, Decimal("641.9454997")),
    Tuple(373, Decimal("643.2788838")),
    Tuple(374, Decimal("644.9905782")),
    Tuple(375, Decimal("646.3481916")),
    Tuple(376, Decimal("647.7617530")),
    Tuple(377, Decimal("648.7864009")),
    Tuple(378, Decimal("650.1975193")),
    Tuple(379, Decimal("650.6686839")),
    Tuple(380, Decimal("653.6495716")),
    Tuple(381, Decimal("654.3019206")),
    Tuple(382, Decimal("655.7094630")),
    Tuple(383, Decimal("656.9640846")),
    Tuple(384, Decimal("658.1756144")),
    Tuple(385, Decimal("659.6638460")),
    Tuple(386, Decimal("660.7167326")),
    Tuple(387, Decimal("662.2965864")),
    Tuple(388, Decimal("664.2446047")),
    Tuple(389, Decimal("665.3427631")),
    Tuple(390, Decimal("666.5151477")),
    Tuple(391, Decimal("667.1484949")),
    Tuple(392, Decimal("668.9758488")),
    Tuple(393, Decimal("670.3235852")),
    Tuple(394, Decimal("672.4581836")),
    Tuple(395, Decimal("673.0435783")),
    Tuple(396, Decimal("674.3558978")),
    Tuple(397, Decimal("676.1396744")),
    Tuple(398, Decimal("677.2301807")),
    Tuple(399, Decimal("677.8004447")),
    Tuple(400, Decimal("679.7421979")),
    Tuple(401, Decimal("681.8949915")),
    Tuple(402, Decimal("682.6027350")),
    Tuple(403, Decimal("684.0135498")),
    Tuple(404, Decimal("684.9726299")),
    Tuple(405, Decimal("686.1632236")),
    Tuple(406, Decimal("687.9615432")),
    Tuple(407, Decimal("689.3689414")),
    Tuple(408, Decimal("690.4747350")),
    Tuple(409, Decimal("692.4516844")),
    Tuple(410, Decimal("693.1769701")),
    Tuple(411, Decimal("694.5339087")),
    Tuple(412, Decimal("695.7263359")),
    Tuple(413, Decimal("696.6260699")),
    Tuple(414, Decimal("699.1320955")),
    Tuple(415, Decimal("700.2967391")),
    Tuple(416, Decimal("701.3017430")),
    Tuple(417, Decimal("702.2273431")),
    Tuple(418, Decimal("704.0338393")),
    Tuple(419, Decimal("705.1258140")),
    Tuple(420, Decimal("706.1846548")),
    Tuple(421, Decimal("708.2690709")),
    Tuple(422, Decimal("709.2295886")),
    Tuple(423, Decimal("711.1302742")),
    Tuple(424, Decimal("711.9002899")),
    Tuple(425, Decimal("712.7493835")),
    Tuple(426, Decimal("714.0827718")),
    Tuple(427, Decimal("716.1123965")),
    Tuple(428, Decimal("717.4825697")),
    Tuple(429, Decimal("718.7427865")),
    Tuple(430, Decimal("719.6971010")),
    Tuple(431, Decimal("721.3511622")),
    Tuple(432, Decimal("722.2775050")),
    Tuple(433, Decimal("723.8458210")),
    Tuple(434, Decimal("724.5626139")),
    Tuple(435, Decimal("727.0564032")),
    Tuple(436, Decimal("728.4054816")),
    Tuple(437, Decimal("728.7587498")),
    Tuple(438, Decimal("730.4164821")),
    Tuple(439, Decimal("731.4173549")),
    Tuple(440, Decimal("732.8180527")),
    Tuple(441, Decimal("734.7896433")),
    Tuple(442, Decimal("735.7654592")),
    Tuple(443, Decimal("737.0529289")),
    Tuple(444, Decimal("738.5804212")),
    Tuple(445, Decimal("739.9095237")),
    Tuple(446, Decimal("740.5738074")),
    Tuple(447, Decimal("741.7573356")),
    Tuple(448, Decimal("743.8950131")),
    Tuple(449, Decimal("745.3449896")),
    Tuple(450, Decimal("746.4993059")),
    Tuple(451, Decimal("747.6745636")),
    Tuple(452, Decimal("748.2427545")),
    Tuple(453, Decimal("750.6559504")),
    Tuple(454, Decimal("750.9663811")),
    Tuple(455, Decimal("752.8876216")),
    Tuple(456, Decimal("754.3223705")),
    Tuple(457, Decimal("755.8393090")),
    Tuple(458, Decimal("756.7682484")),
    Tuple(459, Decimal("758.1017292")),
    Tuple(460, Decimal("758.9002382")),
    Tuple(461, Decimal("760.2823670")),
    Tuple(462, Decimal("762.7000332")),
    Tuple(463, Decimal("763.5930662")),
    Tuple(464, Decimal("764.3075227")),
    Tuple(465, Decimal("766.0875401")),
    Tuple(466, Decimal("767.2184722")),
    Tuple(467, Decimal("768.2814618")),
    Tuple(468, Decimal("769.6934073")),
    Tuple(469, Decimal("771.0708393")),
    Tuple(470, Decimal("772.9616176")),
    Tuple(471, Decimal("774.1177446")),
    Tuple(472, Decimal("775.0478471")),
    Tuple(473, Decimal("775.9997120")),
    Tuple(474, Decimal("777.2997485")),
    Tuple(475, Decimal("779.1570769")),
    Tuple(476, Decimal("780.3489250")),
    Tuple(477, Decimal("782.1376644")),
    Tuple(478, Decimal("782.5979439")),
    Tuple(479, Decimal("784.2888226")),
    Tuple(480, Decimal("785.7390897")),
    Tuple(481, Decimal("786.4611475")),
    Tuple(482, Decimal("787.4684638")),
    Tuple(483, Decimal("790.0590924")),
    Tuple(484, Decimal("790.8316205")),
    Tuple(485, Decimal("792.4277076")),
    Tuple(486, Decimal("792.8886526")),
    Tuple(487, Decimal("794.4837919")),
    Tuple(488, Decimal("795.6065962")),
    Tuple(489, Decimal("797.2634700")),
    Tuple(490, Decimal("798.7075702")),
    Tuple(491, Decimal("799.6543362")),
    Tuple(492, Decimal("801.6042465")),
    Tuple(493, Decimal("802.5419849")),
    Tuple(494, Decimal("803.2430962")),
    Tuple(495, Decimal("804.7622391")),
    Tuple(496, Decimal("805.8616357")),
    Tuple(497, Decimal("808.1518149")),
    Tuple(498, Decimal("809.1977834")),
    Tuple(499, Decimal("810.0818049")),
    Tuple(500, Decimal("811.1843588"))))))


make_entry(ID("2e1cc7"),
    Description("Table of", Im(RiemannZetaZero(10**n)), "to 50 digits for", LessEqual(0, n, 16)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(Im(RiemannZetaZero(10**n)), 50)),
      TableSplit(1),
      List(
      Tuple(0, Decimal("14.134725141734693790457251983562470270784257115699")),
      Tuple(1, Decimal("49.773832477672302181916784678563724057723178299677")),
      Tuple(2, Decimal("236.52422966581620580247550795566297868952949521219")),
      Tuple(3, Decimal("1419.4224809459956864659890380799168192321006010642")),
      Tuple(4, Decimal("9877.7826540055011427740990706901235776224680517811")),
      Tuple(5, Decimal("74920.827498994186793849200946918346620223555216802")),
      Tuple(6, Decimal("600269.67701244495552123391427049074396819125790619")),
      Tuple(7, Decimal("4992381.0140031786660182508391600932712387635814368")),
      Tuple(8, Decimal("42653549.760951553903050309232819667982595130452178")),
      Tuple(9, Decimal("371870203.83702805273405479598662519100082698522485")),
      Tuple(10, Decimal("3293531632.3971367042089917031338769677069644102625")),
      Tuple(11, Decimal("29538618431.613072810689561192671546108506486777642")),
      Tuple(12, Decimal("267653395648.62594824214264940920070899588029633790")),
      Tuple(13, Decimal("2445999556030.2468813938032396773514175248139258741")),
      Tuple(14, Decimal("22514484222485.729124253904444090280880182979014905")),
      Tuple(15, Decimal("208514052006405.46942460229754774510609948399247941")),
      Tuple(16, Decimal("1941393531395154.7112809113883108073327538053720311")))))

make_entry(ID("71d9d9"),
    Description("Table of", Im(RiemannZetaZero(n)), "to 50 digits for", LessEqual(1, n, 50)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(Im(RiemannZetaZero(n)), 50)),
      TableSplit(1),
      List(
    Tuple(1, Decimal("14.134725141734693790457251983562470270784257115699")),
    Tuple(2, Decimal("21.022039638771554992628479593896902777334340524903")),
    Tuple(3, Decimal("25.010857580145688763213790992562821818659549672558")),
    Tuple(4, Decimal("30.424876125859513210311897530584091320181560023715")),
    Tuple(5, Decimal("32.935061587739189690662368964074903488812715603517")),
    Tuple(6, Decimal("37.586178158825671257217763480705332821405597350831")),
    Tuple(7, Decimal("40.918719012147495187398126914633254395726165962777")),
    Tuple(8, Decimal("43.327073280914999519496122165406805782645668371837")),
    Tuple(9, Decimal("48.005150881167159727942472749427516041686844001144")),
    Tuple(10, Decimal("49.773832477672302181916784678563724057723178299677")),
    Tuple(11, Decimal("52.970321477714460644147296608880990063825017888821")),
    Tuple(12, Decimal("56.446247697063394804367759476706127552782264471717")),
    Tuple(13, Decimal("59.347044002602353079653648674992219031098772806467")),
    Tuple(14, Decimal("60.831778524609809844259901824524003802910090451219")),
    Tuple(15, Decimal("65.112544048081606660875054253183705029348149295167")),
    Tuple(16, Decimal("67.079810529494173714478828896522216770107144951746")),
    Tuple(17, Decimal("69.546401711173979252926857526554738443012474209603")),
    Tuple(18, Decimal("72.067157674481907582522107969826168390480906621457")),
    Tuple(19, Decimal("75.704690699083933168326916762030345922811903530697")),
    Tuple(20, Decimal("77.144840068874805372682664856304637015796032449234")),
    Tuple(21, Decimal("79.337375020249367922763592877116228190613246743120")),
    Tuple(22, Decimal("82.910380854086030183164837494770609497508880593782")),
    Tuple(23, Decimal("84.735492980517050105735311206827741417106627934241")),
    Tuple(24, Decimal("87.425274613125229406531667850919213252171886401269")),
    Tuple(25, Decimal("88.809111207634465423682348079509378395444893409819")),
    Tuple(26, Decimal("92.491899270558484296259725241810684878721794027731")),
    Tuple(27, Decimal("94.651344040519886966597925815208153937728027015655")),
    Tuple(28, Decimal("95.870634228245309758741029219246781695256461224988")),
    Tuple(29, Decimal("98.831194218193692233324420138622327820658039063428")),
    Tuple(30, Decimal("101.31785100573139122878544794029230890633286638430")),
    Tuple(31, Decimal("103.72553804047833941639840810869528083448117306950")),
    Tuple(32, Decimal("105.44662305232609449367083241411180899728275392854")),
    Tuple(33, Decimal("107.16861118427640751512335196308619121347670788140")),
    Tuple(34, Decimal("111.02953554316967452465645030994435041534596839007")),
    Tuple(35, Decimal("111.87465917699263708561207871677059496031174987339")),
    Tuple(36, Decimal("114.32022091545271276589093727619107980991765772383")),
    Tuple(37, Decimal("116.22668032085755438216080431206475512732985123238")),
    Tuple(38, Decimal("118.79078286597621732297913970269982434730621059281")),
    Tuple(39, Decimal("121.37012500242064591894553297049992272300131063173")),
    Tuple(40, Decimal("122.94682929355258820081746033077001649621438987386")),
    Tuple(41, Decimal("124.25681855434576718473200796612992444157353877469")),
    Tuple(42, Decimal("127.51668387959649512427932376690607626808830988155")),
    Tuple(43, Decimal("129.57870419995605098576803390617997360864095326466")),
    Tuple(44, Decimal("131.08768853093265672356637246150134905920354750298")),
    Tuple(45, Decimal("133.49773720299758645013049204264060766497417494390")),
    Tuple(46, Decimal("134.75650975337387133132606415716973617839606861365")),
    Tuple(47, Decimal("138.11604205453344320019155519028244785983527462415")),
    Tuple(48, Decimal("139.73620895212138895045004652338246084679005256538")),
    Tuple(49, Decimal("141.12370740402112376194035381847535509030066087975")),
    Tuple(50, Decimal("143.11184580762063273940512386891392996623310243035")))))

def_Topic(
    Title("Riemann hypothesis"),
    Section("Definitions"),
    Entries(
        "c03de4",
    ),
    Section("Formal statement"),
    Description("Related topics:",
        TopicReference("Riemann zeta function"), ",",
        TopicReference("Zeros of the Riemann zeta function"),
    ),
    Entries(
        "9fa2a1",
        "49704a",
    ),
    Section("Statements equivalent to the Riemann hypothesis"),
    Subsection("Prime counting function"),
    Description("Related topic:",
        TopicReference("Prime numbers"),
    ),
    Entries(
        "bfaeb5",
    ),
    Subsection("Robin's criterion"),
    Entries(
        "3142ec",
        "e4287f",
    ),
    Subsection("Li's criterion"),
    Description("Related topic:", TopicReference("Keiper-Li coefficients")),
    Entries(
        "e68f82",
        "a5d65f",
    ),
    Subsection("Landau's function"),
    Description("Related topic:", TopicReference("Landau's function")),
    Entries(
        "65fa9f",  # included from landau's function
    ),
    Subsection("Definite integrals"),
    Entries(
        "7783f9",
        "cf70ce",
    ),
    Subsection("De Bruijn-Newman constant"),
    Entries(
        "22ab47",
        "a71ddd",
    ),
    Section("Formulas conditional on the Riemann hypothesis"),
    Entries(
        "e6ff64",
        "375afe",
    ),
    Section("Generalizations"),
    Description("Related topic:",
        TopicReference("Dirichlet L-functions"),
    ),
    Entries(
        "dc593e",
        "e2a734",
    ),
)

make_entry(ID("c03de4"),
    SymbolDefinition(RiemannHypothesis, RiemannHypothesis, "Riemann hypothesis"),
    Description("Represents the truth value of the Riemann hypothesis, defined in ", EntryReference("49704a"), "."),
    Description("Semantically, ", Element(RiemannHypothesis, Set(True_, False_)), "."),
    Description("This symbol can be used in an assumption to express that a formula is valid conditionally on the truth of the Riemann hypothesis."))

make_entry(ID("9fa2a1"),
    Formula(Equivalent(RiemannHypothesis, All(Equal(Re(s), Div(1,2)), ForElement(s, CC), And(LessEqual(0, Re(s), 1), Equal(RiemannZeta(s), 0))))))

make_entry(ID("49704a"),
    Formula(Equivalent(RiemannHypothesis, All(Equal(Re(RiemannZetaZero(n)), Div(1,2)), ForElement(n, ZZGreaterEqual(1))))))

make_entry(ID("bfaeb5"),
    Formula(Equivalent(RiemannHypothesis, All(Less(Abs(PrimePi(x) - LogIntegral(x)), Sqrt(x) * Log(x)), ForElement(x, ClosedOpenInterval(2, Infinity))))),
    References("https://mathoverflow.net/q/338066"))

make_entry(ID("3142ec"),
    Formula(Equivalent(RiemannHypothesis, All(Less(DivisorSigma(1,n), Exp(ConstGamma) * n*Log(Log(n))), ForElement(n, ZZGreaterEqual(5041))))))

make_entry(ID("e4287f"),
    Formula(Equivalent(RiemannHypothesis, All(Less(DivisorSigma(1,n), HarmonicNumber(n) + Exp(HarmonicNumber(n)) * Log(HarmonicNumber(n))), ForElement(n, ZZGreaterEqual(2))))),
    References("https://doi.org/10.2307/2695443"))

make_entry(ID("22ab47"),
    SymbolDefinition(DeBruijnNewmanLambda, DeBruijnNewmanLambda, "De Bruijn-Newman constant"))

make_entry(ID("a71ddd"),
    Formula(Equivalent(RiemannHypothesis, Equal(DeBruijnNewmanLambda, 0))),
    References("https://arxiv.org/abs/1801.05914"))

make_entry(ID("7783f9"),
    Formula(Equivalent(RiemannHypothesis, Equal(
        (1/Pi) * Integral(Log(Abs(RiemannZeta(Div(1,2)+ConstI*t)/RiemannZeta(Div(1,2)))) * Div(1,t**2), For(t, 0, Infinity)),
        Pi/8 + ConstGamma/4 + Log(8*Pi)/4 - 2))),
    References("https://mathoverflow.net/q/279936"))

make_entry(ID("cf70ce"),
    Formula(Equivalent(RiemannHypothesis, Equal(
        Integral((1-12*t**2)/(1+4*t**2)**3 * Integral(Log(Abs(RiemannZeta(sigma + ConstI*t))), For(sigma, Div(1,2), Infinity)), For(t, 0, Infinity)),
        Pi * (3-ConstGamma) / 32))),
    References("https://doi.org/10.1007/BF01056314"))


def_Topic(
    Title("Keiper-Li coefficients"),
    Section("Definitions"),
    Entries(
        "432bee",
    ),
    Section("Representations"),
    Entries(
        "fcab61",
        "cce75b",
    ),
    Section("Specific values"),
    Entries(
        "081205",
        "d8d820",
        "faf448",
        "706f66",
    ),
    Section("Asymptotics"),
    Entries(
        "64bd32",
    ),
    Section("Riemann hypothesis (Li's criterion)"),
    Entries
    (
        "e68f82",
        "a5d65f",
        "8f8fb7",
    ),
)

make_entry(ID("432bee"),
    SymbolDefinition(KeiperLiLambda, KeiperLiLambda(n), "Keiper-Li coefficient"),
    Description(SourceForm(KeiperLiLambda(n)), ", rendered as", KeiperLiLambda(n),
        ", denotes a power series coefficient associated with the Riemann zeta function. "),
    Description("The definition", EntryReference("fcab61"), "follows Keiper (1992). Li (1997) defines the coefficients with a different scaling factor, equivalent to", n*KeiperLiLambda(n), "in Keiper's (and Fungrim's) notation."),
    References("https://doi.org/10.2307/2153215", "https://doi.org/10.1006/jnth.1997.2137", "https://doi.org/10.7169/facm/1317045228"))

make_entry(ID("fcab61"),
    Formula(Equal(KeiperLiLambda(n), (1/Factorial(n)) * ComplexDerivative(Log(2 * RiemannXi(s/(s-1))), For(s, 0, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# todo: absolute convergence? need to encode order of summation?
make_entry(ID("cce75b"),
    Formula(Equal(KeiperLiLambda(n), (1/n) * Sum(Parentheses(1 - (RiemannZetaZero(k) / (RiemannZetaZero(k) - 1))**n), ForElement(k, ZZ), NotEqual(k, 0)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("081205"),
    Formula(Equal(KeiperLiLambda(0), 0)))

make_entry(ID("d8d820"),
    Formula(Equal(KeiperLiLambda(1), (ConstGamma/2 + 1) - Log(4*Pi)/2)))

make_entry(ID("faf448"),
    Description("Table of", KeiperLiLambda(n), "to 50 digits for", LessEqual(0, n, 30)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(KeiperLiLambda(n), 50)),
      TableSplit(1),
      List(
    Tuple(0, Decimal("0")),
    Tuple(1, Decimal("0.023095708966121033814310247906495291621932127152051")),
    Tuple(2, Decimal("0.046172867614023335192864243096033943387066108314123")),
    Tuple(3, Decimal("0.069212973518108267930497348872601068994212026393200")),
    Tuple(4, Decimal("0.092197619873060409647627872409439018065541673490213")),
    Tuple(5, Decimal("0.11510854289223549048622128109857276671349132303596")),
    Tuple(6, Decimal("0.13792766871372988290416713700341666356138966078654")),
    Tuple(7, Decimal("0.16063715965299421294040287257385366292282442046163")),
    Tuple(8, Decimal("0.18321945964338257908193931774721859848998098273432")),
    Tuple(9, Decimal("0.20565733870917046170289387421343304741236553410044")),
    Tuple(10, Decimal("0.22793393631931577436930340573684453380748385942738")),
    Tuple(11, Decimal("0.25003280347456327821404973571398176484638012641151")),
    Tuple(12, Decimal("0.27193794338538498733992383249265390667786600994911")),
    Tuple(13, Decimal("0.29363385060368815285418215009889439246684857721098")),
    Tuple(14, Decimal("0.31510554847718560800576009263276843951188505373007")),
    Tuple(15, Decimal("0.33633862480178623056900742916909716316435743073656")),
    Tuple(16, Decimal("0.35731926555429953996369166686545971896237127626351")),
    Tuple(17, Decimal("0.37803428659512958242032593887899541131751543174423")),
    Tuple(18, Decimal("0.39847116323842905329183170701797400318996274958010")),
    Tuple(19, Decimal("0.41861805759536317393727500409965507879749928476235")),
    Tuple(20, Decimal("0.43846384360466075647997306767236011141956127351910")),
    Tuple(21, Decimal("0.45799812967347233249339981618322155418048244629837")),
    Tuple(22, Decimal("0.47721127886067612259488922142809435229670372335579")),
    Tuple(23, Decimal("0.49609442654413481917007764284527175942412402470703")),
    Tuple(24, Decimal("0.51463949552297154237641907033478550942000739520745")),
    Tuple(25, Decimal("0.53283920851566303199773431527093937195060386800653")),
    Tuple(26, Decimal("0.55068709802460266427322142354105110711472096137358")),
    Tuple(27, Decimal("0.56817751354772529773768642819955547787404863111699")),
    Tuple(28, Decimal("0.58530562612777004271739082427374534543603950676386")),
    Tuple(29, Decimal("0.60206743023974549532618306036749838157067445931420")),
    Tuple(30, Decimal("0.61845974302711452077115586049317787034309975741269")),
    )))

make_entry(ID("706f66"),
    Description("Table of", KeiperLiLambda(10**n), "to 50 digits for", LessEqual(0, n, 5)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(KeiperLiLambda(10**n), 50)),
      TableSplit(1),
      List(
    Tuple(0, Decimal("0.023095708966121033814310247906495291621932127152051")),
    Tuple(1, Decimal("0.22793393631931577436930340573684453380748385942738")),
    Tuple(2, Decimal("1.1860377537679132992736469839793792693298702359323")),
    Tuple(3, Decimal("2.3260531616864664574065046940832238158044982041693")),
    Tuple(4, Decimal("3.4736579732241613740180609478145593215167373519711")),
    Tuple(5, Decimal("4.6258078240690223140941603808334320467617286152507")),
    )))

make_entry(ID("64bd32"),
    Formula(Implies(RiemannHypothesis, AsymptoticTo(KeiperLiLambda(n), Log(n)/2 - (Log(2*Pi) + 1 - ConstGamma)/2, n, Infinity))),
    References("https://doi.org/10.7169/facm/1317045228"))

make_entry(ID("e68f82"),
    Formula(Equivalent(RiemannHypothesis, All(Greater(KeiperLiLambda(n), 0), ForElement(n, ZZGreaterEqual(1))))),
    References("https://doi.org/10.1006/jnth.1997.2137"))

make_entry(ID("a5d65f"),
    Formula(Equivalent(RiemannHypothesis, Where(Less(Sum(Abs(KeiperLiLambda(n) - a(n))**2, For(n, 1, Infinity)), Infinity),
        Equal(a(n), Log(n)/2 - (Log(2*Pi) + 1 - ConstGamma)/2)))),
    References("https://doi.org/10.7169/facm/1317045228"))

make_entry(ID("8f8fb7"),
    Formula(Implies(
            All(Equal(Re(RiemannZetaZero(n)), Div(1,2)), ForElement(n, ZZGreaterEqual(1)), Less(Im(RiemannZetaZero(n)), T)),
            All(GreaterEqual(KeiperLiLambda(n), 0), ForElement(n, ZZGreaterEqual(0)), LessEqual(n, T**2)))),
    Variables(T),
    Assumptions(Element(T, ClosedOpenInterval(0, Infinity))),
    References("https://arxiv.org/abs/1703.02844"))


def_Topic(
    Title("Stieltjes constants"),
    Section("Definitions"),
    Entries(
        "d10029",
    ),
    Section("Generating functions"),
    Entries(
        "b1a2e1",
        "60c6da",
    ),
    Section("Limit representations"),
    Entries(
        "411f3b",
    ),
    Section("Specific values"),
    Entries(
        "51206a",
        "8ae153",
        "b6808d",
        "70a705",
        "e5bd3c",
        "569d5c",
    ),
    Section("Recurrence relations"),
    Entries(
        "687b4d",
    ),
    Section("Integral representations"),
    Entries(
        "a41c92",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "1dec0d",
    )
)

make_entry(ID("d10029"),
    SymbolDefinition(StieltjesGamma, StieltjesGamma(n, a), "Stieltjes constant"),
    Description(SourceForm(StieltjesGamma(n)), ", rendered as", StieltjesGamma(n), ", represents the Stieltjes constant of index", n, "."),
    Description(SourceForm(StieltjesGamma(n, a)), ", rendered as", StieltjesGamma(n, a), ", represents the generalized Stieltjes constant of index", n, " with parameter", a, "."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(n, ZZGreaterEqual(0)), Element(StieltjesGamma(n), RR)),
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), NotElement(a, ZZLessEqual(0))), Element(StieltjesGamma(n, a), CC)),
    ))
)

# Generating functions

make_entry(ID("b1a2e1"),
    Formula(Equal(RiemannZeta(s), 1/(s-1) + Sum((-1)**n/Factorial(n) * StieltjesGamma(n) * (s-1)**n, For(n, 0, Infinity)))),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("60c6da"),
    Formula(Equal(HurwitzZeta(s, a), 1/(s-1) + Sum((-1)**n/Factorial(n) * StieltjesGamma(n, a) * (s-1)**n, For(n, 0, Infinity)))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Element(a, CC), NotElement(a, ZZLessEqual(0)))))

# Limit representations

make_entry(ID("411f3b"),
    Formula(Equal(StieltjesGamma(n, a), SequenceLimit(Brackets(Parentheses(Sum(Log(k+a)**n / (k+a), For(k, 0, N))) - Log(N+a)**(n+1)/(n+1)), For(N, Infinity)))),
    Variables(n, a),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), NotElement(a, ZZLessEqual(0)))))

# Specific values

make_entry(ID("51206a"),
    Formula(Equal(StieltjesGamma(n, 1), StieltjesGamma(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("8ae153"),
    Formula(Equal(StieltjesGamma(0, 1), StieltjesGamma(0), ConstGamma)))

make_entry(ID("b6808d"),
    Formula(Equal(StieltjesGamma(0, a), -DigammaFunction(a))),
    Variables(a),
    Assumptions(And(Element(a, CC), NotElement(a, ZZLessEqual(0)))))

make_entry(ID("70a705"),
    Formula(Equal(StieltjesGamma(1, Div(1,2)), StieltjesGamma(1) - 2*ConstGamma*Log(2) - Log(2)**2)))

make_entry(ID("e5bd3c"),
    Description("Table of", StieltjesGamma(n), "to 50 digits for", LessEqual(0, n, 30)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(StieltjesGamma(n), 50)),
      TableSplit(1),
      List(
    Tuple(0, Decimal("0.57721566490153286060651209008240243104215933593992")),
    Tuple(1, Decimal("-0.072815845483676724860586375874901319137736338334338")),
    Tuple(2, Decimal("-0.0096903631928723184845303860352125293590658061013407")),
    Tuple(3, Decimal("0.0020538344203033458661600465427533842857158044454106")),
    Tuple(4, Decimal("0.0023253700654673000574681701775260680009044694137849")),
    Tuple(5, Decimal("0.00079332381730106270175333487744444483073153940458489")),
    Tuple(6, Decimal("-0.00023876934543019960987242184190800427778371515635808")),
    Tuple(7, Decimal("-0.00052728956705775104607409750547885828199625347296990")),
    Tuple(8, Decimal("-0.00035212335380303950960205216500120874172918053379235")),
    Tuple(9, Decimal("-3.4394774418088048177914623798227390620789538594442e-5")),
    Tuple(10, Decimal("0.00020533281490906479468372228923706530295985377416676")),
    Tuple(11, Decimal("0.00027018443954390352667290208206795567382784205868840")),
    Tuple(12, Decimal("0.00016727291210514019335350154334118344660780663280557")),
    Tuple(13, Decimal("-2.7463806603760158860007603693355181526785337670396e-5")),
    Tuple(14, Decimal("-0.00020920926205929994583713969734458495783154421150607")),
    Tuple(15, Decimal("-0.00028346865532024144664293447499712697706870298071768")),
    Tuple(16, Decimal("-0.00019969685830896977470778456320324039191576497403406")),
    Tuple(17, Decimal("2.6277037109918336699466597630510122816078692929114e-5")),
    Tuple(18, Decimal("0.00030736840814925282659275475194862564552381129073146")),
    Tuple(19, Decimal("0.00050360545304735562905559643771716003532126980764950")),
    Tuple(20, Decimal("0.00046634356151155944940059482443355052511314347392569")),
    Tuple(21, Decimal("0.00010443776975600011581079567436772049104442825070555")),
    Tuple(22, Decimal("-0.00054159958220399770165519617317410558454386092870075")),
    Tuple(23, Decimal("-0.0012439620904082457792997415995371658091470281139646")),
    Tuple(24, Decimal("-0.0015885112789035615619061966115211158573187228221441")),
    Tuple(25, Decimal("-0.0010745919527384888247242919873531730892739793314532")),
    Tuple(26, Decimal("0.00065680351863715443150477300335621524888606506047754")),
    Tuple(27, Decimal("0.0034778369136185382090073595742588115476629156638859")),
    Tuple(28, Decimal("0.0064000685317006294581072282219458636666371981445885")),
    Tuple(29, Decimal("0.0073711517704722391344124024235594021578413274885128")),
    Tuple(30, Decimal("0.0035577288555731609479135377489084026108096506495221")),
    )))

make_entry(ID("569d5c"),
    Description("Table of", StieltjesGamma(10**n), "to 50 digits for", LessEqual(0, n, 20)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(StieltjesGamma(10**n), 50)),
      TableSplit(1),
      List(
    Tuple(0, Decimal("-0.072815845483676724860586375874901319137736338334338")),
    Tuple(1, Decimal("0.00020533281490906479468372228923706530295985377416676")),
    Tuple(2, Decimal("-425340157170802696.23144385197278358247028931053473")),
    Tuple(3, Decimal("-1.5709538442047449345494023425120825242380299554570e+486")),
    Tuple(4, Decimal("-2.2104970567221060862971082857536501900234397174729e+6883")),
    Tuple(5, Decimal("1.9919273063125410956582272431568589205211659777533e+83432")),
    Tuple(6, Decimal("-4.4209504730980210273285480902514758066667150603243e+947352")),
    Tuple(7, Decimal("-2.7882974834697458134414289662704891120456603986498e+10390401")),
    Tuple(8, Decimal("2.7324629454457814909592178706122081982218137653871e+111591574")),
    Tuple(9, Decimal("2.1048416655418517821363600001419516191053973500980e+1181965380")),
    Tuple(10, Decimal("7.5883621237131051948224033799125486921750410324510e+12397849705")),
    Tuple(11, Decimal("3.4076163168007069203916546697422088077748515862016e+129115149508")),
    Tuple(12, Decimal("-1.1713923594956898094830946178584108308869819425684e+1337330792656")),
    Tuple(13, Decimal("5.1442844004429501778205029347495102582243127602569e+13792544216233")),
    Tuple(14, Decimal("-5.8565687699062182176274937548885177768345135170181e+141762672271719")),
    Tuple(15, Decimal("1.8441017255847322907032695598351364885675746553316e+1452992510427658")),
    Tuple(16, Decimal("1.0887949866822670316936532894122644696901837098117e+14857814744168222")),
    Tuple(17, Decimal("-9.0932573236841531922129808939176217547651121139948e+151633823511792145")),
    Tuple(18, Decimal("2.6314370018873515830151010192294307578971415626833e+1544943249673388947")),
    Tuple(19, Decimal("4.8807917914447513336887536981308809263719031557975e+15718277029330950920")),
    Tuple(20, Decimal("2.3945266166432844875810628102042011083015231233149e+159718433793014252763")),
    )))

# Recurrence relations

make_entry(ID("687b4d"),
    Formula(Equal(StieltjesGamma(n, a+1), StieltjesGamma(n, a) - Log(a)**n / a)),
    Variables(n, a),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), NotElement(a, ZZLessEqual(0)))))

# Integral representations

make_entry(ID("a41c92"),
    Formula(Equal(StieltjesGamma(n, a), -((Pi/(2*(n+1))) * Integral((Log(a-Div(1,2)+ConstI*x)**(n+1) + Log(a-Div(1,2)-ConstI*x)**(n+1))/Cosh(Pi*x)**2, For(x, 0, Infinity))))),
    Variables(n, a),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), Greater(Re(a), Div(1,2)))))

# Bounds and inequalities

make_entry(ID("1dec0d"),
    Formula(Less(Abs(StieltjesGamma(n)), Pow(10,-4) * Exp(n*Log(Log(n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(5))))

