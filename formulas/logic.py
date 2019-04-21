# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Elementary logic and set theory"),
    Entries(
        "cf447f",
        "66ca58",
        "81efd5",
    ),
)

make_entry(ID("cf447f"),
    SymbolDefinition(Set, Set(Ellipsis), "Set with given elements"),
    Description(SourceForm(Set(x, y, Ellipsis)), ", rendered as", Set(x, y, Ellipsis),
        ", represents the finite set containing the given elements.",
        "In particular, ", SourceForm(Set()), "or", Set(),
            "is the empty set, and", SourceForm(Set(x)), "or", Set(x), "is a singleton set."))

make_entry(ID("66ca58"),
    SymbolDefinition(SetBuilder, SetBuilder(f(x), x, P(x)), "Set comprehension"),
    Description("Called with 3 arguments", SourceForm(SetBuilder(f(x), x, P(x))), ", rendered as", SetBuilder(f(x), x, P(x)),
        ", represents the set of values", f(x), "for all", x, "satisfying the predicate", P(x), "."),
    description_x_predicate)


make_entry(ID("81efd5"),
    SymbolDefinition(Cardinality, Cardinality(S), "Set cardinality"),
    Description(SourceForm(Cardinality(S)), ", rendered as", Cardinality(S),
        ", represents the cardinality of the set", S, ".",
        "The cardinality of a finite set is a nonnegative integer.",
        "Cardinalities of infinite sets may be represented in terms of this symbol;",
        "for example,", Cardinality(ZZ), "is the cardinality of any countable set",
        "and", Cardinality(RR), "is the cardinality of the continuum."))


"""

Not And Or Equivalent Implies

Set List Tuple

PowerSet
Union Intersection SetMinus
Element NotElement Subset SubsetEqual




EqualAndElement




76dcd2
4859f4
fe71db
98beb3
cd3986
ef370d
45bc43
73c495
8a2bca
c6a864
150f0a
6556d4
bf2fc7
c84a18


Set()
Set(x)

Set(f(x), x, Element(x, S))

SetBuilder(f(x), Element(x, S))


Supremum(f(x), x, Element(x, ZZ))


Sum(f(k), r, Range(0, k - 1), Equal(GCD(r, k), 1)))



Sum(f(k), Tuple(k, a, b))

Sum(f(k), k, Indices(k, a, b))

    The sum is only defined if the absolutely convergent


Sum(S)

Sum(f(x), x, P(x))



CC = SetBuilder(x + y*ConstI, Var(x, y), Element(x, CC), Element(y, CC))





Zeros(f(x), x, Element(x, CC))



Sum(Set(f(k), k, P(k)))


Sum(f(k), Variables(k), Element(k, ZZ))


Equal(SL2Z, SetBuilder(Matrix2x2(a, b, c, d), Tuple(a, b, c, d), ZZ


And(Element(a,ZZ), Element(b,ZZ), Element(c,ZZ), Element(d,ZZ), Equal(a*d-b*c, 1))))


Equal(SL2Z, SetBuilder(Matrix2x2(a, b, c, d), And(Element(a,ZZ), Element(b,ZZ), Element(c,ZZ), Element(d,ZZ), Equal(a*d-b*c, 1))))

Equal(PSL2Z, SetBuilder(Matrix2x2(a, b, c, d), And(Element(Matrix2x2(a, b, c, d), SL2Z), Or(Greater(c, 0), And(Equal(c, 0), Greater(d, 0))))))





Maximum


Sum(f(k), k, 



Sum(f(k), r, And(Indices(r, 0, k - 1), Equal(GCD(r, k), 1)))



Sum(Mul(Exp(Mul(Mul(ConstPi, ConstI), Sub(DedekindSum(r, k), Div(Mul(Mul(2, n), r), k))))), r, Range(0, k - 1), Equal(GCD(r, k), 1))




Maximum(f(x), Element(x, S))

Supremum(f(x), x, Element(x, S))


Over(x, S)



(GCD(r, k)

Tuple(r, 0, Sub(k, 1))))),

Sum(f(x), x, Limits(a, b))


Sum(f(x), x, ZZGreaterEqual(0), Divides(x)


Supremum(f(x), x, Element(x, S))

Filter(Tuple(x, y), 

SetBuilder(x+y*ConstI, Tuple(x, y), Tuple(RR, RR))



Sum(1/p**2, Element(p, PP))

Sum(1/p, p, And(Element(p, PP), Divides(Parentheses(p-1), 2*n)))



formulas/bernoulli_numbers.py:    Formula(Element(Parentheses(BernoulliB(2*n) + SumCondition(1/p, p, And(Element(p, PP), Divides(Parentheses(p-1), 2*n)))), ZZ)),
formulas/expr.py:        if head in (SumCondition, ProductCondition):
formulas/expr.py:            if head is SumCondition:
formulas/expr.py:SumCondition ProductCondition
formulas/weierstrass_elliptic.py:    Formula(Equal(WeierstrassP(z,tau), 1/z**2 + SumCondition(1/(z+m+n*tau)**2-1/(m+n*tau)**2, Tuple(m, n), Unequal(m**2+n**2, 0)))),
formulas/weierstrass_elliptic.py:        1/z + SumCondition(1/(z-m-n*tau)+1/(m+n*tau)+z/(m+n*tau)**2, Tuple(m, n), Unequal(m**2+n**2, 0)))),



formulas/complex_plane.py:    Formula(Equal(CC, SetBuilder(x+y*ConstI, And(Element(x, RR), Element(y, RR))))))

formulas/complex_plane.py:    Formula(Equal(HH, SetBuilder(tau, And(Element(tau, CC), Greater(Im(tau), 0))))))

formulas/complex_plane.py:    Formula(Equal(UnitCircle, SetBuilder(z, And(Element(z, CC), Equal(Abs(z), 1))))))

formulas/complex_plane.py:    Formula(Equal(UnitCircle, SetBuilder(Exp(ConstI*theta), Element(t, ClosedOpenInterval(0, 2*ConstPi))))))

formulas/complex_plane.py:    Formula(Equal(OpenDisk(z, r), SetBuilder(t, And(Element(t, CC), Less(Abs(z-t), r))))),

formulas/complex_plane.py:    Formula(Equal(ClosedDisk(z, r), SetBuilder(t, And(Element(t, CC), LessEqual(Abs(z-t), r))))),

formulas/complex_plane.py:    Formula(Equal(BernsteinEllipse(rho), SetBuilder(Div(rho*Exp(ConstI*theta) + rho**(-1)*Exp(-(ConstI*theta)), 2), Element(theta, ClosedOpenInterval(0, 
2*ConstPi))))),

formulas/const_gamma.py:    Formula(NotElement(ConstGamma, SetBuilder(p/q, And(Element(p,ZZ), Element(q, ZZGreaterEqual(1)), LessEqual(q, Pow(10,242080)))))),

formulas/expr.py:        if head is SetBuilder:

formulas/expr.py:SetBuilder

formulas/expr.py:    SetBuilder, "instead to construct finite and infinite sets without explicitly listing each element."))

formulas/jacobi_theta.py:    Formula(Equal(Zeros(JacobiTheta1(z,tau), z, CC), SetBuilder(m+n*tau, And(Element(m, ZZ), Element(n, ZZ))))),

formulas/jacobi_theta.py:    Formula(Equal(Zeros(JacobiTheta2(z,tau), z, CC), SetBuilder(Parentheses(m+Div(1,2))+n*tau, And(Element(m, ZZ), Element(n, ZZ))))),

formulas/jacobi_theta.py:    Formula(Equal(Zeros(JacobiTheta3(z,tau), z, CC), SetBuilder(Parentheses(m+Div(1,2))+(n+Div(1,2))*tau, And(Element(m, ZZ), Element(n, ZZ))))),

formulas/jacobi_theta.py:    Formula(Equal(Zeros(JacobiTheta4(z,tau), z, CC), SetBuilder(m+(n+Div(1,2))*tau, And(Element(m, ZZ), Element(n, ZZ))))),

formulas/legendre_polynomial.py:    Formula(Equal(Zeros(LegendrePolynomial(n,z), z, CC), SetBuilder(LegendrePolynomialZero(n,k), Element(k, ZZBetween(1, n))))),

formulas/modular_j.py:    Formula(Equal(Zeros(ModularJ(tau), tau, HH), SetBuilder(ModularGroupAction(gamma, Exp(2*ConstPi*ConstI/3)), Element(gamma, PSL2Z)))))

formulas/modular_j.py:    Formula(Equal(SetBuilder(ModularJ(tau), Element(tau, ModularGroupFundamentalDomain)), CC)))

formulas/modular_transformations.py:    Formula(Equal(SL2Z, SetBuilder(Matrix2x2(a, b, c, d), And(Element(a,ZZ), Element(b,ZZ), Element(c,ZZ), Element(d,ZZ), Equal(a*d-b*c, 1))))))

formulas/modular_transformations.py:    Formula(Equal(PSL2Z, SetBuilder(Matrix2x2(a, b, c, d), And(Element(Matrix2x2(a, b, c, d), SL2Z), Or(Greater(c, 0), And(Equal(c, 0), Greater(d, 0))))))))

formulas/modular_transformations.py:    Formula(Equal(ModularGroupFundamentalDomain, SetBuilder(tau, And(Element(tau, HH),

formulas/modular_transformations.py:    Formula(Equal(SetBuilder(ModularGroupAction(gamma, tau), And(Element(tau, ModularGroupFundamentalDomain), Element(gamma, PSL2Z))), HH)))

formulas/operators.py:        ", represents", Supremum(SetBuilder(f(x), Element(x, S))), "."),

formulas/operators.py:        ", represents", Supremum(SetBuilder(f(x), Element(x, S))), "."),

formulas/operators.py:        ", represents", Minimum(SetBuilder(f(x), Element(x, S))), "."),

formulas/operators.py:        ", represents", Maximum(SetBuilder(f(x), Element(x, S))), "."),

formulas/prime_numbers.py:    Formula(Equal(PP, SetBuilder(PrimeNumber(n), Element(n, ZZGreaterEqual(1))))))

formulas/prime_numbers.py:    Formula(Equal(PrimePi(x), Cardinality(SetBuilder(p, And(Element(p, PP), LessEqual(p, x)))))),

formulas/riemann_zeta.py:    Formula(Equal(Zeros(RiemannZeta(s), s, RR), SetBuilder(-(2*n), Element(n, ZZGreaterEqual(1))))))

formulas/riemann_zeta.py:    Formula(Equal(Zeros(RiemannZeta(s), s, CC), Union(SetBuilder(-(2*n), Element(n, ZZGreaterEqual(1))),

formulas/riemann_zeta.py:        SetBuilder(RiemannZetaZero(n), And(Element(n, ZZ), Unequal(n, 0)))))))

formulas/weierstrass_elliptic.py:    Formula(Equal(Lattice(a,b), SetBuilder(a*m+b*n, And(Element(m,ZZ), Element(n,ZZ))))),

formulas/weierstrass_elliptic.py:    Formula(Equal(Zeros(WeierstrassP(z,ConstI),z,CC), SetBuilder(Parentheses(m+Div(1,2))+(n+Div(1,2))*ConstI, And(Element(m, ZZ), Element(n, ZZ))))))

"""

