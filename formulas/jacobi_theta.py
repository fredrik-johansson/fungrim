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
        "e2035a",
    ),
    Section("Series and product representations"),
    Description("Main topic:", TopicReference("Series and product representations of Jacobi theta functions")),
    Subsection("Trigonometric Fourier series"),
    Entries(
        "2ba423",
        "06633e",
        "f3e75c",
        "8a34d1",
    ),
    Subsection("Jacobi triple product"),
    Entries(
        "13d2a1",
    ),
    Section("Zeros"),
    Entries(
        "154c44",
        "ad1eaf",
        "caf10a",
        "926b2c",
    ),
    Section("Specific values"),
    Description("Main topic:", TopicReference("Specific values of Jacobi theta functions")),
    Entries(
        "d15f11",
    ),
    Section("Argument transformations"),
    Description("Main topic:", TopicReference("Argument transformations for Jacobi theta functions")),
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
    Section("Sums and products"),
    Subsection("Fourth powers"),
    Entries(
        "1fbc09",
        "08822c",
        "5a3ebf",
        "e08bb4",
    ),
    Subsection("Sums of squares"),
    Entries(
        "fa7251",
        "265d9c",
        "0e2635",
        "6fad93",
        "abbe42",
        "1c67c8",
    ),
    Section("Differential equations"),
    Description("Main topic:", TopicReference("Differential equations for Jacobi theta functions")),
    Subsection("Notation and conversion to argument derivatives"),
    Entries(
        "a222ed",
        "37e644",
    ),
    Subsection("Heat equation"),
    Entries(
        "ebc673",
    ),
    Subsection("Jacobi's differential equation"),
    Entries(
        "936694",
    ),
    Subsection("Derivatives of ratios"),
    Entries(
        "cb493d",
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
    Title("Series and product representations of Jacobi theta functions"),
    Description("See", TopicReference("Jacobi theta functions"), "for an introduction to these functions."),
    Section("Fourier series"),
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
    Section("Fourier series for derivatives"),
    Subsection("Exponential Fourier series"),
    Entries(
        "2ae142",
        "42d832",
        "f551ca",
        "1842d9",
    ),
    Section("Infinite products"),
    Subsection("Infinite q-products with trigonometric factors"),
    Entries(
        "024a84",
        "d6a799",
        "77aed2",
        "2a2a38",
    ),
    Subsection("Infinite q-products with exponential factors"),
    Entries(
        "39b699",
        "465810",
        "21851b",
        "d45548",
    ),
    Subsection("Jacobi triple product"),
    Entries(
        "13d2a1",
    ),
    Subsection("Trigonometric infinite products"),
    Entries(
        "d2f183",
        "64081c",
        "816057",
        "3c88a7",
    ),
    Section("Series for logarithmic derivatives"),
    Subsection("Lambert series with trigonometric factors"),
    Entries(
        "dfbddd",
        "c7f7a5",
        "44e8fb",
        "1848f1",
    ),
    Subsection("Reciprocal trigonometric series"),
    Entries(
        "d81f05",
        "561d75",
    ),
    Section("Taylor series"),
    Entries(
        "1cdd7b",
        "d637c5",
    ),
    Section("Series for theta constants"),
    Subsection("Reciprocal trigonometric series"),
    Entries(
        "9b7d8c",
        "7b3ac4",
        "ab1c77",
    ),
)

def_Topic(
    Title("Lattice transformations for Jacobi theta functions"),
    Description("This topic lists identities for how Jacobi theta functions", JacobiTheta(j,z,tau), "transform when the lattice parameter", tau, " is transformed. ",
        "See", TopicReference("Argument transformations for Jacobi theta functions"), "for identities involving the argument", z, "when", tau, "is fixed.",
        "See", TopicReference("Jacobi theta functions"), "for other properties of these functions."),
    Section("Reflection symmetry"),
    Entries(
        "fe1b96",
    ),
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

def_Topic(
    Title("Differential equations for Jacobi theta functions"),
    Description("This topic lists identities involving derivatives of Jacobi theta functions", JacobiTheta(j,z,tau), ". ",
        "See the topic", TopicReference("Jacobi theta functions"), "for other properties of these functions."),
    Section("Fundamentals"),
    Subsection("Notation for argument derivatives"),
    Entries(
        "a222ed",
    ),
    Subsection("Conversion of parameter derivatives to argument derivatives"),
    Entries(
        "37e644",
    ),
    Section("Heat equation"),
    Entries(
        "ebc673",
    ),
    Section("Jacobi's differential equation"),
    Entries(
        "936694",
    ),
    Section("Relations at zero"),
    Entries(
        "d967af",
        "cdbdc7",
        "a19141",
        "901934",
        "f2e28a",
        "278274",
        "59184e",  # included from lattice transf
        "46f244",  # included from lattice transf
    ),
    Section("Derivatives of ratios"),
    Entries(
        "cb493d",
        "d41a95",
        "a4eecf",
        "713b6b",
        "64b65d",
        "89985a",
        "0373dc",
        "2853d4",
        "378949",
        "a0552b",
        "775637",
        "23077c",
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
    Description("The values of the Jacobi theta functions at", Equal(z, 0), "are known as theta constants."),
    Description("Called with four arguments, ", SourceForm(JacobiTheta(j,z,tau,r)), ", rendered as",
        JacobiTheta(j,z,tau,1), ", ",
        JacobiTheta(j,z,tau,2), ", ",
        JacobiTheta(j,z,tau,3), ", ",
        JacobiTheta(j,z,tau,4), " (", LessEqual(1, r, 4), "), or",
        JacobiTheta(j,z,tau,r), ", represents the order", r, "derivative of the Jacobi theta function with respect to the argument", z, ".",
        "Derivatives with respect to the lattice parameter", tau, "(and mixed derivatives) can always be converted to derivatives with respect to", z, ", using", EntryReference("37e644"), "."),
    Description("The Jacobi theta functions are defined by the respective Fourier series (",
        EntryReference("700d94"), ", ",
        EntryReference("495a98"), ", ",
        EntryReference("2f97f5"), ", ",
        EntryReference("d923de"), "). ",
        "It is important to note that Fungrim defines theta functions with a factor", ConstPi, "applied to the argument", z,
        "in the Fourier series, for uniformity with the lattice parameter", tau, ". Many authors omit this scaling factor or replace the input", tau,
        "by", Equal(q, Exp(ConstPi*ConstI*tau)), ". Other conventions exist in the mathematical literature as well, "
        "so care is required when using different reference works."),
    Description("The following table lists conditions such that", SourceForm(JacobiTheta(j,z,tau)), "or", SourceForm(JacobiTheta(j,z,tau,r)), "is defined in Fungrim."),
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

# Fourier series for derivatives

make_entry(ID("2ae142"),
    Formula(Equal(JacobiTheta(1,z,tau,r), Where(-ConstI * (ConstPi*ConstI)**r * Exp(ConstPi*ConstI*tau/4) * Sum((-1)**n * (2*n+1)**r * q**(n*(n+1)) * w**(2*n+1), Tuple(n, -Infinity, Infinity)),
        Equal(q, Exp(ConstPi*ConstI*tau)), Equal(w, Exp(ConstPi*ConstI*z))))),
    Variables(z, tau, r),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("42d832"),
    Formula(Equal(JacobiTheta(2,z,tau,r), Where((ConstPi*ConstI)**r * Exp(ConstPi*ConstI*tau/4) * Sum((2*n+1)**r * q**(n*(n+1)) * w**(2*n+1), Tuple(n, -Infinity, Infinity)),
        Equal(q, Exp(ConstPi*ConstI*tau)), Equal(w, Exp(ConstPi*ConstI*z))))),
    Variables(z, tau, r),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("f551ca"),
    Formula(Equal(JacobiTheta(3,z,tau,r), Where((2*ConstPi*ConstI)**r * Sum(n**r * q**(n**2) * w**(2*n), Tuple(n, -Infinity, Infinity)),
        Equal(q, Exp(ConstPi*ConstI*tau)), Equal(w, Exp(ConstPi*ConstI*z))))),
    Variables(z, tau, r),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("1842d9"),
    Formula(Equal(JacobiTheta(4,z,tau,r), Where((2*ConstPi*ConstI)**r * Sum((-1)**n * n**r * q**(n**2) * w**(2*n), Tuple(n, -Infinity, Infinity)),
        Equal(q, Exp(ConstPi*ConstI*tau)), Equal(w, Exp(ConstPi*ConstI*z))))),
    Variables(z, tau, r),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

# Infinite products

make_entry(ID("024a84"),
    Formula(Equal(JacobiTheta(1,z,tau), Where(2 * Exp(ConstPi*ConstI*tau/4) * Sin(ConstPi*z) *
        Product((1-q**(2*n))*(1-2*q**(2*n)*Cos(2*ConstPi*z) + q**(4*n)), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("d6a799"),
    Formula(Equal(JacobiTheta(2,z,tau), Where(2 * Exp(ConstPi*ConstI*tau/4) * Cos(ConstPi*z) *
        Product((1-q**(2*n))*(1+2*q**(2*n)*Cos(2*ConstPi*z) + q**(4*n)), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("77aed2"),
    Formula(Equal(JacobiTheta(3,z,tau), Where(
        Product((1-q**(2*n))*(1+2*q**(2*n-1)*Cos(2*ConstPi*z) + q**(4*n-2)), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("2a2a38"),
    Formula(Equal(JacobiTheta(4,z,tau), Where(
        Product((1-q**(2*n))*(1-2*q**(2*n-1)*Cos(2*ConstPi*z) + q**(4*n-2)), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("13d2a1"),
    Formula(Where(Equal(JacobiTheta(3,z,tau),
        Sum(q**(n**2) * w**(2*n), Tuple(n, -Infinity, Infinity)),
        Product((1-q**(2*n))*(1+q**(2*n-1)*w**2)*(1+q**(2*n-1)*w**(-2)), Tuple(n, 1, Infinity))),
            Equal(q, Exp(ConstPi*ConstI*tau)),
            Equal(w, Exp(ConstPi*ConstI*z)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("39b699"),
    Formula(Where(Equal(JacobiTheta(2,z,tau),
        -(ConstI*Exp(ConstPi*ConstI*tau/4) * (w - w**-1) * Product((1-q**(2*n)) * (1 - q**(2*n)*w**2) * (1 - q**(2*n)*w**-2), Tuple(n, 1, Infinity)))),
            Equal(q, Exp(ConstPi*ConstI*tau)),
            Equal(w, Exp(ConstPi*ConstI*z)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("465810"),
    Formula(Where(Equal(JacobiTheta(2,z,tau),
        Exp(ConstPi*ConstI*tau/4) * (w + w**-1) * Product((1-q**(2*n)) * (1 + q**(2*n)*w**2) * (1 + q**(2*n)*w**-2), Tuple(n, 1, Infinity))),
            Equal(q, Exp(ConstPi*ConstI*tau)),
            Equal(w, Exp(ConstPi*ConstI*z)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("21851b"),
    Formula(Where(Equal(JacobiTheta(3,z,tau),
        Product((1-q**(2*n))*(1+q**(2*n-1)*w**2)*(1+q**(2*n-1)*w**(-2)), Tuple(n, 1, Infinity))),
            Equal(q, Exp(ConstPi*ConstI*tau)),
            Equal(w, Exp(ConstPi*ConstI*z)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("d45548"),
    Formula(Where(Equal(JacobiTheta(4,z,tau),
        Product((1-q**(2*n))*(1-q**(2*n-1)*w**2)*(1-q**(2*n-1)*w**(-2)), Tuple(n, 1, Infinity))),
            Equal(q, Exp(ConstPi*ConstI*tau)),
            Equal(w, Exp(ConstPi*ConstI*z)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))


make_entry(ID("d2f183"),
    Formula(Equal(JacobiTheta(1,z,tau),
        (JacobiTheta(1,0,tau,1)/ConstPi) * Sin(ConstPi*z) * Product(Sin(ConstPi*(n*tau+z))*Sin(ConstPi*(n*tau-z))/Sin(ConstPi*n*tau)**2, Tuple(n, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("64081c"),
    Formula(Equal(JacobiTheta(2,z,tau),
        JacobiTheta(2,0,tau) * Cos(ConstPi*z) * Product(Cos(ConstPi*(n*tau+z))*Cos(ConstPi*(n*tau-z))/Cos(ConstPi*n*tau)**2, Tuple(n, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("816057"),
    Formula(Equal(JacobiTheta(3,z,tau),
        JacobiTheta(3,0,tau) * Product(Cos(ConstPi*((n-Div(1,2))*tau+z))*Cos(ConstPi*((n-Div(1,2))*tau-z))/Cos(ConstPi*((n-Div(1,2))*tau))**2, Tuple(n, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("3c88a7"),
    Formula(Equal(JacobiTheta(4,z,tau),
        JacobiTheta(4,0,tau) * Product(Sin(ConstPi*((n-Div(1,2))*tau+z))*Sin(ConstPi*((n-Div(1,2))*tau-z))/Sin(ConstPi*((n-Div(1,2))*tau))**2, Tuple(n, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))


make_entry(ID("dfbddd"),
    Formula(Equal(
        (1/ConstPi) * (JacobiTheta(1,z,tau,1) / JacobiTheta(1,z,tau)), Where(Cot(ConstPi*z) + 4 * Sum(q**(2*n) / (1 - q**(2*n)) * Sin(2*ConstPi*n*z), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), Less(Abs(Im(z)), Abs(Im(tau))), Unequal(Sin(ConstPi*z), 0))))

make_entry(ID("c7f7a5"),
    Formula(Equal(
        (1/ConstPi) * (JacobiTheta(2,z,tau,1) / JacobiTheta(2,z,tau)), Where(-Tan(ConstPi*z) + 4 * Sum((-1)**n * (q**(2*n) / (1 - q**(2*n))) * Sin(2*ConstPi*n*z), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), Less(Abs(Im(z)), Abs(Im(tau))), Unequal(Cos(ConstPi*z), 0))))

make_entry(ID("44e8fb"),
    Formula(Equal(
        (1/ConstPi) * (JacobiTheta(3,z,tau,1) / JacobiTheta(3,z,tau)), Where(4 * Sum((-1)**n * (q**(n) / (1 - q**(2*n))) * Sin(2*ConstPi*n*z), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), Less(Abs(Im(z)), Div(1,2)*Abs(Im(tau))))))

make_entry(ID("1848f1"),
    Formula(Equal(
        (1/ConstPi) * (JacobiTheta(4,z,tau,1) / JacobiTheta(4,z,tau)), Where(4 * Sum(q**(n) / (1 - q**(2*n)) * Sin(2*ConstPi*n*z), Tuple(n, 1, Infinity)), Equal(q, Exp(ConstPi*ConstI*tau))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), Less(Abs(Im(z)), Div(1,2)*Abs(Im(tau))))))

# Taylor series

make_entry(ID("1cdd7b"),
    Formula(Equal(JacobiTheta(j,z+x,tau),
        Sum((JacobiTheta(j,z,tau,n) / Factorial(n)) * x**n, Tuple(n, 0, Infinity)))),
    Variables(j, z, tau, x),
    Assumptions(And(Element(j, Set(1, 2, 3, 4)), Element(z, CC), Element(tau, HH), Element(x, CC))))

make_entry(ID("d637c5"),
    Formula(Equal(JacobiTheta(j,z,tau+x),
        Sum((1/(4*ConstPi*ConstI)**n) * (JacobiTheta(j,z,tau,2*n) / Factorial(n)) * x**n, Tuple(n, 0, Infinity)))),
    Variables(j, z, tau, x),
    Assumptions(And(Element(j, Set(1, 2, 3, 4)), Element(z, CC), Element(tau, HH), Element(x, CC), Less(Abs(x), Im(tau)))))

# Other series

"""
todo: formally correct, but divergent -- what is an elegant regularization?

make_entry(ID(""),
    Formula(Equal(JacobiTheta(1,z,tau,1)/JacobiTheta(1,z,tau),
        -(ConstPi * Sum(1/Tan(ConstPi*(z+n*tau)), Tuple(n, -Infinity, Infinity))))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH),
        Unequal(JacobiTheta(1, z, tau), 0))))

make_entry(ID(""),
    Formula(Equal(JacobiTheta(2,z,tau,1)/JacobiTheta(2,z,tau),
        ConstPi * Sum(Tan(ConstPi*(z+n*tau)), Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH),
        Unequal(JacobiTheta(2, z, tau), 0))))
"""

# todo: introduce a log-derivative operator?
make_entry(ID("d81f05"),
    Formula(Equal(ComplexBranchDerivative(Log(JacobiTheta(1,z,tau)), z, z, 2),
        ConstPi**2 * Sum(1/Sin(ConstPi*(z+n*tau))**2, Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH),
        Unequal(JacobiTheta(1, z, tau), 0))))

make_entry(ID("561d75"),
    Formula(Equal(ComplexBranchDerivative(Log(JacobiTheta(2,z,tau)), z, z, 2),
        #JacobiTheta(2,z,tau,2)/JacobiTheta(2,z,tau), - (JacobiTheta(2,z,tau,1)/JacobiTheta(2,z,tau))**2
        ConstPi**2 * Sum(1/Cos(ConstPi*(z+n*tau))**2, Tuple(n, -Infinity, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH),
        Unequal(JacobiTheta(2, z, tau), 0))))

make_entry(ID("9b7d8c"),
    Formula(Equal(JacobiTheta(2,0,tau)**2,
        Sum(1/Cos(ConstPi*tau*(n+Div(1,2))), Tuple(n, -Infinity, Infinity)))),
    Variables(tau),
    Assumptions(Element(z, CC), Element(tau, HH)))

make_entry(ID("7b3ac4"),
    Formula(Equal(JacobiTheta(3,0,tau)**2,
        Sum(1/Cos(ConstPi*tau*n), Tuple(n, -Infinity, Infinity)))),
    Variables(tau),
    Assumptions(Element(z, CC), Element(tau, HH)))

make_entry(ID("ab1c77"),
    Formula(Equal(JacobiTheta(4,0,tau)**2,
        Sum(1/Cos(ConstPi*(tau+1)*n), Tuple(n, -Infinity, Infinity)))),
    Variables(tau),
    Assumptions(Element(z, CC), Element(tau, HH)))

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

# Lattice transformations

# Reflection symmetry

make_entry(ID("fe1b96"),
    Formula(Equal(JacobiTheta(j, z, -Conjugate(tau)), Conjugate(JacobiTheta(j,Conjugate(z), tau)))),
    Variables(j, z, tau),
    Assumptions(And(Element(j, Set(1, 2, 3, 4)), Element(z, CC), Element(tau, HH))))

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
    Formula(Equal(JacobiTheta(4,4*z,4*tau), JacobiTheta(4,z,tau)*JacobiTheta(4,Div(1,4)-z,tau)*JacobiTheta(4,Div(1,4)+z,tau)*JacobiTheta(3,z,tau)/(JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(3,Div(1,4),tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Differential equations

make_entry(ID("a222ed"),
    Formula(Equal(ComplexDerivative(JacobiTheta(j,z,tau), z, z, r), JacobiTheta(j,z,tau,r))),
    Variables(j, z, tau, r),
    Assumptions(And(Element(j, Set(1, 2, 3, 4)), Element(z, CC), Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("37e644"),
    Formula(Equal(ComplexDerivative(JacobiTheta(j,z,tau,s), tau, tau, r), (1/(4*ConstPi*ConstI)**r) * (JacobiTheta(j,z,tau,2*r+s)))),
    Variables(j, z, tau, r, s),
    Assumptions(And(Element(j, Set(1, 2, 3, 4)), Element(z, CC), Element(tau, HH), Element(r, ZZGreaterEqual(0), Element(s, ZZGreaterEqual(0))))))

# Heat equation

make_entry(ID("ebc673"),
    Formula(Equal(JacobiTheta(j,z,tau,2) - 4*ConstPi*ConstI*Derivative(JacobiTheta(j,z,tau), tau, tau), 0)),
    Variables(j, z, tau),
    Assumptions(And(Element(j, Set(1, 2, 3, 4)), Element(z, CC), Element(tau, HH))))

# Jacobi differential equation

D0 = Subscript(D, 0)
D1 = Subscript(D, 1)
D2 = Subscript(D, 2)
D3 = Subscript(D, 3)

make_entry(ID("936694"),
    Formula(Where(Equal((30*D1**3-15*D0*D1*D2+D0**2*D3)**2 + 32*(D0*D2-3*D1**2)**3 + ConstPi**2*(D0*D2 - 3*D1**2)**2*D0**10, 0),
        Equal(Subscript(D, r), Derivative(JacobiTheta(j, 0, tau), tau, tau, r)))),
    Variables(j, tau),
    Assumptions(And(Element(j, Set(1, 2, 3, 4)), Element(tau, HH))))

# Relations at zero

make_entry(ID("d967af"),
    Formula(Equal(JacobiTheta(1,0,tau,2*r), 0)),
    Variables(tau, r),
    Assumptions(And(Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("cdbdc7"),
    Formula(Equal(JacobiTheta(2,0,tau,2*r+1), 0)),
    Variables(tau, r),
    Assumptions(And(Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("a19141"),
    Formula(Equal(JacobiTheta(3,0,tau,2*r+1), 0)),
    Variables(tau, r),
    Assumptions(And(Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("901934"),
    Formula(Equal(JacobiTheta(4,0,tau,2*r+1), 0)),
    Variables(tau, r),
    Assumptions(And(Element(tau, HH), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("f2e28a"),
    Formula(Equal(JacobiTheta(1,0,tau,1), ConstPi*JacobiTheta(2,0,tau)*JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau))),
    Variables(tau),
    Assumptions(And(Element(tau, HH))))

make_entry(ID("278274"),
    Formula(Equal(JacobiTheta(1,0,tau,3) / JacobiTheta(1,0,tau,1), JacobiTheta(2,0,tau,2)/JacobiTheta(2,0,tau) + JacobiTheta(3,0,tau,2)/JacobiTheta(3,0,tau) + JacobiTheta(4,0,tau,2)/JacobiTheta(4,0,tau))),
    Variables(tau),
    Assumptions(And(Element(tau, HH))))

# Derivatives of ratios

make_entry(ID("cb493d"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(1,z,tau)/JacobiTheta(2,z,tau), z, z), ConstPi * JacobiTheta(2,0,tau)**2 * (JacobiTheta(3,z,tau) * JacobiTheta(4,z,tau) / JacobiTheta(2,z,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("d41a95"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(1,z,tau)/JacobiTheta(3,z,tau), z, z), ConstPi * JacobiTheta(3,0,tau)**2 * (JacobiTheta(2,z,tau) * JacobiTheta(4,z,tau) / JacobiTheta(3,z,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("a4eecf"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(1,z,tau)/JacobiTheta(4,z,tau), z, z), ConstPi * JacobiTheta(4,0,tau)**2 * (JacobiTheta(2,z,tau) * JacobiTheta(3,z,tau) / JacobiTheta(4,z,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("713b6b"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(2,z,tau)/JacobiTheta(1,z,tau), z, z), -(ConstPi*JacobiTheta(2,0,tau)**2 * (JacobiTheta(3,z,tau) * JacobiTheta(4,z,tau) / JacobiTheta(1,z,tau)**2)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("64b65d"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(2,z,tau)/JacobiTheta(3,z,tau), z, z), -(ConstPi * JacobiTheta(4,0,tau)**2 * (JacobiTheta(1,z,tau) * JacobiTheta(4,z,tau) / JacobiTheta(3,z,tau)**2)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("89985a"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(2,z,tau)/JacobiTheta(4,z,tau), z, z), -(ConstPi * JacobiTheta(3,0,tau)**2 * (JacobiTheta(1,z,tau) * JacobiTheta(3,z,tau) / JacobiTheta(4,z,tau)**2)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))


make_entry(ID("0373dc"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(3,z,tau)/JacobiTheta(1,z,tau), z, z), -(ConstPi * JacobiTheta(3,0,tau)**2 * (JacobiTheta(2,z,tau) * JacobiTheta(4,z,tau) / JacobiTheta(1,z,tau)**2)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("2853d4"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(3,z,tau)/JacobiTheta(2,z,tau), z, z), ConstPi * JacobiTheta(4,0,tau)**2 * (JacobiTheta(1,z,tau) * JacobiTheta(4,z,tau) / JacobiTheta(2,z,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("378949"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(3,z,tau)/JacobiTheta(4,z,tau), z, z), -(ConstPi * JacobiTheta(2,0,tau)**2 * (JacobiTheta(1,z,tau) * JacobiTheta(2,z,tau) / JacobiTheta(4,z,tau)**2)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))


make_entry(ID("a0552b"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(4,z,tau)/JacobiTheta(1,z,tau), z, z), -(ConstPi * JacobiTheta(4,0,tau)**2 * (JacobiTheta(2,z,tau) * JacobiTheta(3,z,tau) / JacobiTheta(1,z,tau)**2)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("775637"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(4,z,tau)/JacobiTheta(2,z,tau), z, z), ConstPi * JacobiTheta(3,0,tau)**2 * (JacobiTheta(1,z,tau) * JacobiTheta(3,z,tau) / JacobiTheta(2,z,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("23077c"),
    Formula(Equal(MeromorphicDerivative(JacobiTheta(4,z,tau)/JacobiTheta(3,z,tau), z, z), ConstPi * JacobiTheta(2,0,tau)**2 * (JacobiTheta(1,z,tau) * JacobiTheta(2,z,tau) / JacobiTheta(3,z,tau)**2))),    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

#-----------------------------------------------------------------------------#
#                                                                             #
#                           Argument transformations                          #
#                                                                             #
#-----------------------------------------------------------------------------#

def_Topic(
    Title("Argument transformations for Jacobi theta functions"),
    Description("This topic lists identities for how Jacobi theta functions", JacobiTheta(j,z,tau), "transform when the argument", z, " is transformed. ",
        "This topic mainly covers identities where the lattice parameter", tau, "is fixed.",
        "See", TopicReference("Lattice transformations for Jacobi theta functions"), "for identities involving transformations of", tau, ".",
        "See", TopicReference("Jacobi theta functions"), "for other properties of these functions."),
    Section("Reflection symmetry"),
    Subsection("Odd-even symmetry"),
    Entries(
        "59f8e1",
        "fb55cb",
        "380076",
        "4f939e",
    ),
    Subsection("Conjugate symmetry"),
    Entries(
        "a891da",
    ),
    Section("Periodicity"),
    Entries(
        "2faeb9",
        "b46534",
        "5cdae6",
        "f697d5",
        "e56f77",
        "4448f1",
    ),
    Section("Quasi-periodicity"),
    Subsection("Single shifts"),
    Entries(
        "d989cd",
        "cd5f45",
        "103bfb",
        "b83f63",
    ),
    Subsection("General shifts"),
    Entries(
        "43fa0e",
        "d29148",
        "2e4da0",
        "8d6a1d",
    ),
    Section("Half-period or quarter-period shifts"),
    Entries(
        "563d18",
        "47f6dd",
        "7d559c",
        "bb2d01",
        "d5a29e",
        "cc6d21",
        "2d2dde",
        "429093",
    ),
    Section("Theta functions represented in terms of each other"),
    Subsection("Theta 1"),
    Entries(
        "95988c",
        "4c462b",
        "ed0756",
    ),
    Subsection("Theta 2"),
    Entries(
        "785668",
        "0878a4",
        "6a7704",
    ),
    Subsection("Theta 3"),
    Entries(
        "b3fc6d",
        "71d5ee",
        "235d0d",
    ),
    Subsection("Theta 4"),
    Entries(
        "5d41b1",
        "6d918c",
        "10ca40",
    ),
    Section("Double argument"),
    Subsection("Theta 1"),
    Entries(
        "5fe58d",
    ),
    Subsection("Theta 2"),
    Entries(
        "3a77e0",
        "e6dc09",
        "aaa582",
        "b1d07b",
    ),
    Subsection("Theta 3"),
    Entries(
        "20d581",
        "ed3ff9",
        "794106",
        "a94b43",
    ),
    Subsection("Theta 4"),
    Entries(
        "8b825c",
        "7131cd",
        "931201",
        "21dc98",
    ),
    Section("Relations involving sums and differences of arguments"),
    Subsection("Cross-products with two factors and double lattice parameter"),
    Entries(
        "1792a9",
        "5f9e54",
        "9a9487",
        "f4554f",
        "d36e97",
        "73eb5d",
    ),
    Subsection("Cross-products with four factors"),
    Entries(
        "34d1c6",
        "47e587",
        "ee8617",
        "dfea7d",
        "9973ef",
        "077394",
    ),
    Subsection("Cross-products of squares"),
    Entries(
        "45165c",
        "75cb8c",
        "663a02",
        "1feda6",
        "89c9e4",
        "48a1c6",
        "66efb8",
        "9aa437",
        "5752b8",
        "c891a1",
        "3cac28",
        "45a130",
    ),
)


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

# Conjugate symmetry

make_entry(ID("a891da"),
    Formula(Equal(JacobiTheta(j, Conjugate(z), tau), Conjugate(JacobiTheta(j,z, -Conjugate(tau))))),
    Variables(j, z, tau),
    Assumptions(And(Element(j, Set(1, 2, 3, 4)), Element(z, CC), Element(tau, HH))))

# Periodicity

make_entry(ID("2faeb9"),
    Formula(Equal(JacobiTheta(1,z+2*n,tau), JacobiTheta(1,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("b46534"),
    Formula(Equal(JacobiTheta(2,z+2*n,tau), JacobiTheta(2,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("5cdae6"),
    Formula(Equal(JacobiTheta(1,z+n,tau), (-1)**n * JacobiTheta(1,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("f697d5"),
    Formula(Equal(JacobiTheta(2,z+n,tau), (-1)**n * JacobiTheta(2,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("e56f77"),
    Formula(Equal(JacobiTheta(3,z+n,tau), JacobiTheta(3,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("4448f1"),
    Formula(Equal(JacobiTheta(4,z+n,tau), JacobiTheta(4,z,tau))),
    Variables(z, tau, n),
    Assumptions(And(Element(z, CC), Element(tau, HH), Element(n, ZZ))))

# Single translates
# check(JacobiTheta(1,z+1,tau), -JacobiTheta(1,z,tau))
# check(JacobiTheta(2,z+1,tau), -JacobiTheta(2,z,tau))
# check(JacobiTheta(3,z+1,tau), JacobiTheta(3,z,tau))
# check(JacobiTheta(4,z+1,tau), JacobiTheta(4,z,tau))

# Quasi-periodicity

# Single shifts

make_entry(ID("d989cd"),
    Formula(Equal(JacobiTheta(1,z+tau,tau), -Exp(-(ConstPi*ConstI*(2*z+tau))) * JacobiTheta(1,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("cd5f45"),
    Formula(Equal(JacobiTheta(2,z+tau,tau), Exp(-(ConstPi*ConstI*(2*z+tau))) * JacobiTheta(2,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("103bfb"),
    Formula(Equal(JacobiTheta(3,z+tau,tau), Exp(-(ConstPi*ConstI*(2*z+tau))) * JacobiTheta(3,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("b83f63"),
    Formula(Equal(JacobiTheta(4,z+tau,tau), -Exp(-(ConstPi*ConstI*(2*z+tau))) * JacobiTheta(4,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# General shifts

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

# Half-shifts

make_entry(ID("563d18"),
    Formula(Equal(JacobiTheta(1,z+Div(1,2),tau), JacobiTheta(2,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("47f6dd"),
    Formula(Equal(JacobiTheta(2,z+Div(1,2),tau), -JacobiTheta(1,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("7d559c"),
    Formula(Equal(JacobiTheta(3,z+Div(1,2),tau), JacobiTheta(4,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("bb2d01"),
    Formula(Equal(JacobiTheta(4,z+Div(1,2),tau), JacobiTheta(3,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("d5a29e"),
    Formula(Equal(JacobiTheta(1,z+Div(1,2)*tau,tau), Exp(-(ConstPi*ConstI*(z+tau/4))) * ConstI * JacobiTheta(4,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("cc6d21"),
    Formula(Equal(JacobiTheta(2,z+Div(1,2)*tau,tau), Exp(-(ConstPi*ConstI*(z+tau/4))) * JacobiTheta(3,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("2d2dde"),
    Formula(Equal(JacobiTheta(3,z+Div(1,2)*tau,tau), Exp(-(ConstPi*ConstI*(z+tau/4))) * JacobiTheta(2,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("429093"),
    Formula(Equal(JacobiTheta(4,z+Div(1,2)*tau,tau), Exp(-(ConstPi*ConstI*(z+tau/4))) * ConstI * JacobiTheta(1,z,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Theta functions representated in terms of each other

make_entry(ID("95988c"),
    Formula(Equal(JacobiTheta(1,z,tau), -JacobiTheta(2,z+Div(1,2),tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("4c462b"),
    Formula(Equal(JacobiTheta(1,z,tau), -ConstI*Exp(ConstPi*ConstI*(z+tau/4))*JacobiTheta(4,z+Div(1,2)*tau,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("ed0756"),
    Formula(Equal(JacobiTheta(1,z,tau), -ConstI*Exp(ConstPi*ConstI*(z+tau/4))*JacobiTheta(3,z+Div(1,2)+Div(1,2)*tau,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("785668"),
    Formula(Equal(JacobiTheta(2,z,tau), JacobiTheta(1,z+Div(1,2),tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("0878a4"),
    Formula(Equal(JacobiTheta(2,z,tau), Exp(ConstPi*ConstI*(z+tau/4))*JacobiTheta(3,z+Div(1,2)*tau,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("6a7704"),
    Formula(Equal(JacobiTheta(2,z,tau), Exp(ConstPi*ConstI*(z+tau/4))*JacobiTheta(4,z+Div(1,2)+Div(1,2)*tau,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("b3fc6d"),
    Formula(Equal(JacobiTheta(3,z,tau), JacobiTheta(4,z+Div(1,2),tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("71d5ee"),
    Formula(Equal(JacobiTheta(3,z,tau), Exp(ConstPi*ConstI*(z+tau/4))*JacobiTheta(2,z+Div(1,2)*tau,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("235d0d"),
    Formula(Equal(JacobiTheta(3,z,tau), Exp(ConstPi*ConstI*(z+tau/4))*JacobiTheta(1,z+Div(1,2)+Div(1,2)*tau,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("5d41b1"),
    Formula(Equal(JacobiTheta(4,z,tau), JacobiTheta(3,z+Div(1,2),tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("6d918c"),
    Formula(Equal(JacobiTheta(4,z,tau), -ConstI*Exp(ConstPi*ConstI*(z+tau/4))*JacobiTheta(1,z+Div(1,2)*tau,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("10ca40"),
    Formula(Equal(JacobiTheta(4,z,tau), ConstI*Exp(ConstPi*ConstI*(z+tau/4))*JacobiTheta(2,z+Div(1,2)+Div(1,2)*tau,tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Double argument

make_entry(ID("5fe58d"),
    Formula(Equal(JacobiTheta(1,2*z,tau), 2*JacobiTheta(1,z,tau)*JacobiTheta(2,z,tau)*JacobiTheta(3,z,tau)*JacobiTheta(4,z,tau)/(JacobiTheta(2,0,tau)*JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("3a77e0"),
    Formula(Equal(JacobiTheta(2,2*z,tau), (JacobiTheta(2,z,tau)**4 - JacobiTheta(1,z,tau)**4)/JacobiTheta(2,0,tau)**3)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("e6dc09"),
    Formula(Equal(JacobiTheta(2,2*z,tau), (JacobiTheta(3,z,tau)**4 - JacobiTheta(4,z,tau)**4)/JacobiTheta(2,0,tau)**3)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("aaa582"),
    Formula(Equal(JacobiTheta(2,2*z,tau), (JacobiTheta(2,z,tau)**2*JacobiTheta(3,z,tau)**2 - JacobiTheta(1,z,tau)**2*JacobiTheta(4,z,tau)**2)/(JacobiTheta(2,0,tau)*JacobiTheta(3,0,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("b1d07b"),
    Formula(Equal(JacobiTheta(2,2*z,tau), (JacobiTheta(2,z,tau)**2*JacobiTheta(4,z,tau)**2 - JacobiTheta(1,z,tau)**2*JacobiTheta(3,z,tau)**2)/(JacobiTheta(2,0,tau)*JacobiTheta(4,0,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("20d581"),
    Formula(Equal(JacobiTheta(3,2*z,tau), (JacobiTheta(1,z,tau)**4 + JacobiTheta(3,z,tau)**4)/JacobiTheta(3,0,tau)**3)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("ed3ff9"),
    Formula(Equal(JacobiTheta(3,2*z,tau), (JacobiTheta(2,z,tau)**4 + JacobiTheta(4,z,tau)**4)/JacobiTheta(3,0,tau)**3)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("794106"),
    Formula(Equal(JacobiTheta(3,2*z,tau), (JacobiTheta(2,z,tau)**2*JacobiTheta(3,z,tau)**2 + JacobiTheta(1,z,tau)**2*JacobiTheta(4,z,tau)**2)/(JacobiTheta(3,0,tau)*JacobiTheta(2,0,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("a94b43"),
    Formula(Equal(JacobiTheta(3,2*z,tau), (JacobiTheta(3,z,tau)**2*JacobiTheta(4,z,tau)**2 - JacobiTheta(1,z,tau)**2*JacobiTheta(2,z,tau)**2)/(JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("8b825c"),
    Formula(Equal(JacobiTheta(4,2*z,tau), (JacobiTheta(4,z,tau)**4 - JacobiTheta(1,z,tau)**4)/JacobiTheta(4,0,tau)**3)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("7131cd"),
    Formula(Equal(JacobiTheta(4,2*z,tau), (JacobiTheta(3,z,tau)**4 - JacobiTheta(2,z,tau)**4)/JacobiTheta(4,0,tau)**3)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("931201"),
    Formula(Equal(JacobiTheta(4,2*z,tau), (JacobiTheta(1,z,tau)**2*JacobiTheta(3,z,tau)**2 + JacobiTheta(2,z,tau)**2*JacobiTheta(4,z,tau)**2)/(JacobiTheta(4,0,tau)*JacobiTheta(2,0,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("21dc98"),
    Formula(Equal(JacobiTheta(4,2*z,tau), (JacobiTheta(1,z,tau)**2*JacobiTheta(2,z,tau)**2 + JacobiTheta(3,z,tau)**2*JacobiTheta(4,z,tau)**2)/(JacobiTheta(4,0,tau)*JacobiTheta(3,0,tau)**2))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Relations involving sums and differences of arguments

# Cross-products with two factors

make_entry(ID("1792a9"),
    Formula(Equal(JacobiTheta(1,z,tau)*JacobiTheta(1,w,tau), JacobiTheta(3,z+w,2*tau)*JacobiTheta(2,z-w,2*tau) - JacobiTheta(2,z+w,2*tau)*JacobiTheta(3,z-w,2*tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("5f9e54"),
    Formula(Equal(JacobiTheta(1,z,tau)*JacobiTheta(2,w,tau), JacobiTheta(1,z+w,2*tau)*JacobiTheta(4,z-w,2*tau) + JacobiTheta(4,z+w,2*tau)*JacobiTheta(1,z-w,2*tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("9a9487"),
    Formula(Equal(JacobiTheta(2,z,tau)*JacobiTheta(2,w,tau), JacobiTheta(2,z+w,2*tau)*JacobiTheta(3,z-w,2*tau) + JacobiTheta(3,z+w,2*tau)*JacobiTheta(2,z-w,2*tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("f4554f"),
    Formula(Equal(JacobiTheta(3,z,tau)*JacobiTheta(3,w,tau), JacobiTheta(3,z+w,2*tau)*JacobiTheta(3,z-w,2*tau) + JacobiTheta(2,z+w,2*tau)*JacobiTheta(2,z-w,2*tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("d36e97"),
    Formula(Equal(JacobiTheta(3,z,tau)*JacobiTheta(4,w,tau), JacobiTheta(4,z+w,2*tau)*JacobiTheta(4,z-w,2*tau) - JacobiTheta(1,z+w,2*tau)*JacobiTheta(1,z-w,2*tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("73eb5d"),
    Formula(Equal(JacobiTheta(4,z,tau)*JacobiTheta(4,w,tau), JacobiTheta(3,z+w,2*tau)*JacobiTheta(3,z-w,2*tau) - JacobiTheta(2,z+w,2*tau)*JacobiTheta(2,z-w,2*tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

# Cross-products with four factors

make_entry(ID("34d1c6"),
    Formula(Equal(JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(1,z+w,tau)*JacobiTheta(2,z-w, tau), JacobiTheta(1,z,tau)*JacobiTheta(2,z,tau)*JacobiTheta(3,w,tau)*JacobiTheta(4,w,tau) + JacobiTheta(3,z,tau)*JacobiTheta(4,z,tau)*JacobiTheta(1,w,tau)*JacobiTheta(2,w,tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("47e587"),
    Formula(Equal(JacobiTheta(2,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(1,z+w,tau)*JacobiTheta(3,z-w, tau), JacobiTheta(1,z,tau)*JacobiTheta(3,z,tau)*JacobiTheta(2,w,tau)*JacobiTheta(4,w,tau) + JacobiTheta(2,z,tau)*JacobiTheta(4,z,tau)*JacobiTheta(1,w,tau)*JacobiTheta(3,w,tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("ee8617"),
    Formula(Equal(JacobiTheta(2,0,tau)*JacobiTheta(3,0,tau)*JacobiTheta(1,z+w,tau)*JacobiTheta(4,z-w, tau), JacobiTheta(1,z,tau)*JacobiTheta(4,z,tau)*JacobiTheta(2,w,tau)*JacobiTheta(3,w,tau) + JacobiTheta(2,z,tau)*JacobiTheta(3,z,tau)*JacobiTheta(1,w,tau)*JacobiTheta(4,w,tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("dfea7d"),
    Formula(Equal(JacobiTheta(2,0,tau)*JacobiTheta(3,0,tau)*JacobiTheta(2,z+w,tau)*JacobiTheta(3,z-w, tau), JacobiTheta(2,z,tau)*JacobiTheta(3,z,tau)*JacobiTheta(2,w,tau)*JacobiTheta(3,w,tau) - JacobiTheta(1,z,tau)*JacobiTheta(4,z,tau)*JacobiTheta(1,w,tau)*JacobiTheta(4,w,tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("9973ef"),
    Formula(Equal(JacobiTheta(2,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(2,z+w,tau)*JacobiTheta(4,z-w, tau), JacobiTheta(2,z,tau)*JacobiTheta(4,z,tau)*JacobiTheta(2,w,tau)*JacobiTheta(4,w,tau) - JacobiTheta(1,z,tau)*JacobiTheta(3,z,tau)*JacobiTheta(1,w,tau)*JacobiTheta(3,w,tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("077394"),
    Formula(Equal(JacobiTheta(3,0,tau)*JacobiTheta(4,0,tau)*JacobiTheta(3,z+w,tau)*JacobiTheta(4,z-w, tau), JacobiTheta(3,z,tau)*JacobiTheta(4,z,tau)*JacobiTheta(3,w,tau)*JacobiTheta(4,w,tau) - JacobiTheta(1,z,tau)*JacobiTheta(2,z,tau)*JacobiTheta(1,w,tau)*JacobiTheta(2,w,tau))),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

# Cross-products of squares

make_entry(ID("45165c"),
    Formula(Equal(JacobiTheta(1,z+w,tau)*JacobiTheta(1,z-w,tau)*JacobiTheta(2,0,tau)**2, JacobiTheta(1,z,tau)**2*JacobiTheta(2,w,tau)**2 - JacobiTheta(2,z,tau)**2*JacobiTheta(1,w,tau)**2, JacobiTheta(4,z,tau)**2*JacobiTheta(3,w,tau)**2 - JacobiTheta(3,z,tau)**2*JacobiTheta(4,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("75cb8c"),
    Formula(Equal(JacobiTheta(1,z+w,tau)*JacobiTheta(1,z-w,tau)*JacobiTheta(3,0,tau)**2, JacobiTheta(1,z,tau)**2*JacobiTheta(3,w,tau)**2 - JacobiTheta(3,z,tau)**2*JacobiTheta(1,w,tau)**2, JacobiTheta(4,z,tau)**2*JacobiTheta(2,w,tau)**2 - JacobiTheta(2,z,tau)**2*JacobiTheta(4,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("663a02"),
    Formula(Equal(JacobiTheta(1,z+w,tau)*JacobiTheta(1,z-w,tau)*JacobiTheta(4,0,tau)**2, JacobiTheta(3,z,tau)**2*JacobiTheta(2,w,tau)**2 - JacobiTheta(2,z,tau)**2*JacobiTheta(3,w,tau)**2, JacobiTheta(1,z,tau)**2*JacobiTheta(4,w,tau)**2 - JacobiTheta(4,z,tau)**2*JacobiTheta(1,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))



make_entry(ID("1feda6"),
    Formula(Equal(JacobiTheta(2,z+w,tau)*JacobiTheta(2,z-w,tau)*JacobiTheta(2,0,tau)**2, JacobiTheta(2,z,tau)**2*JacobiTheta(2,w,tau)**2 - JacobiTheta(1,z,tau)**2*JacobiTheta(1,w,tau)**2, JacobiTheta(3,z,tau)**2*JacobiTheta(3,w,tau)**2 - JacobiTheta(4,z,tau)**2*JacobiTheta(4,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("89c9e4"),
    Formula(Equal(JacobiTheta(2,z+w,tau)*JacobiTheta(2,z-w,tau)*JacobiTheta(3,0,tau)**2, JacobiTheta(2,z,tau)**2*JacobiTheta(3,w,tau)**2 - JacobiTheta(4,z,tau)**2*JacobiTheta(1,w,tau)**2, JacobiTheta(3,z,tau)**2*JacobiTheta(2,w,tau)**2 - JacobiTheta(1,z,tau)**2*JacobiTheta(4,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("48a1c6"),
    Formula(Equal(JacobiTheta(2,z+w,tau)*JacobiTheta(2,z-w,tau)*JacobiTheta(4,0,tau)**2, JacobiTheta(4,z,tau)**2*JacobiTheta(2,w,tau)**2 - JacobiTheta(1,z,tau)**2*JacobiTheta(3,w,tau)**2, JacobiTheta(2,z,tau)**2*JacobiTheta(4,w,tau)**2 - JacobiTheta(3,z,tau)**2*JacobiTheta(1,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))


make_entry(ID("66efb8"),
    Formula(Equal(JacobiTheta(3,z+w,tau)*JacobiTheta(3,z-w,tau)*JacobiTheta(2,0,tau)**2, JacobiTheta(3,z,tau)**2*JacobiTheta(2,w,tau)**2 + JacobiTheta(4,z,tau)**2*JacobiTheta(1,w,tau)**2, JacobiTheta(2,z,tau)**2*JacobiTheta(3,w,tau)**2 + JacobiTheta(1,z,tau)**2*JacobiTheta(4,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("9aa437"),
    Formula(Equal(JacobiTheta(3,z+w,tau)*JacobiTheta(3,z-w,tau)*JacobiTheta(3,0,tau)**2, JacobiTheta(1,z,tau)**2*JacobiTheta(1,w,tau)**2 + JacobiTheta(3,z,tau)**2*JacobiTheta(3,w,tau)**2, JacobiTheta(2,z,tau)**2*JacobiTheta(2,w,tau)**2 + JacobiTheta(4,z,tau)**2*JacobiTheta(4,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("5752b8"),
    Formula(Equal(JacobiTheta(3,z+w,tau)*JacobiTheta(3,z-w,tau)*JacobiTheta(4,0,tau)**2, JacobiTheta(4,z,tau)**2*JacobiTheta(3,w,tau)**2 - JacobiTheta(1,z,tau)**2*JacobiTheta(2,w,tau)**2, JacobiTheta(3,z,tau)**2*JacobiTheta(4,w,tau)**2 - JacobiTheta(2,z,tau)**2*JacobiTheta(1,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))


make_entry(ID("c891a1"),
    Formula(Equal(JacobiTheta(4,z+w,tau)*JacobiTheta(4,z-w,tau)*JacobiTheta(2,0,tau)**2, JacobiTheta(4,z,tau)**2*JacobiTheta(2,w,tau)**2 + JacobiTheta(3,z,tau)**2*JacobiTheta(1,w,tau)**2, JacobiTheta(1,z,tau)**2*JacobiTheta(3,w,tau)**2 + JacobiTheta(2,z,tau)**2*JacobiTheta(4,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("3cac28"),
    Formula(Equal(JacobiTheta(4,z+w,tau)*JacobiTheta(4,z-w,tau)*JacobiTheta(3,0,tau)**2, JacobiTheta(1,z,tau)**2*JacobiTheta(2,w,tau)**2 + JacobiTheta(3,z,tau)**2*JacobiTheta(4,w,tau)**2, JacobiTheta(2,z,tau)**2*JacobiTheta(1,w,tau)**2 + JacobiTheta(4,z,tau)**2*JacobiTheta(3,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))

make_entry(ID("45a130"),
    Formula(Equal(JacobiTheta(4,z+w,tau)*JacobiTheta(4,z-w,tau)*JacobiTheta(4,0,tau)**2, JacobiTheta(3,z,tau)**2*JacobiTheta(3,w,tau)**2 - JacobiTheta(2,z,tau)**2*JacobiTheta(2,w,tau)**2, JacobiTheta(4,z,tau)**2*JacobiTheta(4,w,tau)**2 - JacobiTheta(1,z,tau)**2*JacobiTheta(1,w,tau)**2)),
    Variables(z, w, tau),
    Assumptions(And(Element(z, CC), Element(w, tau), Element(tau, HH))))


# Sums and products

# Fourth powers

make_entry(ID("1fbc09"),
    Formula(Equal(JacobiTheta(3,0,tau)**4, JacobiTheta(2,0,tau)**4 + JacobiTheta(4,0,tau)**4)),
    Variables(tau),
    Assumptions(And(Element(tau, HH))))

make_entry(ID("08822c"),
    Formula(Equal(JacobiTheta(1,z,tau)**4 + JacobiTheta(3,z,tau)**4, JacobiTheta(2,z,tau)**4 + JacobiTheta(4,z,tau)**4)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("5a3ebf"),
    Formula(Equal(JacobiTheta(1,z,tau)**4 - JacobiTheta(2,z,tau)**4, JacobiTheta(4,z,tau)**4 - JacobiTheta(3,z,tau)**4)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("e08bb4"),
    Formula(Equal(JacobiTheta(1,z,tau)**4 - JacobiTheta(4,z,tau)**4, JacobiTheta(2,z,tau)**4 - JacobiTheta(3,z,tau)**4)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

# Sums of squares

make_entry(ID("fa7251"),
    Formula(Equal(JacobiTheta(2,0,tau)**2 * JacobiTheta(3,z,tau)**2, JacobiTheta(4,0,tau)**2 * JacobiTheta(1,z,tau)**2 + JacobiTheta(3,0,tau)**2 * JacobiTheta(2,z,tau)**2)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("265d9c"),
    Formula(Equal(JacobiTheta(2,0,tau)**2 * JacobiTheta(4,z,tau)**2, JacobiTheta(3,0,tau)**2 * JacobiTheta(1,z,tau)**2 + JacobiTheta(4,0,tau)**2 * JacobiTheta(2,z,tau)**2)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("0e2635"),
    Formula(Equal(JacobiTheta(3,0,tau)**2 * JacobiTheta(2,z,tau)**2, JacobiTheta(2,0,tau)**2 * JacobiTheta(3,z,tau)**2 - JacobiTheta(4,0,tau)**2 * JacobiTheta(1,z,tau)**2)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("6fad93"),
    Formula(Equal(JacobiTheta(3,0,tau)**2 * JacobiTheta(3,z,tau)**2, JacobiTheta(4,0,tau)**2 * JacobiTheta(4,z,tau)**2 + JacobiTheta(2,0,tau)**2 * JacobiTheta(2,z,tau)**2)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("abbe42"),
    Formula(Equal(JacobiTheta(3,0,tau)**2 * JacobiTheta(4,z,tau)**2, JacobiTheta(2,0,tau)**2 * JacobiTheta(1,z,tau)**2 + JacobiTheta(4,0,tau)**2 * JacobiTheta(3,z,tau)**2)),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

make_entry(ID("1c67c8"),
    Formula(Equal((JacobiTheta(1,z,tau)**2 - JacobiTheta(2,z,tau)**2)*JacobiTheta(2,0,2*tau), (JacobiTheta(4,z,tau)**2-JacobiTheta(3,z,tau)**2)*JacobiTheta(3,0,2*tau))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH))))

#-----------------------------------------------------------------------------#
#                                                                             #
#                           Specific values                                   #
#                                                                             #
#-----------------------------------------------------------------------------#

def_Topic(
    Title("Specific values of Jacobi theta functions"),
    Description("See", TopicReference("Jacobi theta functions"), "for other properties of these functions."),
    Section("Particular theta constants"),
    Subsection("Constant for the square lattice"),
    Entries(
        "d15f11",
        "1403b5",
        "8697b8",
        "0d4608",
        "7d7c65",
    ),
    Subsection("Conversion from index 2 and 4 to index 3"),
    Entries(
        "47f4ba",
        "e2288d",
        "cf7ee3",
        "81550a",
    ),
    Subsection("Algebraic ratios for real part 0"),
    Entries(
        "4256f0",
        "52302f",
        "7f9273",
        "cf3c8e",
        "f12e20",
        "95e9e4",
        "483e7e",
        "cb6c9c",
        "669765",
        "72f583",
        "8356db",
        "6ade92",
    ),
    Subsection("Algebraic ratios for real part 1"),
    Entries(
        "4c8873",
        "324483",
        "b58070",
        "6cbce8",
        "5384f3",
        "e2bc80",
        "390158",
        "675f23",
    ),
),

# Fundamental constant

make_entry(ID("d15f11"),
    Formula(Equal(JacobiTheta(3,0,ConstI), ConstPi**Div(1,4) / GammaFunction(Div(3,4)))))

make_entry(ID("1403b5"),
    Formula(Equal(JacobiTheta(3,0,ConstI), GammaFunction(Div(1,4)) / (Sqrt(2) * ConstPi**Div(3,4)))))

make_entry(ID("8697b8"),
    Formula(Element(JacobiTheta(3,0,ConstI), RealBall(Decimal("1.0864348112133080145753161215102234570702057072452"), Decimal("1.89e-50")))))

make_entry(ID("0d4608"),
    Formula(NotElement(JacobiTheta(3,0,ConstI), AlgebraicNumbers)),
    Description("Consequence of Nesterenko's theorem."))

make_entry(ID("7d7c65"),
    Formula(Equal(JacobiTheta(2,0,ConstI), JacobiTheta(4,0,ConstI), JacobiTheta(3,0,1+ConstI), Brackets(2**(-Div(1,4))) * JacobiTheta(3,0,ConstI))))

# Conversions

make_entry(ID("47f4ba"),
    Formula(Equal(JacobiTheta(2,0,y*ConstI), (1/Sqrt(y)) * JacobiTheta(3,0,1+ConstI/y))),
    Variables(y),
    Assumptions(Element(y, OpenInterval(0, Infinity))))

make_entry(ID("e2288d"),
    Formula(Equal(JacobiTheta(2,0,1+y*ConstI), ((1+ConstI)/Sqrt(2*y)) * JacobiTheta(3,0,1+ConstI/y))),
    Variables(y),
    Assumptions(Element(y, OpenInterval(0, Infinity))))

make_entry(ID("cf7ee3"),
    Formula(Equal(JacobiTheta(4,0,y*ConstI), JacobiTheta(3,0,1+y*ConstI))),
    Variables(y),
    Assumptions(Element(y, OpenInterval(0, Infinity))))

make_entry(ID("81550a"),
    Formula(Equal(JacobiTheta(4,0,1+y*ConstI), JacobiTheta(3,0,y*ConstI))),
    Variables(y),
    Assumptions(Element(y, OpenInterval(0, Infinity))))

# Algebraic ratios at real part zero

make_entry(ID("4256f0"),
    Formula(Equal(JacobiTheta(3,0,ConstI/2), Brackets(Sqrt((Sqrt(2)+1)/2) * 2**Div(1,4)) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("52302f"),
    Formula(Equal(JacobiTheta(3,0,ConstI/3), Brackets((2*Sqrt(3)+3)**Div(1,4)) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("7f9273"),
    Formula(Equal(JacobiTheta(3,0,ConstI/4), Brackets((1+2**(-Div(1,4)))/Sqrt(1+Sqrt(2)) * Sqrt((Sqrt(2)+1)/2) * 2**Div(1,2)) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("cf3c8e"),
    Formula(Equal(JacobiTheta(3,0,2*ConstI), Brackets(Sqrt(Sqrt(2)+2)/2) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("f12e20"),
    Formula(Equal(JacobiTheta(3,0,3*ConstI), Brackets(Sqrt(Sqrt(3)+1)/(Pow(2,Div(1,4)) * Pow(3,Div(3,8)))) * JacobiTheta(3,0,ConstI))),
#    Formula(Equal(JacobiTheta(3,0,3*ConstI), Brackets(1/Pow(6*Sqrt(3)-9, Div(1,4))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("95e9e4"),
    Formula(Equal(JacobiTheta(3,0,4*ConstI), Brackets((1+Pow(2, -Div(1,4)))/2) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("483e7e"),
    Formula(Equal(JacobiTheta(3,0,5*ConstI), Brackets(1/Sqrt(5*Sqrt(5)-10)) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("cb6c9c"),
    Formula(Equal(JacobiTheta(3,0,5*ConstI), Brackets(Sqrt(5+2*Sqrt(5))/Pow(5,Div(3,4))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("669765"),
    Formula(Equal(JacobiTheta(3,0,6*ConstI), Brackets((-4+3*Sqrt(2)+3**Div(5,4) + 2*Sqrt(3) - 3**Div(3,4) + 2*Sqrt(2)*Parentheses(3**Div(3,4)))**Div(1,3) / (2*Parentheses(3**Div(3,8))*((Sqrt(2)-1)*(Sqrt(3)-1))**Div(1,6))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("72f583"),
    Formula(Equal(JacobiTheta(3,0,7*ConstI), Brackets(Sqrt((((Sqrt(13 + Sqrt(7)) + Sqrt(7 + 3*Sqrt(7))) / 14) * Pow(Parentheses(28),Div(1,8))))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("8356db"),
    Formula(Equal(JacobiTheta(3,0,9*ConstI), Brackets((1 + Pow(2*(Sqrt(3)+1),Div(1,3)))/3) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("6ade92"),
    Formula(Equal(JacobiTheta(3,0,45*ConstI), Brackets(((3+Sqrt(5)+(Sqrt(3)+Sqrt(5)+Pow(60,Div(1,4)))*Pow(2+Sqrt(3), Div(1,3)))/(3*Sqrt(10+10*Sqrt(5))))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

# Algebraic ratios at real part one

make_entry(ID("4c8873"),
    Formula(Equal(JacobiTheta(3,0,1+ConstI), Brackets(2**(-Div(1,4))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("324483"),
    Formula(Equal(JacobiTheta(3,0,1+ConstI/2), Brackets((Pow(Sqrt(2)-1, Div(2,3)) * Pow(4 + 3*Sqrt(2), Div(1,12))) / Pow(2, Div(7,24))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("b58070"),
    Formula(Equal(JacobiTheta(3,0,1+2*ConstI), Brackets(2**(-Div(1,8))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("6cbce8"),
    Formula(Equal(JacobiTheta(3,0,1+4*ConstI), Brackets(2**(-Div(7,16)) * (Sqrt(2)+1)**Div(1,4)) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("5384f3"),
    Formula(Equal(JacobiTheta(3,0,1+6*ConstI), Brackets((1+Sqrt(3)+Sqrt(2)*27**Div(1,4))**Div(1,3) / (2**Div(11,24)*3**Div(3,8)*(Sqrt(3)-1)**Div(1,6))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("e2bc80"),
    Formula(Equal(JacobiTheta(3,0,1+8*ConstI), Brackets(2**(-Div(7,8)) * (16 + 15*2**Div(1,4) + 12*Sqrt(2) + 9*8**Div(1,4))**Div(1,8)) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("390158"),
    Formula(Equal(JacobiTheta(3,0,1+10*ConstI), Brackets(2**Div(7,8) / ((5**Div(1,4)-1)*Sqrt(5*Sqrt(5)+5))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

make_entry(ID("675f23"),
    Formula(Equal(JacobiTheta(3,0,1+12*ConstI), Brackets(2**(-Div(19,48)) * 3**(-Div(3,8)) * (2-3*Sqrt(2)+3**Div(5,4)+3**Div(3,4))**Div(1,3) / ((Sqrt(2)-1)**Div(1,12)*(Sqrt(3)+1)**Div(1,6)*(-1-Sqrt(3)+Sqrt(2)*Parentheses(3**Div(3,4)))**Div(1,3))) * JacobiTheta(3,0,ConstI))),
    References("https://doi.org/10.1016/j.jmaa.2003.12.009"))

