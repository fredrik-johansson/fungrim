# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Imaginary unit"),
    Section("Definitions"),
    Entries(
        "be8e05",
    ),
    Section("Domain"),
    Entries(
        "88ad6f",
        "cd8a07",
        "a08fb9",
    ),
    Section("Quadratic equations"),
    Entries(
        "08ad28",
    ),
    Section("Numerical value"),
    Entries(
        "72cef9",
        "27586f",
    ),
    Section("Complex parts"),
    Entries(
        "65bbd6",
        "249fd6",
        "61784f",
        "735409",
        "089f85",
        "09c107",
    ),
    Section("Transformations"),
    Entries(
        "31b0df",
        "8be138",
        "e0425a",
        "c12a41",
        "44ae4a",
        "67c262",
        "f8a56f",
        "15f92d",
        "0ad836",
        "a39534",
    ),
    Section("Special functions at this value"),
    Entries(
        "c331da", # log
        "9c93bb",
        "3ac0ce",
        "208da7",
    ),
),

make_entry(ID("be8e05"),
    SymbolDefinition(ConstI, ConstI, "Imaginary unit"),
    Description("Represents the constant", i, ", the imaginary unit."))

# Domain

make_entry(ID("88ad6f"),
    Formula(Element(ConstI, CC)))

make_entry(ID("cd8a07"),
    Formula(Element(ConstI, AlgebraicNumbers)))

make_entry(ID("a08fb9"),
    Formula(NotElement(ConstI, RR)))

# Quadratic equations

make_entry(ID("08ad28"),
    Formula(Equal(Solutions(Brackets(Equal(x**2 + 1, 0)), ForElement(x, CC)), Set(ConstI, -ConstI))))

# Numerical value

make_entry(ID("72cef9"),
    Formula(Equal(ConstI, Sqrt(-1))))

make_entry(ID("27586f"),
    Formula(Equal(ConstI, Pow(-1, Div(1,2)))))

# Complex parts

make_entry(ID("65bbd6"),
    Formula(Equal(Abs(ConstI), 1)))

make_entry(ID("249fd6"),
    Formula(Equal(Re(ConstI), 0)))

make_entry(ID("61784f"),
    Formula(Equal(Im(ConstI), 1)))

make_entry(ID("09c107"),
    Formula(Equal(Sign(ConstI), ConstI)))

# Operations

make_entry(ID("31b0df"),
    Formula(Equal(ConstI**2, -1)))

make_entry(ID("8be138"),
    Formula(Equal(ConstI**3, -ConstI)))

make_entry(ID("e0425a"),
    Formula(Equal(ConstI**4, 1)))

make_entry(ID("c12a41"),
    Formula(Equal(ConstI**n, Cases(
        Tuple(1, CongruentMod(n, 0, 4)),
        Tuple(ConstI, CongruentMod(n, 1, 4)),
        Tuple(-1, CongruentMod(n, 2, 4)),
        Tuple(-ConstI, CongruentMod(n, 3, 4))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("44ae4a"),
    Formula(Equal(Conjugate(ConstI), -ConstI)))

make_entry(ID("67c262"),
    Formula(Equal(1/ConstI, -ConstI)))

make_entry(ID("f8a56f"),
    Formula(Equal(ConstI**z, Exp(ConstPi*ConstI*z/2))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("15f92d"),
    Formula(Equal(ConstI**z, Cos(ConstPi/2 * z) + Sin(ConstPi/2 * z) * ConstI)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("a39534"),
    Formula(Equal(ConstI**ConstI, Exp(-(ConstPi/2)))))

# Special functions at this value

make_entry(ID("9c93bb"),
    Formula(Equal(Abs(GammaFunction(ConstI)), Sqrt(ConstPi/Sinh(ConstPi)))))

make_entry(ID("3ac0ce"),
    Formula(Equal(Im(DigammaFunction(ConstI)), Div(1,2)*(ConstPi*Coth(ConstPi) + 1))))

make_entry(ID("208da7"),
    Formula(Equal(PolyLog(2, ConstI), -(ConstPi**2/48) + ConstCatalan*ConstI)))




"""



19773f
35e09c


40f42c
22c52e
7c4b00
daaa7a
efe0fb


i**n


(actuall n in CC)




# log(i)
# 



"""
