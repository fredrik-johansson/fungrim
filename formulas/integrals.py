# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Definite integrals"),
    Section("Sophomore's dream"),
    Entries(
        "b77faf",
        "66fefb",
    ),
)

make_entry(ID("b77faf"),
    Formula(Equal(Integral(x**(-x), Tuple(x, 0, 1)), Sum(n**(-n), Tuple(n, 1, Infinity)))))

make_entry(ID("66fefb"),
    Formula(Equal(Integral(x**x, Tuple(x, 0, 1)), Sum((-1)**(n+1) * n**(-n), Tuple(n, 1, Infinity)))))



