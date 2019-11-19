# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Natural logarithm"),
    Section("Definitions"),
    Entries(
        "ed210c",
    ),
    Section("Illustrations"),
    Entries(
        "4fe0ff",
    ),
    Section("Particular values"),
    Entries(
        "07731b",
        "699c83",
        "d496b8",
        "c331da",
        "2f1f7b",
    ),
    Section("Functional equations and connection formulas"),
    Entries(
        "d87f6e",
        "4c1e1e",
        "c43533",
        "f67fa2",
    ),
    Section("Analytic properties"),
    Entries(
        "4538ba",
        "c464e3",
        "ddc8a1",
        "940c48",
        "b5ded1",
        "ed6590",
        "c1bee1",
        "a2189a",
        "cbfd70",
        "1d447b",
    ),
    Section("Complex parts"),
    Entries(
        "13895b",
        "099b19",
        "fbfb81",
        "dcc1e5",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "4986ed",
        "792c76",
        "77aa12",
    ),
    Section("Integral representations"),
    Entries(
        "0ba9b2",
        "c77f9a",
        "e4f73a",
        "a4ac32",
    ),
)

Log_branch_cut = OpenClosedInterval(-Infinity, 0)
Log_holomorphic_domain = SetMinus(CC, Log_branch_cut)

make_entry(ID("ed210c"),
    SymbolDefinition(Log, Log(z), "Natural logarithm"),
    Description("The principal branch of the natural logarithm", Log(z), "is a function of one complex variable", z, ".",),
    Description("It has a branch point singularity at", Equal(z, 0),
        "and a branch cut on", OpenClosedInterval(-Infinity, 0), "where the value on",
            OpenInterval(-Infinity, 0), "is taken to be continuous with the upper half plane."),
    Description("The following table lists all conditions such that", SourceForm(Log(z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, Set(1)), Element(Log(z), Set(0))),
        Tuple(Element(z, OpenInterval(0,Infinity)), Element(Log(z), RR)),
        Tuple(Element(z, SetMinus(CC, Set(0))), Element(Log(z), CC)),
        TableSection("Infinities"),
        Tuple(Element(z, Set(Infinity)), Element(Log(z), Set(Infinity))),
        TableSection("Formal power series"),
        Tuple(And(Element(z, PowerSeries(QQ, x)), Equal(SeriesCoefficient(z, x, 0), 1)),
            And(Element(Log(z), PowerSeries(QQ, x)), Equal(SeriesCoefficient(Log(z), x, 0), 0))),
        Tuple(And(Element(z, PowerSeries(RR, x)), Element(SeriesCoefficient(z, x, 0), OpenInterval(0,Infinity))),
            And(Element(Log(z), PowerSeries(RR, x)))),
        Tuple(And(Element(z, PowerSeries(CC, x)), Unequal(SeriesCoefficient(z, x, 0), 0)),
            And(Element(Log(z), PowerSeries(CC, x)))),
      )))

make_entry(ID("4fe0ff"),
    Image(Description("X-ray of", Log(z), "on", Element(z, ClosedInterval(-3,3) + ClosedInterval(-3,3)*ConstI)),
        ImageSource("xray_log")),
    description_xray,
    )

make_entry(ID("07731b"),
    Formula(Equal(Log(1), 0)))

make_entry(ID("699c83"),
    Formula(Equal(Log(ConstE), 1)))

make_entry(ID("d496b8"),
    Description("Table of", Log(n), "to 50 digits for", LessEqual(1, n, 50)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(Log(n), 50)),
      TableSplit(1),
      List(
    Tuple(1, Decimal("0")),
    Tuple(2, Decimal("0.69314718055994530941723212145817656807550013436026")),
    Tuple(3, Decimal("1.0986122886681096913952452369225257046474905578227")),
    Tuple(4, Decimal("1.3862943611198906188344642429163531361510002687205")),
    Tuple(5, Decimal("1.6094379124341003746007593332261876395256013542685")),
    Tuple(6, Decimal("1.7917594692280550008124773583807022727229906921830")),
    Tuple(7, Decimal("1.9459101490553133051053527434431797296370847295819")),
    Tuple(8, Decimal("2.0794415416798359282516963643745297042265004030808")),
    Tuple(9, Decimal("2.1972245773362193827904904738450514092949811156455")),
    Tuple(10, Decimal("2.3025850929940456840179914546843642076011014886288")),
    Tuple(11, Decimal("2.3978952727983705440619435779651292998217068539374")),
    Tuple(12, Decimal("2.4849066497880003102297094798388788407984908265433")),
    Tuple(13, Decimal("2.5649493574615367360534874415653186048052679447602")),
    Tuple(14, Decimal("2.6390573296152586145225848649013562977125848639421")),
    Tuple(15, Decimal("2.7080502011022100659960045701487133441730919120913")),
    Tuple(16, Decimal("2.7725887222397812376689284858327062723020005374410")),
    Tuple(17, Decimal("2.8332133440562160802495346178731265355882030125857")),
    Tuple(18, Decimal("2.8903717578961646922077225953032279773704812500058")),
    Tuple(19, Decimal("2.9444389791664404600090274318878535372373792612991")),
    Tuple(20, Decimal("2.9957322735539909934352235761425407756766016229890")),
    Tuple(21, Decimal("3.0445224377234229965005979803657054342845752874046")),
    Tuple(22, Decimal("3.0910424533583158534791756994233058678972069882977")),
    Tuple(23, Decimal("3.1354942159291496908067528318101961184423803148404")),
    Tuple(24, Decimal("3.1780538303479456196469416012970554088739909609035")),
    Tuple(25, Decimal("3.2188758248682007492015186664523752790512027085370")),
    Tuple(26, Decimal("3.2580965380214820454707195630234951728807680791205")),
    Tuple(27, Decimal("3.2958368660043290741857357107675771139424716734682")),
    Tuple(28, Decimal("3.3322045101752039239398169863595328657880849983024")),
    Tuple(29, Decimal("3.3672958299864740271832720323619116054945129139227")),
    Tuple(30, Decimal("3.4011973816621553754132366916068899122485920464515")),
    Tuple(31, Decimal("3.4339872044851462459291643245423572104499389304806")),
    Tuple(32, Decimal("3.4657359027997265470861606072908828403775006718013")),
    Tuple(33, Decimal("3.4965075614664802354571888148876550044691974117602")),
    Tuple(34, Decimal("3.5263605246161613896667667393313031036637031469460")),
    Tuple(35, Decimal("3.5553480614894136797061120766693673691626860838504")),
    Tuple(36, Decimal("3.5835189384561100016249547167614045454459813843660")),
    Tuple(37, Decimal("3.6109179126442244443680956710314471639000775871676")),
    Tuple(38, Decimal("3.6375861597263857694262595533460301053128793956594")),
    Tuple(39, Decimal("3.6635616461296464274487326784878443094527585025830")),
    Tuple(40, Decimal("3.6888794541139363028524556976007173437521017573493")),
    Tuple(41, Decimal("3.7135720667043078038667633730374075883764104693993")),
    Tuple(42, Decimal("3.7376696182833683059178301018238820023600754217649")),
    Tuple(43, Decimal("3.7612001156935624234728425133458470355591361848816")),
    Tuple(44, Decimal("3.7841896339182611628964078208814824359727071226579")),
    Tuple(45, Decimal("3.8066624897703197573912498070712390488205824699140")),
    Tuple(46, Decimal("3.8286413964890950002239849532683726865178804492007")),
    Tuple(47, Decimal("3.8501476017100585868209506697721737088960505020202")),
    Tuple(48, Decimal("3.8712010109078909290641737227552319769494910952638")),
    Tuple(49, Decimal("3.8918202981106266102107054868863594592741694591637")),
    Tuple(50, Decimal("3.9120230054281460586187507879105518471267028428973")))))



make_entry(ID("c331da"),
    Formula(Equal(Log(ConstI), Pi*ConstI/2)))

make_entry(ID("2f1f7b"),
    Formula(Equal(Log(-1), Pi*ConstI)))

make_entry(ID("4538ba"),
    Formula(IsHolomorphic(Log(z), ForElement(z, Log_holomorphic_domain))))

make_entry(ID("c464e3"),
    Formula(Equal(Poles(Log(z), ForElement(z, Union(CC, Set(UnsignedInfinity)))), Set())))

make_entry(ID("ddc8a1"),
    Formula(Equal(EssentialSingularities(Log(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("940c48"),
    Formula(Equal(BranchPoints(Log(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity, 0))))

make_entry(ID("b5ded1"),
    Formula(Equal(BranchCuts(Log(z), z, CC), Set(Log_branch_cut))))

make_entry(ID("ed6590"),
    Formula(Equal(AnalyticContinuation(Log(z), For(z, a, b)), Log(-b) + Pi*ConstI)),
    Variables(a,b),
    Assumptions(And(Element(a, CC), Element(b, CC), Greater(Im(a), 0), Less(Im(b), 0), Greater(Re(a)*Im(b)-Re(b)*Im(a), 0))))

make_entry(ID("c1bee1"),
    Formula(Equal(AnalyticContinuation(Log(z), For(z, a, b)), Log(-b) - Pi*ConstI)),
    Variables(a,b),
    Assumptions(And(Element(a, CC), Element(b, CC), Less(Im(a), 0), Greater(Im(b), 0), Less(Re(a)*Im(b)-Re(b)*Im(a), 0))))

make_entry(ID("a2189a"),
    Formula(Equal(AnalyticContinuation(Log(z), For(z, CurvePath(R * Exp(ConstI*t), For(t, 0, theta)))), Log(R) + theta*ConstI)),
    Variables(R, theta),
    Assumptions(And(Element(R, OpenInterval(0, Infinity)), Element(theta, RR))))

make_entry(ID("cbfd70"),
    Formula(Equal(AnalyticContinuation(Log(R * Exp(ConstI*t)), For(t, 0, theta)), Log(R) + theta*ConstI)),
    Variables(R, theta),
    Assumptions(And(Element(R, OpenInterval(0, Infinity)), Element(theta, RR))))

make_entry(ID("1d447b"),
    Formula(Equal(Zeros(Log(z), ForElement(z, CC)), Set(1))))

make_entry(ID("13895b"),
    Formula(Equal(Log(Conjugate(z)), Conjugate(Log(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Log_branch_cut))))

make_entry(ID("099b19"),
    Formula(Equal(Re(Log(z)), Log(Abs(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("fbfb81"),
    Formula(Equal(Im(Log(z)), Arg(z))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("dcc1e5"),
    Formula(Equal(Abs(Log(z)), Sqrt(Log(Abs(z))**2 + Arg(z)**2))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("4986ed"),
    Formula(LessEqual(Log(x), x-1)),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0,Infinity))))

make_entry(ID("792c76"),
    Formula(LessEqual(Abs(Log(z)), Abs(Log(Abs(z))) + Pi)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("d87f6e"),
    Formula(Equal(Exp(Log(z)), z)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("4c1e1e"),
    Formula(Equal(Log(Exp(z)), z)),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(Im(z), OpenClosedInterval(-Pi, Pi)))))

make_entry(ID("c43533"),
    Formula(Equal(Log(z), Log(Abs(z)) + Arg(z)*ConstI)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("f67fa2"),
    Formula(Equal(Log(c*z), Log(c) + Log(z))),
    Variables(c, z),
    Assumptions(And(Element(c, OpenInterval(0, Infinity)), Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("0ba9b2"),
    Formula(Equal(Log(z), Integral(1/t, For(t, 1, z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Log_branch_cut))))

make_entry(ID("77aa12"),
    Formula(LessEqual(Abs(Log(x+a)-Log(x)), Log(1+Abs(a)/(x-Abs(a))))),
    Variables(x, a),
    Assumptions(And(Element(x, RR), Element(a, RR), GreaterEqual(a, 0), Less(Abs(a), x))))

make_entry(ID("c77f9a"),
    Formula(ComplexIndefiniteIntegralEqual(1/z, Log(z), z)),
    Variables(z),
    Assumptions(Element(z, Log_holomorphic_domain)))

make_entry(ID("e4f73a"),
    Formula(ComplexIndefiniteIntegralEqual(1/z, Log(-z), z)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ClosedOpenInterval(0, Infinity)))))

make_entry(ID("a4ac32"),
    Formula(RealIndefiniteIntegralEqual(1/x, Log(Abs(x)), x)),
    Variables(x),
    Assumptions(Element(x, SetMinus(RR, Set(0)))))


