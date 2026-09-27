"""Symbol-mapping tables: Fungrim head/atom -> Compute Engine name.

Data only, no logic. Every entry in SYMBOL_MAP below was either verified
during the M0 spike (see SPIKE-DECISIONS.md for the ce.box transcripts), is a
trivial structural rename exercised by the spike candidates, or was verified
during M1/M2 against the live Compute Engine (`ce.lookupDefinition` oracle +
ce.box/evaluate probes; see the M1 verification notes at the bottom).

The M0 rule stands: a head is either
  (a) mapped here (SYMBOL_MAP),
  (b) kept verbatim + shell-declared (SHELL_HEADS / VERIFIED_SHELLS),
  (c) a structural construct (structural.py / STRUCTURAL_HEADS),
  (d) metadata-extracted (METADATA_HEADS, top-level routing), or
  (e) on SKIP_HEADS.
An unknown head is a translator error.
"""

# ---------------------------------------------------------------------------
# Pure renames (Fungrim name -> CE name). Identity mappings are listed
# explicitly when they were verified, so we can distinguish "verified same
# name" from "not yet audited".
# ---------------------------------------------------------------------------
SYMBOL_MAP: dict = {
    # -- arithmetic / elementary (exercised throughout the spike candidates)
    "Add": "Add",
    "Sub": "Subtract",
    "Mul": "Multiply",
    "Div": "Divide",
    "Pow": "Power",
    "Neg": "Negate",       # Neg(Infinity) special-cased in walker
    # "Pos": (strip, structural)
    # "Inv": (structural: Inv(x) -> ["Divide", 1, x]; CE Inverse is matrix inverse)
    "Sqrt": "Sqrt",
    "NthRoot": "Root",     # NthRoot(x, n) = x^(1/n); CE Root(x, n) verified Root(8,3)=2
    "Exp": "Exp",
    "Log": "Ln",           # Fungrim Log is the natural log; CE Ln (verified Ln(e)=1)
    "LogBase": "Log",      # CE Log(x, base); 0 formula occurrences but kept for safety
    "Sign": "Sign",
    "Csgn": "Csgn",        # no CE def -> shell (also in SHELL_HEADS)
    "Abs": "Abs",
    "Re": "Real",
    "Im": "Imaginary",
    "Arg": "Argument",
    "Conjugate": "Conjugate",     # CE lookupDefinition verified
    "Floor": "Floor",
    "Ceil": "Ceil",
    "Max": "Max",
    "Min": "Min",
    "Mod": "Mod",
    "GCD": "GCD",
    "LCM": "LCM",
    "Factorial": "Factorial",
    "DoubleFactorial": "Factorial2",
    "Odd": "IsOdd",        # CE boolean predicate, verified boxes + EL-3 compatible
    "Even": "IsEven",

    # -- trigonometric / hyperbolic (all CE names verified via lookupDefinition)
    "Sin": "Sin",
    "Cos": "Cos",
    "Tan": "Tan",
    "Sec": "Sec",
    "Csc": "Csc",
    "Cot": "Cot",
    "Sinh": "Sinh",
    "Cosh": "Cosh",
    "Tanh": "Tanh",
    "Sech": "Sech",
    "Csch": "Csch",
    "Coth": "Coth",
    "Asin": "Arcsin",
    "Acos": "Arccos",
    "Atan": "Arctan",
    "Asec": "Arcsec",
    "Acsc": "Arccsc",
    "Acot": "Arccot",
    "Asinh": "Arsinh",
    "Acosh": "Arcosh",
    "Atanh": "Artanh",
    "Asech": "Arsech",
    "Acsch": "Arcsch",
    "Acoth": "Arcoth",
    "Atan2": "Arctan2",
    "Sinc": "Sinc",        # verified present (trigonometry.ts:263)

    # -- constants
    "Pi": "Pi",
    "ConstI": "ImaginaryUnit",
    "ConstE": "ExponentialE",
    "ConstGamma": "EulerGamma",        # arithmetic.ts:1574
    "GoldenRatio": "GoldenRatio",      # arithmetic.ts:1537
    "ConstCatalan": "CatalanConstant",
    # ConstGlaisher: no CE def -> verbatim shell

    # -- infinities / undefined (decision: M0 spike #5)
    "Infinity": "PositiveInfinity",
    "UnsignedInfinity": "ComplexInfinity",
    "Undefined": "NaN",
    "True_": "True",
    "False_": "False",
    # Neg(Infinity) -> "NegativeInfinity" handled structurally.
    # Directed infinities c*Infinity: passthrough as ["Multiply", c,
    # "PositiveInfinity"] + entry flag `directedInfinity` (boxes OK,
    # evaluates to NaN -- see SPIKE-DECISIONS.md #5).

    # -- sets / domains
    "ZZ": "Integers",
    "QQ": "RationalNumbers",
    "RR": "RealNumbers",
    "CC": "ComplexNumbers",
    "PP": "Primes",        # set of primes == the spike #3 Primes shell collection
    "AlgebraicNumbers": "AlgebraicNumbers",  # CE sets.ts, verified boxes
    "Element": "Element",
    "NotElement": "NotElement",
    "Union": "Union",
    "Intersection": "Intersection",
    "SetMinus": "SetMinus",
    "Set": "Set",          # NOTE: Set(body, ForElement(...)) comprehension is structural
    "Subset": "Subset",
    "SubsetEqual": "SubsetEqual",
    "PowerSet": "PowerSet",
    "Cardinality": "Count",  # CE has Count (collections.ts:566), no Cardinality;
                             # verified Count(Set(1,2,3)) evaluates to 3.
                             # (M0 table erroneously listed identity mapping.)
    "CartesianProduct": "CartesianProduct",
    "Tuple": "Tuple",
    "List": "List",
    "Item": "At",          # Item(t, Tuple(i,j)) -> ["At", t, i, j] (structural reshape)
    "Length": "Length",
    # ZZGreaterEqual / ZZLessEqual / Range are structural (see structural.py):
    #   ZZGreaterEqual(0) -> "NonNegativeIntegers"
    #   ZZGreaterEqual(1) -> "PositiveIntegers"
    #   ZZGreaterEqual(a) -> ["Range", a, "PositiveInfinity"]
    #   ZZLessEqual(0)    -> "NonPositiveIntegers"
    #   ZZLessEqual(b)    -> ["Range", "NegativeInfinity", b]
    #   Range(a, b)       -> ["Range", a, b]
    # Interval family is structural (Open markers).

    # -- relations / logic (n-ary chains pass through, spike #9)
    "Equal": "Equal",
    "Same": "Equal",       # Same(a,b,c) used once (61480c) as an identity chain
    "NotEqual": "NotEqual",
    "Less": "Less",
    "LessEqual": "LessEqual",
    "Greater": "Greater",
    "GreaterEqual": "GreaterEqual",
    "And": "And",
    "Or": "Or",
    "Not": "Not",
    "Implies": "Implies",
    "Equivalent": "Equivalent",
    # All/Exists -> ForAll/Exists with ["Element", x, S] first argument
    # (structural; CE logic.ts:145/168, signature "(value, boolean) -> boolean",
    # box-verified including Implies/And condition folding).

    # -- min/max/sup/inf over sets (CE arithmetic.ts:1844+, "(value*) -> ...";
    #    generator forms become set-builder arguments, structural.py)
    "Minimum": "Min",
    "Maximum": "Max",
    "Supremum": "Supremum",
    "Infimum": "Infimum",

    # -- linear algebra
    "Det": "Determinant",
    "Matrix": "Matrix",    # generator form Matrix(b, For, For) -> skip matrix-generator
    "IdentityMatrix": "IdentityMatrix",
    "ZeroMatrix": "ZeroMatrix",
    # Matrix2x2(a,b,c,d) / Matrix2x1(a,b) -> ["Matrix", ["List", ...]] (structural)

    # -- special functions: name-collision audit (spike #15 + M1 batch, all
    #    verified numerically against CE kernels where a kernel exists)
    "RiemannZeta": "Zeta",        # corpus uses arity 1 only; Zeta(2)=pi^2/6 verified
    "BetaFunction": "Beta",       # Beta(2,3)=1/12 verified; B(1/2,1/2)=pi
    "Erf": "Erf",                 # same function; CE kernel has ~1.2e-7 accuracy bug (flagged)
    "Erfc": "Erfc",               # same function; same kernel caveat
    "Gamma": "Gamma",
    "LogGamma": "GammaLn",
    "DigammaFunction": "Digamma",
    "PolyGamma": "PolyGamma",
    "Totient": "Totient",         # number-theory.ts:7, verified
    "KroneckerDelta": "KroneckerDelta",
    "Binomial": "Binomial",
    "Fibonacci": "Fibonacci",          # combinatorics.ts:26
    "StirlingS2": "Stirling",     # CE Stirling IS the 2nd kind S(n,m); Stirling(4,2)=7 verified
    "BellNumber": "BellNumber",   # BellNumber(4)=15 verified
    "PartitionsP": "NPartition",  # CE NPartition(n) = # integer partitions; NPartition(5)=7 verified
    "BesselJ": "BesselJ",         # CE (order, x) == Fungrim (nu, z); 3-arg = derivative
    "BesselY": "BesselY",         #   order -> derivative encoding (structural)
    "BesselI": "BesselI",
    "BesselK": "BesselK",
    "AiryAi": "AiryAi",           # CE 1-arg; Fungrim 2-arg (z, r) = r-th derivative
    "AiryBi": "AiryBi",           #   -> derivative encoding (structural)
    "LambertW": "LambertW",       # CE 2-arg (z, k), branch index last; see note below

    # -- calculus (structural reshaping in structural.py; CE target names)
    "Sum": "Sum",
    "Product": "Product",
    "Integral": "Integrate",
    # ComplexDerivative & friends -> Apply/Derivative (structural, spike #2)
    # *Limit variants -> Limit (+ flavor annotation) (structural, spike #13)
}

# Variable RENAMES: Fungrim variable names that collide with *semantically
# loaded* CE built-ins. Emitting them verbatim would silently change
# semantics, so they are renamed everywhere (formula, assumptions, variables
# list; bound and free alike). Verified against ce.lookupDefinition over the
# full 73-name census of non-builtin symbols in the corpus:
#   i -> ImaginaryUnit, e -> ExponentialE   (constants, holdUntil never)
#   N -> CE numeric-evaluation operator     (boxing "N" infers (any)->unknown)
#   D -> CE partial-derivative operator
# The remaining CE-known names (A, C, F, K, W, m, s) are declared but INERT
# (type unknown, no value) and are safe to keep. "pi" is not a CE symbol.
# Synthesized subscript names ("a_1", family "a_") are exempt -- they never
# collide (see structural.translate_subscript).
VARIABLE_RENAMES: dict = {
    "i": "i_var",
    "e": "e_var",
    "N": "N_var",
    "D": "D_var",
}

# Fungrim heads kept VERBATIM and shell-declared via declarations.json (M4).
# Values are CE `declare` type signatures *verified by ce.declare() during the
# spike*; heads added in M1/M2 without a verified signature live in
# SHELL_HEADS below and get "(any+) -> any" until M4 derives real signatures.
VERIFIED_SHELLS: dict = {
    "JacobiTheta": "(integer, complex, complex, integer?) -> complex",  # spike #8
    "HurwitzZeta": "(complex, complex, integer?) -> complex",
    "Erfi": "(complex) -> complex",
    "RiemannZetaZero": "(integer) -> complex",
    "DirichletGroup": "(integer) -> collection",
    "BernoulliB": "(integer) -> rational",
    "KeiperLiLambda": "(integer) -> real",
    "SloaneA": "(any, integer) -> any",  # 1st arg may be a designator string
                                         # ("A000793", entry 6af603) -- spike
                                         # tested only the integer form
    "DedekindEta": "(complex) -> complex",
    "ModularJ": "(complex) -> complex",
    "Spectrum": "(matrix) -> set<complex>",
    "AGM": "(complex, complex) -> complex",
    # predicates needed by indexing-set conditions (spike #3): a condition
    # head MUST be boolean-typed or Element's EL-3 form rejects it.
    "Divides": "(integer, integer) -> boolean",
    "CongruentMod": "(integer, integer, integer) -> boolean",
    # synthesized collections (spike #3):
    "Primes": "collection<integer>",          # PrimeSum/PrimeProduct index domain; also PP
    "Divisors": "(integer) -> collection<integer>",  # DivisorSum/DivisorProduct
    # inert structural domains:
    "SL2Z": "collection",
    "HH": "collection<complex>",              # upper half-plane
    "RealBall": "(real, real) -> collection<real>",
    # M4: CE knows AlgebraicNumbers only in the LaTeX dictionary
    # (definitions-sets.ts:89) -- no global-library definition, so the
    # shell table must cover it (it boxes fine either way; SYMBOL_MAP keeps
    # the identity mapping so translation output is unchanged).
    "AlgebraicNumbers": "collection<complex>",
}

# Heads/atoms kept verbatim WITHOUT a verified signature yet (M4 derives one
# from the SymbolDefinition domain tables; until then "(any+) -> any" for
# function heads, "any" for atoms). Grouped for review only -- flat set.
SHELL_HEADS: frozenset = frozenset([
    # special functions, no CE definition (lookupDefinition oracle, M1)
    "ChebyshevT", "ChebyshevU", "LegendrePolynomial", "LegendrePolynomialZero",
    "HermitePolynomial", "GaussLegendreWeight",
    "RisingFactorial", "FallingFactorial", "HarmonicNumber",
    "StirlingS1", "StirlingCycle", "StirlingSeriesRemainder",
    "MoebiusMu", "DivisorSigma", "LiouvilleLambda", "SquaresR", "DedekindSum",
    "PrimePi", "PrimeNumber", "KroneckerSymbol", "LegendreSymbol", "JacobiSymbol",
    "DiscreteLog", "HardyRamanujanA", "LandauG",
    "EllipticK", "EllipticE", "EllipticPi",
    "IncompleteEllipticF", "IncompleteEllipticE", "IncompleteEllipticPi",
    "EllipticSingularValue", "EllipticInvariantG", "EllipticRootE",
    "CarlsonRF", "CarlsonRG", "CarlsonRJ", "CarlsonRD", "CarlsonRC",
    "CarlsonHypergeometricR", "CarlsonHypergeometricT",
    "AGMSequence", "XGCD",
    "Hypergeometric0F1", "Hypergeometric1F1", "Hypergeometric2F1",
    "Hypergeometric2F0", "Hypergeometric3F2", "Hypergeometric1F2",
    "Hypergeometric2F2", "HypergeometricPFQ",
    "Hypergeometric0F1Regularized", "Hypergeometric1F1Regularized",
    "Hypergeometric2F1Regularized", "Hypergeometric3F2Regularized",
    "Hypergeometric1F2Regularized", "Hypergeometric2F2Regularized",
    "HypergeometricPFQRegularized",
    "HypergeometricU", "HypergeometricUStar", "HypergeometricUStarRemainder",
    "CoulombF", "CoulombG", "CoulombH", "CoulombC", "CoulombSigma",
    "AiryAiZero", "AiryBiZero", "BesselJZero", "BesselYZero",
    "HankelH1", "HankelH2",
    "SinIntegral", "LogIntegral",
    "UpperGamma", "LowerGamma",
    "DigammaFunctionZero",
    "BarnesG", "LogBarnesG", "LogBarnesGRemainder",
    "PolyLog", "LerchPhi", "MultiZetaValue", "StieltjesGamma", "RiemannXi",
    "DeBruijnNewmanLambda",
    "GeneralizedBernoulliB", "BernoulliPolynomial", "EulerE", "EulerPolynomial",
    "IncompleteBeta", "IncompleteBetaRegularized",
    "LambertWPuiseuxCoefficient",
    "EisensteinE", "EisensteinG",
    "WeierstrassP", "WeierstrassZeta", "WeierstrassSigma",
    "ModularLambda", "ModularGroupAction",
    "DedekindEtaEpsilon", "EulerQSeries",
    "JacobiThetaEpsilon", "JacobiThetaPermutation", "JacobiThetaQ",
    "DirichletL", "DirichletLZero", "DirichletLambda", "DirichletCharacter",
    "PrimitiveDirichletCharacters", "ConreyGenerator",
    "GaussSum", "JacobiSum",
    "HilbertClassPolynomial", "HilbertMatrix",
    "PrimitiveReducedPositiveIntegralBinaryQuadraticForms",
    # predicates kept verbatim (boolean-typed shells)
    "AsymptoticTo", "EqualNearestDecimal", "NearestDecimal",
    "ComplexIndefiniteIntegralEqual", "RealIndefiniteIntegralEqual",
    "IndefiniteIntegralEqual",
    "IsHolomorphic", "IsMeromorphic",   # also METADATA_HEADS at top level
    # generator heads kept verbatim in expression position (METADATA_HEADS
    # routing applies only at top level; see structural.translate_generator_head)
    "Zeros", "Poles", "BranchPoints", "BranchCuts", "EssentialSingularities",
    "Residue", "AnalyticContinuation", "ComplexZeroMultiplicity",
    "Solutions", "UniqueSolution", "UniqueZero",
    "ArgMin", "ArgMax", "ArgMinUnique", "ArgMaxUnique",
    "SequenceLimitInferior", "SequenceLimitSuperior",
    # domain / geometry constructs
    "Lattice", "Matrices", "GeneralLinearGroup", "SpecialLinearGroup",
    "CartesianPower", "Interior", "InteriorClosure",
    "OpenDisk", "ClosedDisk", "BernsteinEllipse", "UnitCircle",
    "ModularGroupFundamentalDomain", "ModularLambdaFundamentalDomain",
    "PSL2Z", "Csgn",
    # atoms (propositions / constants without CE equivalents)
    "RiemannHypothesis", "GeneralizedRiemannHypothesis",
    "ConstGlaisher", "HalphenConstant",
    "Rings", "Fields",
]) | frozenset(VERIFIED_SHELLS)

# NOTE on LambertW: CE defines LambertW natively as 2-arg
# `(number, number?) -> number` with the branch index LAST (SymPy/Fungrim
# convention), as of 2026-07-09. The corpus maps LambertW(z) and
# LambertW(z, 0) to the 1-arg form ["LambertW", z] (principal branch) and
# non-principal branches to 2-arg ["LambertW", z, k]; both box directly with
# no harness re-declaration needed. LambertW(z, k, r) = r-th derivative ->
# derivative encoding (structural), like BesselJ/AiryAi derivative orders.

# Heads whose entries are routed to properties.json when they are the
# top-level operator shape (spike #12 fixes the micro-format). In expression
# position they translate verbatim with a Function-literal first argument.
METADATA_HEADS = frozenset([
    "Zeros",
    "Poles",
    "BranchPoints",
    "BranchCuts",
    "EssentialSingularities",
    "Residue",
    "AnalyticContinuation",
    "ComplexZeroMultiplicity",
    "IsHolomorphic",
    "IsMeromorphic",
    "Solutions",
    "UniqueSolution",
    "UniqueZero",
])

# Heads/atoms that force a skip record (machine-readable reason as value).
SKIP_HEADS: dict = {
    # variadic splices (Carlson entries and a few sums)
    "Repeat": "repeat-splice",
    "Step": "step-splice",
    # formal indeterminates / power-series domains
    "XX": "formal-indeterminate",
    "XXSeries": "formal-indeterminate",
    "XXNonCommutative": "formal-indeterminate",
    "SerX": "formal-indeterminate",
    "SerY": "formal-indeterminate",
    "SerQ": "formal-indeterminate",
    "Ser": "formal-indeterminate",
    "Pol": "formal-indeterminate",
    "PolX": "formal-indeterminate",
    "PolY": "formal-indeterminate",
    "PolZ": "formal-indeterminate",
    "NonComX": "formal-indeterminate",
    "NonComY": "formal-indeterminate",
    "NonCom": "formal-indeterminate",
    "PowerSeries": "formal-indeterminate",
    "LaurentSeries": "formal-indeterminate",
    "FormalPowerSeries": "formal-indeterminate",
    "FormalLaurentSeries": "formal-indeterminate",
    "FormalPuiseuxSeries": "formal-indeterminate",
    "SeriesCoefficient": "formal-indeterminate",
    "FormalGenerator": "formal-indeterminate",
    "QSeriesCoefficient": "formal-indeterminate",
    "Coefficient": "formal-indeterminate",
    "CallIndeterminate": "formal-indeterminate",
    "EvaluateIndeterminate": "formal-indeterminate",
    "Polynomials": "formal-indeterminate",
    "PolynomialFractions": "formal-indeterminate",
    "RationalFunctions": "formal-indeterminate",
    "RationalFunctionDegree": "formal-indeterminate",
    "PolynomialDegree": "formal-indeterminate",
    "SymmetricPolynomial": "formal-indeterminate",
    "Polynomial": "formal-indeterminate",
    "Cyclotomic": "formal-indeterminate",
    "StandardIndeterminates": "formal-indeterminate",
    "StandardNoncommutativeIndeterminates": "formal-indeterminate",
    "QuotientRing": "formal-indeterminate",
    # contour / path integrals (no CE representation)
    "CurvePath": "path-integral",
    "Path": "path-integral",
    # ellipses
    "Ellipsis": "ellipsis",
    "EqualQSeriesEllipsis": "ellipsis",
    # presentation-only
    "CodeExample": "presentation",
    "Description": "presentation",
    "SourceForm": "presentation",
    "Table": "presentation",
    "TableRelation": "presentation",
    "Image": "presentation",
}

# Structural skip reason codes emitted by structural.py (not head-keyed):
#   where-def-tuple      Def(Tuple(...), rhs) with non-literal-Tuple rhs
#   where-function-def   Def(f(..), body) that cannot be beta-reduced
#                        (f used as a bare function value)
#   where-recursive-def  Def(f(n), body) where body references f
#   tuple-indexing-set   ForElement(Tuple(...), S) / For(Tuple(...)) binders
#                        (CE indexing sets require a symbol index)
#   generator-list       List/Tuple(x_(k), For(k, ...)) variadic splice
#   matrix-generator     Matrix(body, For(i,...), For(j,...))
#   bare-for-generator   For(x) binder without an extractable Element domain
#   symbol-definition    entry has no Formula (SymbolDefinition entries; these
#                        feed the M4 shell table, not the corpus)
#   unknown-head         catch-all -- a hard error under --strict
