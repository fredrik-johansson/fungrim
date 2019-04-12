from .expr import *

def_Topic(
    Title("Modular transformations"),
    Entries(
        "094772",
        "1e211d",
        "76de9d",
        "dc2c26",
    ),
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

make_entry(ID("094772"),
    SymbolDefinition(SL2Z, SL2Z, "Modular group"),
    Description("Whether", SL2Z, "or", PSL2Z,
    """should be called "the modular group" is an arbitrary convention. Here we allow any element of""",
    SL2Z, "to represent an element of the modular group, but we use", PSL2Z, "when uniqueness is desired."))

make_entry(ID("1e211d"),
    SymbolDefinition(PSL2Z, PSL2Z, "Modular group (canonical representatives)"))

make_entry(ID("76de9d"),
    SymbolDefinition(ModularGroupAction, ModularGroupAction(gamma, tau), "Action of modular group"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(gamma, SL2Z), Element(tau, HH)), Element(ModularGroupAction(gamma, tau), HH)),
      )))

# todo: in PowerSet(HH)
make_entry(ID("dc2c26"),
    SymbolDefinition(ModularGroupFundamentalDomain, ModularGroupFundamentalDomain, "Fundamental domain for action of the modular group"))


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
        Element(Re(tau), ClosedOpenInterval(-Div(1,2), Div(1,2))),
            Or(Greater(Abs(tau), 1), And(Equal(Abs(tau), 1), LessEqual(Re(tau), 0))))))),
    Description("The choice to include the left or right boundary is arbitrary; the present definition follows Cohen and simplifies the treatment of reduced binary quadratic forms."),
    References("H. Cohen, A Course in Computational Algebraic Number Theory, Springer, 1993"))

make_entry(ID("1d1028"),
    Formula(Element(ConstI, ModularGroupFundamentalDomain)))

make_entry(ID("21b67f"),
    Formula(EqualAndElement(Exp(2*ConstPi*ConstI/3), (-1+Sqrt(3)*ConstI)/2, ModularGroupFundamentalDomain)),
    Description("Corner of the fundamental domain."))

make_entry(ID("e28209"),
    Formula(Less(Abs(Exp(2*ConstPi*ConstI*tau)), Decimal("0.004334"))),   # exp(-pi sqrt(3)) ...
    Variables(tau),
    Assumptions(Element(tau, ModularGroupFundamentalDomain)))

make_entry(ID("fd53ab"),
    Formula(Equal(SetBuilder(ModularGroupAction(gamma, tau), And(Element(tau, ModularGroupFundamentalDomain), Element(gamma, PSL2Z))), HH)))

