from .expr import *

class EvaluationContext(object):
    pass

class Simplification(object):

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
        if x in (Pi, ConstGamma, ConstE, ConstCatalan):
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
        if x in (Pi, ConstGamma, ConstE, ConstCatalan):
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
        if x in (Pi, ConstGamma, ConstI, ConstE, ConstCatalan):
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

        head = self.simple(expr.head(), context)

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

        if head == Pos:
            assert len(args) == 1
            return args[0]

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

        """
        # note: need to be aware of associativity, commutativity...

        if head == Add:
            term_coeff = {}
            for arg in args:
                term, coeff = as_term_coeff(arg)
                if term in term_coeff:
                    term_coeff[term] += coeff
                else:
                    term_coeff[term] = coeff
        if head == Mul:
            base_exp = {}
            for arg in args:
                base, exp = as_base_exp(arg)
                if base in base_exp:
                    base_exp[base] += exp
                else:
                    base_exp[base] = exp
            base_exp = [(base, simple(exp)) for (base, exp) in base_exp]
            base_exp = [(base, exp) for (base, exp) in base_exp if exp != 0]
            if len(base_exp) == 0:
                return Expr(1)
            if len(base_exp) == 1:
                pass
        """
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

