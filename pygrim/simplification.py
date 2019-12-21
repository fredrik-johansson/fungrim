from .expr import *

class EvaluationContext(object):
    def __init__(self, symbol_values=None, assumptions=None):
        pass

additive_ops = set([Pos, Neg, Add, Sub])
ring_arithmetic_ops = set([Pos, Neg, Add, Sub, Mul])
field_arithmetic_ops = set([Pos, Neg, Add, Sub, Mul, Div])
arithmetic_ops = set([Pos, Neg, Add, Sub, Mul, Div, Sqrt, Pow])

# assumed not to contain integers...
positive_real_constants = set([Pi, ConstE, ConstGamma, ConstCatalan, GoldenRatio])
irrational_constants = set([Pi, ConstE, GoldenRatio])
complex_constants = positive_real_constants.union(set([ConstI]))

set_logic_ops = set([Not, And, Or, Implies, Equal, NotEqual, Element, NotElement])



class Simplification(object):

    def __init__(self):
        try:
            from flint import fmpz, fmpq
            self._mpz = fmpz
            self._mpq = fmpq
            def numer_denom(x):
                if isinstance(x, fmpq):
                    return x.p, x.q
                else:
                    return x, 1
            self._mpq_numer_denom = numer_denom
        except ImportError:
            from fractions import Fraction
            self._mpz = int
            self._mpq = Fraction
            def numer_denom(x):
                if isinstance(x, Fraction):
                    return x.numerator, x.denominator
                else:
                    return x, 1
            self._mpq_numer_denom = numer_denom

    def _rational(self, p, q):
        p = int(p)
        q = int(q)
        if q == 1:
            return Expr(p)
        if p < 0:
            return Neg(Div(-p, q))
        return Div(p, q)

    def is_zero(self, x, context=None):
        """
        Checks if x is the number zero.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        if x.is_integer():
            return int(x) == 0
        if self.is_integer(x) == False:
            return False
        if self.is_positive(x, context):
            return False
        return None

    def is_not_zero(self, x, context=None):
        """
        Checks if x is not the number zero.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        v = self.is_zero(x, context=None)
        if v is None:
            return v
        return not v

    def is_infinity(self, x, context=None):
        """
        Checks if x is an infinity (equal to UnsignedInfinity or c * Infinity
        for some nonzero complex number c).

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        if x == Infinity:
            return True
        if x == UnsignedInfinity:
            return True
        if x == Undefined:
            return False
        if x.head() in (Pos, Neg):
            arg, = x.args()
            if self.is_infinity(arg, context):
                return True
        if x.head() == Mul:
            args = x.args()
            if any(self.is_infinity(arg, context) for arg in args):
                if all(self.is_infinity(arg, context) or (self.is_complex(arg, context) and self.is_not_zero(arg, context)) for arg in x.args()):
                    return True
        return None

    def is_nonnegative(self, x, context=None):
        """
        Checks if x is an object satisfying x >= 0.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        if x.is_integer():
            return int(x) >= 0
        if x in positive_real_constants:
            return True
        if self.is_real(x, context):
            if x.head() in (Pos, Add, Mul, Exp, Sqrt):
                if all(self.is_nonnegative(arg, context) for arg in x.args()):
                    return True
            if x.head() == Div:
                p, q = x.args()
                if self.is_nonnegative(p, context) and self.is_positive(q, context):
                    return True
            if x.head() == Pow:
                base, exp = x.args()
                if self.is_positive(base, context):
                    return True
        return None

    def is_positive(self, x, context=None):
        """
        Checks if x is an object satisfying x > 0.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        if x.is_integer():
            return int(x) > 0
        if x in positive_real_constants:
            return True
        if self.is_real(x, context):
            if x.head() in (Exp, Cosh):
                return True
            if x.head() in (Pos, Add, Mul, Sqrt):
                if all(self.is_positive(arg, context) for arg in x.args()):
                    return True
            if x.head() == Div:
                p, q = x.args()
                if self.is_positive(p, context) and self.is_positive(q, context):
                    return True
            if x.head() == Pow:
                base, exp = x.args()
                if self.is_positive(base, context):
                    return True
        return None

    def is_integer(self, x, context=None):
        """
        Checks if x is an integer.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        if x.is_integer():
            return True
        if x.head() in (Pos, Neg, Add, Sub, Mul):
            if all(self.is_integer(arg, context) for arg in x.args()):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            if self.is_integer(base, context) and self.is_integer(exp, context) and self.is_nonnegative(exp, context):
                return True
        if x.head() == Factorial:
            n, = x.args()
            if self.is_integer(n, context) and self.is_nonnegative(n, context):
                return True
        if x in complex_constants:
            return False
        if self.is_infinity(x, context) or x == Undefined:
            return False
        return None

    # todo: irrational + rational, irrational * rational, irrational / rational, rational / irrational
    # todo: square roots
    # todo: exp, log, sin, cos, tan of rational numbers
    def is_rational(self, x, context=None):
        """
        Checks if x is a rational number.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        if self.is_integer(x, context):
            return True
        if x == Pi or x == ConstE:
            return False
        if x.head() in (Pos, Neg, Add, Sub, Mul):
            if all(self.is_rational(arg, context) for arg in x.args()):
                return True
        if x.head() == Div:
            p, q = x.args()
            if self.is_integer(p, context) and self.is_integer(q, context) and self.is_not_zero(q, context):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            if self.is_rational(base, context) and self.is_integer(exp, context) and (self.is_not_zero(base, context) or self.is_nonnegative(exp, context)):
                return True
        if self.is_infinity(x, context) or x == Undefined:
            return False
        return None

    def is_real(self, x, context=None):
        """
        Checks if x is a real number.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        if self.is_rational(x, context):
            return True
        if x in (Pi, ConstGamma, ConstE, ConstCatalan):
            return True
        if x == ConstI:
            return False
        if x.head() in (Pos, Neg, Add, Sub, Mul, Exp, Sin, Cos):
            if all(self.is_real(arg, context) for arg in x.args()):
                return True
        if x.head() == Div:
            p, q = x.args()
            if self.is_real(p, context) and self.is_real(q, context) and self.is_not_zero(q, context):
                return True
        if x.head() == Sqrt:
            arg, = x.args()
            if self.is_real(arg, context) and self.is_nonnegative(arg, context):
                return True
        if x.head() == Log:
            arg, = x.args()
            if self.is_real(arg, context) and self.is_positive(arg, context):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            if self.is_real(base, context) and self.is_real(exp, context) and \
                (self.is_not_zero(base, context) or self.is_positive(exp, context)):
                return True
        if self.is_infinity(x, context) or x == Undefined:
            return False
        return None

    def is_complex(self, x, context=None):
        """
        Checks if x is a complex number.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        if self.is_real(x, context):
            return True
        if x == ConstI:
            return True
        if x.head() in (Pos, Neg, Add, Sub, Mul, Sqrt, Exp, Sin, Cos):
            if all(self.is_complex(arg, context) for arg in x.args()):
                return True
        if x.head() == Div:
            p, q = x.args()
            if self.is_complex(p, context) and self.is_complex(q, context) and self.is_not_zero(q, context):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            # todo: more generally for re(exp) > 0
            if self.is_complex(base, context) and self.is_complex(exp, context) and \
                (self.is_not_zero(base, context) or (self.is_real(exp, context) and self.is_positive(exp, context))):
                return True
        if x.head() == Log:
            arg, = x.args()
            if self.is_complex(arg, context) and self.is_not_zero(arg, context):
                return True
        if self.is_infinity(x, context) or x == Undefined:
            return False
        return None

    # todo: identify different types; bools, tuples, sets, matrices, ...
    def equal(self, a, b, context=None):
        """
        Checks if a and b are equal (represent exactly the same mathematical
        object).

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        assert isinstance(a, Expr)
        assert isinstance(b, Expr)
        if a == b:
            return True
        if a.is_integer() and b.is_integer():
            return False

        aq = self.is_rational(a, context)
        bq = self.is_rational(b, context)
        if aq is not None and bq is not None and aq != bq:
            return False
        if aq and bq:
            aq = self.is_integer(a, context)
            bq = self.is_integer(b, context)
            if aq is not None and bq is not None and aq != bq:
                return False

        aq = self.is_complex(a, context)
        bq = self.is_complex(b, context)
        if aq is not None and bq is not None and aq != bq:
            return False
        if aq and bq:
            aq = self.is_real(a, context)
            bq = self.is_real(b, context)
            if aq is not None and bq is not None and aq != bq:
                return False

        aq = self.is_infinity(a, context)
        bq = self.is_infinity(b, context)
        if aq is not None and bq is not None and aq != bq:
            return False
        return None

    def element(self, a, S, context=None):
        """
        Checks if a is an element of S.

        Returns True, False, or None for unknown. Uses only cheap checks
        without simplifying the input. The user may pre-simplify the input
        to improve success rates.
        """
        assert isinstance(a, Expr)
        if S == CC:
            return self.is_complex(a, context)
        if S == RR:
            return self.is_real(a, context)
        if S == QQ:
            return self.is_rational(a, context)
        if S == ZZ:
            return self.is_integer(a, context)
        # todo: check for comprehensions
        if S.head() == Set:
            check = [self.equal(a, b, context) for b in S.args()]
            if True in check:
                return True
            if all(c == False for c in check):
                return False
        # todo: check for comprehensions
        if S.head() == Union:
            if len(S.args()) == 0:
                return False
            check = [self.element(a, T, context) for T in S.args()]
            if True in check:
                return True
            if all(c == False for c in check):
                return False
        # todo: check for comprehensions
        if S.head() == Intersection:
            assert len(S.args()) >= 1
            check = [self.element(a, T, context) for T in S.args()]
            if all(c == True for c in check):
                return True
            if False in check:
                return False
        if S.head() == SetMinus:
            assert len(S.args()) == 2
            T, U = S.args()
            v1 = self.element(a, T, context)
            if v1 == False:
                return False
            v2 = self.element(a, U, context)
            if v1 == True and v2 == False:
                return True
            if v1 == True and v2 == True:
                return False
        return None

    def _simple_Add(self, expr, head, args, context=None):
        if len(args) == 0:
            return Expr(0)
        if len(args) == 1:
            return args[0]
        if all(self.is_complex(arg, context) for arg in args):
            def iter_terms_coeffs(args, context=None):
                for arg in args:
                    if arg.is_integer():
                        yield Expr(1), int(arg)
                    elif arg.head() == Add:
                        for term, coeff in iter_terms_coeffs(arg.args(), context):
                            yield term, coeff
                    elif arg.head() == Sub:
                        args2 = arg.args()
                        assert len(args2) == 2
                        (term1, coeff1), (term2, coeff2) = iter_terms_coeffs(args2, context)
                        yield term1, coeff1
                        yield term2, -coeff2
                    elif arg.head() == Neg:
                        args2 = arg.args()
                        assert len(args2) == 1
                        (term, coeff), = iter_terms_coeffs(args2, context)
                        yield term, -coeff
                    elif arg.head() == Mul:
                        inert = []
                        coeff = 1
                        for (term2, coeff2) in iter_terms_coeffs(arg.args(), context):
                            if term2 != Expr(1):
                                inert.append(term2)
                            coeff *= coeff2
                        if len(inert) == 0:
                            inert = Expr(1)
                        elif len(inert) == 1:
                            inert = inert[0]
                        else:
                            inert = Mul(*inert)
                        yield inert, coeff
                    elif arg.head() == Div:
                        args2 = arg.args()
                        assert len(args2) == 2
                        (term1, coeff1), (term2, coeff2) = iter_terms_coeffs(args2, context)
                        if term1 == term2:
                            yield Expr(1), self._mpq(coeff1) / self._mpq(coeff2)
                        elif term2 == Expr(1):
                            yield term1, self._mpq(coeff1) / self._mpq(coeff2)
                        else:
                            yield Div(term1, term2), self._mpq(coeff1) / self._mpq(coeff2)
                    else:
                        yield arg, 1

            term_coeff = {}
            for term, coeff in iter_terms_coeffs(args, context):
                if term in term_coeff:
                    term_coeff[term] += coeff
                else:
                    term_coeff[term] = coeff

            term_coeff = term_coeff.items()
            term_coeff = [(term, coeff) for (term, coeff) in term_coeff if coeff != 0]

            if len(term_coeff) == 0:
                return Expr(0)

            #if 0:
            #    term_coeff = [(term, *self._mpq_numer_denom(coeff)) for (term, coeff) in term_coeff]

            def merge_term_coeff(term, coeff):
                if coeff == 1:
                    return term, 1
                if coeff == -1:
                    if term.head() == Neg:
                        assert len(term.args()) == 1
                        return term.args()[0], 1
                    return term, -1
                p, q = self._mpq_numer_denom(coeff)
                if term == Expr(1):
                    if p > 0:
                        coeff_expr = self._rational(p, q)
                        return coeff_expr, 1
                    else:
                        coeff_expr = self._rational(-p, q)
                        return coeff_expr, -1
                else:
                    if p > 0:
                        coeff_expr = self._rational(p, q)
                        return coeff_expr * term, 1
                    else:
                        coeff_expr = self._rational(-p, q)
                        return coeff_expr * term, -1

            if len(term_coeff) == 1:
                term, coeff = term_coeff[0]
                expr, sign = merge_term_coeff(term, coeff)
                if sign == 1:
                    return expr
                else:
                    return Neg(expr)

            term_sign = [merge_term_coeff(term, coeff) for (term, coeff) in term_coeff]

            positive = [term for (term, sign) in term_sign if sign == 1]
            negative = [term for (term, sign) in term_sign if sign == -1]

            # todo: logical sort order?
            positive = sorted(positive, key=str)
            negative = sorted(negative, key=str)

            if positive and not negative:
                return Add(*positive)

            if negative and not positive:
                return Neg(Add(*negative))

            if len(positive) == 1:
                positive = positive[0]
            else:
                positive = Add(*positive)

            if len(negative) == 1:
                negative = negative[0]
            else:
                negative = Add(*negative)

            return Sub(positive, negative)

            # from pygrim import *
            # Add(3*Pi, -4*Pi, 3*ConstE).simple()


        return expr

    def simple_arithmetic(self, expr, context=None):

        head = expr.head()
        args = expr.args()

        if head == Neg:
            assert len(args) == 1
            x = args[0]
            if x.is_integer():
                return Expr(-int(x))
            if x.head() == Neg:
                v = x.args()[0]
                if self.is_complex(v, context):
                    return v
            return expr

        if head == Pos:
            assert len(args) == 1
            return args[0]

        if head == Add:
            return self._simple_Add(expr, head, args, context)

        if head == Mul:
            if len(args) == 0:
                return Expr(1)
            if len(args) == 1:
                return args[0]
            if all(self.is_complex(arg, context) for arg in args):
                pass

        return expr

    def simple_set_logic(self, expr, context=None):
        # head = self.simple(expr.head(), context)
        head = expr.head()

        # todo: identify For-expression iteration, etc.
        # todo: for some operations (like And/Or, could terminate early)
        args = [self.simple(arg, context) for arg in expr.args()]

        if head == Not:
            assert len(args) == 1
            x = args[0]
            if x == True_:
                return False_
            if x == False_:
                return True_
            if x.head() == NotEqual and len(x.args()) == 2:
                return Equal(*x.args())
            if x.head() == Equal and len(x.args()) == 2:
                return NotEqual(*x.args())
            if x.head() == NotElement and len(x.args()) == 2:
                return Element(*x.args())
            if x.head() == Element and len(x.args()) == 2:
                return NotElement(*x.args())
            return expr

        if head == And:
            if False_ in args:
                return False_
            args = [arg for arg in args if arg != True_]
            if len(args) == 0:
                return True_
            if len(args) == 1:
                return args[0]
            return And(*args)

        if head == Or:
            if True_ in args:
                return True_
            args = [arg for arg in args if arg != False_]
            if len(args) == 0:
                return False_
            if len(args) == 1:
                return args[0]
            return Or(*args)

        if head == Implies:
            assert len(args) == 2
            P, Q = args
            if P == False_:
                return True_
            if P == True_:
                return Q
            return expr

        if head == Equal or (head == NotEqual and len(args) == 2):
            assert len(args) >= 2   # define Equal for len = 0, 1 ?
            # all equal
            if all(self.equal(args[0], arg, context) for arg in args[1:]):
                if head == Equal:
                    return True_
                else:
                    return False_
            # any not equal
            for i in range(len(args)):
                for j in range(i + 1, len(args)):
                    a = args[i]
                    b = args[j]
                    if self.equal(a, b, context) == False:
                        if head == Equal:
                            return False_
                        else:
                            return True_
            # todo: remove duplicates?
            return expr

        if head == Element or head == NotElement:
            assert len(args) == 2
            v = self.element(args[0], args[1], context)
            if v == True:
                if head == Element:
                    return True_
                else:
                    return False_
            if v == False:
                if head == Element:
                    return False_
                else:
                    return True_
            return expr

        return expr

    def simple(self, expr, context=None):
        """
        Simple formula simplification (todo):
        * Constant folding (at least for booleans, small integers & rationals)
        * Stripping non-semantic markup
        * Standardizations (Not(Equal(x, y)) -> NotEqual(x, y))
        * Eliminating duplicate terms
        * Expanding short constant-length iterations/comprehensions

        Others could be considered:
        * Collecting coefficients in arithmetic formulas (where permissible)
        * Evaluation of predicates using enclosures
        """

        if expr.is_atom():
            return expr

        head = expr.head()

        if head in set_logic_ops:
            return self.simple_set_logic(expr, context)

        if head in arithmetic_ops:
            return self.simple_arithmetic(expr, context)

        return expr


default_simplification = Simplification()

simple = default_simplification.simple


class TestSimplification(object):

    def __init__(self):
        pass

    def run(self):
        for method in dir(self):
            if method.startswith("test_"):
                print(method, "...", end=" ")
                getattr(self, method)()
                print("OK!")

    def test_equal(self):
        simp = Simplification()
        assert simp.equal(Pi, Pi) is True
        assert simp.equal(x, x) is True
        assert simp.equal(1+x, 1+x) is True
        assert simp.equal(1+x, x+1) is None
        assert simp.equal(Pi, Expr(2)) is False
        assert simp.equal(Expr(3), Expr(3)) is True
        assert simp.equal(Expr(3), Expr(-3)) is False
        assert simp.equal(Expr(3), Pi) is False
        assert simp.equal(Expr(3), ConstI) is False

    def test_element(self):
        simp = Simplification()
        assert simp.element(Expr(3), ZZ) is True
        assert simp.element(Expr(3) * Expr(-4) + Pow(5, 2) - Expr(1), ZZ) is True
        assert simp.element(Factorial(10**20), ZZ) is True
        assert simp.element(Pi, ZZ) is False
        assert simp.element(Div(3, 2), ZZ) in (False, None)
        assert simp.element(Pi, Set(Pi)) is True
        assert simp.element(Pi, Union(ZZ, Set(Pi))) is True
        assert simp.element(Pi, SetMinus(RR, QQ)) is True

    def test_is_positive(self):
        simp = Simplification()
        assert simp.is_positive(Expr(3)) is True
        assert simp.is_positive(Pi) is True
        assert simp.is_positive(1 + Sqrt(2)) is True
        assert simp.is_positive(Expr(-3)) is False
        assert simp.is_positive(Pi - 3) in (False, None)

    def test_simple(self):
        simp = Simplification()
        assert simp.simple(Element(Add(3, 5), ZZ)) == True_
        assert simp.simple(And(Not(False_), Or(True_, False_))) == True_

    def test_simple_arithmetic(self):
        simp = Simplification()
        assert simp.simple(Add(2, 3)) == Expr(5)
        assert simp.simple(Add(-1, 1)) == Expr(0)
        assert simp.simple(Add(0, 0, 0)) == Expr(0)
        assert simp.simple(Add(0, 0, 1)) == Expr(1)
        assert simp.simple(Add(-1, Pi, 1)) == Pi
        assert simp.simple(Add(3*Pi, 5*Pi/7, Pi/2, Pi/3, 2*Pi, -Div(191,42)*Pi)) == Mul(2, Pi)


