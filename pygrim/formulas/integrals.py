# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Definite integrals"),
    Section("Powers"),
    Entries(
        "463077",
    ),
    Section("Exponential functions"),
    Entries(
        "02e3d2",
        "9a06fb",
        "f8de2e",
        "16a1f4",
    ),
    Section("Sophomore's dream"),
    Entries(
        "b77faf",
        "66fefb",
    ),
)

make_entry(ID("463077"),
    Formula(Equal(Integral(1/(a*x+b)**c, Tuple(x, z, Infinity)),
        1/(a * (c-1) * (a*z+b)**(c-1)))),
    Variables(a, b, c, z),
    Assumptions(And(Element(a, RR), Element(b, RR), Element(c, RR),
        Element(z, RR), Greater(a, 0), Greater(a*z+b, 0), Greater(c, 1))))

make_entry(ID("02e3d2"),
    Formula(Equal(Integral(Exp(-(a*x)+b), Tuple(x, z, Infinity)),
        Exp(b-a*z)/a)),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), Greater(Re(a), 0))))

# todo: stronger conditions
make_entry(ID("9a06fb"),
    Formula(Equal(Integral(x**c * Exp(-(a*x)+b), Tuple(x, z, Infinity)),
        Exp(b) / a**(c+1) * UpperGamma(c+1, a*z))),
    Variables(a, b, c, z),
    Assumptions(And(Element(a, RR), Element(b, RR), Element(c, RR), Element(z, RR),
        Greater(a, 0), Greater(c, 0), Greater(z, 0))))

make_entry(ID("f8de2e"),
    Formula(Equal(Integral(Exp(-(a*x**2)+b), Tuple(x, z, Infinity)),
        Exp(b) / 2 * Sqrt(ConstPi/a) * Erfc(Sqrt(a) * z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC),
        Greater(Re(a), 0))))

make_entry(ID("16a1f4"),
    Formula(Equal(Integral(Exp(-(a*x**c)+b), Tuple(x, z, Infinity)),
        Exp(b) / (c * a**(1/c)) * UpperGamma(1/c, a*z**c))),
    Variables(a, b, c, z),
    Assumptions(And(Element(a, RR), Element(b, RR), Element(c, RR), Element(z, RR),
        Greater(a, 0), Greater(c, 0), Greater(z, 0))))

make_entry(ID("b77faf"),
    Formula(Equal(Integral(x**(-x), Tuple(x, 0, 1)), Sum(n**(-n), For(n, 1, Infinity)))))

make_entry(ID("66fefb"),
    Formula(Equal(Integral(x**x, Tuple(x, 0, 1)), Sum((-1)**(n+1) * n**(-n), For(n, 1, Infinity)))))



