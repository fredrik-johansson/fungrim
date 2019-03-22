# -*- coding: utf-8 -*-

from .expr import *

index_ConstPi = ("ConstPi", "The constant pi (3.14...)",
    [
        ("Numerical value", ["6505a9","0c838a"]),
        ("Elementary function representations", ["0c9939","f8d280","590136"]),
        ("Integral representations", ["464961","04cd99","dae4a7"]),
        ("Series representations", ["f617c0","fddfe6"]),
        ("Product representations", ["69fe63"]),
        ("Limit representations", ["e1e106"]),
        ("Approximations", ["4c0698"]),
    ])

make_entry(ID("6505a9"),
    Formula(Element(ConstPi,
        RealBall(Decimal("3.1415926535897932384626433832795028841971693993751"), Decimal("5.83e-51")))))

make_entry(ID("0c838a"),
    Formula(NotElement(ConstPi, QQ)))

make_entry(ID("0c9939"),
    Formula(Equal(ConstPi, 4*Atan(1))))

make_entry(ID("f8d280"),
    Formula(Equal(ConstPi, 16*Acot(5) - 4*Acot(239))))

make_entry(ID("590136"),
    Formula(Equal(ConstPi, -(ConstI * Log(-1)))))

make_entry(ID("464961"),
    Formula(Equal(ConstPi, 2 * Integral(Sqrt(1-x**2), Tuple(x, -1, 1)))))

make_entry(ID("04cd99"),
    Formula(Equal(ConstPi, Integral(1/(x**2+1), Tuple(x, -Infinity, Infinity)))))

make_entry(ID("dae4a7"),
    Formula(Equal(ConstPi, Integral(Exp(-x**2), Tuple(x, -Infinity, Infinity))**2)))

make_entry(ID("f617c0"),
    Formula(Equal(ConstPi, 4*Sum((-1)**k / (2*k+1), Tuple(k, 0, Infinity)))))

make_entry(ID("fddfe6"),
    Formula(Equal(ConstPi, Sum((1 / 16**k) * (4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)), Tuple(k, 0, Infinity)))))

make_entry(ID("69fe63"),
    Formula(Equal(ConstPi, 2*Product((4*k**2)/(4*k**2-1), Tuple(k, 1, Infinity)))))

make_entry(ID("e1e106"),
    Formula(Equal(ConstPi, Limit(16**k/(k*Binomial(2*k,k)**2), k, Infinity))))

make_entry(ID("4c0698"),
    Formula(Less(Abs(1/ConstPi - 
        Parenthesis(12*Sum((-1)**k*Factorial(6*k)*(13591409+545140134*k)/(Factorial(3*k)*Factorial(k)**3*640320**(3*k+Div(3,2))),
            Tuple(k, 0, N-1)))), Div(1,151931373056000**N))),
    Variables(N),
    Assumptions(Element(N, ZZGreaterEqual(0))))

