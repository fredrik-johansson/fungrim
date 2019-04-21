# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Operators"),
    Section("Extreme values"),
    Entries(
        "6ec976",
        "bbeb35",
        "d0cb24",
        "65ccf2",
        "0a3e5a",
        "617fe3",
        "f4fbb8",
        "be4926",
    ),

)


make_entry(ID("6ec976"),
    SymbolDefinition(Supremum, Supremum(f(x), x, P(x)), "Supremum of a set or function"),
    Description("This operator can be called with 1 or 3 arguments."),
    Description("Called with 1 argument, ", SourceForm(Supremum(S)), ", rendered", Supremum(S), ", represents the supremum of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), ".",
        "The supremum does not need to be an element of", S, "itself; in particular, for an open interval",
        Equal(S, OpenInterval(a,b)), ", we have", Equal(Supremum(S), b), "."),
    Description("Called with 3 arguments, ", SourceForm(Supremum(f(x), x, P(x))), ", rendered", Supremum(f(x), x, P(x)),
        ", represents", Supremum(SetBuilder(f(x), x, P(x))), "where", P(x), "is a predicate defining the range of", x, "."),
    description_x_predicate)

make_entry(ID("bbeb35"),
    SymbolDefinition(Infimum, Infimum(f(x), x, P(x)), "Infimum of a set or function"),
    Description("This operator can be called with 1 or 3 arguments."),
    Description("Called with 1 argument, ", SourceForm(Infimum(S)), ", rendered", Infimum(S), ", represents the infimum of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), ".",
        "The infimum does not need to be an element of", S, "itself; in particular, for an open interval",
        Equal(S, OpenInterval(a,b)), ", we have", Equal(Infimum(S), a), "."),
    Description("Called with 3 arguments, ", SourceForm(Infimum(f(x), x, P(x))), ", rendered", Infimum(f(x), x, P(x)),
        ", represents", Infimum(SetBuilder(f(x), x, P(x))), "where", P(x), "is a predicate defining the range of", x, "."),
    description_x_predicate)

make_entry(ID("d0cb24"),
    SymbolDefinition(Minimum, Minimum(f(x), x, P(x)), "Minimum value of a set or function"),
    Description("This operator can be called with 1 or 3 arguments."),
    Description("Called with 1 argument, ", SourceForm(Minimum(S)), ", rendered", Minimum(S), ", represents the minimum element of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), " and the minimum exists."),
    Description("Called with 3 arguments, ", SourceForm(Minimum(f(x), x, P(x))), ", rendered", Minimum(f(x), x, P(x)),
        ", represents", Minimum(SetBuilder(f(x), x, P(x))), "."),
    description_x_predicate)

make_entry(ID("65ccf2"),
    SymbolDefinition(Maximum, Maximum(f(x), x, P(x)), "Maximum value of a set or function"),
    Description("This operator can be called with 1 or 3 arguments."),
    Description("Called with 1 argument, ", SourceForm(Maximum(S)), ", rendered", Maximum(S), ", represents the maximum element of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), " and the maximum exists."),
    Description("Called with 3 arguments, ", SourceForm(Maximum(f(x), x, P(x))), ", rendered", Maximum(f(x), x, P(x)),
        ", represents", Maximum(SetBuilder(f(x), x, P(x))), "."),
    description_x_predicate)

make_entry(ID("0a3e5a"),
    SymbolDefinition(ArgMin, ArgMin(f(x), x, P(x)), "Locations of minimum value"),
    Description(SourceForm(ArgMin(f(x), x, P(x))), ", rendered", ArgMin(f(x), x, P(x)), ", gives the set of points", r,
        "satisfying", P(r),
        "such that", Equal(f(r), Minimum(f(x), x, P(x))), ", if the minimum value exists."),
    Description("If", f(x), "does not attain a minimum value on the set of points defined by", P(x), ", the result is the empty set", Set(), "."),
    description_x_predicate)

make_entry(ID("617fe3"),
    SymbolDefinition(ArgMax, ArgMax(f(x), x, P(x)), "Locations of maximum value"),
    Description(SourceForm(ArgMax(f(x), x, P(x))), ", rendered", ArgMax(f(x), x, P(x)), ", gives the set of points", r,
        "satisfying", P(r),
        "such that", Equal(f(r), Maximum(f(x), x, P(x))), ", if the maximum value exists."),
    Description("If", f(x), "does not attain a maximum value on the set of points defined by", P(x), ", the result is the empty set", Set(), "."),
    description_x_predicate)

make_entry(ID("f4fbb8"),
    SymbolDefinition(ArgMinUnique, ArgMinUnique(f(x), x, P(x)), "Unique location of minimum value"),
    Description(SourceForm(ArgMinUnique(f(x), x, P(x))), "represents the unique point", r,
        "satisfying", P(r),
        "such that", Equal(f(r), Minimum(f(x), x, P(x))), ". This operation is only defined if such a unique point exists."),
    description_x_predicate)

make_entry(ID("be4926"),
    SymbolDefinition(ArgMaxUnique, ArgMaxUnique(f(x), x, P(x)), "Unique location of maximum value"),
    Description(SourceForm(ArgMaxUnique(f(x), x, P(x))), "represents the unique point", r,
        "satisfying", P(r),
        "such that", Equal(f(r), Maximum(f(x), x, P(x))), ". This operation is only defined if such a unique point exists."),
    description_x_predicate)

