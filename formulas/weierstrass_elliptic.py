from .expr import *

def_Topic(
    Title("Weierstrass elliptic functions"),
    Entries(
        "f7a534",
        "69be32",
        "5f3210",
    ),
    Section("Complex lattices"),
    Entries(
        "3c1659",
        "d530b1",
    ),
    Section("Series and product representations"),
    Entries(
        "58d67b",
        "b10ca7",
        "7c4457",
    ),
    Section("Derivatives"),
    Entries(
        "e677fb",
        "0e649f",
    ),
    Section("Theta function representations"),
    Entries(
        "af0dfc",
        "0207dc",
        "b96c9d",
    ),
    Section("Symmetries"),
    Entries(
        "12a9e8",
        "72eb69",
        "23beb5",
    ),
    Section("Periodicity"),
    Entries(
        "a95b7e",
        "ffcc0f",
        "a0c85d",
        "35403b",
        "de9f42",
    ),
    Section("Analytic properties"),
    Entries(
        "ae2c5d",
        "6021ba",
        "1da705",
        "c6234b",
        "69eb9b",
        "151e42",
        "881aee",
    ),
)

# todo: should the lattice parameter be tau, the lattice, or either?

make_entry(ID("f7a534"),
    SymbolDefinition(WeierstrassP, WeierstrassP(z,tau), "Weierstrass elliptic function"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(z, SetMinus(CC, Lattice(1, tau))), Element(tau, HH)), Element(WeierstrassP(z,tau), CC)),
        Tuple(And(Element(z, Lattice(1, tau)), Element(tau, HH)), Element(WeierstrassP(z,tau), Set(UnsignedInfinity))),
      )),
    )

make_entry(ID("69be32"),
    SymbolDefinition(WeierstrassZeta, WeierstrassZeta(z,tau), "Weierstrass zeta function"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(z, SetMinus(CC, Lattice(1, tau))), Element(tau, HH)), Element(WeierstrassZeta(z,tau), CC)),
        Tuple(And(Element(z, Lattice(1, tau)), Element(tau, HH)), Element(WeierstrassZeta(z,tau), Set(UnsignedInfinity))),
      )),
    )

make_entry(ID("5f3210"),
    SymbolDefinition(WeierstrassSigma, WeierstrassSigma(z,tau), "Weierstrass sigma function"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(z, CC), Element(tau, HH)), Element(WeierstrassSigma(z,tau), CC)),
      )),
    )

make_entry(ID("3c1659"),
    SymbolDefinition(Lattice, Lattice(a,b), "Complex lattice with periods a, b"))

make_entry(ID("d530b1"),
    Formula(Equal(Lattice(a,b), SetBuilder(a*m+b*n, Tuple(m, n), And(Element(m,ZZ), Element(n,ZZ))))),
    Variables(a,b),
    Assumptions(And(Element(a, SetMinus(CC, Set(0))), Element(b, SetMinus(CC, Set(0))), Greater(Im(b/a), 0))))

make_entry(ID("58d67b"),
    Formula(Equal(WeierstrassP(z,tau), 1/z**2 + SumCondition(1/(z+m+n*tau)**2-1/(m+n*tau)**2, Tuple(m, n), Unequal(m**2+n**2, 0)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("b10ca7"),
    Formula(Equal(WeierstrassZeta(z,tau),
        1/z + SumCondition(1/(z-m-n*tau)+1/(m+n*tau)+z/(m+n*tau)**2, Tuple(m, n), Unequal(m**2+n**2, 0)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("7c4457"),
    Formula(Equal(WeierstrassSigma(z,tau),
        z * ProductCondition((1-z/(m+n*tau)) * Exp(z/(m+n*tau) + z**2/(2*(m+n*tau)**2)), Tuple(m, n), Unequal(m**2+n**2, 0)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))


make_entry(ID("e677fb"),
    Formula(Equal(Derivative(WeierstrassZeta(z,tau), Tuple(z, z, 1)), -WeierstrassP(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("0e649f"),
    Formula(Equal(Derivative(WeierstrassSigma(z,tau), Tuple(z, z, 1)), WeierstrassZeta(z,tau) * WeierstrassSigma(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))


make_entry(ID("af0dfc"),
    Formula(Equal(WeierstrassP(z,tau),
        (ConstPi * JacobiTheta2(0,tau) * JacobiTheta3(0,tau) * Div(JacobiTheta4(z,tau), JacobiTheta1(z,tau)))**2
            - ConstPi**2/3 * (JacobiTheta2(0,tau)**4 + JacobiTheta3(0,tau)**4))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("0207dc"),
    Formula(Equal(WeierstrassZeta(z,tau),
        -Div(z,3) * Div(Derivative(JacobiTheta1(z,tau), Tuple(z, 0, 3)), Derivative(JacobiTheta1(z,tau), Tuple(z, 0, 1)))
            + Div(Derivative(JacobiTheta1(z,tau), Tuple(z, z, 1)), JacobiTheta1(z,tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("b96c9d"),
    Formula(Equal(WeierstrassSigma(z,tau),
        Exp(-Div(z**2,6) * Div(Derivative(JacobiTheta1(z,tau), Tuple(z, 0, 3)), Derivative(JacobiTheta1(z,tau), Tuple(z, 0, 1))))
            * (JacobiTheta1(z,tau) / Derivative(JacobiTheta1(z,tau), Tuple(z, 0, 1))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))


make_entry(ID("12a9e8"),
    Formula(Equal(WeierstrassP(-z,tau), WeierstrassP(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("72eb69"),
    Formula(Equal(WeierstrassZeta(-z,tau), -WeierstrassZeta(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("23beb5"),
    Formula(Equal(WeierstrassSigma(-z,tau), -WeierstrassSigma(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))


make_entry(ID("a95b7e"),
    Formula(Equal(WeierstrassP(z+m+n*tau,tau), WeierstrassP(z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)), Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("ffcc0f"),
    Formula(Equal(WeierstrassZeta(z+1,tau), WeierstrassZeta(z,tau) + WeierstrassZeta(Div(1,2),tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("a0c85d"),
    Formula(Equal(WeierstrassZeta(z+tau,tau), WeierstrassZeta(z,tau) + WeierstrassZeta(Div(tau,2),tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), NotElement(z, Lattice(1, tau)))))

make_entry(ID("35403b"),
    Formula(Equal(WeierstrassSigma(z+1,tau), -(Exp(2*(z+Div(1,2))*WeierstrassZeta(Div(1,2),tau)) * WeierstrassSigma(z,tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("de9f42"),
    Formula(Equal(WeierstrassSigma(z+tau,tau), -(Exp(2*(z+Div(tau,2))*WeierstrassZeta(Div(tau,2),tau)) * WeierstrassSigma(z,tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))



make_entry(ID("ae2c5d"),
    Formula(Equal(Poles(WeierstrassP(z,tau),z,CC), Lattice(1, tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("6021ba"),
    Formula(Equal(Poles(WeierstrassZeta(z,tau),z,CC), Lattice(1, tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("1da705"),
    Formula(Equal(Zeros(WeierstrassSigma(z,tau),z,Element(z, CC)), Lattice(1, tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("c6234b"),
    Formula(Equal(Zeros(WeierstrassP(z,ConstI),z,Element(z, CC)), SetBuilder(Parentheses(m+Div(1,2))+(n+Div(1,2))*ConstI, Tuple(m, n), And(Element(m, ZZ), Element(n, ZZ))))))

make_entry(ID("69eb9b"),
    Formula(Equal(HolomorphicDomain(WeierstrassP(z,tau),z,CC), SetMinus(CC, Lattice(1, tau)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("151e42"),
    Formula(Equal(HolomorphicDomain(WeierstrassZeta(z,tau),z,CC), SetMinus(CC, Lattice(1, tau)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("881aee"),
    Formula(Equal(HolomorphicDomain(WeierstrassSigma(z,tau),z,CC), CC)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

