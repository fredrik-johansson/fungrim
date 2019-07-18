# -*- coding: utf-8 -*-

from .expr import *

from .logic import *
from .numbers import *
from .operators import *
from .complex_parts import *
from .const_gamma import *
from .pi import *
from .golden_ratio import *
from .exp import *
from .powers import *
from .sqrt import *
from .sine import *
from .atan import *
from .lambertw import *
from .gcd import *
from .factorials import *
from .fibonacci import *
from .gamma import *
from .legendre_polynomial import *
from .chebyshev import *
from .log import *
from .partitions import *
from .riemann_zeta import *
from .integrals import *
from .airy import *
from .bessel import *
from .coulomb_wave import *
from .bernoulli_numbers import *
from .stirling_numbers import *
from .gaussian_quadrature import *
from .general_functions import *
from .complex_plane import *
from .gauss_hypergeometric import *
from .confluent_hypergeometric import *
from .error_functions import *
from .jacobi_theta import *
from .weierstrass_elliptic import *
from .prime_numbers import *
from .modular_transformations import *
from .modular_j import *
from .dedekind_eta import *
from .eisenstein import *
from .dirichlet import *

describe(ComplexZeroMultiplicity, ComplexZeroMultiplicity(f(z), z, z), [], None, "Multiplicity (order) of complex zero at the given point")

describe(DivisorSigma, DivisorSigma(k, n), [Element(k, ZZGreaterEqual(0)), Element(n, ZZ)], ZZ, "Sum of divisors function")
describe(MoebiusMu, MoebiusMu(n), [Element(n, ZZGreaterEqual(1))], ZZ, "Möbius function")
describe(KroneckerDelta, KroneckerDelta(x,y), [Element(x, CC), Element(y, CC)], Set(0, 1), "Kronecker delta")
describe(LegendrePolynomial, LegendrePolynomial(n,z), [Element(n, ZZGreaterEqual(0)), Element(z, CC)], CC, "Legendre polynomial")
describe(LegendrePolynomialZero, LegendrePolynomialZero(n,k), [Element(n, ZZGreaterEqual(1)), Element(k, ZZBetween(1, n))], RR, "Legendre polynomial zero")
describe(GaussLegendreWeight, GaussLegendreWeight(n,k), [Element(n, ZZGreaterEqual(1)), Element(k, ZZBetween(1, n))], RR, "Gauss-Legendre quadrature weight")
describe(HermitePolynomial, HermitePolynomial(n,z), [Element(n, ZZGreaterEqual(0)), Element(z, CC)], CC, "Hermite polynomial")

describe(BernsteinEllipse, BernsteinEllipse(rho), [Element(rho, RR), Greater(rho, 1)], PowerSet(CC), "Bernstein ellipse with foci -1,+1 and semi-axis sum rho")
describe(UnitCircle, UnitCircle, [], PowerSet(CC), "Unit circle")

describe(JacobiTheta1, JacobiTheta1(z,tau), [Element(z, CC), Element(tau, HH)], CC, "Jacobi theta function")
describe(JacobiTheta2, JacobiTheta2(z,tau), [Element(z, CC), Element(tau, HH)], CC, "Jacobi theta function")
describe(JacobiTheta3, JacobiTheta3(z,tau), [Element(z, CC), Element(tau, HH)], CC, "Jacobi theta function")
describe(JacobiTheta4, JacobiTheta4(z,tau), [Element(z, CC), Element(tau, HH)], CC, "Jacobi theta function")

describe(Matrix2x2, Matrix2x2(a,b,c,d), [], None, "Two by two matrix")

describe(LogIntegral, LogIntegral(z), [Element(z, SetMinus(CC, Set(1)))], CC, "Logarithmic integral")

describe2(FormalPowerSeries, FormalPowerSeries(K,x), "Formal power series", None,
    Description("Represents the set of formal power series in the (formal) symbol", x,
    "and with coefficients in the set", K, ", equivalently infinite series",
    Sum(c(k) * x**k, Tuple(k, 0, Infinity)), "where", Element(c(k), K), "."))

describe2(FormalLaurentSeries, FormalLaurentSeries(K,x), "Formal Laurent series", None,
    Description("Represents the set of formal Laurent series in the (formal) symbol", x,
    "and with coefficients in the set", K, ", equivalently infinite series",
    Sum(c(k) * x**k, Tuple(k, n, Infinity)), "where", Element(c(k), K), "and", Element(n, ZZ), " may be negative."))

describe2(List, List(Ellipsis), "List with given elements", None,
    Description("Called with a finite number of arguments, represents the list with those arguments as elements.",
    "The difference between a", List, "and a", Tuple, "is mainly notational (square brackets or parentheses).",
    "A ", List, "is sometimes more natural for a homogeneous collection while a", Tuple,
    "is more natural for a heterogeneous collection."))

describe2(Tuple, Tuple(Ellipsis), "Tuple with given elements", None,
    Description("Called with a finite number of arguments, represents the tuple with those arguments as elements.",
    "The difference between a", List, "and a", Tuple, "is mainly notational (square brackets or parentheses).",
    "A ", List, "is sometimes more natural for a homogeneous collection while a", Tuple,
    "is more natural for a heterogeneous collection."))

entries_dict = {}
for entry in all_entries:
    if entry.id() in entries_dict:
        raise ValueError("duplicated ID %s" % entry.id())
    entries_dict[entry.id()] = entry

topics_dict = {}
for topic in all_topics:
    if topic.title() in topics_dict:
        raise ValueError("duplicated title %s" % topic.title())
    topics_dict[topic.title()] = topic

