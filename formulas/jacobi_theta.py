from .expr import *

def_Topic(
    Title("Jacobi theta functions"),
    Section("Definitions"),
    Entries(
        "f96eac",
    ),
    Section("Exponential Fourier series"),
    Entries(
        "ed4ce5",
        "7cb651",
        "580ba0",
        "27c319",
    ),
    Section("Trigonometric Fourier series"),
    Entries(
        "2ba423",
        "06633e",
        "f3e75c",
        "8a34d1",
    ),
    Section("Zeros"),
    Entries(
        "154c44",
        "ad1eaf",
        "caf10a",
        "926b2c",
    ),
    Section("Symmetry"),
    Entries(
        "59f8e1",
        "fb55cb",
        "380076",
        "4f939e",
    ),
    Section("Periodicity"),
    Entries(
        "2faeb9",
        "b46534",
        "e56f77",
        "4448f1",
    ),
    Section("Quasi-periodicity"),
    Entries(
        "43fa0e",
        "d29148",
        "2e4da0",
        "8d6a1d",
    ),
    Section("Modular transformations"),
    Entries(
        "c4714a",
        "20172a",
        "9bda2f",
        "03356b",
        "3c56c7",
        "fc3ef5",
        "89e79d",
        "4d8b0f",
    ),
)

# Definitions

make_entry(ID("f96eac"),
    SymbolDefinition(JacobiTheta, JacobiTheta(j,z,tau), "Jacobi theta function"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(j, Set(1,2,3,4)), Element(z, CC), Element(tau, HH)), Element(JacobiTheta(j,z,tau), CC)),
      )),
    )

# Exponential Fourier series

make_entry(ID("ed4ce5"),
    Formula(Equal(JacobiTheta(1,z,tau), -ConstI*Sum((-1)**n * Exp(ConstPi*ConstI*((n+Div(1,2))**2*tau + (2*n+1)*z)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("7cb651"),
    Formula(Equal(JacobiTheta(2,z,tau), Sum(Exp(ConstPi*ConstI*((n+Div(1,2))**2*tau + (2*n+1)*z)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("580ba0"),
    Formula(Equal(JacobiTheta(3,z,tau), Sum(Exp(ConstPi*ConstI*(n**2*tau + 2*n*z)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("27c319"),
    Formula(Equal(JacobiTheta(4,z,tau), Sum((-1)**n * Exp(ConstPi*ConstI*(n**2*tau + 2*n*z)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Trigonometric series

make_entry(ID("2ba423"),
    Formula(Equal(JacobiTheta(1,z,tau), 2 * Sum((-1)**n * Exp(ConstPi*ConstI*(n+Div(1,2))**2*tau) * Sin((2*n+1)*ConstPi*z), Tuple(n, 0, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("06633e"),
    Formula(Equal(JacobiTheta(2,z,tau), 2 * Sum(Exp(ConstPi*ConstI*(n+Div(1,2))**2*tau) * Cos((2*n+1)*ConstPi*z), Tuple(n, 0, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("f3e75c"),
    Formula(Equal(JacobiTheta(3,z,tau), 1 + 2 * Sum(Exp(ConstPi*ConstI*n**2*tau) * Cos(2*n*ConstPi*z), Tuple(n, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("8a34d1"),
    Formula(Equal(JacobiTheta(4,z,tau), 1 + 2 * Sum((-1)**n * Exp(ConstPi*ConstI*n**2*tau) * Cos(2*n*ConstPi*z), Tuple(n, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Symmetry

make_entry(ID("59f8e1"),
    Formula(Equal(JacobiTheta(1,-z,tau), -JacobiTheta(1,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("fb55cb"),
    Formula(Equal(JacobiTheta(2,-z,tau), JacobiTheta(2,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("380076"),
    Formula(Equal(JacobiTheta(3,-z,tau), JacobiTheta(3,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("4f939e"),
    Formula(Equal(JacobiTheta(4,-z,tau), JacobiTheta(4,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Zeros

make_entry(ID("154c44"),
    Formula(Equal(Zeros(JacobiTheta(1,z,tau), z, Element(z, CC)), SetBuilder(m+n*tau, Tuple(m, n), And(Element(m, ZZ), Element(n, ZZ))))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("ad1eaf"),
    Formula(Equal(Zeros(JacobiTheta(2,z,tau), z, Element(z, CC)), SetBuilder(Parentheses(m+Div(1,2))+n*tau, Tuple(m, n), And(Element(m, ZZ), Element(n, ZZ))))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("caf10a"),
    Formula(Equal(Zeros(JacobiTheta(3,z,tau), z, Element(z, CC)), SetBuilder(Parentheses(m+Div(1,2))+(n+Div(1,2))*tau, Tuple(m, n), And(Element(m, ZZ), Element(n, ZZ))))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("926b2c"),
    Formula(Equal(Zeros(JacobiTheta(4,z,tau), z, Element(z, CC)), SetBuilder(m+(n+Div(1,2))*tau, Tuple(m, n), And(Element(m, ZZ), Element(n, ZZ))))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Periodicity

make_entry(ID("2faeb9"),
    Formula(Equal(JacobiTheta(1,z+2*n,tau), JacobiTheta(1,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("b46534"),
    Formula(Equal(JacobiTheta(2,z+2*n,tau), JacobiTheta(2,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("e56f77"),
    Formula(Equal(JacobiTheta(3,z+2*n,tau), JacobiTheta(3,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("4448f1"),
    Formula(Equal(JacobiTheta(4,z+2*n,tau), JacobiTheta(3,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

# Quasi-periodicity

make_entry(ID("43fa0e"),
    Formula(Equal(JacobiTheta(1,z+(m+n*tau),tau), (-1)**(m+n) * Exp(-(ConstPi*ConstI*(tau*n**2 + 2*n*z))) * JacobiTheta(1,z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("d29148"),
    Formula(Equal(JacobiTheta(2,z+(m+n*tau),tau), (-1)**m * Exp(-(ConstPi*ConstI*(tau*n**2 + 2*n*z))) * JacobiTheta(2,z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("2e4da0"),
    Formula(Equal(JacobiTheta(3,z+(m+n*tau),tau), Exp(-(ConstPi*ConstI*(tau*n**2 + 2*n*z))) * JacobiTheta(3,z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("8d6a1d"),
    Formula(Equal(JacobiTheta(4,z+(m+n*tau),tau), (-1)**n * Exp(-(ConstPi*ConstI*(tau*n**2 + 2*n*z))) * JacobiTheta(4,z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(m, ZZ), Element(n, ZZ))))

# Modular transformations

make_entry(ID("c4714a"),
    SymbolDefinition(JacobiThetaEpsilon, JacobiThetaEpsilon(j,a,b,c,d), "Root of unity in modular transformation of Jacobi theta functions"))

make_entry(ID("20172a"),
    SymbolDefinition(JacobiThetaPermutation, JacobiThetaPermutation(j,a,b,c,d), "Index permutation in modular transformation of Jacobi theta functions"))

make_entry(ID("9bda2f"),
    Formula(Equal(JacobiThetaPermutation(j,a,b,c,d),
        Where(Cases(Tuple(1, Equal(j, 1)), Tuple(T(c,d), Equal(j,2)), Tuple(T(a+c,b+d), Equal(j,3)), Tuple(T(a, b), Equal(j, 4))),
            Equal(T(m,n), Cases(
                Tuple(1, CongruentMod(Tuple(m, n), Tuple(0, 0), 2)),
                Tuple(2, CongruentMod(Tuple(m, n), Tuple(0, 1), 2)),
                Tuple(4, CongruentMod(Tuple(m, n), Tuple(1, 0), 2)),
                Tuple(3, CongruentMod(Tuple(m, n), Tuple(1, 1), 2))))))),
    Variables(j,a,b,c,d),
    Assumptions(And(Element(j, Set(1,2,3,4)), Element(Matrix2x2(a, b, c, d), PSL2Z))))

make_entry(ID("03356b"),
    Formula(Equal(JacobiThetaEpsilon(1,a,b,c,d),
        Cases(Tuple(KroneckerSymbol(c,d) * Call(Exp, ((ConstPi*ConstI/4) * Brackets(d*(b-c-1)+2))), Even(c)),
              Tuple(KroneckerSymbol(d,c) * Call(Exp, ((ConstPi*ConstI/4) * Brackets(c*(a+d+1)-3))), Odd(c))))),
    Variables(a,b,c,d),
    Assumptions(Element(Matrix2x2(a,b,c,d), SL2Z)))

make_entry(ID("3c56c7"),
    Formula(Equal(JacobiThetaEpsilon(j,a,b,c,d),
        Where((1/JacobiThetaEpsilon(1,-d,b,c,-a)) *
        Cases(
            Tuple(Call(Exp, ((ConstPi*ConstI/4) * Brackets((c-2)*d - 2 + 2*(1-c)*Subscript(delta, d+1)))), Equal(j, 2)),
            Tuple(Call(Exp, ((ConstPi*ConstI/4) * Brackets((a+c-2)*(b+d) - 3 + 2*(1-a-c)*Subscript(delta, b+d+1)))), Equal(j, 3)),
            Tuple(Call(Exp, ((ConstPi*ConstI/4) * Brackets((a-2)*b - 4 + 2*(1-a)*Subscript(delta, b+1)))), Equal(j, 4))),
            Equal(Subscript(delta, n), Mod(n, 2))))),
    Variables(j,a,b,c,d),
    Assumptions(And(Element(j, Set(2,3,4)), Element(Matrix2x2(a,b,c,d), SL2Z))))

make_entry(ID("fc3ef5"),
    Formula(Equal(JacobiThetaEpsilon(j,a,b,c,d)**4,
        Where((-1)**n, Equal(n,
        Cases(Tuple((a*(b+d) + c*d), Equal(j, 1)),
              Tuple((a*(b+d)), Equal(j, 2)),
              Tuple((a*d), Equal(j, 3)),
              Tuple((d*(a+c)), Equal(j, 4))))))),
    Variables(j,a,b,c,d),
    Assumptions(And(Element(j, Set(1,2,3,4)), Element(Matrix2x2(a,b,c,d), SL2Z))))

make_entry(ID("89e79d"),
    Formula(Equal(JacobiThetaEpsilon(j,a,b,c,d)**8, 1)),
    Variables(j,a,b,c,d),
    Assumptions(And(Element(j, Set(1,2,3,4)), Element(Matrix2x2(a,b,c,d), SL2Z))))

make_entry(ID("4d8b0f"),
    Formula(Equal(JacobiTheta(j,z,(a*tau+b)/(c*tau+d)),
        Where(JacobiThetaEpsilon(j,a,b,c,d) * Sqrt(v/ConstI) * Exp(ConstPi*ConstI*c*v*z**2) * JacobiTheta(JacobiThetaPermutation(j,a,b,c,d), v*z,tau), Equal(v, (c*tau+d)),
        ))),
    Variables(z, tau, a, b, c, d),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(Matrix2x2(a, b, c, d), PSL2Z))))

