#!/usr/bin/env python3
"""M0 spike: emit candidate MathJSON translations for the 15 risk items.

Rough by design. Each candidate is a hand translation of a real Fungrim
entry (cited by ID) exhibiting the construct. Running this script writes
spike_candidates.json next to it; verify with (from the compute-engine
repo):

    npx tsx /Users/arno/dev/fungrim-master/grim2mathjson/spike_verify.ts

The TS runner ce.box()es every candidate, checks for Error subexpressions,
and round-trips the canonical JSON.
"""

import json
import os
import sys

# Make sure the Fungrim snapshot is importable when run from anywhere.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def expect_source(entry_id):
    """Return str(Formula) for an entry id (sanity: cite real entries)."""
    from pygrim.formulas import all_entries

    for e in all_entries:
        args = e.args()
        ident = None
        for a in args:
            if not a.is_atom() and a.head().is_atom() and a.head()._symbol == "ID":
                ident = a.args()[0]._text
        if ident == entry_id:
            for a in args:
                if not a.is_atom() and a.head().is_atom() and a.head()._symbol == "Formula":
                    return str(a.args()[0])
    return None


# Shell declarations the candidates depend on (mirrors mapping.VERIFIED_SHELLS)
SHELLS = {
    "JacobiTheta": "(integer, complex, complex, integer?) -> complex",
    "HurwitzZeta": "(complex, complex, integer?) -> complex",
    "Erfi": "(complex) -> complex",
    "RiemannZetaZero": "(integer) -> complex",
    "DirichletGroup": "(integer) -> collection",
    "BernoulliB": "(integer) -> rational",
    "KeiperLiLambda": "(integer) -> real",
    "SloaneA": "(integer, integer) -> any",
    "Spectrum": "(matrix) -> set<complex>",
    "Divides": "(integer, integer) -> boolean",
    "CongruentMod": "(integer, integer, integer) -> boolean",
    "Primes": "collection<integer>",
    "Divisors": "(integer) -> collection<integer>",
    "SL2Z": "collection",
    "HH": "collection<complex>",
}

I = "ImaginaryUnit"
OO = "PositiveInfinity"


def C(item, entry, label, expr, declare=None, note=None):
    d = {"item": item, "entry": entry, "label": label, "json": expr}
    if declare:
        d["declare"] = declare
    if note:
        d["note"] = note
    return d


CANDIDATES = [
    # ---- #1 Where/Def ------------------------------------------------------
    C(1, "2ae142", "Where plain Defs q,w substituted (JacobiTheta r-deriv series)",
      ["Equal", ["JacobiTheta", 1, "z", "tau", "r"],
       ["Multiply",
        ["Negate", I],
        ["Power", ["Multiply", "Pi", I], "r"],
        ["Exp", ["Divide", ["Multiply", "Pi", I, "tau"], 4]],
        ["Sum",
         ["Multiply",
          ["Power", -1, "n"],
          ["Power", ["Add", ["Multiply", 2, "n"], 1], "r"],
          ["Power", ["Exp", ["Multiply", "Pi", I, "tau"]],
           ["Multiply", "n", ["Add", "n", 1]]],
          ["Power", ["Exp", ["Multiply", "Pi", I, "z"]],
           ["Add", ["Multiply", 2, "n"], 1]]],
         ["Limits", "n", "NegativeInfinity", OO]]]],
      declare={"r": "integer"}),
    C(1, "ff5e82", "Where function-def beta-reduced (a_(n) := D^n Sinc / n!)",
      ["Equal",
       ["Add",
        ["Multiply", "z",
         ["Add", ["Power", "n", 2], ["Multiply", 5, "n"], 6],
         ["Divide",
          ["Apply", ["Derivative", ["Function", ["Sinc", "z"], "z"],
                     ["Add", "n", 3]], "z"],
          ["Factorial", ["Add", "n", 3]]]],
        ["Multiply",
         ["Add", ["Power", "n", 2], ["Multiply", 5, "n"], 6],
         ["Divide",
          ["Apply", ["Derivative", ["Function", ["Sinc", "z"], "z"],
                     ["Add", "n", 2]], "z"],
          ["Factorial", ["Add", "n", 2]]]],
        ["Multiply", "z",
         ["Divide",
          ["Apply", ["Derivative", ["Function", ["Sinc", "z"], "z"],
                     ["Add", "n", 1]], "z"],
          ["Factorial", ["Add", "n", 1]]]],
        ["Divide",
         ["Apply", ["Derivative", ["Function", ["Sinc", "z"], "z"], "n"], "z"],
         ["Factorial", "n"]]],
       0],
      declare={"n": "integer"}),
    C(1, "(policy)", "Apply(Function literal, arg) fallback for unreduced defs",
      ["Apply", ["Function", ["Add", "z", "a"], "z"], "w"]),
    # 95fb3e / 6fce07: skip codes where-def-tuple / where-recursive-def (no candidate)

    # ---- #2 ComplexDerivative ---------------------------------------------
    C(2, "3ba544", "ComplexDerivative(HurwitzZeta, For(s,s)) order 1",
      ["Equal",
       ["Apply", ["Derivative", ["Function", ["HurwitzZeta", "s", "a"], "s"], 1], "s"],
       ["HurwitzZeta", "s", "a", 1]]),
    C(2, "d0d03b", "ComplexDerivative order r (symbolic, typed)",
      ["Equal",
       ["Apply", ["Derivative", ["Function", ["HurwitzZeta", "s", "a"], "s"], "r"], "s"],
       ["HurwitzZeta", "s", "a", "r"]],
      declare={"r": "integer"}),
    C(2, "83065e", "ComplexDerivative wrt 2nd argument",
      ["Equal",
       ["Apply", ["Derivative", ["Function", ["HurwitzZeta", "s", "a"], "a"], 1], "a"],
       ["Negate", ["Multiply", "s", ["HurwitzZeta", ["Add", "s", 1], "a"]]]]),

    # ---- #3 big-op condition forms ----------------------------------------
    C(3, "8f5e66", "PrimeProduct(f, For(p)) Euler product",
      ["Equal", ["Zeta", "s"],
       ["Product", ["Divide", 1, ["Subtract", 1, ["Divide", 1, ["Power", "p", "s"]]]],
        ["Element", "p", "Primes"]]]),
    C(3, "c33e2b", "PrimeProduct with Divides condition (EL-3)",
      ["Element",
       ["Multiply", ["BernoulliB", ["Multiply", 2, "n"]],
        ["Product", ["Divide", 1, "p"],
         ["Element", "p", "Primes",
          ["Divides", ["Subtract", "p", 1], ["Multiply", 2, "n"]]]]],
       "Integers"],
      declare={"n": "integer"}),
    C(3, "08ff0b", "DivisorSum with Less condition (EL-3)",
      ["Equal", ["Totient", "n"],
       ["Subtract", "n",
        ["Sum", ["Totient", "d"],
         ["Element", "d", ["Divisors", "n"], ["Less", "d", "n"]]]]],
      declare={"n": "integer"}),
    C(3, "(semantics)", "EL-3 evaluation semantics: Sum(d, d in 1..6, d<4) = 6",
      ["Sum", "d", ["Element", "d", ["Range", 1, 6], ["Less", "d", 4]]]),

    # ---- #4 ForElement indexing sets --------------------------------------
    C(4, "cce75b", "Sum ForElement(k, ZZ) + NotEqual condition",
      ["Equal", ["KeiperLiLambda", "n"],
       ["Multiply", ["Divide", 1, "n"],
        ["Sum",
         ["Subtract", 1,
          ["Power", ["Divide", ["RiemannZetaZero", "k"],
                     ["Subtract", ["RiemannZetaZero", "k"], 1]], "n"]],
         ["Element", "k", "Integers", ["NotEqual", "k", 0]]]]],
      declare={"n": "integer"}),
    C(4, "3ab92d", "Sum ForElement over symbolic non-enumerable set",
      ["Sum", ["chi", "n"], ["Element", "chi", ["DirichletGroup", "q"]]]),
    # tuple-indexing (b10ca7, 2246a7, ...): skip code tuple-indexing-set

    # ---- #5 infinities ------------------------------------------------------
    C(5, "9b0994", "directed infinity passthrough: Atan(-i) = -i*oo",
      ["Equal", ["Arctan", ["Negate", I]], ["Multiply", ["Negate", I], OO]],
      note="boxes OK; evaluates to NaN -> entries flagged directedInfinity"),
    C(5, "d0b234", "UnsignedInfinity -> ComplexInfinity in value set",
      ["Implies",
       ["And", ["Element", "s", ["Set", 1]],
        ["Element", "a", ["SetMinus", "ComplexNumbers", "NonPositiveIntegers"]]],
       ["Element", ["HurwitzZeta", "s", "a"], ["Set", "ComplexInfinity"]]]),
    C(5, "963387", "Undefined -> NaN in value set",
      ["Implies",
       ["And", ["Element", "X", ["Range", 1, OO]], ["Element", "n", "Integers"]],
       ["Element", ["SloaneA", "X", "n"], ["Union", "Integers", ["Set", "NaN"]]]]),

    # ---- #6 Cases -> Which --------------------------------------------------
    C(6, "18d335", "partial Cases (no Otherwise): Sign",
      ["Equal", ["Sign", "x"],
       ["Which", ["Greater", "x", 0], 1, ["Less", "x", 0], -1,
        ["Equal", "x", 0], 0]]),
    C(6, "91f156", "Cases with Otherwise inside Sum",
      ["Equal", ["Totient", "n"],
       ["Sum", ["Which", ["Equal", ["GCD", "n", "k"], 1], 1, "True", 0],
        ["Limits", "k", 1, "n"]]],
      declare={"n": "integer"}),
    C(6, "c12a41", "partial Cases with CongruentMod conditions",
      ["Equal", ["Power", I, "n"],
       ["Which",
        ["CongruentMod", "n", 0, 4], 1,
        ["CongruentMod", "n", 1, 4], I,
        ["CongruentMod", "n", 2, 4], -1,
        ["CongruentMod", "n", 3, 4], ["Negate", I]]],
      declare={"n": "integer"}),

    # ---- #7 subscripts / family variables -----------------------------------
    C(7, "13f252", "family call z_(k) keeps call form (binding preserved)",
      ["Sum", ["z_", "k"], ["Limits", "k", 1, "n"]]),
    C(7, "2a8ec9", "Subscript(a,k) symbolic index -> call form a_(k)",
      ["Sum", ["a_", "k"], ["Limits", "k", 0, "N"]],
      note="emitting [Subscript,a,k] canonicalizes to fused symbol a_k and LOSES the binding"),
    C(7, "(literal)", "Subscript with literal index -> fused symbol",
      ["Subscript", "a", 1]),

    # ---- #8 JacobiTheta variadic --------------------------------------------
    C(8, "d8cb3e", "JacobiTheta 3-arg",
      ["JacobiTheta", 3, "z", "tau"]),
    C(8, "2ae142", "JacobiTheta 4-arg (derivative order)",
      ["JacobiTheta", 1, "z", "tau", "r"], declare={"r": "integer"}),

    # ---- #9 n-ary relation chains -------------------------------------------
    C(9, "925e5b", "4-term Equal chain passthrough",
      ["Equal", ["Sin", "z"],
       ["Cos", ["Subtract", ["Divide", "Pi", 2], "z"]],
       ["Cos", ["Subtract", "z", ["Divide", "Pi", 2]]],
       ["Negate", ["Cos", ["Add", "z", ["Divide", "Pi", 2]]]]]),
    C(9, "(semantics)", "chain semantics: Equal(2,2,3) is False",
      ["Equal", 2, 2, 3]),
    C(9, "(semantics)", "chain semantics: Less(1,2,3) is True",
      ["Less", 1, 2, 3]),

    # ---- #10 interval family -------------------------------------------------
    C(10, "987e3c", "OpenClosedInterval(-pi, pi]",
      ["Implies",
       ["Element", ["Imaginary", "z"],
        ["Interval", ["Open", ["Negate", "Pi"]], "Pi"]],
       ["Equal", ["Ln", ["Exp", "z"]], "z"]]),
    C(10, "e7224b", "OpenInterval(0, oo)",
      ["Implies",
       ["And", ["Element", "s", ["SetMinus", "RealNumbers", ["Set", 1]]],
        ["Element", "a", ["Interval", ["Open", 0], ["Open", OO]]]],
       ["Element", ["HurwitzZeta", "s", "a"], "RealNumbers"]]),
    C(10, "(variant)", "ClosedInterval / ClosedOpenInterval",
      ["And", ["Element", "x", ["Interval", 3, 4]],
       ["Element", "y", ["Interval", 1, ["Open", OO]]]]),

    # ---- #11 ZZGreaterEqual / ZZLessEqual / Range ----------------------------
    C(11, "c5d844", "ZZGreaterEqual(2) -> Range(2, oo); ZZLessEqual(0) -> NonPositiveIntegers",
      ["Implies",
       ["And", ["Element", "s", ["Range", 2, OO]],
        ["Element", "a", "NonPositiveIntegers"]],
       ["Element", ["HurwitzZeta", "s", "a"], ["Set", "ComplexInfinity"]]]),
    C(11, "(semantics)", "literal membership: Element(5, Range(1, oo))",
      ["Element", 5, ["Range", 1, OO]]),
    C(11, "8c7cdb", "ZZGreaterEqual(0)/(1) -> NonNegative/PositiveIntegers",
      ["And", ["Element", "n", "NonNegativeIntegers"],
       ["Element", "m", "PositiveIntegers"]]),

    # ---- #12 property operators (micro-format values must box) ---------------
    C(12, "718a9b", "Zeros value set",
      ["Set", 0]),
    C(12, "cbce7f", "Solutions value: set-builder",
      ["Set", ["Add", ["Arctan", "z"], ["Multiply", "Pi", "n"]],
       ["Element", "n", "Integers"]]),
    C(12, "26c47c", "BranchPoints value with ComplexInfinity",
      ["Set", ["Negate", I], I, "ComplexInfinity"]),
    C(12, "3b11d3", "BranchCuts value: interval scaled by i",
      ["Set",
       ["Multiply", ["Interval", ["Open", "NegativeInfinity"], -1], I],
       ["Multiply", ["Interval", 1, ["Open", OO]], I]],
      note="scalar-multiple-of-set; boxes as Multiply(Interval, i) - representational only"),

    # ---- #13 typed limits -----------------------------------------------------
    C(13, "4644c0", "SequenceLimit -> Limit at +oo (flavor: sequence)",
      ["Equal", "EulerGamma",
       ["Limit",
        ["Function",
         ["Subtract", ["Sum", ["Divide", 1, "k"], ["Limits", "k", 1, "n"]],
          ["Ln", "n"]], "n"],
        OO]]),
    C(13, "0888b3", "RightLimit -> Limit direction +1 (flavor: right)",
      ["Equal", "EulerGamma",
       ["Limit",
        ["Function",
         ["Subtract", ["Multiply", ["Divide", "Pi", 2], ["BesselY", 0, "x"]],
          ["Ln", ["Divide", "x", 2]]], "x"],
        0, 1]]),
    C(13, "693e0e", "ComplexLimit -> Limit (flavor: complex)",
      ["Equal", ["Digamma", "z"],
       ["Limit",
        ["Function",
         ["Subtract", ["Divide", 1, ["Subtract", "s", 1]],
          ["HurwitzZeta", "s", "z"]], "s"],
        1]]),
    C(13, "5e0c58", "RealLimit inside an Equal chain (flavor: real)",
      ["Equal", ["Sinc", OO],
       ["Limit", ["Function", ["Sinc", "x"], "x"], OO], 0]),

    # ---- #14 Matrix2x2 ---------------------------------------------------------
    C(14, "ebfcd8", "Matrix2x2 -> Matrix; Spectrum shell",
      ["Equal", ["Spectrum", ["Matrix", ["List", ["List", 1, 1], ["List", 1, 0]]]],
       ["Set", "GoldenRatio", ["Subtract", 1, "GoldenRatio"]]]),
    C(14, "(assumption)", "Element(Matrix2x2(a,b,c,d), SL2Z) assumption shape",
      ["Element", ["Matrix", ["List", ["List", "a", "b"], ["List", "c", "d"]]],
       "SL2Z"]),
    C(14, "(check)", "Determinant of translated Matrix2x2",
      ["Determinant", ["Matrix", ["List", ["List", "a", "b"], ["List", "c", "d"]]]]),

    # ---- #15 name collisions ----------------------------------------------------
    C(15, "af23f7", "RiemannZeta -> Zeta (1-arg only in corpus)",
      ["Equal", ["HurwitzZeta", "s", 1], ["Zeta", "s"]]),
    C(15, "591d64", "BetaFunction -> Beta",
      ["Equal", "Pi", ["Beta", ["Divide", 1, 2], ["Divide", 1, 2]]]),
    C(15, "78fca3", "Erf -> Erf",
      ["Equal",
       ["Integrate",
        ["Multiply", ["Exp", ["Negate", ["Multiply", "a", ["Power", "x", 2]]]],
         ["Sinc", "x"]],
        ["Limits", "x", 0, OO]],
       ["Multiply", ["Divide", "Pi", 2],
        ["Erf", ["Divide", 1, ["Multiply", 2, ["Sqrt", "a"]]]]]]),
    C(15, "622772", "Erfi (no CE def) -> verbatim + shell",
      ["Equal", ["Erfi", "z"],
       ["Multiply", ["Divide", 2, ["Sqrt", "Pi"]],
        ["Integrate", ["Exp", ["Power", "t", 2]], ["Limits", "t", 0, "z"]]]]),
]

# Numeric compatibility probes for #15 (run by the TS verifier):
NUMERIC_CHECKS = [
    {"label": "Zeta(2) == pi^2/6", "json": ["Zeta", 2], "expect": 1.6449340668482264},
    {"label": "Beta(2,3) == 1/12", "json": ["Beta", 2, 3], "expect": 0.08333333333333333},
    {"label": "Beta(1/2,1/2) == pi (591d64)",
     "json": ["Beta", ["Divide", 1, 2], ["Divide", 1, 2]], "expect": 3.141592653589793},
    {"label": "Erf(1)", "json": ["Erf", 1], "expect": 0.8427007929497149},
    {"label": "Erfc(1)", "json": ["Erfc", 1], "expect": 0.15729920705028513},
]


def main():
    out = {
        "shells": SHELLS,
        "candidates": CANDIDATES,
        "numericChecks": NUMERIC_CHECKS,
    }
    # Attach the Fungrim source form for each cited entry (provenance).
    try:
        for c in out["candidates"]:
            if len(c["entry"]) == 6 and "(" not in c["entry"]:
                src = expect_source(c["entry"])
                if src:
                    c["source"] = src[:400]
    except Exception as exc:  # pygrim import is optional for regeneration
        print("warning: could not attach sources:", exc, file=sys.stderr)

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "spike_candidates.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {path} ({len(CANDIDATES)} candidates)")


if __name__ == "__main__":
    main()
