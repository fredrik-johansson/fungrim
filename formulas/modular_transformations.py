from .expr import *

def_Topic(
    Title("Modular transformations"),
    Section("Basic formulas"),
    Entries(
        "d7962e",   # HH
        "c84f3f",   # def SL2Z
        "80279d",   # def PSL2Z
        "127a52",   # modular transformation
        "5636db",
    ),
    Section("Fundamental domain"),
    Entries(
        "a637cd",   # fundamental domain
        "1d1028",   # membership of i
        "21b67f",   # corner
        "e28209",
        "fd53ab",   # H from copies of F
    ),
)


make_entry(ID("c84f3f"),
    Formula(Equal(SL2Z, SetBuilder(Matrix2x2(a, b, c, d), And(Element(a,ZZ), Element(b,ZZ), Element(c,ZZ), Element(d,ZZ), Equal(a*d-b*c, 1))))))

make_entry(ID("80279d"),
    Formula(Equal(PSL2Z, SetBuilder(Matrix2x2(a, b, c, d), And(Element(Matrix2x2(a, b, c, d), SL2Z), Or(Greater(c, 0), And(Equal(c, 0), Greater(d, 0))))))))

make_entry(ID("127a52"),
    Formula(Equal(ModularGroupAction(Matrix2x2(a, b, c, d), tau), (a * tau + b) / (c * tau + d))),
    Assumptions(And(Element(Matrix2x2(a, b, c, d), SL2Z), Element(tau, HH))))

# todo: subscript gammas?
# todo: auto-parens in latex output
make_entry(ID("5636db"),
    Formula(Equal(ModularGroupAction(Parenthesis(Mul(gamma, eta)), tau), ModularGroupAction(gamma, Parenthesis(ModularGroupAction(eta, tau))))),
    Variables(gamma, eta, tau),
    Assumptions(And(Element(gamma, SL2Z), Element(eta, SL2Z), Element(tau, HH))))

make_entry(ID("a637cd"),
    Formula(Equal(ModularGroupFundamentalDomain, SetBuilder(tau, And(Element(tau, HH),
        Less(-Div(1,2), Re(tau)), LessEqual(Re(tau), Div(1,2)),
            Or(Greater(Abs(tau), 1), And(Equal(Abs(tau), 1), GreaterEqual(Re(tau), 0))))))))

make_entry(ID("1d1028"),
    Formula(Element(ConstI, ModularGroupFundamentalDomain)))

make_entry(ID("21b67f"),
    Formula(Element(Exp(ConstPi*ConstI/3), ModularGroupFundamentalDomain)))

make_entry(ID("e28209"),
    Formula(Less(Abs(Exp(2*ConstPi*ConstI*tau)), Decimal("0.004334"))),   # exp(-pi sqrt(3)) ...
    Variables(tau),
    Assumptions(Element(tau, ModularGroupFundamentalDomain)))

make_entry(ID("fd53ab"),
    Formula(Equal(SetBuilder(ModularGroupAction(gamma, tau), And(Element(tau, ModularGroupFundamentalDomain), Element(gamma, PSL2Z))), HH)))

"""








1af2a3

"""
