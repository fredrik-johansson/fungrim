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
    Section("Limits"),
    Entries(
        "26ea9f",
        "1d2ee5",
        "6fe5c1",
        "c8a5f0",
        "afd5ca",
        "05a3ee",
        "2be0b5",
    ),
    Section("Derivatives"),
    Entries(
        "1b6a57",
        "452407",
        "b4b319",
        "96f695",
        "4c6780",
    ),
)

# Extreme values

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

# Limits

make_entry(ID("26ea9f"),
    SymbolDefinition(Limit, Limit(f(x), x, a), "Limiting value"),
    Description(SourceForm(Limit(f(x), x, a, P(x))), "rendered as", Limit(f(x), x, a, P(x)), "represents the limiting value of", f(x),
        "for every sequence of", x, "satisfying", P(x), "and approaching the limit point", a, "."),
    Description("If the predicate", P(x), "is omitted, the expression renders correctly to LaTeX, ",
        "but this form should be avoided since it is ambiguous whether it denotes a sequence limit, ",
        "real limit or complex limit (or some other kind of limit). It is better to use",
        SourceForm(SequenceLimit), ",", SourceForm(RealLimit), ",", SourceForm(LeftLimit), ",", SourceForm(RightLimit), "or", SourceForm(ComplexLimit), "."),
    Description("The limit is always a deleted limit. That is, the value of", f(a), "does not need to be equal to the limit and does not even need to be defined."),
    Description("The expression", SourceForm(f(x)), "is not required to be defined for all", x, "satisfying", P(x), ".",
        "It only needs to be defined for all", x, "in some neighborhood of the limit point and also satisfying", P(x), "."))

make_entry(ID("1d2ee5"),
    SymbolDefinition(SequenceLimit, SequenceLimit(f(n), n, a), "Limiting value of sequence"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(SequenceLimit(f(n), n, a)), ", rendered as", SequenceLimit(f(n), n, a), ", is equivalent to", SourceForm(Limit(f(n), n, a, Element(n, ZZ))),
        "but renders to LaTeX without displaying the predicate", Element(n, ZZ), " which readers will typically understand from context."),
    Description(SourceForm(SequenceLimit(f(n), n, a, P(n))), ", rendered as", SequenceLimit(f(n), n, a, P(n)), ", is equivalent to", SourceForm(Limit(f(n), n, a, And(Element(n, ZZ), P(n)))), "."))

make_entry(ID("6fe5c1"),
    SymbolDefinition(RealLimit, RealLimit(f(x), x, a), "Limiting value, real variable"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(RealLimit(f(x), x, a)), ", rendered as", RealLimit(f(x), x, a), ", is equivalent to", SourceForm(Limit(f(x), x, a, Element(x, RR))),
        "but renders to LaTeX without displaying the predicate", Element(x, RR), " which readers will typically understand from context."),
    Description(SourceForm(RealLimit(f(x), x, a, P(x))), ", rendered as", RealLimit(f(x), x, a, P(x)), ", is equivalent to", SourceForm(Limit(f(x), x, a, And(Element(x, RR), P(x)))), "."))

make_entry(ID("c8a5f0"),
    SymbolDefinition(LeftLimit, LeftLimit(f(x), x, a), "Limiting value, from the left"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(LeftLimit(f(x), x, a)), ", rendered as", LeftLimit(f(x), x, a), ", is equivalent to", SourceForm(Limit(f(x), x, a, Element(x, OpenInterval(-Infinity,a)))), "."),
    Description(SourceForm(LeftLimit(f(x), x, a, P(x))), ", rendered as", LeftLimit(f(x), x, a, P(x)), ", is equivalent to", SourceForm(Limit(f(x), x, a, And(Element(x, OpenInterval(-Infinity,a)), P(x)))), "."))

make_entry(ID("afd5ca"),
    SymbolDefinition(RightLimit, RightLimit(f(x), x, a), "Limiting value, from the right"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(RightLimit(f(x), x, a)), ", rendered as", RightLimit(f(x), x, a), ", is equivalent to", SourceForm(Limit(f(x), x, a, Element(x, OpenInterval(a,Infinity)))), "."),
    Description(SourceForm(RightLimit(f(x), x, a, P(x))), ", rendered as", RightLimit(f(x), x, a, P(x)), ", is equivalent to", SourceForm(Limit(f(x), x, a, And(Element(x, OpenInterval(a,Infinity)), P(x)))), "."))

make_entry(ID("05a3ee"),
    SymbolDefinition(ComplexLimit, ComplexLimit(f(z), z, a), "Limiting value, complex variable"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(ComplexLimit(f(z), z, a)), ", rendered as", ComplexLimit(f(z), z, a), ", is equivalent to", SourceForm(Limit(f(z), z, a, Element(z, CC))),
        "but renders to LaTeX without displaying the predicate", Element(z, CC), " which readers will typically understand from context."),
    Description(SourceForm(ComplexLimit(f(z), z, a, P(z))), ", rendered as", ComplexLimit(f(z), z, a, P(z)), ", is equivalent to", SourceForm(Limit(f(z), z, a, And(Element(z, CC), P(z)))), "."))

make_entry(ID("2be0b5"),
    SymbolDefinition(MeromorphicLimit, MeromorphicLimit(f(z), z, a), "Limiting value, allowing poles"),
    Description("This operator is equivalent to", SourceForm(ComplexLimit), "except that whereas", SourceForm(ComplexLimit),
        "in general is undefined when", a, "is a pole (because the direction of the resulting infinity depends on the direction of approach),", SourceForm(MeromorphicLimit), "is taken to give", SourceForm(UnsignedInfinity), "(", UnsignedInfinity, ")", "when", a, "is a pole."))

# Derivatives

make_entry(ID("1b6a57"),
    SymbolDefinition(Derivative, Derivative(Call(f, z), z, z), "Derivative"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(Derivative(f(z), z, a)), ", rendered as ",
        Derivative(Call(f, z), z, a), "or", Derivative(f(z), z, a), ", represents the derivative of", f(z), "evaluated at", Equal(z, a), "."),
    Description(SourceForm(Derivative(f(z), z, a, n)), ", rendered as ",
        Derivative(Call(f, z), z, a, n), "or", Derivative(f(z), z, a, n), ", represents the order", n, "derivative of", f(z), "evaluated at", Equal(z, a), "."),
    Description("The second argument", z, "defines a locally bound variable for the expression in the first argument. With the evaluation point set to", Equal(a, z), ",", SourceForm(Derivative(f(z), z, z)),
        "may render more simply as", Derivative(Call(f, z), z, z), "."),
    Description("This operator is ambiguous since the intended meaning could be a real derivative, a complex derivative, or some other form of derivative.",
        "It is better to use", SourceForm(RealDerivative), ",", SourceForm(ComplexDerivative), ",", SourceForm(ComplexBranchDerivative), ", or", SourceForm(MeromorphicDerivative), "."))

make_entry(ID("452407"),
    SymbolDefinition(RealDerivative, RealDerivative(Call(f, x), x, x), "Real derivative"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("The result is defined as", Equal(RealDerivative(f(x), x, x), RealLimit((f(x+h)-f(x))/h, h, 0)),
        "where the limit is taken with respect to a real variable", h, "(", SourceForm(RealLimit), ")."),
    Description("Note that", x,
        """can be complex and that the "real derivative" can be complex-valued; the "real" qualifier just refers to the direction in which the limit is computed."""))

make_entry(ID("b4b319"),
    SymbolDefinition(ComplexDerivative, ComplexDerivative(Call(f, z), z, z), "Complex derivative"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("The result is defined as", Equal(ComplexDerivative(f(z), z, z), ComplexLimit((f(z+h)-f(z))/h, h, 0)),
        "where the limit is taken with respect to a complex variable", h, "(", SourceForm(ComplexLimit), ")."),
    Description("If this limit exists (and is finite), then", f, "is holomorphic at", z, "."))

make_entry(ID("96f695"),
    SymbolDefinition(ComplexBranchDerivative, ComplexBranchDerivative(Call(f, z), z, z), "Complex derivative, allowing branch cuts"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("This operator is equivalent to", SourceForm(ComplexDerivative),
        "except that whereas", SourceForm(ComplexDerivative), "is undefined on a branch cut (where the function is not complex differentiable),",
        SourceForm(ComplexBranchDerivative), "gives the complex derivative of the analytically continued function across the branch cut."))

make_entry(ID("4c6780"),
    SymbolDefinition(MeromorphicDerivative, MeromorphicDerivative(Call(f, z), z, z), "Complex derivative, allowing poles"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("This operator is equivalent to", SourceForm(ComplexDerivative),
        "except that whereas", SourceForm(ComplexDerivative), "is undefined at a pole,",
        SourceForm(MeromorphicDerivative), "gives",
        SourceForm(UnsignedInfinity), "(", UnsignedInfinity, ")", "at a pole."))

