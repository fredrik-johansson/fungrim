# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Elementary logic and set theory"),
    Section("Logical operations"),
    Entries(
        "488b6d",
        "0a6d2e",
        "a53803",
        "2d6cf1",
        "379aa0",
    ),
    Section("Sets"),
    Entries(
        "cf447f",
    ),
    Section("Set operations"),
    Entries(
        "81efd5",
        "1d963f",
        "985bda",
        "0e613e",
        "ec33ac",
        "27f845",
        "590290",
        "a9e8df",
        "e58aaf",
    ),
)

make_entry(ID("488b6d"),
    SymbolDefinition(Not, Not(x), "Logical not"))

make_entry(ID("0a6d2e"),
    SymbolDefinition(And, And(x, y), "Logical and"))

make_entry(ID("a53803"),
    SymbolDefinition(Or, Or(x, y), "Logical or"))

make_entry(ID("2d6cf1"),
    SymbolDefinition(Equivalent, Equivalent(x, y), "Logical equivalence"))

make_entry(ID("379aa0"),
    SymbolDefinition(Implies, Implies(x, y), "Logical implication"))


make_entry(ID("cf447f"),
    SymbolDefinition(Set, Set(Ellipsis), "Set with given elements"),
    Description(SourceForm(Set(x, y, z)), ", rendered as", Set(x, y, z),
        ", represents the finite set containing the given elements (and similarly with any number of argumeents).",
        "In particular, ", SourceForm(Set()), "or", Set(),
            "is the empty set, and", SourceForm(Set(x)), "or", Set(x), "is a singleton set."),
    Description("The special expressions", SourceForm(For), ", ", SourceForm(ForElement), "define a set comprehension:"),
    Description(SourceForm(Set(f(x), For(x), P(x))), ", rendered as", Set(f(x), For(x), P(x)), "."),
    Description(SourceForm(Set(f(x), ForElement(x, S))), ", rendered as", Set(f(x), ForElement(x, S)), "."),
    Description(SourceForm(Set(f(x), ForElement(x, S), P(x))), ", rendered as", Set(f(x), ForElement(x, S), P(x)), "."),
    Description(SourceForm(Set(f(x), For(x, a, b))), ", rendered as", Set(f(x), For(x, a, b)), ".")
)

make_entry(ID("81efd5"),
    SymbolDefinition(Cardinality, Cardinality(S), "Set cardinality"),
    Description(SourceForm(Cardinality(S)), ", rendered as", Cardinality(S),
        ", represents the cardinality of the set", S, ".",
        "The cardinality of a finite set is a nonnegative integer.",
        "Cardinalities of infinite sets may be represented in terms of this symbol;",
        "for example,", Cardinality(ZZ), "is the cardinality of any countable set",
        "and", Cardinality(RR), "is the cardinality of the continuum."))


make_entry(ID("1d963f"),
    SymbolDefinition(PowerSet, PowerSet(S), "Power set"))

make_entry(ID("985bda"),
    SymbolDefinition(Union, Union(S, T), "Set union"))

make_entry(ID("0e613e"),
    SymbolDefinition(Intersection, Intersection(S, T), "Set intersection"))

make_entry(ID("ec33ac"),
    SymbolDefinition(SetMinus, SetMinus(S, T), "Set difference"))

make_entry(ID("27f845"),
    SymbolDefinition(Element, Element(x, S), "Set membership"))

make_entry(ID("590290"),
    SymbolDefinition(NotElement, NotElement(x, S), "Set non-membership"))

make_entry(ID("a9e8df"),
    SymbolDefinition(Subset, Subset(S, T), "Strict subset"))

make_entry(ID("e58aaf"),
    SymbolDefinition(SubsetEqual, SubsetEqual(S, T), "Subset"))


