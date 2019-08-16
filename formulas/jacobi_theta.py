from .expr import *

def_Topic(
    Title("Jacobi theta functions"),
    Section("Definitions"),
    Entries(
        "f96eac",
    ),
    Section("Illustrations"),
    Description("Main topic:", TopicReference("Illustrations of Jacobi theta functions")),
    Subsection("Variable argument"),
    Entries(
        "bac5fb",
    ),
    Subsection("Variable lattice parameter"),
    Entries(
        "9522c6",
        "e2035a",
    ),
    Section("Series representations"),
    Subsection("Trigonometric Fourier series"),
    Entries(
        "2ba423",
        "06633e",
        "f3e75c",
        "8a34d1",
    ),
    Subsection("Exponential Fourier series"),
    Entries(
        "700d94",
        "495a98",
        "2f97f5",
        "d923de",
    ),
    Subsection("Pure exponential series"),
    Entries(
        "ed4ce5",
        "7cb651",
        "580ba0",
        "27c319",
    ),
    Section("Zeros"),
    Entries(
        "154c44",
        "ad1eaf",
        "caf10a",
        "926b2c",
    ),
    Section("Argument transformations"),
    Subsection("Symmetry"),
    Entries(
        "59f8e1",
        "fb55cb",
        "380076",
        "4f939e",
    ),
    Subsection("Periodicity"),
    Entries(
        "2faeb9",
        "b46534",
        "e56f77",
        "4448f1",
    ),
    Subsection("Quasi-periodicity"),
    Entries(
        "43fa0e",
        "d29148",
        "2e4da0",
        "8d6a1d",
    ),
    Section("Lattice transformations"),
    Description("Main topic:", TopicReference("Lattice transformations for Jacobi theta functions")),
    Subsection("Modular transformations"),
    Entries(
        "9c1e9a",
        "c4b16c",
        "4d8b0f",
    ),
    Subsection("Multiplication of the lattice parameter"),
    Entries(
        "69b32e",
        "3479be",
        "53fef4",
    ),
)

def_Topic(
    Title("Illustrations of Jacobi theta functions"),
    SeeTopics("Jacobi theta functions"),
    Section("X-ray plots, variable argument"),
    Subsection("Square lattice"),
    Entries(
        "d7a4e5",
        "a75407",
        "bac5fb",
        "8c9f96",
    ),
    Subsection("Rectangular lattice"),
    Entries(
        "56acfe",
        "e47bfb",
        "d98ccc",
        "7902fc",
    ),
    Subsection("Nonrectangular lattice"),
    Entries(
        "c4febd",
        "fa8e96",
        "80f43a",
        "0ce854",
    ),
    Section("X-ray plots, variable lattice parameter"),
    Subsection("Zero argument (theta constants)"),
    Entries(
        "ad8a9a",
        "6636f2",
        "9522c6",
    ),
    Subsection("Nonzero argument"),
    Entries(
        "e2035a",
        "9b868d",
        "c2c002",
        "d3b45d",
    ),
)

def_Topic(
    Title("Lattice transformations for Jacobi theta functions"),
    Description("This topic lists identities for how Jacobi theta functions", JacobiTheta(j,z,tau), "transform when the lattice parameter", tau, " is transformed. ",
        "See the topic", TopicReference("Jacobi theta functions"), "for other properties of these functions."),
    Section("Basic modular transformations"),
    Subsection("Single shift"),
    Entries(
        "6b2078",
        "cde93e",
        "9c1e9a",
        "a5c258",
    ),
    Subsection("Single inversion"),
    Entries(
        "e8ce0b",
        "06319a",
        "c4b16c",
        "ed8ba7",
    ),
    Section("General shifts"),
    Entries(
        "1fa8e7",
        "d0dfba",
        "28b4c3",
        "64f0a5",
        "b978f0",
        "d11b7f",
        "772c88",
        "19acd8",
        "b9c650",
        "4cf228",
        "abc1e7",
        "fb4b1b",
    ),
    Section("Helper functions for general modular transformations"),
    Subsection("Index permutations"),
    Entries(
        "20172a",
        "9bda2f",
    ),
    Subsection("Roots of unity"),
    Entries(
        "c4714a",
        "03356b",
        "3c56c7",
        "fc3ef5",
        "89e79d",
    ),
    Section("General modular transformations"),
    Entries(
        "4d8b0f",
        "100d3c",
    ),
    Section("Half parameter"),
    Subsection("Theta constants"),
    Entries(
        "59fd23",
        "de7918",
        "476642",
        "7527f1",
        "59184e",
    ),
    Subsection("General arguments"),
    Entries(
        "66eb8b",
        "a9cdda",
        "e6d333",
        "69b32e",
        "c92a6f",
        "95e508",
    ),
    Section("Double parameter"),
    Subsection("Theta constants"),
    Entries(
        "9a2054",
        "21c2f7",
        "c3d8c2",
        "f14471",
        "46f244",
    ),
    Subsection("General arguments"),
    Entries(
        "e13fe9",
        "7137a2",
        "db4e29",
        "f12569",
        "3479be",
        "7e0002",
        "0a9ec2",
        "686ce0",
    ),
    Section("Quadruple parameter"),
    Entries(
        "a0a1ee",
        "53fef4",
        "27b169",
        "a255e1",
        "0096a8",
        "fc3c44",
    ),
)


# Illustrations

make_entry(ID("d7a4e5"),
    Image(Description("X-ray of", JacobiTheta(1, z, ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_1_z")),
    description_xray)

make_entry(ID("a75407"),
    Image(Description("X-ray of", JacobiTheta(2, z, ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_2_z")),
    description_xray)

make_entry(ID("bac5fb"),
    Image(Description("X-ray of", JacobiTheta(3, z, ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_3_z")),
    description_xray)

make_entry(ID("8c9f96"),
    Image(Description("X-ray of", JacobiTheta(4, z, ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_4_z")),
    description_xray)

make_entry(ID("56acfe"),
    Image(Description("X-ray of", JacobiTheta(1, z, Div(1,2)*ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_1_z_b")),
    description_xray)

make_entry(ID("e47bfb"),
    Image(Description("X-ray of", JacobiTheta(2, z, Div(1,2)*ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_2_z_b")),
    description_xray)

make_entry(ID("d98ccc"),
    Image(Description("X-ray of", JacobiTheta(3, z, Div(1,2)*ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_3_z_b")),
    description_xray)

make_entry(ID("7902fc"),
    Image(Description("X-ray of", JacobiTheta(4, z, Div(1,2)*ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_4_z_b")),
    description_xray)

make_entry(ID("c4febd"),
    Image(Description("X-ray of", JacobiTheta(1, z, Div(1,4)+Div(3,4)*ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_1_z_c")),
    description_xray)

make_entry(ID("fa8e96"),
    Image(Description("X-ray of", JacobiTheta(2, z, Div(1,4)+Div(3,4)*ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_2_z_c")),
    description_xray)

make_entry(ID("80f43a"),
    Image(Description("X-ray of", JacobiTheta(3, z, Div(1,4)+Div(3,4)*ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_3_z_c")),
    description_xray)

make_entry(ID("0ce854"),
    Image(Description("X-ray of", JacobiTheta(4, z, Div(1,4)+Div(3,4)*ConstI), "on", Element(z, ClosedInterval(-2,2) + ClosedInterval(-2,2)*ConstI)),
        ImageSource("xray_jacobi_theta_4_z_c")),
    description_xray)

make_entry(ID("ad8a9a"),
    Image(Description("X-ray of", JacobiTheta(2, 0, tau), "on", Element(tau, ClosedInterval(-Div(5,2),Div(5,2)) + ClosedInterval(0,2)*ConstI)),
        ImageSource("xray_jacobi_theta_2_tau")),
    description_xray)

make_entry(ID("6636f2"),
    Image(Description("X-ray of", JacobiTheta(3, 0, tau), "on", Element(tau, ClosedInterval(-Div(5,2),Div(5,2)) + ClosedInterval(0,2)*ConstI)),
        ImageSource("xray_jacobi_theta_3_tau")),
    description_xray)

make_entry(ID("9522c6"),
    Image(Description("X-ray of", JacobiTheta(4, 0, tau), "on", Element(tau, ClosedInterval(-Div(5,2),Div(5,2)) + ClosedInterval(0,2)*ConstI)),
        ImageSource("xray_jacobi_theta_4_tau")),
    description_xray)

make_entry(ID("e2035a"),
    Image(Description("X-ray of", JacobiTheta(1, Div(1,3)+Div(3,4)*ConstI, tau), "on", Element(tau, ClosedInterval(-Div(5,2),Div(5,2)) + ClosedInterval(0,2)*ConstI)),
        ImageSource("xray_jacobi_theta_1_tau_b")),
    description_xray)

make_entry(ID("9b868d"),
    Image(Description("X-ray of", JacobiTheta(2, Div(1,3)+Div(3,4)*ConstI, tau), "on", Element(tau, ClosedInterval(-Div(5,2),Div(5,2)) + ClosedInterval(0,2)*ConstI)),
        ImageSource("xray_jacobi_theta_2_tau_b")),
    description_xray)

make_entry(ID("c2c002"),
    Image(Description("X-ray of", JacobiTheta(3, Div(1,3)+Div(3,4)*ConstI, tau), "on", Element(tau, ClosedInterval(-Div(5,2),Div(5,2)) + ClosedInterval(0,2)*ConstI)),
        ImageSource("xray_jacobi_theta_3_tau_b")),
    description_xray)

make_entry(ID("d3b45d"),
    Image(Description("X-ray of", JacobiTheta(4, Div(1,3)+Div(3,4)*ConstI, tau), "on", Element(tau, ClosedInterval(-Div(5,2),Div(5,2)) + ClosedInterval(0,2)*ConstI)),
        ImageSource("xray_jacobi_theta_4_tau_b")),
    description_xray)


# Definitions

make_entry(ID("f96eac"),
    SymbolDefinition(JacobiTheta, JacobiTheta(j,z,tau), "Jacobi theta function"),
    Description(SourceForm(JacobiTheta(j,z,tau)), ", rendered as", JacobiTheta(j,z,tau), ", denotes a Jacobi theta function. ",
        "There are four Jacobi theta functions, identified by the index", Element(j, Set(1,2,3,4)), "."),
    Description("The input", z, "is called the argument and can be any complex number. ",
        "The input", tau, "is called the lattice parameter and must be a complex number with positive imaginary part."),
    Description("Called with four arguments, ", SourceForm(JacobiTheta(j,z,tau,r)), ", rendered as",
        JacobiTheta(j,z,tau,1), ", ",
        JacobiTheta(j,z,tau,2), ", ",
        JacobiTheta(j,z,tau,3), ", ",
        JacobiTheta(j,z,tau,4), " (", LessEqual(1, r, 4), "), or",
        JacobiTheta(j,z,tau,r), ", represents the order", r, "derivative of the Jacobi theta function with respect to the argument", z, "."),
    Description("The Jacobi theta functions are defined by the respective Fourier series (",
        EntryReference("700d94"), ", ",
        EntryReference("495a98"), ", ",
        EntryReference("2f97f5"), ", ",
        EntryReference("d923de"), "). ",
        "It is important to note that Fungrim defines theta functions with a factor", ConstPi, "applied to the argument", z,
        "in the Fourier series, for uniformity with the lattice parameter", tau, ". Many authors omit this scaling factor or replace the input", tau,
        "by", Equal(q, Exp(ConstPi*ConstI*tau)), ". Other conventions exist in the mathematical literature as well, "
        "so care is required when using different reference works."),
    Description("The following table lists conditions such that", SourceForm(JacobiTheta(j,z,tau)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(j, Set(1,2,3,4)), Element(z, CC), Element(tau, HH)), Element(JacobiTheta(j,z,tau), CC)),
        Tuple(And(Element(j, Set(1,2,3,4)), Element(z, CC), Element(tau, HH), Element(r, ZZGreaterEqual(0))), Element(JacobiTheta(j,z,tau,r), CC)),
      )),
    References(
        "https://dlmf.nist.gov/20",
        "http://functions.wolfram.com/EllipticFunctions/EllipticTheta1/introductions/JacobiThetas/")
    )

make_entry(ID("700d94"),
    Formula(Equal(JacobiTheta(1,z,tau), Where(-ConstI * Exp(ConstPi*ConstI*tau/4) * Sum((-1)**n * q**(n*(n+1)) * w**(2*n+1), Tuple(n, -Infinity, Infinity)),
        Equal(q, Exp(ConstPi*ConstI*tau)), Equal(w, Exp(ConstPi*ConstI*z))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("495a98"),
    Formula(Equal(JacobiTheta(2,z,tau), Where(Exp(ConstPi*ConstI*tau/4) * Sum(q**(n*(n+1)) * w**(2*n+1), Tuple(n, -Infinity, Infinity)),
        Equal(q, Exp(ConstPi*ConstI*tau)), Equal(w, Exp(ConstPi*ConstI*z))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("2f97f5"),
    Formula(Equal(JacobiTheta(3,z,tau), Where(Sum(q**(n**2) * w**(2*n), Tuple(n, -Infinity, Infinity)),
        Equal(q, Exp(ConstPi*ConstI*tau)), Equal(w, Exp(ConstPi*ConstI*z))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("d923de"),
    Formula(Equal(JacobiTheta(4,z,tau), Where(Sum((-1)**n * q**(n**2) * w**(2*n), Tuple(n, -Infinity, Infinity)),
        Equal(q, Exp(ConstPi*ConstI*tau)), Equal(w, Exp(ConstPi*ConstI*z))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Pure exponential series

make_entry(ID("ed4ce5"),
    Formula(Equal(JacobiTheta(1,z,tau), Sum(Exp(ConstPi*ConstI*((n+Div(1,2))**2*tau + (2*n+1)*z + n - Div(1,2))), Tuple(n, -Infinity, Infinity)))),
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
    Formula(Equal(JacobiTheta(4,z,tau), Sum(Exp(ConstPi*ConstI*(n**2*tau + 2*n*z + n)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Trigonometric series

make_entry(ID("2ba423"),
    Formula(Equal(JacobiTheta(1,z,tau), Where(2 * Exp(ConstPi*ConstI*tau/4) * Sum((-1)**n * q**(n*(n+1)) * Sin((2*n+1)*ConstPi*z), Tuple(n, 0, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("06633e"),
    Formula(Equal(JacobiTheta(2,z,tau), Where(2 * Exp(ConstPi*ConstI*tau/4) * Sum(q**(n*(n+1)) * Cos((2*n+1)*ConstPi*z), Tuple(n, 0, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("f3e75c"),
    Formula(Equal(JacobiTheta(3,z,tau), Where(1 + 2 * Sum(q**(n**2) * Cos(2*n*ConstPi*z), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("8a34d1"),
    Formula(Equal(JacobiTheta(4,z,tau), Where(1 + 2 * Sum((-1)**n * q**(n**2) * Cos(2*n*ConstPi*z), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
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
    Formula(Equal(JacobiTheta(4,z+2*n,tau), JacobiTheta(4,z,tau))),
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

# Lattice transformations

# Basic modular transformations

# Single shift

make_entry(ID("6b2078"),
    Formula(Equal(JacobiTheta(1,z,tau+1), Exp(ConstPi*ConstI/4) * JacobiTheta(1,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("cde93e"),
    Formula(Equal(JacobiTheta(2,z,tau+1), Exp(ConstPi*ConstI/4) * JacobiTheta(2,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("9c1e9a"),
    Formula(Equal(JacobiTheta(3,z,tau+1), JacobiTheta(4,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("a5c258"),
    Formula(Equal(JacobiTheta(4,z,tau+1), JacobiTheta(3,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Single inversion

make_entry(ID("e8ce0b"),
    Formula(Equal(JacobiTheta(1,z,-1/tau), -ConstI*Sqrt(tau/ConstI)*Exp(ConstPi*ConstI*tau*z**2)*JacobiTheta(1,tau*z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("06319a"),
    Formula(Equal(JacobiTheta(2,z,-1/tau), Sqrt(tau/ConstI)*Exp(ConstPi*ConstI*tau*z**2)*JacobiTheta(4,tau*z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("c4b16c"),
    Formula(Equal(JacobiTheta(3,z,-1/tau), Sqrt(tau/ConstI)*Exp(ConstPi*ConstI*tau*z**2)*JacobiTheta(3,tau*z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("ed8ba7"),
    Formula(Equal(JacobiTheta(4,z,-1/tau), Sqrt(tau/ConstI)*Exp(ConstPi*ConstI*tau*z**2)*JacobiTheta(2,tau*z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# General shifts

make_entry(ID("1fa8e7"),
    Formula(Equal(JacobiTheta(1,z,tau+n), Exp(ConstPi*ConstI*n/4) * JacobiTheta(1, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("d0dfba"),
    Formula(Equal(JacobiTheta(2,z,tau+n), Exp(ConstPi*ConstI*n/4) * JacobiTheta(2, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("28b4c3"),
    Formula(Equal(JacobiTheta(3,z,tau+n), Cases(Tuple(JacobiTheta(3, z, tau), Even(n)), Tuple(JacobiTheta(4, z, tau), Odd(n))))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("64f0a5"),
    Formula(Equal(JacobiTheta(4,z,tau+n), Cases(Tuple(JacobiTheta(4, z, tau), Even(n)), Tuple(JacobiTheta(3, z, tau), Odd(n))))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("b978f0"),
    Formula(Equal(JacobiTheta(1,z,tau+2*n), ConstI**n * JacobiTheta(1, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("d11b7f"),
    Formula(Equal(JacobiTheta(2,z,tau+2*n), ConstI**n * JacobiTheta(2, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("772c88"),
    Formula(Equal(JacobiTheta(3,z,tau+2*n), JacobiTheta(3, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("19acd8"),
    Formula(Equal(JacobiTheta(4,z,tau+2*n), JacobiTheta(4, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("b9c650"),
    Formula(Equal(JacobiTheta(1,z,tau+4*n), (-1)**n * JacobiTheta(1, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("4cf228"),
    Formula(Equal(JacobiTheta(2,z,tau+4*n), (-1)**n * JacobiTheta(2, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("abc1e7"),
    Formula(Equal(JacobiTheta(1,z,tau+8*n), JacobiTheta(1, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("fb4b1b"),
    Formula(Equal(JacobiTheta(2,z,tau+8*n), JacobiTheta(2, z, tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

# Helpers

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
    Assumptions(And(Element(j, Set(1,2,3,4)), Element(Matrix2x2(a, b, c, d), PSL2Z))),
    References("Hans Rademacher (1973), Topics in Analytic Number Theory, Springer. Section 81."))

# General modular transformations

make_entry(ID("c4714a"),
    SymbolDefinition(JacobiThetaEpsilon, JacobiThetaEpsilon(j,a,b,c,d), "Root of unity in modular transformation of Jacobi theta functions"))

make_entry(ID("03356b"),
    Formula(Equal(JacobiThetaEpsilon(1,a,b,c,d),
        Cases(Tuple(KroneckerSymbol(c,d) * Call(Exp, ((ConstPi*ConstI/4) * Brackets(d*(b-c-1)+2))), Even(c)),
              Tuple(KroneckerSymbol(d,c) * Call(Exp, ((ConstPi*ConstI/4) * Brackets(c*(a+d+1)-3))), Odd(c))))),
    Variables(a,b,c,d),
    Assumptions(Element(Matrix2x2(a,b,c,d), SL2Z)),
    References("Hans Rademacher (1973), Topics in Analytic Number Theory, Springer. Section 80."))

make_entry(ID("3c56c7"),
    Formula(Equal(JacobiThetaEpsilon(j,a,b,c,d),
        Where((1/JacobiThetaEpsilon(1,-d,b,c,-a)) *
        Cases(
            Tuple(Call(Exp, ((ConstPi*ConstI/4) * Brackets((c-2)*d - 2 + 2*(1-c)*Subscript(delta, d+1)))), Equal(j, 2)),
            Tuple(Call(Exp, ((ConstPi*ConstI/4) * Brackets((a+c-2)*(b+d) - 3 + 2*(1-a-c)*Subscript(delta, b+d+1)))), Equal(j, 3)),
            Tuple(Call(Exp, ((ConstPi*ConstI/4) * Brackets((a-2)*b - 4 + 2*(1-a)*Subscript(delta, b+1)))), Equal(j, 4))),
            Equal(Subscript(delta, n), Mod(n, 2))))),
    Variables(j,a,b,c,d),
    Assumptions(And(Element(j, Set(2,3,4)), Element(Matrix2x2(a,b,c,d), SL2Z))),
    References("Hans Rademacher (1973), Topics in Analytic Number Theory, Springer. Section 81."))

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
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(Matrix2x2(a, b, c, d), PSL2Z))),
    References("Hans Rademacher (1973), Topics in Analytic Number Theory, Springer. Sections 80, 81."))

make_entry(ID("100d3c"),
    Formula(Equal(JacobiTheta(j,z,tau),
        Where(JacobiThetaEpsilon(j,-d,b,c,-a) * Sqrt(v/ConstI) * Exp(ConstPi*ConstI*c*v*z**2) * JacobiTheta(JacobiThetaPermutation(j,-d,b,c,-a), v*z, (a*tau+b)/(c*tau+d)),
            Equal(v, -(1/(c*tau+d))),
        ))),
    Variables(z, tau, a, b, c, d),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(Matrix2x2(a, b, c, d), PSL2Z))),
    References("Hans Rademacher (1973), Topics in Analytic Number Theory, Springer. Sections 80, 81."))


# Half parameter

# Theta constants

make_entry(ID("59fd23"),
    Formula(Equal(JacobiTheta(2,0,tau/2)**2, 2*JacobiTheta(2,0,tau)*JacobiTheta(3,0,tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("de7918"),
    Formula(Equal(JacobiTheta(3,0,tau/2)**2, JacobiTheta(2,0,tau)**2 + JacobiTheta(3,0,tau)**2)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("476642"),
    Formula(Equal(JacobiTheta(3,0,tau/2) * JacobiTheta(4,0,tau/2), JacobiTheta(4,0,tau)**2)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("7527f1"),
    Formula(Equal(JacobiTheta(4,0,tau/2)**2, JacobiTheta(3,0,tau)**2 - JacobiTheta(2,0,tau)**2)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("59184e"),
    Formula(Equal(JacobiTheta(1,0,tau/2,1) * JacobiTheta(2,0,tau/2), 2 * JacobiTheta(1,0,tau,1) * JacobiTheta(4,0,tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# General arguments

make_entry(ID("66eb8b"),
    Formula(Equal(JacobiTheta(1,z,tau/2), 2*JacobiTheta(1,z,tau)*JacobiTheta(4,z,tau)/JacobiTheta(2,0,tau/2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("a9cdda"),
    Formula(Equal(JacobiTheta(2,z,tau/2), 2*JacobiTheta(2,z,tau)*JacobiTheta(3,z,tau)/JacobiTheta(2,0,tau/2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("e6d333"),
    Formula(Equal(JacobiTheta(3,z,tau/2), (JacobiTheta(4,z,tau)**2-JacobiTheta(1,z,tau)**2)/JacobiTheta(4,0,tau/2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("69b32e"),
    Formula(Equal(JacobiTheta(3,z,tau/2), (JacobiTheta(2,z,tau)**2+JacobiTheta(3,z,tau)**2)/JacobiTheta(3,0,tau/2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("c92a6f"),
    Formula(Equal(JacobiTheta(4,z,tau/2), (JacobiTheta(4,z,tau)**2+JacobiTheta(1,z,tau)**2)/JacobiTheta(3,0,tau/2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("95e508"),
    Formula(Equal(JacobiTheta(4,z,tau/2), (JacobiTheta(3,z,tau)**2-JacobiTheta(2,z,tau)**2)/JacobiTheta(4,0,tau/2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Double parameter

# Theta constants

make_entry(ID("9a2054"),
    Formula(Equal(2*JacobiTheta(2,0,2*tau)*JacobiTheta(3,0,2*tau), JacobiTheta(2,0,tau)**2)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("21c2f7"),
    Formula(Equal(2*JacobiTheta(2,0,2*tau)**2, JacobiTheta(3,0,tau)**2 - JacobiTheta(4,0,tau)**2)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("c3d8c2"),
    Formula(Equal(2*JacobiTheta(3,0,2*tau)**2, JacobiTheta(3,0,tau)**2 + JacobiTheta(4,0,tau)**2)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("f14471"),
    Formula(Equal(JacobiTheta(4,0,2*tau)**2, JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("46f244"),
    Formula(Equal(2*JacobiTheta(1,0,2*tau,1) * JacobiTheta(4,0,2*tau), JacobiTheta(1,0,tau,1) * JacobiTheta(2,0,tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# General arguments

make_entry(ID("e13fe9"),
    Formula(Equal(JacobiTheta(1,2*z,2*tau), JacobiTheta(1,z,tau)*JacobiTheta(2,z,tau)/JacobiTheta(4,0,2*tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("7137a2"),
    Formula(Equal(JacobiTheta(2,2*z,2*tau), (JacobiTheta(2,z,tau)**2-JacobiTheta(1,z,tau)**2)/(2*JacobiTheta(3,0,2*tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("db4e29"),
    Formula(Equal(JacobiTheta(2,2*z,2*tau), (JacobiTheta(3,z,tau)**2-JacobiTheta(4,z,tau)**2)/(2*JacobiTheta(2,0,2*tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("f12569"),
    Formula(Equal(JacobiTheta(2,2*z,2*tau), JacobiTheta(1,Div(1,4)-z,tau)*JacobiTheta(1,Div(1,4)+z,tau)/JacobiTheta(4,0,2*tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("3479be"),
    Formula(Equal(JacobiTheta(3,2*z,2*tau), (JacobiTheta(1,z,tau)**2+JacobiTheta(2,z,tau)**2)/(2*JacobiTheta(2,0,2*tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("7e0002"),
    Formula(Equal(JacobiTheta(3,2*z,2*tau), (JacobiTheta(3,z,tau)**2+JacobiTheta(4,z,tau)**2)/(2*JacobiTheta(3,0,2*tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("0a9ec2"),
    Formula(Equal(JacobiTheta(3,2*z,2*tau), JacobiTheta(3,Div(1,4)-z,tau)*JacobiTheta(3,Div(1,4)+z,tau)/JacobiTheta(4,0,2*tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("686ce0"),
    Formula(Equal(JacobiTheta(4,2*z,2*tau), (JacobiTheta(3,z,tau)*JacobiTheta(4,z,tau))/JacobiTheta(4,0,2*tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Quadruple parameter

make_entry(ID("a0a1ee"),
    Formula(Equal(JacobiTheta(2,2*z,4*tau), (JacobiTheta(3,z,tau) - JacobiTheta(4,z,tau))/2)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("53fef4"),
    Formula(Equal(JacobiTheta(3,2*z,4*tau), (JacobiTheta(3,z,tau) + JacobiTheta(4,z,tau))/2)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("27b169"),
    Formula(Equal(JacobiTheta(1,4*z,4*tau), JacobiTheta(1,z,tau)*JacobiTheta(1,Div(1,4)-z,tau)*JacobiTheta(1,Div(1,4)+z,tau)*JacobiTheta(2,z,tau)/(JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(3,Div(1,4),tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("a255e1"),
    Formula(Equal(JacobiTheta(2,4*z,4*tau), JacobiTheta(2,Div(1,8)-z,tau)*JacobiTheta(2,Div(1,8)+z,tau)*JacobiTheta(2,Div(3,8)-z,tau)*JacobiTheta(2,Div(3,8)+z,tau)/(JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(3,Div(1,4),tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("0096a8"),
    Formula(Equal(JacobiTheta(3,4*z,4*tau), JacobiTheta(3,Div(1,8)-z,tau)*JacobiTheta(3,Div(1,8)+z,tau)*JacobiTheta(3,Div(3,8)-z,tau)*JacobiTheta(3,Div(3,8)+z,tau)/(JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(3,Div(1,4),tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("fc3c44"),
    Formula(Equal(JacobiTheta(4,4*z,4*tau), JacobiTheta(4,z,tau)*JacobiTheta(4,Div(1,4)-z,tau)*JacobiTheta(4,Div(1,4)+z,tau)*JacobiTheta(3,z,tau)/(JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(3,Div(1,4),tau)))),    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

