# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Operators"),
    Section("Extreme values"),
    Entries(
        "d0cb24",
        "65ccf2",
        "0a3e5a",
        "617fe3",
        "f4fbb8",
        "be4926",
    ),

)

make_entry(ID("f4fbb8"),
    SymbolDefinition(ArgMinUnique, ArgMinUnique(f(x), x, S), "Unique location of minimum value"),
    Description(SourceForm(ArgMinUnique(f(x), x, S)), "represents the unique point", Element(r, S),
        "such that", Element(f(x), Union(RR, Set(-Infinity, Infinity))), "attains its minimum value on", S, "at the point", Equal(x, r), ".",
        "This operation is undefined if there is no such unique minimum or if", f(x), "is undefined on some points of", S, "."),
    Description("This operator introduces", SourceForm(x), "as a locally bound variable.",
        "More generally,", SourceForm(x), "can be a composite expression such as a tuple, where all new variables become locally bound."))

make_entry(ID("be4926"),
    SymbolDefinition(ArgMaxUnique, ArgMaxUnique(f(x), x, S), "Unique location of maximum value"),
    Description(SourceForm(ArgMaxUnique(f(x), x, S)), "represents the unique point", Element(r, S),
        "such that", Element(f(x), Union(RR, Set(-Infinity, Infinity))), "attains its maximum value on", S, "at the point", Equal(x, r), ".",
        "This operation is undefined if there is no such unique maximum or if", f(x), "is undefined on some points of", S, "."),
    Description("This operator introduces", SourceForm(x), "as a locally bound variable.",
        "More generally,", SourceForm(x), "can be a composite expression such as a tuple, where all new variables become locally bound."))

make_entry(ID("0a3e5a"),
    SymbolDefinition(ArgMin, ArgMin(f(x), x, S), "Locations of minimum value"),
    Description(SourceForm(ArgMin(f(x), x, S)), "represents the set of points", SubsetEqual(R, S),
        "such that", Element(f(x), Union(RR, Set(-Infinity, Infinity))), "attains its minimum value on", S, "at each of the points", Element(x, R), ".",
        "If", f(x), "does not attain a minimum value, the result is the empty set", Equal(R, Set()), ".",
        "This operation is undefined if", f(x), "is undefined on some points of", S, "."),
    Description("This operator introduces", SourceForm(x), "as a locally bound variable.",
        "More generally,", SourceForm(x), "can be a composite expression such as a tuple, where all new variables become locally bound."))

make_entry(ID("617fe3"),
    SymbolDefinition(ArgMax, ArgMax(f(x), x, S), "Locations of maximum value"),
    Description(SourceForm(ArgMax(f(x), x, S)), "represents the set of points", SubsetEqual(R, S),
        "such that", Element(f(x), Union(RR, Set(-Infinity, Infinity))), "attains its maximum value on", S, "at each of the points", Element(x, R), ".",
        "If", f(x), "does not attain a maximum value, the result is the empty set", Equal(R, Set()), ".",
        "This operation is undefined if", f(x), "is undefined on some points of", S, "."),
    Description("This operator introduces", SourceForm(x), "as a locally bound variable.",
        "More generally,", SourceForm(x), "can be a composite expression such as a tuple, where all new variables become locally bound."))

make_entry(ID("d0cb24"),
    SymbolDefinition(Minimum, Minimum(f(x), x, S), "Minimum value"),
    Description(SourceForm(Minimum(f(x), x, S)), "represents the minimum value of", Element(f(x), Union(RR, Set(-Infinity, Infinity))),
        "for", Element(x, S), ".",
        "This operation is undefined if there is no minimum value or if", f(x), "is undefined on some points of", S, "."),
    Description("This operator introduces", SourceForm(x), "as a locally bound variable.",
        "More generally,", SourceForm(x), "can be a composite expression such as a tuple, where all new variables become locally bound."))

make_entry(ID("65ccf2"),
    SymbolDefinition(Maximum, Maximum(f(x), x, S), "Maximum value"),
    Description(SourceForm(Maximum(f(x), x, S)), "represents the maximum value of", Element(f(x), Union(RR, Set(-Infinity, Infinity))),
        "for", Element(x, S), ".",
        "This operation is undefined if there is no maximum value or if", f(x), "is undefined on some points of", S, "."),
    Description("This operator introduces", SourceForm(x), "as a locally bound variable.",
        "More generally,", SourceForm(x), "can be a composite expression such as a tuple, where all new variables become locally bound."))

