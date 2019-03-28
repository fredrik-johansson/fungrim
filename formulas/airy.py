# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Airy functions"),
    Section("Differential equation"),
    Entries(
        "51b241",
        "de9800",  # Wronskian
    ),
    Section("Special values"),
    Entries(
        "693cfe",
        "807917",
        "9a8d4d",
        "fba07c",
    ),
    Section("Higher derivatives"),
    Entries(
        "b2e9d0",  # ai''
        "70ec9f",  # bi''
        "eadca2",  # recurrence
    ),
    Section("Hypergeometric representations"),
    Entries(
        "01bbb6",
        "bd319e",
    ),
    Section("Analytic properties"),
    Entries(
        "def37e",
        "1f0577",
        "90f31e",
        "b88f65",
        "7194d4",
        "d1f9d0",
        "a2df77",
    ),        
)



make_entry(ID("51b241"),
    Formula(Where(Equal(Derivative(y(z), Tuple(z, z, 2)) - z*y(z), 0), Equal(y(z), C*AiryAi(z) + D*AiryBi(z)))),
    Variables(z, C, D),
    Assumptions(And(Element(z, CC), Element(C, CC), Element(D, CC))))

make_entry(ID("de9800"),
    Formula(Equal(AiryAi(z)*AiryBiPrime(z)-AiryAiPrime(z)*AiryBi(z), 1/ConstPi)),
    Variables(z),
    Element(z, CC))

make_entry(ID("693cfe"),
    Formula(Equal(AiryAi(0), Div(1, Pow(3,Div(2,3))*GammaFunction(Div(2,3))))))

make_entry(ID("807917"),
    Formula(Equal(AiryAiPrime(0), -Div(1, Pow(3,Div(1,3))*GammaFunction(Div(1,3))))))

make_entry(ID("9a8d4d"),
    Formula(Equal(AiryBi(0), Div(1, Pow(3,Div(1,6))*GammaFunction(Div(2,3))))))

make_entry(ID("fba07c"),
    Formula(Equal(AiryBiPrime(0), Div(Pow(3,Div(1,6)), GammaFunction(Div(1,3))))))

make_entry(ID("b2e9d0"),
    Formula(Equal(Derivative(AiryAi(z), Tuple(z, z, 2)), z*AiryAi(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("70ec9f"),
    Formula(Equal(Derivative(AiryBi(z), Tuple(z, z, 2)), z*AiryBi(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("eadca2"),
    Formula(Where(Equal(Derivative(y(z), Tuple(z, z, n)), z*Derivative(y(z), Tuple(z, z, n-2)) + (n-2)*Derivative(y(z), Tuple(z, z, n-3))),
        Equal(y(z), C*AiryAi(z) + D*AiryBi(z)))),
    Variables(n, z, C, D),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(3)), Element(C, CC), Element(D, CC))))

make_entry(ID("01bbb6"),
    Formula(Equal(AiryAi(z), AiryAi(0)*Hypergeometric0F1(Div(2,3),z**3/9) + z*AiryAiPrime(0)*Hypergeometric0F1(Div(4,3),z**3/9))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("bd319e"),
    Formula(Equal(AiryBi(z), AiryBi(0)*Hypergeometric0F1(Div(2,3),z**3/9) + z*AiryBiPrime(0)*Hypergeometric0F1(Div(4,3),z**3/9))),
    Variables(z),
    Assumptions(Element(z, CC)))



make_entry(ID("def37e"),
    Formula(Equal(HolomorphicDomain(C*AiryAi(z) + D*AiryBi(z), z, Union(CC, Set(UnsignedInfinity))), CC)),
    Variables(C, D),
    Assumptions(And(Element(C, CC), Element(D, CC), Not(And(Equal(C,0), Equal(D,0))))))

make_entry(ID("1f0577"),
    Formula(Equal(Poles(C*AiryAi(z) + D*AiryBi(z), z, Union(CC, Set(UnsignedInfinity))), Set())),
    Variables(C, D),
    Assumptions(And(Element(C, CC), Element(D, CC), Not(And(Equal(C,0), Equal(D,0))))))

make_entry(ID("90f31e"),
    Formula(Equal(EssentialSingularities(C*AiryAi(z) + D*AiryBi(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))),
    Variables(C, D),
    Assumptions(And(Element(C, CC), Element(D, CC), Not(And(Equal(C,0), Equal(D,0))))))

make_entry(ID("b88f65"),
    Formula(Equal(BranchPoints(C*AiryAi(z) + D*AiryBi(z), z, Union(CC, Set(UnsignedInfinity))), Set())),
    Variables(C, D),
    Assumptions(And(Element(C, CC), Element(D, CC))))

make_entry(ID("7194d4"),
    Formula(Equal(BranchCuts(C*AiryAi(z) + D*AiryBi(z), z, CC), Set())),
    Variables(C, D),
    Assumptions(And(Element(C, CC), Element(D, CC))))

make_entry(ID("d1f9d0"),
    Formula(Subset(Zeros(AiryAi(z), z, CC), RR)))

make_entry(ID("a2df77"),
    Formula(Subset(Zeros(AiryAiPrime(z), z, CC), RR)))


