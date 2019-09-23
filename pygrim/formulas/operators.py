# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Operators"),
    Section("Sums and products"),
    Entries(
        "044e42",
        "1e2755",
        "9f703a",
        "2a896d",
        "8baf79",
        "5830eb",
    ),
    Section("Solutions and zeros"),
    Entries(
        "f7ce46",
        "d2714b",
        "5862bb",
        "f5ae93",
        "231a99",
    ),
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
        "6cd302",
        "fdf152",
    ),
    Section("Derivatives"),
    Entries(
        "1b6a57",
        "452407",
        "b4b319",
        "96f695",
        "4c6780",
    ),
    Section("Integrals"),
    Entries(
        "c285c7",
    ),
    Section("Indefinite integrals"),
    Entries(
        "2e4fbc",
        "0be77d",
        "fb2790",
    ),
)

# Sums and products

make_entry(ID("044e42"),
    SymbolDefinition(Sum, Sum(f(n), For(n)), "Sum"),
    Description(SourceForm(Sum(S)), ", rendered as ", Sum(S), ", gives the sum of the elements of the set", S, ". "
        "The sum is required to be absolutely convergent."),
    Description(SourceForm(Sum(f(n), For(n, a, b))), ", rendered as ", Sum(f(n), For(n, a, b)), ", gives the sum of", f(n),
        "for integers", n, "from", a, "to", b, ", where", a, "and", b, "should be integers or", -Infinity, "or", Infinity, ". ",
        "If", Less(a, b), ", the sum is empty. The sum", Sum(f(n), For(n, 0, Infinity)), "is interpreted as",
        SequenceLimit(Sum(f(n), For(n, 0, N)), Var(N), Infinity), "and can be conditionally convergent."),
    Description(SourceForm(Sum(f(n), For(n, a, b), P(n))), ", rendered as ", Sum(f(n), For(n, a, b), P(n)), ", is as above but",
        "only terms satisfying the predicate", P(n), "are included."),
    Description(SourceForm(Sum(f(x), ForElement(x, S))), ", rendered as ", Sum(f(x), ForElement(x, S)), ", gives the sum of", f(x),
        "for all", x, "in the set", S, ". The sum is required to be absolutely convergent."),
    Description(SourceForm(Sum(f(x), ForElement(x, S), P(x))), ", rendered as ", Sum(f(x), ForElement(x, S), P(x)), ", gives the sum of", f(x),
        "for all", x, "in the set", S, "and satisfying the predicate", P(x), ". The sum is required to be absolutely convergent."),
    Description(SourceForm(Sum(f(x), For(x), P(x))), ", rendered as ", Sum(f(x), For(x), P(x)), ", gives the sum of", f(x),
        "for all", x, "satisfying the predicate", P(x), ". ",
        "The predicate", P(x), "should define the domain of", x, "unambiguously; that is, it must include a statement such as",
        Element(x, S), "where", S, "is a known set.",
         "The sum is required to be absolutely convergent."),
    Description("The empty sum is", 0, ". The sum can range over an uncountable number of terms, as long as only countably many terms are nonzero."),
    Description("The special expression", SourceForm(For(x)), ", ", SourceForm(For(x, a, b)), " or", SourceForm(ForElement(x)),
        "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator. ",
        "Similarly", SourceForm(For(Tuple(x, y))), ", ", SourceForm(ForElement(Tuple(x, y), S)), "etc. defines multiple locally bound variables."))

make_entry(ID("1e2755"),
    SymbolDefinition(Product, Product(f(n), For(n)), "Product"),
    Description(SourceForm(Product(S)), ", rendered as ", Product(S), ", gives the product of the elements of the set", S, ". "
        "The product is required to be absolutely convergent. The empty product is 1."),
    Description(SourceForm(Product(f(n), For(n, a, b))), ", rendered as ", Product(f(n), For(n, a, b)), ", gives the product of", f(n),
        "for integers", n, "from", a, "to", b, ", where", a, "and", b, "should be integers or", -Infinity, "or", Infinity, ". ",
        "If", Less(a, b), ", the product is empty. The product", Product(f(n), For(n, 0, Infinity)), "is interpreted as",
        SequenceLimit(Product(f(n), For(n, 0, N)), Var(N), Infinity), "and can be conditionally convergent."),
    Description(SourceForm(Product(f(n), For(n, a, b), P(n))), ", rendered as ", Product(f(n), For(n, a, b), P(n)), ", is as above but",
        "only terms satisfying the predicate", P(n), "are included."),
    Description(SourceForm(Product(f(x), ForElement(x, S))), ", rendered as ", Product(f(x), ForElement(x, S)), ", gives the product of", f(x),
        "for all", x, "in the set", S, ". The product is required to be absolutely convergent."),
    Description(SourceForm(Product(f(x), ForElement(x, S), P(x))), ", rendered as ", Product(f(x), ForElement(x, S), P(x)), ", gives the product of", f(x),
        "for all", x, "in the set", S, "and satisfying the predicate", P(x), ". The product is required to be absolutely convergent."),
    Description(SourceForm(Product(f(x), For(x), P(x))), ", rendered as ", Product(f(x), For(x), P(x)), ", gives the product of", f(x),
        "for all", x, "satisfying the predicate", P(x), ". ",
        "The predicate", P(x), "should define the domain of", x, "unambiguously; that is, it must include a statement such as",
        Element(x, S), "where", S, "is a known set.",
         "The product is required to be absolutely convergent."),
    Description("The empty product is", 1, ". The product can range over an uncountable number of factors, as long as only countably many factors are nonzero."),
    Description("The special expression", SourceForm(For(x)), ", ", SourceForm(For(x, a, b)), " or", SourceForm(ForElement(x)),
        "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator. ",
        "Similarly", SourceForm(For(Tuple(x, y))), ", ", SourceForm(ForElement(Tuple(x, y), S)), "etc. defines multiple locally bound variables."))

make_entry(ID("9f703a"),
    SymbolDefinition(PrimeSum, PrimeSum(f(p), For(p)), "Sum over primes"),
    Description(SourceForm(PrimeSum(f(p), For(p))), ", rendered as ",
        PrimeSum(f(p), For(p)), ", represents the sum of", f(p), "taken over all prime numbers", p, "."),
    Description(SourceForm(PrimeSum(f(p), For(p), P(p))), ", rendered as ",
        PrimeSum(f(p), For(p), P(p)), ", represents the sum of", f(p), "taken over all prime numbers", p, "satisfying the predicate", P(p), "."),
    Description("The special expression", SourceForm(For(p)), "defines", SourceForm(p), "as a locally bound variable."),
    Description("The empty sum is equal to zero. Sums taken over an infinite number of terms are required to be absolutely convergent."))

make_entry(ID("2a896d"),
    SymbolDefinition(PrimeProduct, PrimeProduct(f(p), For(p)), "Product over primes"),
    Description(SourceForm(PrimeProduct(f(p), For(p))), ", rendered as ",
        PrimeProduct(f(p), For(p)), ", represents the product of", f(p), "taken over all prime numbers", p, "."),
    Description(SourceForm(PrimeProduct(f(p), For(p), P(p))), ", rendered as ",
        PrimeProduct(f(p), For(p), P(p)), ", represents the product of", f(p), "taken over all prime numbers", p, "satisfying the predicate", P(p), "."),
    Description("The special expression", SourceForm(For(p)), "defines", SourceForm(p), "as a locally bound variable."),
    Description("The empty product is equal to one. Products taken over an infinite number of factors are required to be absolutely convergent."))

make_entry(ID("8baf79"),
    SymbolDefinition(DivisorSum, DivisorSum(f(k), For(k, n)), "Sum over divisors"),
    Description(SourceForm(DivisorSum(f(k), For(k, n))), ", rendered as ",
        DivisorSum(f(k), For(k, n)), ", represents the sum of", f(k), "taken over all positive integers", k, "dividing the integer", n, "."),
    Description(SourceForm(DivisorSum(f(k), For(k, n), P(k))), ", rendered as ",
        DivisorSum(f(k), For(k, n), P(k)), ", represents the sum of", f(k), "taken over all positive integers", k, "dividing the integer", n, "and satisfying the predicate", P(k), "."),
    Description("The special expression", SourceForm(For(k, n)), "defines", SourceForm(k), "as a locally bound variable."),
    Description("The empty sum is equal to zero."))

make_entry(ID("5830eb"),
    SymbolDefinition(DivisorProduct, DivisorProduct(f(k), For(k, n)), "Product over divisors"),
    Description(SourceForm(DivisorProduct(f(k), For(k, n))), ", rendered as ",
        DivisorProduct(f(k), For(k, n)), ", represents the product of", f(k), "taken over all positive integers", k, "dividing the integer", n, "."),
    Description(SourceForm(DivisorProduct(f(k), For(k, n), P(k))), ", rendered as ",
        DivisorProduct(f(k), For(k, n), P(k)), ", represents the product of", f(k), "taken over all positive integers", k, "dividing the integer", n, "and satisfying the predicate", P(k), "."),
    Description("The special expression", SourceForm(For(k, n)), "defines", SourceForm(k), "as a locally bound variable."),
    Description("The empty product is equal to one."))

# Solutions and zeros

description_var_xyz = Description("The special expression", SourceForm(Var(x)),
    "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator. ",
    "The corresponding predicate", P(x), "must define the domain of", x, "unambiguously; that is, it must include a statement such as",
    Element(x, S), "where", S, "is a known set. Similarly,", SourceForm(Var(x, y)), ", ", SourceForm(Var(x, y, z)), ", etc.",
    "defines multiple locally bound variables which must be accompanied by a multivariate predicate", P(x,y), ", ", P(x,y,z), ", etc.")

make_entry(ID("f7ce46"),
    SymbolDefinition(Zeros, Zeros(f(x), Var(x), P(x)), "Zeros (roots) of function"),
    Description(SourceForm(Zeros(f(x), Var(x), P(x))), ", rendered", Zeros(f(x), Var(x), P(x)), ", represents the set of values",
        x, "satisfying", P(x), "and", Equal(f(x), 0), "."),
    Description(SourceForm(Zeros(f(x,y), Var(x,y), P(x,y))), ", rendered", Zeros(f(x,y), Var(x,y), P(x,y)), ", represents the set of tuples",
        Tuple(x, y), "satisfying", P(x, y), "and", Equal(f(x,y), 0), ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("d2714b"),
    SymbolDefinition(UniqueZero, UniqueZero(f(x), Var(x), P(x)), "Unique zero (root) of function"),
    Description(SourceForm(UniqueZero(f(x), Var(x), P(x))), ", rendered", UniqueZero(f(x), Var(x), P(x)), ", represents the unique value",
        x, "satisfying", P(x), "and", Equal(f(x), 0), "."),
    Description("This operation is undefined if such a value does not exist or is not unique."),
    Description(SourceForm(UniqueZero(f(x,y), Var(x,y), P(x,y))), ", rendered", UniqueZero(f(x,y), Var(x,y), P(x,y)), ", represents the unique tuple",
        Tuple(x, y), "satisfying", P(x, y), "and", Equal(f(x,y), 0), ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("5862bb"),
    SymbolDefinition(Solutions, Solutions(Q(x), Var(x), P(x)), "Solution set"),
    Description(SourceForm(Solutions(Q(x), Var(x), P(x))), ", rendered", Solutions(Q(x), Var(x), P(x)), ", represents the set of values",
        x, "satisfying", P(x), "and", Q(x), "."),
    Description(SourceForm(Solutions(Q(x,y), Var(x,y), P(x,y))), ", rendered", Solutions(Q(x,y), Var(x,y), P(x,y)), ", represents the set of tuples",
        Tuple(x, y), "satisfying", P(x, y), "and", Q(x, y), ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("f5ae93"),
    SymbolDefinition(UniqueSolution, UniqueSolution(Q(x), Var(x), P(x)), "Unique solution"),
    Description(SourceForm(UniqueSolution(Q(x), Var(x), P(x))), ", rendered", UniqueSolution(f(x), Var(x), P(x)), ", represents the unique value",
        x, "satisfying", P(x), "and", Q(x), "."),
    Description("This operation is undefined if such a value does not exist or is not unique."),
    Description(SourceForm(UniqueSolution(Q(x,y), Var(x,y), P(x,y))), ", rendered", UniqueSolution(f(x,y), Var(x,y), P(x,y)), ", represents the unique tuple",
        Tuple(x,y), "satisfying", P(x,y), "and", Q(x,y), ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("231a99"),
    SymbolDefinition(ComplexZeroMultiplicity, ComplexZeroMultiplicity(f(z), Var(z), c), "Multiplicity (order) of complex zero"),
    Description(SourceForm(ComplexZeroMultiplicity(f(z), Var(z), c)), ", rendered", ComplexZeroMultiplicity(f(z), Var(z), c),
        ", gives the root multiplicity (order of vanishing) of", f(z), "at the point", Equal(z, c), "."),
    Description("If", Unequal(f(c), 0), ", the multiplicity is zero."),
    Description("It is required that", f(z), "is holomorphic and not identically zero in a neighborhood of", c, "."),
    Description("The special expression", SourceForm(Var(z)), "declares", SourceForm(z), "as a locally bound variable within the scope of the arguments to this operator."),
)

# Extreme values

make_entry(ID("6ec976"),
    SymbolDefinition(Supremum, Supremum(f(x), Var(x), P(x)), "Supremum of a set or function"),
    Description("This operator can be called with 1 or 3 arguments."),
    Description("Called with 1 argument, ", SourceForm(Supremum(S)), ", rendered", Supremum(S), ", represents the supremum of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), ".",
        "The supremum does not need to be an element of", S, "itself; in particular, for an open interval",
        Equal(S, OpenInterval(a,b)), ", we have", Equal(Supremum(S), b), "."),
    Description("Called with 3 arguments, ", SourceForm(Supremum(f(x), Var(x), P(x))), ", rendered", Supremum(f(x), Var(x), P(x)),
        ", represents", Supremum(Set(f(x), For(x), P(x))), "where", P(x), "is a predicate defining the range of", x, "."),
    Description(SourceForm(Supremum(f(x,y), Var(x,y), P(x,y))), ", rendered", Supremum(f(x,y), Var(x, y), P(x,y)),
        ", represents", Supremum(Set(f(x,y), For(Tuple(x,y)), P(x,y))), "where", P(x,y), "is a predicate defining the range of", x, "and", y,
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("bbeb35"),
    SymbolDefinition(Infimum, Infimum(f(x), Var(x), P(x)), "Infimum of a set or function"),
    Description("This operator can be called with 1 or 3 arguments."),
    Description("Called with 1 argument, ", SourceForm(Infimum(S)), ", rendered", Infimum(S), ", represents the infimum of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), ".",
        "The infimum does not need to be an element of", S, "itself; in particular, for an open interval",
        Equal(S, OpenInterval(a,b)), ", we have", Equal(Infimum(S), a), "."),
    Description("Called with 3 arguments, ", SourceForm(Infimum(f(x), Var(x), P(x))), ", rendered", Infimum(f(x), Var(x), P(x)),
        ", represents", Infimum(Set(f(x), For(x), P(x))), "where", P(x), "is a predicate defining the range of", x, "."),
    Description(SourceForm(Infimum(f(x,y), Var(x,y), P(x,y))), ", rendered", Infimum(f(x,y), Var(x, y), P(x,y)),
        ", represents", Infimum(Set(f(x,y), For(Tuple(x,y)), P(x,y))), "where", P(x,y), "is a predicate defining the range of", x, "and", y,
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("d0cb24"),
    SymbolDefinition(Minimum, Minimum(f(x), Var(x), P(x)), "Minimum value of a set or function"),
    Description("This operator can be called with 1 or 3 arguments."),
    Description("Called with 1 argument, ", SourceForm(Minimum(S)), ", rendered", Minimum(S), ", represents the minimum element of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), " and the minimum exists."),
    Description("Called with 3 arguments, ", SourceForm(Minimum(f(x), Var(x), P(x))), ", rendered", Minimum(f(x), Var(x), P(x)),
        ", represents", Minimum(Set(f(x), For(x), P(x))), "."),
    Description(SourceForm(Minimum(f(x,y), Var(x,y), P(x,y))), ", rendered", Minimum(f(x,y), Var(x, y), P(x,y)),
        ", represents", Minimum(Set(f(x,y), For(Tuple(x,y)), P(x,y))), "where", P(x,y), "is a predicate defining the range of", x, "and", y,
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("65ccf2"),
    SymbolDefinition(Maximum, Maximum(f(x), Var(x), P(x)), "Maximum value of a set or function"),
    Description("This operator can be called with 1 or 3 arguments."),
    Description("Called with 1 argument, ", SourceForm(Maximum(S)), ", rendered", Maximum(S), ", represents the maximum element of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), " and the maximum exists."),
    Description("Called with 3 arguments, ", SourceForm(Maximum(f(x), Var(x), P(x))), ", rendered", Maximum(f(x), Var(x), P(x)),
        ", represents", Maximum(Set(f(x), For(x), P(x))), "."),
    Description(SourceForm(Maximum(f(x,y), Var(x,y), P(x,y))), ", rendered", Maximum(f(x,y), Var(x, y), P(x,y)),
        ", represents", Maximum(Set(f(x,y), For(Tuple(x,y)), P(x,y))), "where", P(x,y), "is a predicate defining the range of", x, "and", y,
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("0a3e5a"),
    SymbolDefinition(ArgMin, ArgMin(f(x), Var(x), P(x)), "Locations of minimum value"),
    Description(SourceForm(ArgMin(f(x), Var(x), P(x))), ", rendered", ArgMin(f(x), Var(x), P(x)), ", gives the set of values", x,
        "satisfying", P(x),
        "such that", Equal(f(x), Minimum(f(s), Var(s), P(s))), ", if the minimum value exists."),
    Description("If", f(x), "does not attain a minimum value on the set of points defined by", P(x), ", the result is the empty set", Set(), "."),
    Description(SourceForm(ArgMin(f(x,y), Var(x,y), P(x,y))), ", rendered", ArgMin(f(x,y), Var(x,y), P(x,y)), ", gives the set of tuples",
        Tuple(x, y), "satisfying", P(x,y),
        "such that", Equal(f(x,y), Minimum(f(s,t), Var(s,t), P(s,t))),
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("617fe3"),
    SymbolDefinition(ArgMax, ArgMax(f(x), Var(x), P(x)), "Locations of maximum value"),
    Description(SourceForm(ArgMax(f(x), Var(x), P(x))), ", rendered", ArgMax(f(x), Var(x), P(x)), ", gives the set of values", x,
        "satisfying", P(x),
        "such that", Equal(f(x), Maximum(f(s), Var(s), P(s))), ", if the maximum value exists."),
    Description("If", f(x), "does not attain a maximum value on the set of points defined by", P(x), ", the result is the empty set", Set(), "."),
    Description(SourceForm(ArgMax(f(x,y), Var(x,y), P(x,y))), ", rendered", ArgMax(f(x,y), Var(x,y), P(x,y)), ", gives the set of tuples",
        Tuple(x, y), "satisfying", P(x,y),
        "such that", Equal(f(x,y), Maximum(f(s,t), Var(s,t), P(s,t))),
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("f4fbb8"),
    SymbolDefinition(ArgMinUnique, ArgMinUnique(f(x), Var(x), P(x)), "Unique location of minimum value"),
    Description(SourceForm(ArgMinUnique(f(x), Var(x), P(x))), "represents the unique value", x,
        "satisfying", P(x),
        "such that", Equal(f(x), Minimum(f(s), Var(s), P(s))), ". This operation is only defined if such a unique value exists."),
    Description(SourceForm(ArgMinUnique(f(x,y), Var(x,y), P(x,y))), "represents the unique tuple", Tuple(x, y),
        "satisfying", P(x, y),
        "such that", Equal(f(x, y), Minimum(f(s,t), Var(s,t), P(s,t))),
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("be4926"),
    SymbolDefinition(ArgMaxUnique, ArgMaxUnique(f(x), Var(x), P(x)), "Unique location of maximum value"),
    Description(SourceForm(ArgMaxUnique(f(x), Var(x), P(x))), "represents the unique value", x,
        "satisfying", P(x),
        "such that", Equal(f(x), Maximum(f(s), Var(s), P(s))), ". This operation is only defined if such a unique value exists."),
    Description(SourceForm(ArgMaxUnique(f(x,y), Var(x,y), P(x,y))), "represents the unique tuple", Tuple(x, y),
        "satisfying", P(x, y),
        "such that", Equal(f(x, y), Maximum(f(s,t), Var(s,t), P(s,t))),
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

# Limits

make_entry(ID("26ea9f"),
    SymbolDefinition(Limit, Limit(f(x), Var(x), a), "Limiting value"),
    Description(SourceForm(Limit(f(x), Var(x), a, P(x))), "rendered as", Limit(f(x), Var(x), a, P(x)), "represents the limiting value of", f(x),
        "for every sequence of", x, "satisfying", P(x), "and approaching the limit point", a, "."),
    Description("If the predicate", P(x), "is omitted, the expression renders correctly to LaTeX, ",
        "but this form should be avoided since it is ambiguous whether it denotes a sequence limit, ",
        "real limit or complex limit (or some other kind of limit). It is better to use",
        SourceForm(SequenceLimit), ",", SourceForm(RealLimit), ",", SourceForm(LeftLimit), ",", SourceForm(RightLimit), "or", SourceForm(ComplexLimit), "."),
    Description("The limit is always a deleted limit. That is, the value of", f(a), "does not need to be equal to the limit and does not even need to be defined."),
    Description("The expression", SourceForm(f(x)), "is not required to be defined for all", x, "satisfying", P(x), ".",
        "It only needs to be defined for all", x, "in some neighborhood of the limit point and also satisfying", P(x), "."),
    Description("The expression", SourceForm(Var(x)), "serves to declare", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("1d2ee5"),
    SymbolDefinition(SequenceLimit, SequenceLimit(f(n), Var(n), a), "Limiting value of sequence"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(SequenceLimit(f(n), Var(n), a)), ", rendered as", SequenceLimit(f(n), Var(n), a), ", is equivalent to", SourceForm(Limit(f(n), Var(n), a, Element(n, ZZ))),
        "but renders to LaTeX without displaying the predicate", Element(n, ZZ), " which readers will typically understand from context."),
    Description(SourceForm(SequenceLimit(f(n), Var(n), a, P(n))), ", rendered as", SequenceLimit(f(n), Var(n), a, P(n)), ", is equivalent to", SourceForm(Limit(f(n), Var(n), a, And(Element(n, ZZ), P(n)))), "."),
    Description("The expression", SourceForm(Var(n)), "serves to declare", SourceForm(n), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("6fe5c1"),
    SymbolDefinition(RealLimit, RealLimit(f(x), Var(x), a), "Limiting value, real variable"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(RealLimit(f(x), Var(x), a)), ", rendered as", RealLimit(f(x), Var(x), a), ", is equivalent to", SourceForm(Limit(f(x), Var(x), a, Element(x, RR))),
        "but renders to LaTeX without displaying the predicate", Element(x, RR), " which readers will typically understand from context."),
    Description(SourceForm(RealLimit(f(x), Var(x), a, P(x))), ", rendered as", RealLimit(f(x), Var(x), a, P(x)), ", is equivalent to", SourceForm(Limit(f(x), Var(x), a, And(Element(x, RR), P(x)))), "."),
    Description("The expression", SourceForm(Var(x)), "serves to declare", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("c8a5f0"),
    SymbolDefinition(LeftLimit, LeftLimit(f(x), Var(x), a), "Limiting value, from the left"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(LeftLimit(f(x), Var(x), a)), ", rendered as", LeftLimit(f(x), Var(x), a), ", is equivalent to", SourceForm(Limit(f(x), Var(x), a, Element(x, OpenInterval(-Infinity,a)))), "."),
    Description(SourceForm(LeftLimit(f(x), Var(x), a, P(x))), ", rendered as", LeftLimit(f(x), Var(x), a, P(x)), ", is equivalent to", SourceForm(Limit(f(x), Var(x), a, And(Element(x, OpenInterval(-Infinity,a)), P(x)))), "."),
    Description("The expression", SourceForm(Var(x)), "serves to declare", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("afd5ca"),
    SymbolDefinition(RightLimit, RightLimit(f(x), Var(x), a), "Limiting value, from the right"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(RightLimit(f(x), Var(x), a)), ", rendered as", RightLimit(f(x), Var(x), a), ", is equivalent to", SourceForm(Limit(f(x), Var(x), a, Element(x, OpenInterval(a,Infinity)))), "."),
    Description(SourceForm(RightLimit(f(x), Var(x), a, P(x))), ", rendered as", RightLimit(f(x), Var(x), a, P(x)), ", is equivalent to", SourceForm(Limit(f(x), Var(x), a, And(Element(x, OpenInterval(a,Infinity)), P(x)))), "."),
    Description("The expression", SourceForm(Var(x)), "serves to declare", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("05a3ee"),
    SymbolDefinition(ComplexLimit, ComplexLimit(f(z), Var(z), a), "Limiting value, complex variable"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(ComplexLimit(f(z), Var(z), a)), ", rendered as", ComplexLimit(f(z), Var(z), a), ", is equivalent to", SourceForm(Limit(f(z), Var(z), a, Element(z, CC))),
        "but renders to LaTeX without displaying the predicate", Element(z, CC), " which readers will typically understand from context."),
    Description(SourceForm(ComplexLimit(f(z), Var(z), a, P(z))), ", rendered as", ComplexLimit(f(z), Var(z), a, P(z)), ", is equivalent to", SourceForm(Limit(f(z), Var(z), a, And(Element(z, CC), P(z)))), "."),
    Description("The expression", SourceForm(Var(z)), "serves to declare", SourceForm(z), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("2be0b5"),
    SymbolDefinition(MeromorphicLimit, MeromorphicLimit(f(z), Var(z), a), "Limiting value, allowing poles"),
    Description("This operator is equivalent to", SourceForm(ComplexLimit), "except that whereas", SourceForm(ComplexLimit),
        "in general is undefined when", a, "is a pole (because the direction of the resulting infinity depends on the direction of approach),", SourceForm(MeromorphicLimit), "is taken to give", SourceForm(UnsignedInfinity), "(", UnsignedInfinity, ")", "when", a, "is a pole."))

make_entry(ID("6cd302"),
    SymbolDefinition(SequenceLimitInferior, SequenceLimitInferior(f(n), Var(n), a), "Limit inferior of sequence"))

make_entry(ID("fdf152"),
    SymbolDefinition(SequenceLimitSuperior, SequenceLimitSuperior(f(n), Var(n), a), "Limit superior of sequence"))

# Derivatives

make_entry(ID("1b6a57"),
    SymbolDefinition(Derivative, Derivative(Call(f, z), For(z, z)), "Derivative"),
    Description(SourceForm(Derivative(f(z), For(z, a))), ", rendered as ",
        Derivative(Call(f, z), For(z, a)), "or", Derivative(f(z), For(z, a)), ", represents the derivative of", f(z), "evaluated at", Equal(z, a), "."),
    Description(SourceForm(Derivative(f(z), For(z, a, n))), ", rendered as ",
        Derivative(Call(f, z), For(z, a, n)), "or", Derivative(f(z), For(z, a, n)), ", represents the order", n, "derivative of", f(z), "evaluated at", Equal(z, a), "."),
    Description("The second argument", z, "defines a locally bound variable for the expression in the first argument. With the evaluation point set to", Equal(a, z), ",", SourceForm(Derivative(f(z), For(z, z))),
        "may render more simply as", Derivative(Call(f, z), For(z, z)), "."),
    Description("This operator is ambiguous since the intended meaning could be a real derivative, a complex derivative, or some other form of derivative.",
        "It is better to use", SourceForm(RealDerivative), ",", SourceForm(ComplexDerivative), ",", SourceForm(ComplexBranchDerivative), ", or", SourceForm(MeromorphicDerivative), "."))

make_entry(ID("452407"),
    SymbolDefinition(RealDerivative, RealDerivative(Call(f, x), For(x, x)), "Real derivative"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("The result is defined as", Equal(RealDerivative(f(x), For(x, x)), RealLimit((f(x+h)-f(x))/h, Var(h), 0)),
        "where the limit is taken with respect to a real variable", h, "(", SourceForm(RealLimit), ")."),
    Description("Note that", x,
        """can be complex and that the "real derivative" can be complex-valued; the "real" qualifier just refers to the direction in which the limit is computed."""))

make_entry(ID("b4b319"),
    SymbolDefinition(ComplexDerivative, ComplexDerivative(Call(f, z), For(z, z)), "Complex derivative"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("The result is defined as", Equal(ComplexDerivative(f(z), For(z, z)), ComplexLimit((f(z+h)-f(z))/h, Var(h), 0)),
        "where the limit is taken with respect to a complex variable", h, "(", SourceForm(ComplexLimit), ")."),
    Description("If this limit exists (and is finite), then", f, "is holomorphic at", z, "."))

make_entry(ID("96f695"),
    SymbolDefinition(ComplexBranchDerivative, ComplexBranchDerivative(Call(f, z), For(z, z)), "Complex derivative, allowing branch cuts"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("This operator is equivalent to", SourceForm(ComplexDerivative),
        "except that whereas", SourceForm(ComplexDerivative), "is undefined on a branch cut (where the function is not complex differentiable),",
        SourceForm(ComplexBranchDerivative), "gives the complex derivative of the analytically continued function across the branch cut."))

make_entry(ID("4c6780"),
    SymbolDefinition(MeromorphicDerivative, MeromorphicDerivative(Call(f, z), For(z, z)), "Complex derivative, allowing poles"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("This operator is equivalent to", SourceForm(ComplexDerivative),
        "except that whereas", SourceForm(ComplexDerivative), "is undefined at a pole,",
        SourceForm(MeromorphicDerivative), "gives",
        SourceForm(UnsignedInfinity), "(", UnsignedInfinity, ")", "at a pole."))

# Integrals

make_entry(ID("c285c7"),
    SymbolDefinition(Integral, Integral(f(x), For(x, a, b)), "Integral"),
    Description(SourceForm(Integral(f(x), For(x, a, b))), ", rendered as ",
        Integral(f(x), For(x, a, b)), ", represents the integral of", f(x), "from", a, "to", b, ". ",
        "The order is significant: ", Equal(Integral(f(x), For(x, a, b)), Neg(Integral(f(x), For(x, b, a)))), "."),
    Description(SourceForm(Integral(f(x), ForElement(x, S))), ", rendered as ",
        Integral(f(x), ForElement(x, S)), ", represents the integral of", f(x), "over the set", S, "."),
    Description("The special expression", SourceForm(For(x, a, b)), "or", SourceForm(ForElement(x, S)), "defines a locally bound variable."),
    Description("The precise class of integrals allowed by this operator is yet to be defined, but should normally encompass Lebesgue integrals."),
    Description("The integrand is allowed to be undefined on a subset of measure of zero."))

# Indefinite integrals

make_entry(ID("2e4fbc"),
    SymbolDefinition(IndefiniteIntegralEqual, IndefiniteIntegralEqual(f(x), g(x), x), "Indefinite integral"),
    Description(SourceForm(IndefiniteIntegralEqual(f(x), g(x), x, c)), ", rendered as ",
        IndefiniteIntegralEqual(f(x), g(x), x, c), ", expresses that", g(x), "is an antiderivative of", f(x), "at the point", c,
        ", or formally that", Equal(Derivative(g(x), For(x, c)), f(c)), ".",
        "In other words,", g(x), "belongs to the equivalence class of antiderivatives of", f(x),
        "at the point", c, ". This is rendered as a statement of equality (with an arbitrary constant of integration) to follow the conventional notation for indefinite integrals."),
    Description("This operator is ambiguous since the intended meaning could be a real derivative, a complex derivative, or some other form of derivative.",
        "It is better to use", SourceForm(RealIndefiniteIntegralEqual), "or", SourceForm(ComplexIndefiniteIntegralEqual), "."),
    Description("The argument", SourceForm(x), "defines a locally bound variable used in the expressions", f(x), "and", g(x), ". ",
        "If this operator is called more simply as", SourceForm(IndefiniteIntegralEqual(f(x), g(x), x)), ", ",
            "the meaning is the same as", SourceForm(IndefiniteIntegralEqual(f(x), g(x), x, x)), ", where the", SourceForm(x),
            "appearing in",  f(x), "and", g(x), "is understood as a new dummy variable. This dummy variable is evaluated at the value",
            SourceForm(x), "defined in the surrounding context only after the functions have been constructed."))

make_entry(ID("0be77d"),
    SymbolDefinition(RealIndefiniteIntegralEqual, RealIndefiniteIntegralEqual(f(x), g(x), x), "Indefinite integral, real derivative"),
    Description(SourceForm(RealIndefiniteIntegralEqual(f(x), g(x), x, c)), ", rendered as ",
        RealIndefiniteIntegralEqual(f(x), g(x), x, c), ", expresses that", g(x), "is an antiderivative of", f(x), "at the point", c,
        ", or formally that", Equal(RealDerivative(g(x), For(x, c)), f(c)), ".",
        "In other words,", g(x), "belongs to the equivalence class of antiderivatives of", f(x),
        "at the point", c, ". This is rendered as a statement of equality (with an arbitrary constant of integration) to follow the conventional notation for indefinite integrals."),
    Description("The argument", SourceForm(x), "defines a locally bound variable used in the expressions", f(x), "and", g(x), ". ",
        "If this operator is called more simply as", SourceForm(RealIndefiniteIntegralEqual(f(x), g(x), x)), ", ",
            "the meaning is the same as", SourceForm(RealIndefiniteIntegralEqual(f(x), g(x), x, x)), ", where the", SourceForm(x),
            "appearing in",  f(x), "and", g(x), "is understood as a new dummy variable. This dummy variable is evaluated at the value",
            SourceForm(x), "defined in the surrounding context only after the functions have been constructed."))

make_entry(ID("fb2790"),
    SymbolDefinition(ComplexIndefiniteIntegralEqual, ComplexIndefiniteIntegralEqual(f(x), g(x), x), "Indefinite integral, complex derivative"),
    Description(SourceForm(ComplexIndefiniteIntegralEqual(f(x), g(x), x, c)), ", rendered as ",
        ComplexIndefiniteIntegralEqual(f(x), g(x), x, c), ", expresses that", g(x), "is an antiderivative of", f(x), "at the point", c,
        ", or formally that", Equal(ComplexDerivative(g(x), For(x, c)), f(c)), ".",
        "In other words,", g(x), "belongs to the equivalence class of antiderivatives of", f(x),
        "at the point", c, ". This is rendered as a statement of equality (with an arbitrary constant of integration) to follow the conventional notation for indefinite integrals."),
    Description("The argument", SourceForm(x), "defines a locally bound variable used in the expressions", f(x), "and", g(x), ". ",
        "If this operator is called more simply as", SourceForm(ComplexIndefiniteIntegralEqual(f(x), g(x), x)), ", ",
            "the meaning is the same as", SourceForm(ComplexIndefiniteIntegralEqual(f(x), g(x), x, x)), ", where the", SourceForm(x),
            "appearing in",  f(x), "and", g(x), "is understood as a new dummy variable. This dummy variable is evaluated at the value",
            SourceForm(x), "defined in the surrounding context only after the functions have been constructed."))

