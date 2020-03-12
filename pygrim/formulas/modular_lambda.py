# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Modular lambda function"),
    Section("Definitions"),
    Entries(
        "f53771",
        "6c6204",
    ),
    Section("Illustrations"),
    Entries(
        "f0981b",
        "fc6cf6",
    ),
    Section("Domain"),
    Entries(
        "813d25",
        "c7f85b",
        "ad5aff",
        "55ee4a",
    ),
    Section("Modular transformations"),
    Subsection("Level 2 principal subgroup"),
    Entries(
        "6678af",
        "ec5a44",
        "21839d",
    ),
    Subsection("Arbitrary modular transformations"),
    Entries(
        "73427b",
        "bbfb6c",
        "07bf27",
        "e9f0c8",
        "2ba627",
        "3a7a0b",
        "099301",
    ),
    Subsection("Fundamental domain"),
    Entries(
        "737f2b",
        "b23575",
    ),
    Section("Theta function representations"),
    Entries(
        "5b9c02",
        "903962",
        "04d3a6",
    ),
    Section("Dedekind eta function representations"),
    Entries(
        "5dd24a",
        "033d39",
    ),
    Section("Elliptic function representations"),
    Entries(
        "166402",
    ),
    Section("Fourier series (q-series)"),
    Entries(
        "921f34",
        "e96684",
        "ac236f",
    ),
    Section("Range"),
    Entries(
        "90b419",
        "4b20ab",
        "e4315f",
        "830dd4",
    ),
    Section("Specific values"),
    Entries(
        "a35b3c",
        "fe2627",
        "078869",
        "ea56d1",
        "b0e1cb",
        "4877f2",
        "35c85f",
    ),
    Subsection("Limiting values"),
    Entries(
        "e8252c",
        "231141",
    ),
    Section("Inverse and transcendental equations"),
    Entries(
        "b7174d",
        "5d550c",
    ),
    Section("Connection to the j-invariant"),
    Entries(
        "44a529",
    ),
    Section("Derivatives"),
    Entries(
        "27b2c7",
        "c18c95",
        "38b4f3",
    ),
)

make_entry(ID("f53771"),
    SymbolDefinition(ModularLambda, ModularLambda(tau), "Modular lambda function"),
    Description("The modular lambda function", ModularLambda(tau), "is a function of one variable", tau, "in the upper half-plane."),
    CodeExample(ModularLambda(tau), "represents the modular lambda function evaluated at", tau, "."))

make_entry(ID("6c6204"),
    SymbolDefinition(ModularLambdaFundamentalDomain, ModularLambdaFundamentalDomain, "Fundamental domain of the modular lambda function"),
    Description("This subset of the upper half-planed is defined by ", EntryReference("737f2b"), "."))

# Illustrations

make_entry(ID("f0981b"),
    Image(Description("X-ray of", ModularLambda(tau), "on", Element(tau, ClosedInterval(-Div(3,2),Div(3,2)) + ClosedInterval(0,2)*ConstI), "with", ModularLambdaFundamentalDomain, "highlighted"),
        ImageSource("xray_modular_lambda")),
    description_xray)

make_entry(ID("fc6cf6"),
    Image(Description("Plot of", ModularLambda(ConstI*x), "on", Element(x, ClosedInterval(0,4))),
        ImageSource("plot_modular_lambda")),
    description_xray)

# Domain

make_entry(ID("813d25"),
    Formula(Implies(Element(tau, HH), Element(ModularLambda(tau), SetMinus(CC, Set(0, 1))))),
    Variables(tau))

make_entry(ID("c7f85b"),
    Formula(Implies(Element(tau, Set(ConstI*Infinity)), Element(ModularLambda(tau), Set(0)))),
    Variables(tau))

make_entry(ID("ad5aff"),
    Formula(Implies(Element(tau, Set(2*n, ForElement(n, ZZ))), Element(ModularLambda(tau), Set(1)))),
    Variables(tau))

make_entry(ID("55ee4a"),
    Formula(IsHolomorphic(ModularLambda(tau), ForElement(tau, Union(HH, Set(ConstI*Infinity))))))

# Modular transformations

make_entry(ID("6678af"),
    Formula(Equal(ModularLambda(tau+2), ModularLambda(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("ec5a44"),
    Formula(Equal(ModularLambda(tau/(2*tau+1)), ModularLambda(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))


make_entry(ID("21839d"),
    Formula(Equal(ModularLambda((a*tau+b)/(c*tau+d)), ModularLambda(tau))),
    Variables(tau, a, b, c, d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a,b,c,d), SL2Z), CongruentMod(Matrix2x2(a,b,c,d), Matrix2x2(1,0,0,1), 2))))

lam = ModularLambda(tau)

make_entry(ID("73427b"),
    Formula(Element(ModularLambda((a*tau+b)/(c*tau+d)), Set(lam, 1-lam, 1/lam, 1/(1-lam), (lam-1)/lam, lam/(lam-1)))),
    Variables(tau, a, b, c, d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a,b,c,d), SL2Z))))

make_entry(ID("bbfb6c"),
    Formula(Equal(ModularLambda(tau+1), lam/(lam-1))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("07bf27"),
    Formula(Equal(ModularLambda(-(1/tau)), 1-lam)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("e9f0c8"),
    Formula(Equal(ModularLambda(tau/(1-tau)), 1/lam)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("2ba627"),
    Formula(Equal(ModularLambda(1/(1-tau)), 1/(1-lam))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("3a7a0b"),
    Formula(Equal(ModularLambda((tau-1)/tau), (lam-1)/lam)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("099301"),
    Formula(Equal(ModularLambda((a*tau+b)/(c*tau+d)),
        Cases(
            Tuple(lam, CongruentMod(Tuple(a,b,c,d), Tuple(1,0,0,1), 2)),
            Tuple(1-lam, CongruentMod(Tuple(a,b,c,d), Tuple(0,1,1,0), 2)),
            Tuple(1/lam, CongruentMod(Tuple(a,b,c,d), Tuple(1,0,1,1), 2)),
            Tuple(1/(1-lam), CongruentMod(Tuple(a,b,c,d), Tuple(0,1,1,1), 2)),
            Tuple((lam-1)/lam, CongruentMod(Tuple(a,b,c,d), Tuple(1,1,1,0), 2)),
            Tuple(lam/(lam-1), CongruentMod(Tuple(a,b,c,d), Tuple(1,1,0,1), 2))))),
    Variables(tau, a, b, c, d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a,b,c,d), SL2Z))))


## Fundamental domain

make_entry(ID("737f2b"),
    Formula(Equal(ModularLambdaFundamentalDomain, Set(tau, For(tau), And(Element(tau, HH),
        Or(And(Element(Re(tau), OpenInterval(-1,1)),
            Greater(Min(Abs(tau-Div(1,2)), Abs(z+Div(1,2))), Div(1,2))),
            Equal(Re(tau), -1),
            Equal(Abs(tau+Div(1,2)), Div(1,2))))))),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987. p. 113."))

make_entry(ID("b23575"),
    Formula(Equal(HH, Set(ModularGroupAction(gamma, tau), For(Tuple(tau, gamma)),
        And(Element(tau, ModularLambdaFundamentalDomain),
            Element(gamma, SL2Z),
            CongruentMod(gamma, Matrix2x2(1,0,0,1), 2))))))

# Theta function representations

make_entry(ID("5b9c02"),
    Formula(Equal(ModularLambda(tau), JacobiTheta(2,0,tau)**4 / JacobiTheta(3,0,tau)**4)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("903962"),
    Formula(Equal(lam/(lam-1), -(JacobiTheta(2,0,tau)**4 / JacobiTheta(4,0,tau)**4))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("04d3a6"),
    Formula(Equal(1-lam, JacobiTheta(4,0,tau)**4 / JacobiTheta(3,0,tau)**4)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Dedekind eta function representations

make_entry(ID("5dd24a"),
    Formula(Equal(ModularLambda(tau), 16 * (DedekindEta(tau/2)**8 * DedekindEta(2*tau)**16 / DedekindEta(tau)**24))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("033d39"),
    Formula(Equal(1/ModularLambda(tau), Div(1,16) * (DedekindEta(tau/2)**8 / (DedekindEta(2*tau)**8)) + 1)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Elliptic function representations

_e1 = WeierstrassP(Div(1,2), tau)
_e2 = WeierstrassP(Div(tau,2), tau)
_e3 = WeierstrassP(Div(1,2)*(1+tau), tau)

make_entry(ID("166402"),
    Formula(Equal(ModularLambda(tau), (_e3 - _e2) / (_e1 - _e2))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Fourier series (q-series)

make_entry(ID("921f34"),
    Formula(EqualQSeriesEllipsis(ModularLambda(tau), tau, q, 16*q - 128*q**2 + 704*q**3 - 3072*q**4 + 11488*q**5 - 38400*q**6, Equal(q, Exp(Pi*ConstI*tau)))),
    Variables(tau),
    Assumptions(Element(tau, HH)),
    References("https://oeis.org/A115977"))

make_entry(ID("e96684"),
    Formula(Equal(ModularLambda(tau), Where(16*q*Product(((1+q**(2*k))/(1+q**(2*k-1)))**8, For(k, 1, Infinity)), Equal(q, Exp(Pi*ConstI*tau))))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("ac236f"),
    Formula(Where(AsymptoticTo(a(n), (-1)**(n+1) * (Exp(2*Pi*Sqrt(n)) / (32 * n**Div(3,4))),
        n, Infinity), Equal(a(n), QSeriesCoefficient(ModularLambda(tau), tau, q, n, Equal(q, Exp(Pi*ConstI*tau)))))),
    References("https://oeis.org/A115977"))

# Range

make_entry(ID("90b419"),
    Formula(Equal(Set(ModularLambda(tau), ForElement(tau, HH)),
        Set(ModularLambda(tau), ForElement(tau, ModularLambdaFundamentalDomain)), SetMinus(CC, Set(0, 1)))))

make_entry(ID("4b20ab"),
    Formula(Equal(Set(ModularLambda(tau), For(tau), And(Element(tau, HH), Equal(Re(tau), -1))), OpenInterval(-Infinity, 0))),
    Description("This mapping is one-to-one."),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987. p. 118."))

make_entry(ID("e4315f"),
    Formula(Equal(Set(ModularLambda(tau), For(tau), And(Element(tau, HH), Equal(Abs(tau+Div(1,2)), Div(1,2)))), OpenInterval(1, Infinity))),
    Description("This mapping is one-to-one."),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987. p. 118."))

make_entry(ID("830dd4"),
    Formula(Equal(Set(ModularLambda(tau), For(tau), Element(tau, Interior(ModularLambdaFundamentalDomain))),
        SetMinus(CC, Parentheses(Union(OpenClosedInterval(-Infinity, 0), ClosedOpenInterval(1, Infinity)))))),
    Description("This mapping is one-to-one."),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987. p. 118."))

# Specific values

make_entry(ID("a35b3c"),
    Formula(Equal(ModularLambda(ConstI), Div(1,2))))

make_entry(ID("fe2627"),
    Formula(Equal(ModularLambda(1+ConstI), -1)))

make_entry(ID("078869"),
    Formula(Equal(ModularLambda((1+ConstI)/2), 2)))

make_entry(ID("ea56d1"),
    Formula(Element(ModularLambda((a*ConstI+b)/(c*ConstI+d)), Set(-1, Div(1,2), 2))),
    Variables(a, b, c, d),
    Assumptions(Element(Matrix2x2(a,b,c,d), SL2Z)))

make_entry(ID("b0e1cb"),
    Formula(Where(Equal(ModularLambda(omega), -omega), Equal(omega, Exp(2*Pi*ConstI/3)))))

make_entry(ID("4877f2"),
    Formula(Equal(ModularLambda(ConstI/2), 12*Sqrt(2)-16)))

make_entry(ID("35c85f"),
    Formula(Equal(ModularLambda(2*ConstI), 17 - 12*Sqrt(2))))

# Limiting values

make_entry(ID("e8252c"),
    Formula(Equal(ModularLambda(ConstI*Infinity), ComplexLimit(ModularLambda(tau), For(tau, ConstI*Infinity)), 0)))

make_entry(ID("231141"),
    Formula(Equal(RightLimit(ModularLambda(n+ConstI*epsilon), For(epsilon, 0)), Cases(Tuple(1, Even(n)), Tuple(-Infinity, Odd(n))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# Inverse and transcendental equations

make_entry(ID("b7174d"),
    Formula(Equal(tau, ConstI * (EllipticK(1-ModularLambda(tau))/EllipticK(ModularLambda(tau))))),
    Variables(tau),
    Assumptions(Element(tau, Union(Interior(ModularLambdaFundamentalDomain), Set(tau, For(tau), And(Element(tau, HH), Equal(Re(tau), 1)))))))

tau1 = Subscript(tau,1)

make_entry(ID("5d550c"),
    Formula(Equal(tau, ConstI * (EllipticK(1-ModularLambda(tau))/EllipticK(ModularLambda(tau))) + 2 * Ceil(Div(1,2)*Re(tau) - Div(1,2)))),
    Variables(tau),
    Assumptions(Element(tau, Set(tau1+n, For(Tuple(tau1, n)), And(Element(tau1, Interior(ModularLambdaFundamentalDomain)), Element(n, ZZ))))))

make_entry(ID("44a529"),
    Formula(Equal(ModularJ(tau), 256 * ((1-ModularLambda(tau)+ModularLambda(tau)**2)**3 / (ModularLambda(tau)**2 * (1 - ModularLambda(tau))**2)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Derivatives

make_entry(ID("27b2c7"),
    Formula(Equal(ComplexDerivative(ModularLambda(tau), For(tau, tau)),
        ((Pi*ConstI)/3) * (EisensteinE(2,tau/2) + 8*EisensteinE(2,2*tau) - 6*EisensteinE(2,tau)) * ModularLambda(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("c18c95"),
    Formula(Equal(ComplexDerivative(ModularLambda(tau), For(tau, tau)),
        ((2*ConstI)/Pi) * (WeierstrassZeta(Div(1,2),tau/2) + 8*WeierstrassZeta(Div(1,2),2*tau) - 6*WeierstrassZeta(Div(1,2),tau)) * ModularLambda(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("38b4f3"),
    Formula(Equal(ComplexDerivative(ModularLambda(tau), For(tau, tau)),
        -((4*ConstI)/Pi) * EllipticK(ModularLambda(tau))**2 * (ModularLambda(tau)-1) * ModularLambda(tau))),
    Variables(tau),
    Assumptions(Element(tau, Set(tau1+n, For(Tuple(tau1, n)), And(Element(tau1, Interior(ModularLambdaFundamentalDomain)), Element(n, ZZ))))),
    References("http://functions.wolfram.com/EllipticFunctions/ModularLambda/20/01/0001/ Note: because of the branch cut of the elliptic integral, only valid on part of the domain."))

