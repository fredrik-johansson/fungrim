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
    Section("Holomorphic functions"),
    Entries(
        "499bdf",
        "0895b1",
        "231a99",
        "c54261",
    ),
    Section("Paths and analytic continuation"),
    Entries(
        "4d0e14",
        "bf8f37",
        "457aaa",
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
        SequenceLimit(Sum(f(n), For(n, 0, N)), For(N, Infinity)), "and can be conditionally convergent."),
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

description_var_xyz = Description("The special expression", SourceForm(For(x)), "or", SourceForm(ForElement(x, S)),
    "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator. ",
    "If", SourceForm(For(x)), "is used instead of", SourceForm(ForElement(x, S)), ", "
    "the corresponding predicate", P(x), "must define the domain of", x, "unambiguously; that is, it must include a statement such as",
    Element(x, S), "where", S, "is a known set. Similarly,", SourceForm(For(Tuple(x, y))), ", ", SourceForm(For(Tuple(x, y, z))), ", etc.",
    "defines multiple locally bound variables which must be accompanied by a multivariate predicate", P(x,y), ", ", P(x,y,z), ", etc.")

make_entry(ID("f7ce46"),
    SymbolDefinition(Zeros, Zeros(f(x), ForElement(x, S)), "Zeros (roots) of function"),
    Description(SourceForm(Zeros(f(x), ForElement(x, S))), ", rendered", Zeros(f(x), ForElement(x, S)), ", represents the set of values",
        Element(x, S), "satisfying", Equal(f(x), 0), "."),
    Description(SourceForm(Zeros(f(x), ForElement(x, S), P(x))), ", rendered", Zeros(f(x), ForElement(x, S), P(x)), ", represents the set of values",
        Element(x, S), "satisfying", P(x), "and", Equal(f(x), 0), "."),
    Description(SourceForm(Zeros(f(x), For(x), P(x))), ", rendered", Zeros(f(x), For(x), P(x)), ", represents the set of values",
        x, "satisfying", P(x), "and", Equal(f(x), 0), "."),
    Description(SourceForm(Zeros(f(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", Zeros(f(x,y), For(Tuple(x,y)), P(x,y)), ", represents the set of tuples",
        Tuple(x, y), "satisfying", P(x, y), "and", Equal(f(x,y), 0), ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("d2714b"),
    SymbolDefinition(UniqueZero, UniqueZero(f(x), ForElement(x, S)), "Unique zero (root) of function"),
    Description(SourceForm(UniqueZero(f(x), ForElement(x, S))), ", rendered", UniqueZero(f(x), ForElement(x, S)), ", represents the unique value",
        Element(x, S), "satisfying", Equal(f(x), 0), "."),
    Description("This operation is undefined if such a value does not exist or is not unique."),
    Description(SourceForm(UniqueZero(f(x), ForElement(x, S), P(x))), ", rendered", UniqueZero(f(x), ForElement(x, S), P(x)), ", represents the unique value",
        Element(x, S), "satisfying", P(x), "and", Equal(f(x), 0), "."),
    Description(SourceForm(UniqueZero(f(x), For(x), P(x))), ", rendered", UniqueZero(f(x), For(x), P(x)), ", represents the unique value",
        x, "satisfying", P(x), "and", Equal(f(x), 0), "."),
    Description(SourceForm(UniqueZero(f(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", UniqueZero(f(x,y), For(Tuple(x,y)), P(x,y)), ", represents the unique tuple",
        Tuple(x, y), "such that", P(x, y), "and", Equal(f(x,y), 0), ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("5862bb"),
    SymbolDefinition(Solutions, Solutions(Q(x), ForElement(x, S)), "Solution set"),
    Description(SourceForm(Solutions(Q(x), ForElement(x, S))), ", rendered", Solutions(Q(x), ForElement(x, S)), ", represents the set of values",
        Element(x, S), "satisfying", Q(x), "."),
    Description(SourceForm(Solutions(Q(x), ForElement(x, S), P(x))), ", rendered", Solutions(Q(x), ForElement(x, S), P(x)), ", represents the set of values",
        Element(x, S), "satisfying", P(x), "and", Q(x), "."),
    Description(SourceForm(Solutions(Q(x), For(x), P(x))), ", rendered", Solutions(Q(x), For(x), P(x)), ", represents the set of values",
        x, "satisfying", P(x), "and", Q(x), "."),
    Description(SourceForm(Solutions(Q(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", Solutions(Q(x,y), For(Tuple(x,y)), P(x,y)), ", represents the set of tuples",
        Tuple(x, y), "satisfying", P(x, y), "and", Q(x,y), ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("f5ae93"),
    SymbolDefinition(UniqueSolution, UniqueSolution(Q(x), ForElement(x, S)), "Unique solution"),
    Description(SourceForm(UniqueSolution(Q(x), ForElement(x, S))), ", rendered", UniqueSolution(Q(x), ForElement(x, S)), ", represents the unique value",
        Element(x, S), "satisfying", Q(x), "."),
    Description("This operation is undefined if such a value does not exist or is not unique."),
    Description(SourceForm(UniqueSolution(Q(x), ForElement(x, S), P(x))), ", rendered", UniqueSolution(Q(x), ForElement(x, S), P(x)), ", represents the unique value",
        Element(x, S), "satisfying", P(x), "and", Q(x), "."),
    Description(SourceForm(UniqueSolution(Q(x), For(x), P(x))), ", rendered", UniqueSolution(Q(x), For(x), P(x)), ", represents the unique value",
        x, "satisfying", P(x), "and", Q(x), "."),
    Description(SourceForm(UniqueSolution(Q(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", UniqueSolution(Q(x,y), For(Tuple(x,y)), P(x,y)), ", represents the unique tuple",
        Tuple(x, y), "satisfying", P(x, y), "and", Q(x,y), ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)


# Extreme values

make_entry(ID("6ec976"),
    SymbolDefinition(Supremum, Supremum(f(x), ForElement(x, S)), "Supremum of a set or function"),
    Description(SourceForm(Supremum(S)), ", rendered", Supremum(S), ", represents the supremum of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), ".",
        "The supremum does not need to be an element of", S, "itself; in particular, for an open interval",
        Equal(S, OpenInterval(a,b)), ", we have", Equal(Supremum(S), b), "."),
    Description(SourceForm(Supremum(f(x), ForElement(x, S))), ", rendered", Supremum(f(x), ForElement(x, S)),
        ", represents", Supremum(Set(f(x), ForElement(x, S))), "."),
    Description(SourceForm(Supremum(f(x), ForElement(x, S), P(x))), ", rendered", Supremum(f(x), ForElement(x, S), P(x)),
        ", represents", Supremum(Set(f(x), ForElement(x, S), P(x))), "."),
    Description(SourceForm(Supremum(f(x), For(x), P(x))), ", rendered", Supremum(f(x), For(x), P(x)),
        ", represents", Supremum(Set(f(x), For(x), P(x))), "."),
    Description(SourceForm(Supremum(f(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", Supremum(f(x,y), For(Tuple(x, y)), P(x,y)),
        ", represents", Supremum(Set(f(x,y), For(Tuple(x,y)), P(x,y))), "where", P(x,y), "is a predicate defining the range of", x, "and", y,
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("bbeb35"),
    SymbolDefinition(Infimum, Infimum(f(x), ForElement(x, S)), "Infimum of a set or function"),
    Description(SourceForm(Infimum(S)), ", rendered", Infimum(S), ", represents the infimum of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), ".",
        "The infimum does not need to be an element of", S, "itself; in particular, for an open interval",
        Equal(S, OpenInterval(a,b)), ", we have", Equal(Infimum(S), b), "."),
    Description(SourceForm(Infimum(f(x), ForElement(x, S))), ", rendered", Infimum(f(x), ForElement(x, S)),
        ", represents", Infimum(Set(f(x), ForElement(x, S))), "."),
    Description(SourceForm(Infimum(f(x), ForElement(x, S), P(x))), ", rendered", Infimum(f(x), ForElement(x, S), P(x)),
        ", represents", Infimum(Set(f(x), ForElement(x, S), P(x))), "."),
    Description(SourceForm(Infimum(f(x), For(x), P(x))), ", rendered", Infimum(f(x), For(x), P(x)),
        ", represents", Infimum(Set(f(x), For(x), P(x))), "."),
    Description(SourceForm(Infimum(f(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", Infimum(f(x,y), For(Tuple(x, y)), P(x,y)),
        ", represents", Infimum(Set(f(x,y), For(Tuple(x,y)), P(x,y))), "where", P(x,y), "is a predicate defining the range of", x, "and", y,
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("d0cb24"),
    SymbolDefinition(Minimum, Minimum(f(x), ForElement(x, S)), "Minimum value of a set or function"),
    Description(SourceForm(Minimum(S)), ", rendered", Minimum(S), ", represents the minimum element of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), " and the minimum exists."),
    Description(SourceForm(Minimum(f(x), ForElement(x, S))), ", rendered", Minimum(f(x), ForElement(x, S)),
        ", represents", Minimum(Set(f(x), ForElement(x, S))), "."),
    Description(SourceForm(Minimum(f(x), ForElement(x, S), P(x))), ", rendered", Minimum(f(x), ForElement(x, S), P(x)),
        ", represents", Minimum(Set(f(x), ForElement(x, S), P(x))), "."),
    Description(SourceForm(Minimum(f(x), For(x), P(x))), ", rendered", Minimum(f(x), For(x), P(x)),
        ", represents", Minimum(Set(f(x), For(x), P(x))), "."),
    Description(SourceForm(Minimum(f(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", Minimum(f(x,y), For(Tuple(x, y)), P(x,y)),
        ", represents", Minimum(Set(f(x,y), For(Tuple(x,y)), P(x,y))), "where", P(x,y), "is a predicate defining the range of", x, "and", y,
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("65ccf2"),
    SymbolDefinition(Maximum, Maximum(f(x), ForElement(x, S)), "Maximum value of a set or function"),
    Description("Called with 1 argument, ", SourceForm(Maximum(S)), ", rendered", Maximum(S), ", represents the maximum element of the set", S, ".",
        "This operator is only defined if", S, "is a subset of", Union(RR, Set(-Infinity, +Infinity)), " and the maximum exists."),
    Description(SourceForm(Maximum(f(x), ForElement(x, S))), ", rendered", Maximum(f(x), ForElement(x, S)),
        ", represents", Maximum(Set(f(x), ForElement(x, S))), "."),
    Description(SourceForm(Maximum(f(x), ForElement(x, S), P(x))), ", rendered", Maximum(f(x), ForElement(x, S), P(x)),
        ", represents", Maximum(Set(f(x), ForElement(x, S), P(x))), "."),
    Description(SourceForm(Maximum(f(x), For(x), P(x))), ", rendered", Maximum(f(x), For(x), P(x)),
        ", represents", Maximum(Set(f(x), For(x), P(x))), "."),
    Description(SourceForm(Maximum(f(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", Maximum(f(x,y), For(Tuple(x, y)), P(x,y)),
        ", represents", Maximum(Set(f(x,y), For(Tuple(x,y)), P(x,y))), "where", P(x,y), "is a predicate defining the range of", x, "and", y,
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("0a3e5a"),
    SymbolDefinition(ArgMin, ArgMin(f(x), ForElement(x, S)), "Locations of minimum value"),
    Description(SourceForm(ArgMin(f(x), ForElement(x, S))), ", rendered", ArgMin(f(x), ForElement(x, S)), ", gives the set of values",
        Element(x, S),
        "such that", Equal(f(x), Minimum(f(s), ForElement(s, S))), "."),
    Description(SourceForm(ArgMin(f(x), ForElement(x, S), P(x))), ", rendered", ArgMin(f(x), ForElement(x, S), P(x)), ", gives the set of values",
        Element(x, S),
        "satisfying", P(x),
        "and such that", Equal(f(x), Minimum(f(s), ForElement(s, S), P(s))), "."),
    Description("If", f(x), "does not attain a minimum value satisfying the conditions, the result is the empty set", Set(), "."),
    Description(SourceForm(ArgMin(f(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", ArgMin(f(x,y), For(Tuple(x,y)), P(x,y)), ", gives the set of tuples",
        Tuple(x, y), "satisfying", P(x,y),
        "such that", Equal(f(x,y), Minimum(f(s,t), For(Tuple(s,t)), P(s,t))),
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("617fe3"),
    SymbolDefinition(ArgMax, ArgMax(f(x), ForElement(x, S)), "Locations of maximum value"),
    Description(SourceForm(ArgMax(f(x), ForElement(x, S))), ", rendered", ArgMax(f(x), ForElement(x, S)), ", gives the set of values",
        Element(x, S),
        "such that", Equal(f(x), Maximum(f(s), ForElement(s, S))), "."),
    Description(SourceForm(ArgMax(f(x), ForElement(x, S), P(x))), ", rendered", ArgMax(f(x), ForElement(x, S), P(x)), ", gives the set of values",
        Element(x, S),
        "satisfying", P(x),
        "and such that", Equal(f(x), Maximum(f(s), ForElement(s, S), P(s))), "."),
    Description("If", f(x), "does not attain a maximum value satisfying the conditions, the result is the empty set", Set(), "."),
    Description(SourceForm(ArgMax(f(x,y), For(Tuple(x,y)), P(x,y))), ", rendered", ArgMax(f(x,y), For(Tuple(x,y)), P(x,y)), ", gives the set of tuples",
        Tuple(x, y), "satisfying", P(x,y),
        "such that", Equal(f(x,y), Maximum(f(s,t), For(Tuple(s,t)), P(s,t))),
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("f4fbb8"),
    SymbolDefinition(ArgMinUnique, ArgMinUnique(f(x), ForElement(x, S)), "Unique location of minimum value"),
    Description(SourceForm(ArgMinUnique(f(x), ForElement(x, S))), ", rendered", ArgMinUnique(f(x), ForElement(x, S)), ", ",
        "represents the unique value", Element(x, S),
        "such that", Equal(f(x), Minimum(f(s), ForElement(s, S))), ". This operation is only defined if such a unique value exists."),
    Description(SourceForm(ArgMinUnique(f(x), ForElement(x, S), P(x))), ", rendered", ArgMinUnique(f(x), ForElement(x, S), P(x)), ", ",
        "represents the unique value", Element(x, S),
        "satisfying", P(x), "and",
        "such that", Equal(f(x), Minimum(f(s), ForElement(s, S))), ". This operation is only defined if such a unique value exists."),
    Description(SourceForm(ArgMinUnique(f(x,y), For(Tuple(x,y)), P(x,y))), "represents the unique tuple", Tuple(x, y),
        "satisfying", P(x, y),
        "such that", Equal(f(x, y), Minimum(f(s,t), For(Tuple(s,t)), P(s,t))),
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

make_entry(ID("be4926"),
    SymbolDefinition(ArgMaxUnique, ArgMaxUnique(f(x), ForElement(x, S)), "Unique location of maximum value"),
    Description(SourceForm(ArgMaxUnique(f(x), ForElement(x, S))), ", rendered", ArgMaxUnique(f(x), ForElement(x, S)), ", ",
        "represents the unique value", Element(x, S),
        "such that", Equal(f(x), Maximum(f(s), ForElement(s, S))), ". This operation is only defined if such a unique value exists."),
    Description(SourceForm(ArgMaxUnique(f(x), ForElement(x, S), P(x))), ", rendered", ArgMaxUnique(f(x), ForElement(x, S), P(x)), ", ",
        "represents the unique value", Element(x, S),
        "satisfying", P(x), "and",
        "such that", Equal(f(x), Maximum(f(s), ForElement(s, S))), ". This operation is only defined if such a unique value exists."),
    Description(SourceForm(ArgMaxUnique(f(x,y), For(Tuple(x,y)), P(x,y))), "represents the unique tuple", Tuple(x, y),
        "satisfying", P(x, y),
        "such that", Equal(f(x, y), Maximum(f(s,t), For(Tuple(s,t)), P(s,t))),
        ", and similarly for any number", GreaterEqual(n, 2), "of variables."),
    description_var_xyz)

# Limits

make_entry(ID("26ea9f"),
    SymbolDefinition(Limit, Limit(f(x), For(x, a)), "Limiting value"),
    Description(SourceForm(Limit(f(x), For(x, a), P(x))), "rendered as", Limit(f(x), For(x, a), P(x)), "represents the limiting value of", f(x),
        "for every sequence of", x, "satisfying", P(x), "and approaching the limit point", a, "."),
    Description("If the predicate", P(x), "is omitted, the expression renders correctly to LaTeX, ",
        "but this form should be avoided since it is ambiguous whether it denotes a sequence limit, ",
        "real limit or complex limit (or some other kind of limit). It is better to use",
        SourceForm(SequenceLimit), ",", SourceForm(RealLimit), ",", SourceForm(LeftLimit), ",", SourceForm(RightLimit), "or", SourceForm(ComplexLimit), "."),
    Description("The limit is always a deleted limit. That is, the value of", f(a), "does not need to be equal to the limit and does not even need to be defined."),
    Description("The expression", SourceForm(f(x)), "is not required to be defined for all", x, "satisfying", P(x), ".",
        "It only needs to be defined for all", x, "in some neighborhood of the limit point and also satisfying", P(x), "."),
    Description("The expression", SourceForm(For(x, a)), "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("1d2ee5"),
    SymbolDefinition(SequenceLimit, SequenceLimit(f(n), For(n, a)), "Limiting value of sequence"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(SequenceLimit(f(n), For(n, a))), ", rendered as", SequenceLimit(f(n), For(n, a)), ", is equivalent to", SourceForm(Limit(f(n), For(n, a), Element(n, ZZ))),
        "but renders to LaTeX without displaying the predicate", Element(n, ZZ), " which readers will typically understand from context."),
    Description(SourceForm(SequenceLimit(f(n), For(n, a), P(n))), ", rendered as", SequenceLimit(f(n), For(n, a), P(n)), ", is equivalent to", SourceForm(Limit(f(n), For(n, a), And(Element(n, ZZ), P(n)))), "."),
    Description("The expression", SourceForm(For(x, a)), "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("6fe5c1"),
    SymbolDefinition(RealLimit, RealLimit(f(x), For(x, a)), "Limiting value, real variable"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(RealLimit(f(x), For(x, a))), ", rendered as", RealLimit(f(x), For(x, a)), ", is equivalent to", SourceForm(Limit(f(x), For(x, a), Element(x, RR))),
        "but renders to LaTeX without displaying the predicate", Element(x, RR), " which readers will typically understand from context."),
    Description(SourceForm(RealLimit(f(x), For(x, a), P(x))), ", rendered as", RealLimit(f(x), For(x, a), P(x)), ", is equivalent to", SourceForm(Limit(f(x), For(x, a), And(Element(x, RR), P(x)))), "."),
    Description("The expression", SourceForm(For(x, a)), "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("c8a5f0"),
    SymbolDefinition(LeftLimit, LeftLimit(f(x), For(x, a)), "Limiting value, from the left"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(LeftLimit(f(x), For(x, a))), ", rendered as", LeftLimit(f(x), For(x, a)), ", is equivalent to", SourceForm(Limit(f(x), For(x, a), Element(x, OpenInterval(-Infinity,a)))), "."),
    Description(SourceForm(LeftLimit(f(x), For(x, a), P(x))), ", rendered as", LeftLimit(f(x), For(x, a), P(x)), ", is equivalent to", SourceForm(Limit(f(x), For(x, a), And(Element(x, OpenInterval(-Infinity,a)), P(x)))), "."),
    Description("The expression", SourceForm(For(x, a)), "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("afd5ca"),
    SymbolDefinition(RightLimit, RightLimit(f(x), For(x, a)), "Limiting value, from the right"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(RightLimit(f(x), For(x, a))), ", rendered as", RightLimit(f(x), For(x, a)), ", is equivalent to", SourceForm(Limit(f(x), For(x, a), Element(x, OpenInterval(a,Infinity)))), "."),
    Description(SourceForm(RightLimit(f(x), For(x, a), P(x))), ", rendered as", RightLimit(f(x), For(x, a), P(x)), ", is equivalent to", SourceForm(Limit(f(x), For(x, a), And(Element(x, OpenInterval(a,Infinity)), P(x)))), "."),
    Description("The expression", SourceForm(For(x, a)), "declares", SourceForm(x), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("05a3ee"),
    SymbolDefinition(ComplexLimit, ComplexLimit(f(z), For(z, a)), "Limiting value, complex variable"),
    Description("This operator can be called with three or four arguments."),
    Description(SourceForm(ComplexLimit(f(z), For(z, a))), ", rendered as", ComplexLimit(f(z), For(z, a)), ", is equivalent to", SourceForm(Limit(f(z), For(z, a), Element(z, CC))),
        "but renders to LaTeX without displaying the predicate", Element(z, CC), " which readers will typically understand from context."),
    Description(SourceForm(ComplexLimit(f(z), For(z, a), P(z))), ", rendered as", ComplexLimit(f(z), For(z, a), P(z)), ", is equivalent to", SourceForm(Limit(f(z), For(z, a), And(Element(z, CC), P(z)))), "."),
    Description("The expression", SourceForm(For(z, a)), "declares", SourceForm(z), "as a locally bound variable within the scope of the arguments to this operator."))

make_entry(ID("2be0b5"),
    SymbolDefinition(MeromorphicLimit, MeromorphicLimit(f(z), For(z, a)), "Limiting value, allowing poles"),
    Description("This operator is equivalent to", SourceForm(ComplexLimit), "except that whereas", SourceForm(ComplexLimit),
        "in general is undefined when", a, "is a pole (because the direction of the resulting infinity depends on the direction of approach),", SourceForm(MeromorphicLimit), "is taken to give", SourceForm(UnsignedInfinity), "(", UnsignedInfinity, ")", "when", a, "is a pole."))

make_entry(ID("6cd302"),
    SymbolDefinition(SequenceLimitInferior, SequenceLimitInferior(f(n), For(n, a)), "Limit inferior of sequence"))

make_entry(ID("fdf152"),
    SymbolDefinition(SequenceLimitSuperior, SequenceLimitSuperior(f(n), For(n, a)), "Limit superior of sequence"))

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
    Description("The result is defined as", Equal(RealDerivative(f(x), For(x, x)), RealLimit((f(x+h)-f(x))/h, For(h, 0))),
        "where the limit is taken with respect to a real variable", h, "(", SourceForm(RealLimit), ")."),
    Description("Note that", x,
        """can be complex and that the "real derivative" can be complex-valued; the "real" qualifier just refers to the direction in which the limit is computed."""))

make_entry(ID("b4b319"),
    SymbolDefinition(ComplexDerivative, ComplexDerivative(Call(f, z), For(z, z)), "Complex derivative"),
    Description("The call syntax for this operator is the same as for", SourceForm(Derivative), "."),
    Description("The result is defined as", Equal(ComplexDerivative(f(z), For(z, z)), ComplexLimit((f(z+h)-f(z))/h, For(h, 0))),
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

# Holomorphic functions

make_entry(ID("499bdf"),
    SymbolDefinition(IsHolomorphic, IsHolomorphic(f(z), For(z, c)), "Holomorphic predicate"),
    Description(SourceForm(IsHolomorphic(f(z), For(z, c))), ", rendered", IsHolomorphic(f(z), For(z, c)), ", represents the predicate",
        "that", f(z), "is complex differentiable in some open neighborhood of the point", c, "."),
    Description(SourceForm(IsHolomorphic(f(z), ForElement(z, S))), ", rendered", IsHolomorphic(f(z), ForElement(z, S)), ", represents the predicate",
        "that", f(z), "is complex differentiable in some open neighborhood of every point in the set", S, "."),
    Description("As a special case", IsHolomorphic(f(z), For(z, UnsignedInfinity)), " is equivalent to", IsHolomorphic(f(1/z), For(z, 0)), "."),
    Description("As a special case", IsHolomorphic(f(z), For(z, ConstI*Infinity)), " represents the predicate that",
        f(z), "is a periodic function on the upper half plane that is holomorphic at infinity (in the sense of modular function theory)"))

make_entry(ID("0895b1"),
    SymbolDefinition(IsMeromorphic, IsMeromorphic(f(z), For(z, c)), "Meromorphic predicate"),
    Description(SourceForm(IsMeromorphic(f(z), For(z, c))), ", rendered", IsMeromorphic(f(z), For(z, c)), ", represents the predicate",
        "that", f(z), "is meromorphic in some open neighborhood of the point", c, "."),
    Description(SourceForm(IsMeromorphic(f(z), ForElement(z, S))), ", rendered", IsMeromorphic(f(z), ForElement(z, S)), ", represents the predicate",
        "that", f(z), "is meromorphic in some open neighborhood of every point in the set", S, "."),
    Description("As a special case", IsMeromorphic(f(z), For(z, UnsignedInfinity)), " is equivalent to", IsMeromorphic(f(1/z), For(z, 0)), "."),
    Description("As a special case", IsMeromorphic(f(z), For(z, ConstI*Infinity)), " represents the predicate that",
        f(z), "is a periodic function on the upper half plane that is meromorphic at infinity (in the sense of modular function theory)"))

make_entry(ID("231a99"),
    SymbolDefinition(ComplexZeroMultiplicity, ComplexZeroMultiplicity(f(z), For(z, c)), "Multiplicity (order) of complex zero"),
    Description(SourceForm(ComplexZeroMultiplicity(f(z), For(z, c))), ", rendered", ComplexZeroMultiplicity(f(z), For(z, c)),
        ", gives the root multiplicity (order of vanishing) of", f(z), "at the point", Equal(z, c), "."),
    Description("If", f, "is holomorphic at", c, "and", Unequal(f(c), 0), ", the multiplicity is zero."),
    Description("If", Equal(z, c), "is a pole of", f(z), ", returns", -n, "where", n, "is the order of the pole."),
    Description("In other words, this operator returns the order of the first nonzero term in the Laurent series of", f(z), "at", Equal(z, c), "."),
    Description("In the special case where", Equal(f(z), 0), "in a neighborhood of", c, ", the order is", Infinity, "."),
    Description("The result is undefined if", f(z), "is not meromorphic at", c, "."),
    Description("The special expression", SourceForm(For(z, c)), "declares", SourceForm(z), "as a locally bound variable within the scope of the arguments to this operator."),
)

make_entry(ID("c54261"),
    SymbolDefinition(Residue, Residue(f(z), For(z, c)), "Complex residue"),
    Description(SourceForm(Residue(f(z), For(z, c))), ", rendered", Residue(f(z), For(z, c)),
        ", gives the complex residue of", f(z), "at the point", Equal(z, c), "."))

# Paths and analytic continuation

# todo: Cartesian powers
make_entry(ID("4d0e14"),
    SymbolDefinition(Path, Path(a, b, c), "Line path"),
    Description("This object represents the path formed by connecting the given points or paths by line segments. ",
        "A path is a formal object, semantically different from a set of points: for a path object, the direction is significant, "
        "and it is undefined whether a path segment corresponds to an open interval or a closed interval between the points.",
        "The typical application is to represent a path of integration."),
    CodeExample(Path(1, -1), "Represents the path going left from", 1, "to", -1, "."),
    CodeExample(Path(a, Path(b, c)), "Equivalent to", SourceForm(Path(a, b, c)), "."),
    CodeExample(Path(1, ConstI, -1, -ConstI, 1),
        "Represents a diamond-shaped loop around the origin in the counterclockwise direction."),
    CodeExample(Path(-(ConstI*Infinity), ConstI*Infinity),
        "Represents the imaginary axis traversed upwards."),
    CodeExample(Path(1, Exp(ConstPi*ConstI/4)*Infinity),
        "Represents the ray from", 1, "to infinity along a 45 degree angle."),
    CodeExample(Path(Tuple(2, 1), Tuple(0, 0)),
        "Represents the line segment from", Tuple(2, 1), "to the origin in", Pow(RR, 2), "."))

make_entry(ID("bf8f37"),
    SymbolDefinition(CurvePath, CurvePath(f(t), For(t, a, b)), "Path along a curve"),
    CodeExample(CurvePath(f(t), For(t, a, b)), "Represents the path traced by", f(t), "as", t, "follows the path", Path(a, b), "."),
    CodeExample(CurvePath(R*Exp(ConstI*t), For(t, 0, 2*ConstPi)), "Represents the circular path counterclockwise around the origin, starting at", R, "."),
    CodeExample(CurvePath(R*Exp(ConstI*t), For(t, 0, -(2*ConstPi))), "Represents the circular path clockwise around the origin, starting at", R, "."),
    CodeExample(Path(+Infinity, CurvePath(Exp(ConstI*t), For(t, ConstPi/2, 3*ConstPi/2)), +Infinity), "Represents the Hankel contour starting at",
        +Infinity, ", moving along a straight line above the real axis to", i, ", moving in a half-circle around the origin to", -i,
        ", and returning to", +Infinity, "along a straight line below the real axis."),
    )

make_entry(ID("457aaa"),
    SymbolDefinition(AnalyticContinuation, AnalyticContinuation(f(z), For(z, a, b)), "Analytic continuation"),
    Description("Represents the value (or limiting value)", g(b), "where", g(z), "is the unique analytic continuation along the path from", a, "to", b,
        "for the function initially represented by", f(z), ". ",
        "It is assumed that the expression", f(z), "represents a holomorphic function of", z, "in a neighborhood of the initial point", a, ". ",
        "More generally, ", a, "is allowed to be a pole, branch point or even an essential singularity as long as", f(z), "is holomorphic locally in a cone around",
        "the path radiating from", a, ". ",
        "Infinite endpoints are allowed, with the obvious interpretation. "
        "Analytic continuation paths are allowed to pass through (isolated) poles of the analytically continued function. ",
        "The path is not allowed to pass through intermediate branch points, but may end at a branch point."),
    CodeExample(AnalyticContinuation(f(z), For(z, a, b)), "Represents the analytic continuation of", f(z), "along the straight-line path from", a, "to", b, "."),
    CodeExample(AnalyticContinuation(f(z), For(z, P)), "Represents the analytic continuation of", f(z), "along the path object", P, "."),
    CodeExample(AnalyticContinuation(f(z), For(z, Path(a, b, c))), "Represents the analytic continuation of", f(z), "along the straight-line path", Path(a, b, c), "."),
    CodeExample(AnalyticContinuation(f(z), For(z, CurvePath(Exp(ConstI*t), For(t, 0, theta)))),
        "Represents the analytic continuation of", f(z), "along the circular path starting at", Equal(z, 1), "and rotating ",
        "counterclockwise by the phase", theta, "."))


