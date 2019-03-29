from .expr import *

def_Topic(
    Title("Jacobi theta functions"),
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
    )
)

make_entry(ID("ed4ce5"),
    Formula(Equal(JacobiTheta1(z,tau), -ConstI*Sum((-1)**n * Exp(ConstPi*ConstI*((n+Div(1,2))**2*tau + (2*n+1)*z)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("7cb651"),
    Formula(Equal(JacobiTheta2(z,tau), Sum(Exp(ConstPi*ConstI*((n+Div(1,2))**2*tau + (2*n+1)*z)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("580ba0"),
    Formula(Equal(JacobiTheta3(z,tau), Sum(Exp(ConstPi*ConstI*(n**2*tau + 2*n*z)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("27c319"),
    Formula(Equal(JacobiTheta4(z,tau), Sum((-1)**n * Exp(ConstPi*ConstI*(n**2*tau + 2*n*z)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("2ba423"),
    Formula(Equal(JacobiTheta1(z,tau), 2 * Sum((-1)**n * Exp(ConstPi*ConstI*(n+Div(1,2))**2*tau) * Sin((2*n+1)*ConstPi*z), Tuple(n, 0, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("06633e"),
    Formula(Equal(JacobiTheta2(z,tau), 2 * Sum(Exp(ConstPi*ConstI*(n+Div(1,2))**2*tau) * Cos((2*n+1)*ConstPi*z), Tuple(n, 0, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("f3e75c"),
    Formula(Equal(JacobiTheta3(z,tau), 1 + 2 * Sum(Exp(ConstPi*ConstI*n**2*tau) * Cos(2*n*ConstPi*z), Tuple(n, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("8a34d1"),
    Formula(Equal(JacobiTheta4(z,tau), 1 + 2 * Sum((-1)**n * Exp(ConstPi*ConstI*n**2*tau) * Cos(2*n*ConstPi*z), Tuple(n, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))


make_entry(ID("59f8e1"),
    Formula(Equal(JacobiTheta1(-z,tau), -JacobiTheta1(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("fb55cb"),
    Formula(Equal(JacobiTheta2(-z,tau), JacobiTheta2(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("380076"),
    Formula(Equal(JacobiTheta3(-z,tau), JacobiTheta3(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("4f939e"),
    Formula(Equal(JacobiTheta4(-z,tau), JacobiTheta4(z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))


make_entry(ID("154c44"),
    Formula(Equal(Zeros(JacobiTheta1(z,tau), z, CC), SetBuilder(m+n*tau, And(Element(m, ZZ), Element(n, ZZ))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("ad1eaf"),
    Formula(Equal(Zeros(JacobiTheta2(z,tau), z, CC), SetBuilder(Parenthesis(m+Div(1,2))+n*tau, And(Element(m, ZZ), Element(n, ZZ))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("caf10a"),
    Formula(Equal(Zeros(JacobiTheta3(z,tau), z, CC), SetBuilder(Parenthesis(m+Div(1,2))+(n+Div(1,2))*tau, And(Element(m, ZZ), Element(n, ZZ))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("926b2c"),
    Formula(Equal(Zeros(JacobiTheta4(z,tau), z, CC), SetBuilder(m+(n+Div(1,2))*tau, And(Element(m, ZZ), Element(n, ZZ))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))


make_entry(ID("2faeb9"),
    Formula(Equal(JacobiTheta1(z+2*n,tau), JacobiTheta1(z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("b46534"),
    Formula(Equal(JacobiTheta2(z+2*n,tau), JacobiTheta2(z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("e56f77"),
    Formula(Equal(JacobiTheta3(z+2*n,tau), JacobiTheta3(z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("4448f1"),
    Formula(Equal(JacobiTheta4(z+2*n,tau), JacobiTheta3(z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))


make_entry(ID("43fa0e"),
    Formula(Equal(JacobiTheta1(z+(m+n*tau),tau), (-1)**(m+n) * Exp(-(ConstPi*ConstI*(tau*n**2 + 2*n*z))) * JacobiTheta1(z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("d29148"),
    Formula(Equal(JacobiTheta2(z+(m+n*tau),tau), (-1)**m * Exp(-(ConstPi*ConstI*(tau*n**2 + 2*n*z))) * JacobiTheta2(z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("2e4da0"),
    Formula(Equal(JacobiTheta3(z+(m+n*tau),tau), Exp(-(ConstPi*ConstI*(tau*n**2 + 2*n*z))) * JacobiTheta3(z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("8d6a1d"),
    Formula(Equal(JacobiTheta4(z+(m+n*tau),tau), (-1)**n * Exp(-(ConstPi*ConstI*(tau*n**2 + 2*n*z))) * JacobiTheta4(z,tau))),
    Variables(z, tau, m, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(m, ZZ), Element(n, ZZ))))


