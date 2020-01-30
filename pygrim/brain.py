from .expr import *

from itertools import chain, zip_longest
import itertools

def interleave_longest(*iterables):
    o = object()
    i = chain.from_iterable(zip_longest(*iterables, fillvalue=o))
    return [x for x in i if x is not o]

some_nonnumbers = [Undefined, True_, False_, Infinity, -Infinity, Infinity*ConstI, -ConstI*Infinity,
    UnsignedInfinity, Undefined, Tuple(), Tuple(Tuple()), Tuple(0), Tuple(0, 0), Tuple(0, 1), Tuple(1, 2, 3),
    Set(), Set(Set()), Set(0), Set(0, 1), Set(-1, 0, 1), ZZ, RR, QQ, CC,
    Matrix2x2(1, 0, 0, 1)]

some_primes = [2,3,5,7,11,13,17,19,101,1009,10007]

some_integers = [Expr(_n) for _n in [0,1,-1,2,-2,3,-3,4,-4,5,-5,6,-6,7,8,9,
    10,11,12,24,30,32,40,41,42,60,64,100,120,127,128,255,256,257,720,
    1000,1729,10**4,10**5,10**6,10**9,10**12,10**15,10**30]]

some_fractions = [Div(1,2),-Div(1,2),Div(3,2),-Div(3,2),Div(5,2),Div(7,2),Div(1,3),Div(2,3),Div(4,3),Div(1,4),Div(3,4),Div(5,4),Div(1,5),Div(1,6),Div(1,24)]

some_algebraic_irrationals = [Sqrt(2), -Sqrt(2), Sqrt(2)/2, -Sqrt(2)/2, GoldenRatio, 1/GoldenRatio, Sqrt(2)+1, Sqrt(2)-1]

some_transcendentals = [Pi, 2*Pi, Pi/2, 3*Pi/2, -Pi, -Pi/2, 2*Pi/3, -2*Pi/3, Pi/4, -Pi/4, 3*Pi/4, -3*Pi/4, Pi/6, 5*Pi/6, Log(2), Log(3), ConstE]

some_complex_algebraics = [ConstI, -ConstI, 2*ConstI, -2*ConstI, ConstI/2, -ConstI/2,
    1+ConstI, 1-ConstI, -1+ConstI, -1-ConstI,
    2+ConstI, 2-ConstI, -2+ConstI, -2-ConstI,
    1+2*ConstI, 1-2*ConstI, -1+2*ConstI, -1-2*ConstI,
    Div(1,2)+ConstI, Div(1,2)-ConstI, Div(3,2)+ConstI,
    (1+ConstI)/2, (1-ConstI)/2, (-1+ConstI)/2, (-1-ConstI)/2,
    Exp(Pi*ConstI/3), Exp(2*Pi*ConstI/3), Exp(Pi*ConstI/6), Exp(5*Pi*ConstI/6),
    Exp(Pi*ConstI/4), Exp(-Pi*ConstI/4), Exp(3*Pi*ConstI/4), Exp(-3*Pi*ConstI/4)]

some_complex_transcendentals = [Pi*ConstI, 2*Pi*ConstI, -Pi*ConstI, Div(1,2)+Pi*ConstI, Div(1,2)-Pi*ConstI, Pi+ConstE*ConstI]

some_rationals = interleave_longest(some_integers, some_fractions)
some_algebraics = interleave_longest(some_integers, some_fractions, some_algebraic_irrationals, some_complex_algebraics)
some_reals = interleave_longest(some_integers, some_fractions, some_algebraic_irrationals, some_transcendentals)
some_extended_reals = interleave_longest(some_integers, some_fractions, some_algebraic_irrationals, some_transcendentals, [Infinity, -Infinity])
some_complexes = interleave_longest(some_integers, some_fractions, some_algebraic_irrationals, some_complex_algebraics, some_transcendentals, some_complex_transcendentals)
some_everything = interleave_longest(some_nonnumbers, some_complexes)

some_upper_half_plane = [ConstI, 2*ConstI, ConstI/2, 1+ConstI, 1+2*ConstI, 1+ConstI/2, -1+ConstI, -1+2*ConstI, -1+ConstI/2, 2+ConstI, 3+ConstI,
    Div(1,2)+ConstI, Div(1,2)+2*ConstI, Div(1,2)+ConstI/2, Div(1,3)+ConstI, Div(1,3)+2*ConstI, Div(1,3)+ConstI/2, Sqrt(2)+Pi*I, -Sqrt(2)+I/Pi]

def And_terms(expr):
    if expr.head() == And:
        for x in expr.args():
            for t in And_terms(x):
                yield t
    else:
        yield expr

# todo: design a real algorithm
def custom_cartesian(*lists):
    if len(lists) == 1:
        for v in lists[0]:
            yield (v,)
    elif len(lists) == 2:
        N = 0
        A = len(lists[0])
        B = len(lists[1])
        for N in range(max(A,B)):
            for i in range(N+1):
                a = i
                b = N - i
                if 0 <= a < A and 0 <= b < B:
                    yield lists[0][a], lists[1][b]
    elif len(lists) == 3:
        N = 0
        A = len(lists[0])
        B = len(lists[1])
        C = len(lists[2])
        for N in range(max(A,B,C)):
            for i in range(N+1):
                for j in range(N+1):
                    a = i
                    b = N - i
                    c = N - i - j
                    if 0 <= a < A and 0 <= b < B and 0 <= c < C:
                        yield lists[0][a], lists[1][b], lists[2][c]
    elif len(lists) == 4:
        N = 0
        A = len(lists[0])
        B = len(lists[1])
        C = len(lists[2])
        D = len(lists[3])
        for N in range(max(A,B,C,D)):
            for i in range(N+1):
                for j in range(N+1):
                    for k in range(N+1):
                        a = i
                        b = N - i
                        c = N - i - j
                        d = N - i - j - k
                        if 0 <= a < A and 0 <= b < B and 0 <= c < C and 0 <= d < D:
                            yield lists[0][a], lists[1][b], lists[2][c], lists[3][d]
    else:
        for v in itertools.product(*lists):
            yield v

additive_ops = set([Pos, Neg, Add, Sub])
ring_arithmetic_ops = set([Pos, Neg, Add, Sub, Mul])
field_arithmetic_ops = set([Pos, Neg, Add, Sub, Mul, Div])
arithmetic_ops = set([Pos, Neg, Add, Sub, Mul, Div, Sqrt, Pow])
number_part_ops = set([Sign, Abs, Re, Im, Conjugate, Floor, Ceil])

positive_real_constants = set([Pi, ConstE, ConstGamma, ConstCatalan, GoldenRatio])
irrational_constants = set([Pi, ConstE, GoldenRatio])
complex_constants = positive_real_constants.union(set([ConstI]))

set_logic_ops = set([Not, And, Or, Implies, Equal, NotEqual, Element, NotElement, Less, LessEqual, Greater, GreaterEqual])

def infer_not_domain(inferences, x, dom):
    if dom.head() == Union:
        for dom2 in dom.head_args_flattened(Union):
            infer_not_domain(inferences, x, dom2)
        return
    def add(x, dom):
         inferences.add(NotElement(x, dom))
    add(x, dom)
    # singleton set
    if dom.head() == Set and len(dom.args()) == 1:
        inferences.add(NotEqual(x, dom.args()[0]))
    if dom == CC:
        add(x, RR)
        add(x, QQ)
        add(x, ZZ)
        add(x, PP)
        add(x, HH)
        add(x, AlgebraicNumbers)
    elif dom == RR:
        add(x, QQ)
        add(x, ZZ)
        add(x, PP)
    elif dom == QQ:
        add(x, ZZ)
        add(x, PP)
    elif dom == ZZ:
        add(x, PP)
    elif dom == AlgebraicNumbers:
        add(x, QQ)
        add(x, ZZ)

def infer_domain(inferences, x, dom):
    if dom.head() == Intersection:
        for dom2 in dom.head_args_flattened(Intersection):
            infer_domain(inferences, x, dom2)
        return
    def add(x, dom):
         inferences.add(Element(x, dom))
    add(x, dom)
    # singleton set
    if dom.head() == Set and len(dom.args()) == 1:
        inferences.add(Equal(x, dom.args()[0]))
    if dom == RR:
        add(x, CC)
    elif dom == QQ:
        add(x, RR)
        add(x, CC)
        add(x, AlgebraicNumbers)
    elif dom == ZZ:
        add(x, QQ)
        add(x, RR)
        add(x, CC)
        add(x, AlgebraicNumbers)
    elif dom == HH:
        add(x, CC)
    elif dom == PP:
        add(x, ZZGreaterEqual(2))
        add(x, ClosedOpenInterval(2, Infinity))
        add(x, ZZ)
        add(x, QQ)
        add(x, RR)
        add(x, CC)
        add(x, AlgebraicNumbers)
    elif dom == AlgebraicNumbers:
        add(x, CC)
    elif dom.head() in (ZZGreaterEqual, ZZLessEqual, Range):
        add(x, ZZ)
        add(x, QQ)
        add(x, RR)
        add(x, CC)
        add(x, AlgebraicNumbers)
    elif dom.head() == OpenInterval:
        add(x, RR)
        add(x, CC)
        a, b = dom.args()
        inferences.add(Less(a, x))
        inferences.add(Less(x, b))
        inferences.add(Greater(x, a))
        inferences.add(Greater(b, x))
        for v in (-1, 0, 1):
            if GreaterEqual(a, v).simple() == True_:
                inferences.add(Greater(x, v))
                inferences.add(Less(v, x))
            if LessEqual(b, v).simple() == True_:
                inferences.add(Less(x, v))
                inferences.add(Greater(v, x))
    elif dom.head() == ClosedInterval:
        a, b = dom.args()
        inferences.add(LessEqual(a, x))
        inferences.add(LessEqual(x, b))
        inferences.add(GreaterEqual(x, a))
        inferences.add(GreaterEqual(b, x))
        # todo: simplify based on other assumptions?
        if Element(a, RR).simple() == True_ and Element(b, RR).simple() == True_:
            add(x, RR)
            add(x, CC)
        for v in (-1, 0, 1):
            if GreaterEqual(a, v).simple() == True_:
                inferences.add(GreaterEqual(x, v))
                inferences.add(LessEqual(v, x))
            if LessEqual(b, v).simple() == True_:
                inferences.add(LessEqual(x, v))
                inferences.add(GreaterEqual(v, x))
    elif dom.head() == OpenClosedInterval:
        a, b = dom.args()
        inferences.add(Less(a, x))
        inferences.add(LessEqual(x, b))
        inferences.add(Greater(x, a))
        inferences.add(GreaterEqual(b, x))
        if Element(b, RR).simple() == True_:
            add(x, RR)
            add(x, CC)
        for v in (-1, 0, 1):
            if GreaterEqual(a, v).simple() == True_:
                inferences.add(Greater(x, v))
                inferences.add(Less(v, x))
            if LessEqual(b, v).simple() == True_:
                inferences.add(LessEqual(x, v))
                inferences.add(GreaterEqual(v, x))
    elif dom.head() == ClosedOpenInterval:
        a, b = dom.args()
        inferences.add(LessEqual(a, x))
        inferences.add(Less(x, b))
        inferences.add(GreaterEqual(x, a))
        inferences.add(Greater(b, x))
        if Element(a, RR).simple() == True_:
            add(x, RR)
            add(x, CC)
        for v in (-1, 0, 1):
            if GreaterEqual(a, v).simple() == True_:
                inferences.add(GreaterEqual(x, v))
                inferences.add(LessEqual(v, x))
            if LessEqual(b, v).simple() == True_:
                inferences.add(Less(x, v))
                inferences.add(Greater(v, x))


class Brain(object):
    """
    A "brain" for performing symbolic computation.
    """

    def infer(self, thm):
        self.inferences.add(thm)
        if thm.head() == Element:
            x, dom = thm.args()
            infer_domain(self.inferences, x, dom)
            if dom.head() == SetMinus:
                inset, outset = dom.args()
                infer_domain(self.inferences, x, inset)
                infer_not_domain(self.inferences, x, outset)

    def __init__(self, variables=(), assumptions=None, fungrim=False, penalty={}):
        """
        Input: a list of symbols representing free variables and
        assumptions involving the free variables, which may be used
        in symbolic simplification.

        >>> Brain(variables=[a,b,c],
                assumptions=And(Element(a, CC), Element(b, ZZ),
                    Element(c, QQ), NotEqual(a, 1)))

        """
        self.simple_cache = {}
        self.penalty = penalty

        # Init computational types
        from flint import arb, acb, fmpz, fmpq, ctx
        self._arb = arb
        self._acb = acb
        self._fmpz = fmpz
        self._fmpq = fmpq
        self._flint_ctx = ctx

        # Init assumptions
        self.variables = frozenset(variables)
        self.inferences = set()
        if assumptions is None:
            self.assumptions = frozenset()
        else:
            self.assumptions = frozenset(assumptions.head_args_flattened(And))
        # Simple inferences (mostly based on the domain)
        for asm in self.assumptions:
            # asm = asm.simple()
            self.infer(asm)

        # Init Fungrim patterns
        self.expr_db = {}
        self.match_db = {}
        if fungrim:
            from . import formulas
            from .expr import all_entries
            for entry in all_entries:
                formula = entry.get_arg_with_head(Formula)
                if formula is None:
                    continue

                variables = entry.get_arg_with_head(Variables)

                # Constant expression
                if variables is None:
                    content = formula.args()[0]
                    self.infer(content)
                    # self.expr_db[content] = True_
                    if content.head() == Equal:
                        args = content.args()
                        best = args[0]
                        cost = self.complexity(best)
                        for arg in args[1:]:
                            cost2 = self.complexity(arg)
                            if cost2 < cost:
                                best = arg
                                cost = cost2
                        for arg in args:
                            if arg != best:
                                self.expr_db[arg] = best
                # Nonconstant expression for matching
                else:
                    content = formula.args()[0]
                    if content.head() == Equal and len(content.args()) == 2:
                        eid = entry.id()
                        lhs_head = content.args()[0].head()
                        if lhs_head in self.match_db:
                            self.match_db[lhs_head].add(eid)
                        else:
                            self.match_db[lhs_head] = set([eid])


    def __repr__(self):
        s = ""
        s += "Variables: " + str(self.variables) + "\n"
        s += "Inferences: (%i)" % len(self.inferences) + "\n"
        for thm in self.inferences:
            s += "  " + str(thm) + "\n"
        return s

    def real_enclosure(self, x):
        """
        Performs numerical evaluation and returns an enclosure of x as an arb.
        Success proves that x is a real number.
        Returns None on failure.
        """
        try:
            val = x.n(as_arb=True)
            if type(val) == self._arb:
                return val
        except (NotImplementedError, ValueError, ImportError):
            pass
        return None

    def complex_enclosure(self, x):
        """
        Performs numerical evaluation and returns an enclosure of x as an acb.
        Success proves that x is a complex number.
        Returns None on failure.
        """
        try:
            val = x.n(as_arb=True)
            assert val.is_finite()
            if type(val) == self._acb:
                return val
            if type(val) == self._arb:
                return self._acb(val)
        except (NotImplementedError, ValueError, ImportError):
            pass
        return None

    def simple(self, expr):
        """
        Given a symbolic expression expr, return an equivalent expression,
        hopefully simplified.
        """
        if expr in self.inferences:
            return True_

        if expr.is_atom():
            return expr

        if expr in self.simple_cache:
            v = self.simple_cache[expr]
            if v is None:
                return expr
            return v

        input_expr = expr
        self.simple_cache[input_expr] = None


        def fungrim_simplify(expr):
            if expr in self.expr_db:
                return self.expr_db[expr]
            if expr.is_atom():
                return expr

            head = expr.head()
            expr = head(*(self.simple(arg) for arg in expr.args()))
            if head in self.match_db:
                exprs = set((self.rewrite_fungrim(expr, id, recursive=False), id) for id in self.match_db[head])
                #for e in exprs:
                #    print(e, self.complexity(e[0]))
                expr2, id = min(exprs, key=lambda v: self.complexity(v[0]))
                if expr2 != expr and self.complexity(expr2) < self.complexity(expr):
                    expr = self.simple(expr2)
            return expr

        if self.expr_db:
            expr = fungrim_simplify(expr)

        head = expr.head()
        if head is not None and head.is_symbol():
            s = head._symbol
            f = "simple_" + s
            if hasattr(self, f):
                args = expr.args()
                expr2 = getattr(self, f)(*args)
                if self.expr_db and expr2 != expr:
                    expr2 = fungrim_simplify(expr2)
                expr = expr2

        self.simple_cache[input_expr] = expr

        return expr

    def is_zero(self, x):
        """
        Check if x is the number zero.
        Return True, False, or None for unknown.
        """
        if x.is_integer():
            return int(x) == 0
        if Equal(x, 0) in self.inferences:
            return True
        if NotEqual(x, 0) in self.inferences:
            return False
        if Greater(x, 0) in self.inferences:
            return False
        if Less(x, 0) in self.inferences:
            return False
        if self.is_integer(x) == False:
            return False
        if self.is_positive(x):
            return False
        val = self.complex_enclosure(x)
        if val is not None and val != 0:
            return False
        if self.is_infinity(x):
            return False
        # todo: try normal form here?
        return None

    def is_not_zero(self, x):
        """
        Check if x is not the number zero.
        Return True, False, or None for unknown.
        """
        v = self.is_zero(x)
        if v is None:
            return v
        return not v

    def is_infinity(self, x):
        """
        Checks if x is an infinity (UnsignedInfinity or c*Infinity for some
        nonzero complex number c). Returns True, False, or None for unknown.
        """
        if x == Infinity:
            return True
        if x == UnsignedInfinity:
            return True
        if x == Undefined:
            return False
        if Element(x, CC) in self.inferences:
            return False
        if x.head() in (Pos, Neg):
            arg, = x.args()
            if self.is_infinity(arg):
                return True
        if x.head() == Mul:
            args = x.args()
            if any(self.is_infinity(arg) for arg in args):
                if all(self.is_infinity(arg) or (self.is_complex(arg) and self.is_not_zero(arg)) for arg in x.args()):
                    return True
        val = self.complex_enclosure(x)
        if val is not None:
            return False
        return None

    def is_nonnegative(self, x):
        """
        Check if x is an object satisfying x >= 0.
        Return True, False, or None for unknown.
        """
        if x.is_integer():
            return int(x) >= 0
        if x in positive_real_constants:
            return True
        if GreaterEqual(x, 0) in self.inferences:
            return True
        if Greater(x, 0) in self.inferences:
            return True
        if Less(x, 0) in self.inferences:
            return False
        if self.is_real(x):
            if x.head() in (Pos, Add, Mul, Exp, Sqrt):
                if all(self.is_nonnegative(arg) for arg in x.args()):
                    return True
            if x.head() == Div:
                p, q = x.args()
                if self.is_nonnegative(p) and self.is_positive(q):
                    return True
            if x.head() == Pow:
                base, exp = x.args()
                if self.is_positive(base):
                    return True
        val = self.complex_enclosure(x)
        if val is not None:
            real, imag = val.real, val.imag
            if imag == 0 and real >= 0:
                return True
            if imag != 0 or real < 0:
                return False
        return None

    def is_positive(self, x):
        """
        Check if x is an object satisfying x > 0.
        Returns True, False, or None for unknown.
        """
        if x.is_integer():
            return int(x) > 0
        if x in positive_real_constants:
            return True
        if Greater(x, 0) in self.inferences:
            return True
        if LessEqual(x, 0) in self.inferences:
            return False
        if Less(x, 0) in self.inferences:
            return False
        if self.is_real(x):
            if x.head() in (Exp, Cosh):
                t, = x.args()
                if self.is_real(t):
                    return True
            if x.head() in (Pos, Add, Mul, Sqrt):
                if all(self.is_positive(arg) for arg in x.args()):
                    return True
            if x.head() == Div:
                p, q = x.args()
                if self.is_positive(p) and self.is_positive(q):
                    return True
            if x.head() == Pow:
                base, exp = x.args()
                if self.is_positive(base):
                    return True
        val = self.complex_enclosure(x)
        if val is not None:
            real, imag = val.real, val.imag
            if imag == 0 and real > 0:
                return True
            if imag != 0 or real <= 0:
                return False
        return None

    def is_negative(self, x):
        """
        Check if x is an object satisfying x < 0.
        Returns True, False, or None for unknown.
        """
        if x.is_integer():
            return int(x) < 0
        if x in positive_real_constants:
            return False
        if Less(x, 0) in self.inferences:
            return True
        if GreaterEqual(x, 0) in self.inferences:
            return False
        if Greater(x, 0) in self.inferences:
            return False
        val = self.complex_enclosure(x)
        if val is not None:
            real, imag = val.real, val.imag
            if imag == 0 and real < 0:
                return True
            if imag != 0 or real >= 0:
                return False
        return None

    def is_nonpositive(self, x):
        """
        Check if x is an object satisfying x <= 0.
        Returns True, False, or None for unknown.
        """
        if x.is_integer():
            return int(x) <= 0
        if x in positive_real_constants:
            return False
        if LessEqual(x, 0) in self.inferences:
            return True
        if Less(x, 0) in self.inferences:
            return True
        if Greater(x, 0) in self.inferences:
            return False
        val = self.complex_enclosure(x)
        if val is not None:
            real, imag = val.real, val.imag
            if imag == 0 and real <= 0:
                return True
            if imag != 0 or real > 0:
                return False
        return None

    def is_integer(self, x):
        """
        Checks if x is an integer. Returns True, False, or None for unknown.
        """
        if x.is_integer():
            return True
        if Element(x, ZZ) in self.inferences:
            return True
        if NotElement(x, ZZ) in self.inferences:
            return False
        if x.head() in (Pos, Neg, Add, Sub, Mul):
            if all(self.is_integer(arg) for arg in x.args()):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            if self.is_integer(base) and self.is_integer(exp) and self.is_nonnegative(exp):
                return True
        if x.head() == Factorial:
            n, = x.args()
            if self.is_integer(n) and self.is_nonnegative(n):
                return True
        if x in complex_constants:
            return False
        val = self.complex_enclosure(x)
        if val is not None:
            # todo: with increased precision when needed
            if not val.contains_integer():
                return False
        if self.is_infinity(x) or x == Undefined:
            return False
        return None

    # todo: irrational + rational, irrational * rational, irrational / rational, rational / irrational
    # todo: square roots
    # todo: exp, log, sin, cos, tan of rational numbers
    def is_rational(self, x):
        """
        Check if x is a rational number.
        Returns True, False, or None for unknown.
        """
        if self.is_integer(x):
            return True
        if Element(x, QQ) in self.inferences:
            return True
        if NotElement(x, QQ) in self.inferences:
            return False
        if x == Pi or x == ConstE:
            return False
        if x.head() in (Pos, Neg, Add, Sub, Mul):
            if all(self.is_rational(arg) for arg in x.args()):
                return True
        if x.head() == Div:
            p, q = x.args()
            if self.is_rational(p) and self.is_rational(q) and self.is_not_zero(q):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            if self.is_rational(base) and self.is_integer(exp) and (self.is_not_zero(base) or self.is_nonnegative(exp)):
                return True
        if x.head() == Sqrt:
            # todo: implement an algorithm
            v, = x.args()
            if v.is_integer():
                v = int(v)
                if v < 0:
                    return False
                if v <= 100:
                    return v in [0,1,4,9,16,25,36,49,64,81,100]
        if self.is_infinity(x) or x == Undefined:
            return False
        return None

    def is_algebraic(self, x):
        """
        Check if x is an algebraic number.
        Returns True, False, or None for unknown.
        """
        if self.is_integer(x):
            return True
        if Element(x, AlgebraicNumbers) in self.inferences:
            return True
        if NotElement(x, AlgebraicNumbers) in self.inferences:
            return False
        if x == Pi or x == ConstE:
            return False
        if x == ConstI or x == GoldenRatio:
            return True
        if x.head() in (Pos, Neg, Add, Sub, Mul):
            if all(self.is_algebraic(arg) for arg in x.args()):
                return True
        if x.head() == Div:
            p, q = x.args()
            if self.is_algebraic(p) and self.is_algebraic(q) and self.is_not_zero(q):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            if self.is_algebraic(base):
                if self.is_rational(exp) and (self.is_not_zero(base) or self.is_nonnegative(exp)):
                    return True
                # Gelfond-Schneider
                if self.is_algebraic(exp) and self.is_rational(exp) == False and self.is_not_zero(base) and self.equal(base, Expr(1)) == False:
                    return False
            # transcendental ^ rational
            if self.is_complex(base) and (self.is_algebraic(base) == False) and self.is_rational(exp) and self.is_not_zero(exp):
                return False
        if x.head() == Sqrt:
            v, = x.args()
            return self.is_algebraic(v)
        if x.head() == Exp:
            v, = x.args()
            if self.is_algebraic(v) and self.is_not_zero(v):
                return False
            if self.is_rational(self.simple(v / (Pi * ConstI))):
                return True
        if x.head() in (Sin, Cos, Tan, Cot, Csc, Sec):
            v, = x.args()
            if self.is_algebraic(v) and self.is_not_zero(v):
                return False
            # todo: exp(pi i * p/q) is algebraic
        if x.head() == Log:
            v, = x.args()
            if self.is_algebraic(v) and (self.equal(v, Expr(1)) == False):
                return False
        if self.is_infinity(x) or x == Undefined:
            return False
        return None

    def is_real(self, x):
        """
        Check if x is a real number.
        Return True, False, or None for unknown.
        """
        if self.is_rational(x):  # todo: remove this?
            return True
        if Element(x, RR) in self.inferences:
            return True
        if NotElement(x, RR) in self.inferences:
            return False
        if x in (Pi, ConstGamma, ConstE, ConstCatalan):
            return True
        if x == ConstI:
            return False
        if x.head() in (Pos, Neg, Add, Sub, Mul, Exp, Sin, Cos):
            if all(self.is_real(arg) for arg in x.args()):
                return True
        if x.head() == Div:
            p, q = x.args()
            if self.is_real(p) and self.is_real(q) and self.is_not_zero(q):
                return True
        if x.head() == Sqrt:
            arg, = x.args()
            if self.is_real(arg) and self.is_nonnegative(arg):
                return True
        if x.head() == Log:
            arg, = x.args()
            if self.is_real(arg) and self.is_positive(arg):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            if self.is_real(base) and self.is_real(exp):
                if self.is_positive(base) and self.is_positive(exp):
                    return True
                if self.is_not_zero(base) and self.is_integer(exp):
                    return True
                if self.is_integer(exp) and self.is_nonnegative(exp):
                    return True
        v = self.complex_enclosure(x)
        if v is not None:
            if v.imag == 0:
                return True
            if v.imag != 0:
                return False
        if self.is_infinity(x) or x == Undefined:
            return False
        return None

    def is_complex(self, x):
        """
        Check if x is a complex number.
        Return True, False, or None for unknown.
        """
        if self.is_real(x):  # todo: remove this?
            return True
        if x == ConstI:
            return True
        if Element(x, CC) in self.inferences:
            return True
        if NotElement(x, CC) in self.inferences:
            return False
        if x.head() in (Pos, Neg, Add, Sub, Mul, Sqrt, Exp, Sin, Cos):
            if all(self.is_complex(arg) for arg in x.args()):
                return True
        if x.head() == Div:
            p, q = x.args()
            if self.is_complex(p) and self.is_complex(q) and self.is_not_zero(q):
                return True
        if x.head() == Pow:
            base, exp = x.args()
            # todo: more generally for re(exp) > 0
            if self.is_complex(base) and self.is_complex(exp) and \
                (self.is_not_zero(base) or (self.is_real(exp) and self.is_positive(exp))):
                return True
        if x.head() == Log:
            arg, = x.args()
            if self.is_complex(arg) and self.is_not_zero(arg):
                return True
        if self.is_infinity(x) or x == Undefined:
            return False
        return None

    # todo: identify different types; bools, tuples, sets, matrices, ...
    def equal(self, a, b):
        """
        Check if a and b are equal (represent exactly the same mathematical
        object). Returns True, False, or None for unknown.
        """
        assert isinstance(a, Expr)
        assert isinstance(b, Expr)
        if a == b:
            return True
        if a.is_integer() and b.is_integer():
            return False

        if Equal(a, b) in self.inferences:
            return True
        if Equal(b, a) in self.inferences:
            return True
        if NotEqual(a, b) in self.inferences:
            return False
        if NotEqual(b, a) in self.inferences:
            return False

        # try numerical exclusion test
        val1 = self.complex_enclosure(a)
        if val1 is not None:
            val2 = self.complex_enclosure(b)
            if val2 is not None:
                if not val1.overlaps(val2):
                    return False

        # try domain exclusions
        aq = self.is_rational(a)
        bq = self.is_rational(b)
        if aq is not None and bq is not None and aq != bq:
            return False
        if aq and bq:
            aq = self.is_integer(a)
            bq = self.is_integer(b)
            if aq is not None and bq is not None and aq != bq:
                return False

        aq = self.is_complex(a)
        bq = self.is_complex(b)
        if aq is not None and bq is not None and aq != bq:
            return False
        if aq and bq:
            aq = self.is_real(a)
            bq = self.is_real(b)
            if aq is not None and bq is not None and aq != bq:
                return False

        aq = self.is_infinity(a)
        bq = self.is_infinity(b)
        if aq is not None and bq is not None and aq != bq:
            return False
        return None

    def greater(self, a, b):
        v = self.simple(Greater(a, b))
        if v == True_:
            return True
        if v == False_:
            return False
        return None

    def less(self, a, b):
        v = self.simple(Less(a, b))
        if v == True_:
            return True
        if v == False_:
            return False
        return None

    def greater_equal(self, a, b):
        v = self.simple(GreaterEqual(a, b))
        if v == True_:
            return True
        if v == False_:
            return False
        return None

    def less_equal(self, a, b):
        v = self.simple(LessEqual(a, b))
        if v == True_:
            return True
        if v == False_:
            return False
        return None

    def is_extended_real(self, x):
        if x == Infinity:
            return True
        if x == -Infinity:
            return True
        v = self.is_real(x)
        if v:
            return True
        if v is False and self.is_complex(x):
            return False
        return None

    def element(self, x, S):
        """
        Check if x is an element of S.
        Returns True, False, or None for unknown.
        """
        assert isinstance(x, Expr)
        if Element(x, S) in self.inferences:
            return True
        if NotElement(x, S) in self.inferences:
            return False
        if S == CC:
            return self.is_complex(x)
        if S == RR:
            return self.is_real(x)
        if S == QQ:
            return self.is_rational(x)
        if S == ZZ:
            return self.is_integer(x)
        if S == HH:
            c1 = self.is_complex(x)
            if not c1:
                return c1
            return self.is_positive(Im(x))
        if S == PP:
            z = self.is_integer(x)
            if not z:
                return z
            if x.is_integer() and int(x) <= 20:
                return int(x) in [2,3,5,7,11,13,17,19]
            return None
        if S == AlgebraicNumbers:
            return self.is_algebraic(x)
        head = S.head()
        if head == ZZGreaterEqual:
            a, = S.args()
            v = self.is_integer(x)
            if not v:
                return v
            return self.less_equal(a, x)
        if head == ZZLessEqual:
            b, = S.args()
            v = self.is_integer(x)
            if not v:
                return v
            return self.less_equal(x, b)
        if head == Range:
            a, b = S.args()
            v = self.is_integer(x)
            if not v:
                return v
            v = self.less_equal(a, x)
            if not v:
                return v
            return self.less_equal(x, b)
        if head in (ClosedInterval, OpenInterval, ClosedOpenInterval, OpenClosedInterval):
            a, b = S.args()
            v = self.is_extended_real(a)
            if not v:
                return None
            v = self.is_extended_real(b)
            if not v:
                return None
            v = self.is_extended_real(x)
            if not v:
                return v
            if head != ClosedInterval and a == b:
                return False
            if head == ClosedInterval or head == ClosedOpenInterval:
                v = self.less_equal(a, x)
                if not v:
                    return v
            else:
                v = self.less(a, x)
                if not v:
                    return v
            if head == ClosedInterval or head == OpenClosedInterval:
                v = self.less_equal(x, b)
                return v
            else:
                v = self.less(x, b)
                return v
        # todo: check for comprehensions
        if head == Set:
            check = [self.equal(x, y) for y in S.args()]
            if True in check:
                return True
            if all(c == False for c in check):
                return False
            return None
        # todo: check for comprehensions
        if head == Union:
            if len(S.args()) == 0:
                return False
            check = [self.element(x, T) for T in S.args()]
            if True in check:
                return True
            if all(c == False for c in check):
                return False
            return None
        # todo: check for comprehensions
        if head == Intersection:
            assert len(S.args()) >= 1
            check = [self.element(x, T) for T in S.args()]
            if all(c == True for c in check):
                return True
            if False in check:
                return False
            return None
        if head == SetMinus:
            assert len(S.args()) == 2
            T, U = S.args()
            v1 = self.element(x, T)
            if v1 == False:
                return False
            v2 = self.element(x, U)
            if v1 == True and v2 == False:
                return True
            if v1 == True and v2 == True:
                return False
            return None
        return None

    def simple_Not(self, x):
        """
        Return an expression equivalent to Not(x), simplified if possible.
        """
        x = self.simple(x)
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
        return Not(x)

    def simple_And(self, *args):
        # todo: identify For-expression iteration, etc.
        # todo: early termination
        # todo: postponed simplifications
        args = [self.simple(arg) for arg in args]
        if False_ in args:
            return False_
        args = [arg for arg in args if arg != True_]
        if len(args) == 0:
            return True_
        if len(args) == 1:
            return args[0]
        return And(*args)

    def simple_Or(self, *args):
        # todo: identify For-expression iteration, etc.
        # todo: early termination
        # todo: postponed simplifications
        args = [self.simple(arg) for arg in args]
        if True_ in args:
            return True_
        args = [arg for arg in args if arg != False_]
        if len(args) == 0:
            return False_
        if len(args) == 1:
            return args[0]
        return Or(*args)

    def simple_Implies(self, *args):
        args = [self.simple(arg) for arg in args]
        assert len(args) == 2
        P, Q = args
        if P == False_:
            return True_
        if P == True_:
            return Q
        return Implies(*args)

    def simple_Equal(self, *args):
        args = [self.simple(arg) for arg in args]
        assert len(args) >= 2   # define Equal for len = 0, 1 ?
        # all equal
        if all(self.equal(args[0], arg) for arg in args[1:]):
            return True_
        # any not equal
        for i in range(len(args)):
            for j in range(i + 1, len(args)):
                a = args[i]
                b = args[j]
                if self.equal(a, b) == False:
                    return False_
        # todo: remove duplicates?
        return Equal(*args)

    def simple_NotEqual(self, *args):
        args = [self.simple(arg) for arg in args]
        if len(args) != 2:
            return NotEqual(*args) # XXX
        # all equal
        if all(self.equal(args[0], arg) for arg in args[1:]):
            return False_
        # any not equal
        for i in range(len(args)):
            for j in range(i + 1, len(args)):
                a = args[i]
                b = args[j]
                if self.equal(a, b) == False:
                    return True_
        # todo: remove duplicates?
        return NotEqual(*args)

    def simple_Element(self, *args):
        args = [self.simple(arg) for arg in args]
        head = Element
        assert len(args) == 2
        v = self.element(args[0], args[1])
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
        return Element(*args)

    def simple_NotElement(self, *args):
        args = [self.simple(arg) for arg in args]
        head = NotElement
        assert len(args) == 2
        v = self.element(args[0], args[1])
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
        return NotElement(*args)

    def simple_LessEqual(self, *args):
        args = [self.simple(arg) for arg in args]
        if len(args) == 2:
            a, b = args
            if a.is_integer() and b.is_integer():
                if int(a) <= int(b):
                    return True_
                else:
                    return False_
            if self.is_real(a) and self.is_real(b):
                v = self.real_enclosure(a - b)
                if v is not None:
                    if v <= 0:
                        return True_
                    if v > 0:
                        return False_
            if self.is_extended_real(a) and self.is_extended_real(b):
                if self.equal(a, b):
                    return True_
                if a == -Infinity:
                    return True_
                if b == Infinity:
                    return True_
                if self.is_real(a) and b == -Infinity:
                    return False_
                if self.is_real(b) and a == Infinity:
                    return False_
                if a == Infinity and b == -Infinity:
                    return False_
        return LessEqual(*args)

    def simple_Less(self, *args):
        args = [self.simple(arg) for arg in args]
        if len(args) == 2:
            a, b = args
            if a.is_integer() and b.is_integer():
                if int(a) < int(b):
                    return True_
                else:
                    return False_
            if self.is_real(a) and self.is_real(b):
                v = self.real_enclosure(a - b)
                if v is not None:
                    if v < 0:
                        return True_
                    if v >= 0:
                        return False_
            if self.is_extended_real(a) and self.is_extended_real(b):
                if self.equal(a, b):
                    return False_
                if a == -Infinity and self.is_real(b):
                    return True_
                if a == -Infinity and b == Infinity:
                    return True_
                if self.is_real(a) and b == Infinity:
                    return True_
                if a == Infinity:
                    return False_
                if b == -Infinity:
                    return False_
        return Less(*args)

    def simple_GreaterEqual(self, *args):
        args = [self.simple(arg) for arg in args]
        if len(args) == 2:
            a, b = args
            if a.is_integer() and b.is_integer():
                if int(a) >= int(b):
                    return True_
                else:
                    return False_
            if self.is_real(a) and self.is_real(b):
                v = self.real_enclosure(a - b)
                if v is not None:
                    if v >= 0:
                        return True_
                    if v < 0:
                        return False_
            if self.is_extended_real(a) and self.is_extended_real(b):
                if self.equal(a, b):
                    return True_
                if b == -Infinity:
                    return True_
                if a == Infinity:
                    return True_
                if self.is_real(b) and a == -Infinity:
                    return False_
                if self.is_real(a) and b == Infinity:
                    return False_
                if b == Infinity and a == -Infinity:
                    return False_
        return GreaterEqual(*args)

    def simple_Greater(self, *args):
        args = [self.simple(arg) for arg in args]
        if len(args) == 2:
            a, b = args
            if a.is_integer() and b.is_integer():
                if int(a) > int(b):
                    return True_
                else:
                    return False_
            if self.is_real(a) and self.is_real(b):
                v = self.real_enclosure(a - b)
                if v is not None:
                    if v > 0:
                        return True_
                    if v <= 0:
                        return False_
            if self.is_extended_real(a) and self.is_extended_real(b):
                if self.equal(a, b):
                    return False_
                if b == -Infinity and self.is_real(a):
                    return True_
                if b == -Infinity and a == Infinity:
                    return True_
                if self.is_real(b) and a == Infinity:
                    return True_
                if b == Infinity:
                    return False_
                if a == -Infinity:
                    return False_
        return Greater(*args)

    def simple_Pos(self, x):
        return self.simple(x)

    def simple_Parentheses(self, x):
        return self.simple(x)

    def simple_Brackets(self, x):
        return self.simple(x)

    def simple_Braces(self, x):
        return self.simple(x)

    def simple_Neg(self, x):
        x = self.simple(x)
        if x.head() == Neg:
            v, = x.args()
            return v
        if x.head() == Sub:
            a, b = x.args()
            return Sub(b, a)
        if x.is_integer():
            v = int(x)
            return Expr(-v)
        return Neg(x)

    def complexity(self, expr):
        if expr in self.penalty:
            return self.penalty[expr]
        if expr.is_integer():
            v = int(expr)
            return 1 + v.bit_length() + (v<0)
        if expr.is_atom():
            if expr in [True_, False_]:
                return 1
            if expr in [Add, Sub, Neg, Pos, Mul]:
                return 10
            if expr in [Div, Sqrt, GoldenRatio, ConstI]:
                return 20
            if expr in [Pi, ConstE, Pow, Exp, Log, Sin, Cos, Tan, Sinh, Cosh, Tanh]:
                return 100
            if expr in [Gamma, Erf, Erfc, Erfi, RiemannZeta, ConstGamma, ConstCatalan]:
                return 1000
            return 1000000
        head = expr.head()
        args = expr.args()
        a = self.complexity(head)
        b = sum(self.complexity(arg) for arg in args)
        return a + 2*b + 1

    def evaluate_fmpq(self, expr):
        if expr.is_integer():
            return self._fmpq(int(expr))
        elif expr.head() == Neg:
            x, = expr.args()
            return -self.evaluate_fmpq(x)
        elif expr.head() == Sub:
            x, y = expr.args()
            return self.evaluate_fmpq(x) - self.evaluate_fmpq(y)
        elif expr.head() == Add:
            s = self._fmpq(0)
            for x in expr.args():
                s += self.evaluate_fmpq(x)
        elif expr.head() == Mul:
            s = self._fmpq(1)
            for x in expr.args():
                s *= self.evaluate_fmpq(x)
        elif expr.head() == Div:
            x, y = expr.args()
            return self.evaluate_fmpq(x) / self.evaluate_fmpq(y)
        else:
            raise NotImplementedError


    def simple_Add(self, *terms):
        """
        
        """
        if len(terms) == 0:
            return Expr(0)
        if len(terms) == 1:
            return self.simple(terms[0])
        # todo: we want to avoid recursive Add simplifies if possible...
        terms = [self.simple(x) for x in terms]
        if not all(self.is_complex(x) for x in terms):
            # todo: simplifications for this case
            return Add(*terms)
        constant_term = self._fmpz(0)
        term_coeff = {}
        def iter_term_coeff(terms):
            for x in terms:
                if x.is_integer():
                    yield Expr(1), self._fmpz(int(x))
                    continue
                head = x.head()
                if head == Add:
                    for t, c in iter_term_coeff(x.args()):
                        yield t, c
                elif head == Sub:
                    x, y = x.args()
                    for t, c in iter_term_coeff([x]):
                        yield t, c
                    for t, c in iter_term_coeff([y]):
                        yield t, -c
                elif head == Neg:
                    x, = x.args()
                    for t, c in iter_term_coeff([x]):
                        yield t, -c
                elif head == Mul:
                    factors = x.args()
                    # todo: make this more robust
                    if len(factors) >= 2:
                        try:
                            v = self.evaluate_fmpq(factors[0])
                        except NotImplementedError:
                            v = None
                        if v is None:
                            yield x, self._fmpz(1)
                        else:
                            red = self.simple_Mul(*factors[1:])
                            for t, c in iter_term_coeff([red]):
                                yield t, c * v
                    else:
                        yield x, self._fmpz(1)
                elif head == Div:
                    p, q = x.args()
                    if q.is_integer():
                        for t, c in iter_term_coeff([p]):
                            yield t, c / self._fmpq(int(q))
                    else:
                        yield x, self._fmpz(1)
                else:
                    yield x, self._fmpz(1)
        for t, c in iter_term_coeff(terms):
            # todo: detect rationals
            #if t.is_integer() and c.is_integer():
            #    t = int(t)
            #    c = int(c)
            #    constant_term += t * c
            #    continue
            if t in term_coeff:
                term_coeff[t] += c
            else:
                term_coeff[t] = c
        terms = []
        for t, c in term_coeff.items():
            if c == 0:
                continue
            elif c == 1:
                terms.append(t)
            elif c == -1:
                if t == Expr(1):
                    terms.append(Expr(-1))
                else:
                    terms.append(Neg(t))
            else:
                if isinstance(c, self._fmpq):
                    p = int(c.p)
                    q = int(c.q)
                    if q == 1:
                        terms.append(self.simple_Mul(t, Expr(p)))
                    else:
                        terms.append(self.simple_Mul(t, Div(p, q)))
                else:
                    c = int(c)
                    terms.append(self.simple_Mul(t, Expr(c)))
        terms = sorted(terms, key=lambda x: (not self.is_real(x), self.complexity(x), str(x)))
        if constant_term != 0:
            terms = [Expr(int(constant_term))] + terms
        if len(terms) == 0:
            return Expr(0)
        if len(terms) == 1:
            return terms[0]
        if len(terms) == 2 and terms[1].head() == Neg:
            x, = terms[1].args()
            return Sub(terms[0], x)
        return Add(*terms)

    def simple_Sub(self, x, y):
        if self.is_complex(x) and self.is_complex(y):
            return self.simple_Add(x, Neg(y))
        return Sub(self.simple(x), self.simple(y))

    def simple_Mul(self, *factors):
        """
        Simple product.
        """
        if len(factors) == 0:
            return Expr(1)
        if len(factors) == 1:
            return self.simple(factors[0])
        # todo: we want to avoid recursive Mul simplifies if possible...
        factors = [self.simple(x) for x in factors]
        if not all(self.is_complex(x) for x in factors):
            # todo: simplifications for this case
            return Mul(*factors)
        for x in factors:
            if x == Expr(0):
                return Expr(0)
        prefactor = self._fmpz(1)
        base_exp = {}
        def iter_base_exp(factors):
            for x in factors:
                head = x.head()
                if head == Mul:
                    for b, e in iter_base_exp(x.args()):
                        yield b, e
                elif head == Div:
                    p, q = x.args()
                    for b, e in iter_base_exp([p]):
                        yield b, e
                    for b, e in iter_base_exp([q]):
                        yield b, self.simple_Neg(e)
                elif head == Exp:
                    v, = x.args()
                    yield ConstE, v
                elif head == Pow:
                    b, e = x.args()
                    #b = self.simple(b)
                    if e.is_integer():
                        for b2, e2 in iter_base_exp([b]):
                            yield b2, self.simple_Mul(e2, e)
                    else:
                        yield b, e
                elif head == Sqrt:
                    v, = x.args()
                    yield v, Div(1, 2)
                elif head == Neg:
                    v, = x.args()
                    yield Expr(-1), Expr(1)
                    for b, e in iter_base_exp([v]):
                        yield b, e
                else:
                    yield x, Expr(1)
        for b, e in iter_base_exp(factors):
            if b.is_integer() and e.is_integer():
                bb = int(b)
                ee = int(e)
                if -2 <= ee <= 2 or bb == -1:
                    if bb == -1:
                        if ee % 2:
                            prefactor = -prefactor
                    elif ee >= 0:
                        prefactor *= self._fmpz(bb)**ee
                    else:
                        prefactor *= self._fmpq(1,bb**(-ee))
                    continue
            if b in base_exp:
                base_exp[b] += e
            else:
                base_exp[b] = e
        factors = []
        den_factors = []
        for b, e in base_exp.items():
            # todo: simple_Pow here?
            e = self.simple(e)
            if b == ConstE:
                if e == Expr(0):
                    pass
                elif e == Expr(1):
                    factors.append(b)
                else:
                    factors.append(Exp(e))
                continue
            if e.is_integer():
                e = int(e)
                if e == 0:
                    continue
                elif e == 1:
                    factors.append(b)
                elif e == -1:
                    den_factors.append(b)
                elif e >= 2:
                    factors.append(Pow(b, e))
                else:
                    den_factors.append(Pow(b, -e))
            elif e.head() == Neg:
                e, = e.args()
                den_factors.append(Pow(b, e))
            elif e == Div(1, 2):
                factors.append(Sqrt(b))
            else:
                factors.append(Pow(b, e))
        if isinstance(prefactor, self._fmpq):
            prefactor_den = Expr(int(prefactor.q))
            prefactor = Expr(int(prefactor.p))
        else:
            prefactor = Expr(int(prefactor))
            prefactor_den = Expr(1)
        factors = sorted(factors, key=lambda x: (not self.is_real(x), self.complexity(x), str(x)))
        den_factors = sorted(den_factors, key=lambda x: (self.is_real(x), self.complexity(x), str(x)))
        if prefactor != Expr(1):
            factors = [prefactor] + factors
        if prefactor_den != Expr(1):
            den_factors = [prefactor_den] + den_factors
        if len(factors) == 0:
            num = Expr(1)
        elif len(factors) == 1:
            num = factors[0]
        else:
            num = Mul(*factors)
        if len(den_factors) == 0:
            den = Expr(1)
        elif len(den_factors) == 1:
            den = den_factors[0]
        else:
            den = Mul(*den_factors)
        if den == Expr(1):
            return num
        else:
            return Div(num, den)

    def simple_Div(self, x, y):
        if self.is_complex(x) and self.is_complex(y) and self.is_not_zero(y):
            return self.simple_Mul(x, Pow(y, -1))
        return Div(self.simple(x), self.simple(y))

    def simple_Pow(self, x, y):
        x = self.simple(x)
        y = self.simple(y)
        # todo: want to combine this with power simplification in Mul...
        if self.is_complex(x) and self.is_complex(y):
            if x.is_integer() and y.is_integer():
                a = int(x)
                b = int(y)
                if 0 <= b <= 2:
                    return Expr(a**b)
            if y == Expr(0):
                return Expr(1)
            if y == Expr(1):
                return x
            if x == Expr(1):
                return Expr(1)
            if x == Expr(0):
                if self.is_positive(y):
                    return Expr(0)
                if self.is_negative(y):
                    return UnsignedInfinity
        if x == ConstE:
            return Exp(y)
        return Pow(x, y)

    def simple_Exp(self, x):
        return self.simple_Pow(ConstE, x)

    def simple_Sin(self, x):
        x = self.simple(x)
        if x == Expr(0):
            return x
        return Sin(x)

    def simple_Cos(self, x):
        x = self.simple(x)
        if x == Expr(0):
            return Expr(1)
        return Cos(x)

    # todo: have this call simple_Pow, implementing all simplifications there?
    def simple_Sqrt(self, x):
        """
        Return an expression equivalent to Sqrt(x), simplified if possible.
        """
        x = self.simple(x)
        if x in (Expr(0), Expr(1), Infinity, UnsignedInfinity, Undefined):
            return x
        if x == Expr(-1):
            return ConstI
        if x == -Infinity:
            return ConstI * Infinity
        if x.is_integer():
            # todo: call an actual square root function
            v = int(x)
            real = v >= 0
            v = abs(v)
            if v < 1e100:
                r = int(round(v ** 0.5))
                if r * r == v:
                    return Expr(r) if real else Expr(r)*ConstI
        # todo: wanted?
        if self.is_negative(x):
            return self.simple_Sqrt(-x) * ConstI
        # todo: generalize
        if x.head() == Pow:
            base, exp = x.args()
            if exp.is_integer():
                exp = int(exp)
                if exp % 2 == 0 and exp > 0 and self.is_real(base) and self.is_nonnegative(base):
                    if exp == 2:
                        return base
                    else:
                        return Pow(base, exp // 2)
        return Sqrt(x)

    def simple_Abs(self, x):
        """
        Return an expression equivalent to Abs(x), simplified if possible.
        """
        x = self.simple(x)
        if x.is_integer():
            v = int(x)
            if v >= 0:
                return x
            else:
                return Expr(-v)
        if x == Undefined:
            return x
        if self.is_infinity(x):
            return Infinity
        val = self.complex_enclosure(x)
        if val is not None:
            real, imag = val.real, val.imag
            if imag == 0:
                if real >= 0:
                    return x
                if real < 0:
                    return self.simple(-x)
            if real == 0:
                if imag >= 0:
                    return self.simple(-ConstI * x)
                if imag < 0:
                    return self.simple(ConstI * x)
        if self.is_nonnegative(x):
            return x
        if self.is_nonpositive(x):
            return self.simple(-x)
        if x.head() == Exp:
            v, = x.args()
            # todo: is_imaginary
            if self.is_complex(v):
                if self.is_real(self.simple(v / ConstI)):
                    return Expr(1)
        return Abs(x)

    def simple_Re(self, x):
        x = self.simple(x)
        if self.is_integer(x):
            return x
        if not self.is_complex(x):
            return Re(x)
        if self.is_real(x):
            return x
        if x.head() == Add:
            return self.simple_Add(*[self.simple_Re(t) for t in x.args()])
        if x.head() == Sub:
            a, b = x.args()
            return self.simple_Sub(self.simple_Re(a), self.simple_Re(b))
        if x.head() == Neg:
            a, = x.args()
            return self.simple_Neg(self.simple_Re(a))
        if x.head() == Mul:
            real = []
            nonreal = []
            for t in x.args():
                if self.is_real(t):
                    real.append(t)
                else:
                    nonreal.append(t)
            if real:
                return self.simple(Mul(*real) * Re(Mul(*nonreal)))
        if x.head() == Exp:
            a, = x.args()
            return self.simple(Exp(Re(a)) * Cos(Im(a)))
        v = self.complex_enclosure(x)
        if v is not None:
            if v.real == 0:
                return Expr(0)
        return Re(x)

    def simple_Im(self, x):
        x = self.simple(x)
        if not self.is_complex(x):
            return Im(x)
        if self.is_real(x):
            return Expr(0)
        if x == ConstI:
            return Expr(1)
        if x.head() == Add:
            return self.simple_Add(*[self.simple_Im(t) for t in x.args()])
        if x.head() == Sub:
            a, b = x.args()
            return self.simple_Sub(self.simple_Im(a), self.simple_Im(b))
        if x.head() == Neg:
            a, = x.args()
            return self.simple_Neg(self.simple_Im(a))
        if x.head() == Mul:
            real = []
            nonreal = []
            for t in x.args():
                if self.is_real(t):
                    real.append(t)
                else:
                    nonreal.append(t)
            if real:
                return self.simple(Mul(*real) * Im(Mul(*nonreal)))
        if x.head() == Exp:
            a, = x.args()
            return self.simple(Exp(Re(a)) * Sin(Im(a)))
        xdivi = self.simple(x / ConstI)
        if self.is_real(xdivi):
            return xdivi
        return Im(x)

    def some_values(self, variables, assumptions, num=10, as_dict=False, max_candidates=100000):
        """
        Attempt to generate values satisfying given assumptions (constraints).

        This is meant to be used to generate test parameters, not to solve
        equations. The method may fail to generate any suitable test values;
        this does not imply that no solutions exist.

        Input:

        variables - Python list of symbols representing variables
        assumptions - single expression giving conditions (can be And(...))
        num - maximal number of instances to generate
        as_dict - yield dict of variable assignments, not just the values

        Examples:

            >>> b = Brain()
            >>> for v in b.some_values([x, y], And(Element(x, ZZ), Element(y, QQ)), as_dict=True):
            ...     print(v)
            ... 
            {x: 0, y: 0}
            {x: 0, y: Div(1, 2)}
            {x: 1, y: 0}
            {x: 0, y: 1}
            {x: 1, y: Div(1, 2)}
            {x: -1, y: 0}
            {x: 0, y: Neg(Div(1, 2))}
            {x: 1, y: 1}
            {x: -1, y: Div(1, 2)}
            {x: 2, y: 0}

        """
        # preprocess assumptions: decouple And; factor by variables
        assert isinstance(assumptions, Expr)
        variables = list(variables)
        assumptions = list(assumptions.head_args_flattened(And))
        assumptions_by_var = {}
        for var in variables:
            for a in assumptions:
                if var in a.subexpressions():
                    assumptions_by_var[var] = assumptions_by_var.get(var, [])
                    assumptions_by_var[var].append(a)
        base_sets = {var:some_everything for var in variables}
        for var in variables:
            if var in assumptions_by_var:
                for a in assumptions_by_var[var]:
                    if a.head() == Element and a.args()[0] == var:
                        S = a.args()[1]
                        if S == PP:
                            base_sets[var] = some_primes
                        elif S == ZZ:
                            base_sets[var] = some_integers
                        elif S == QQ:
                            base_sets[var] = some_rationals
                        elif S == RR:
                            base_sets[var] = some_reals
                        elif S == CC:
                            base_sets[var] = some_complexes
                        elif S == HH:
                            base_sets[var] = some_upper_half_plane
                        elif S == AlgebraicNumbers:
                            base_sets[var] = some_algebraics
                        elif S.head() in (ZZLessEqual, ZZGreaterEqual, Range):
                            base_sets[var] = some_integers
                        elif S.head() in (ClosedInterval, OpenInterval, OpenClosedInterval, ClosedOpenInterval):
                            base_sets[var] = some_extended_reals
        base_sets = [base_sets[var] for var in variables]
        found = 0
        count = 0
        for values in custom_cartesian(*base_sets):
            assignment = {var:val for (var,val) in zip(variables, values)}
            # todo: when the assumptions for the variables are pure domain statements with simple domains, we could skip the checks
            ok = all(self.simple(a.replace(assignment)) == True_ for a in assumptions)
            if count > max_candidates:
                break
            count += 1
            if ok:
                if found == num:
                    break
                found += 1
                if as_dict:
                    yield assignment
                else:
                    yield values

    def match(self, expr, rule, free_variables=[], assumptions=None):
        if assumptions is None:
            assumptions = True_

        match_values = {}

        def match_recursive(expr, rule):
            if rule in free_variables:
                if rule in match_values:
                    if expr != match_values[rule]:
                        raise ValueError
                else:
                    match_values[rule] = expr
                return
            if expr == rule:
                return
            expr_head = expr.head()
            rule_head = rule.head()
            expr_args = expr.args()
            rule_args = rule.args()
            if expr_head != rule_head or expr_head is None or len(expr_args) != len(rule_args):
                raise ValueError
            for a, b in zip(expr_args, rule_args):
                match_recursive(a, b)

        try:
            match_recursive(expr, rule)
        except ValueError:
            return None

        #print("MATCH", rule, match_values)

        # todo: some_values search for matching assumptions if missing variables?

        assumptions = assumptions.replace(match_values)
        assumptions = self.simple(assumptions)

        #print("ASSUMPTIONS", assumptions)

        if assumptions == True_:
            return match_values
        else:
            return None

    def rewrite_fungrim(self, expr, id, recursive=True):
        from .formulas import entries_dict
        entry = entries_dict[id]
        variables = entry.get_arg_with_head(Variables)
        if variables is None:
            variables = []
        else:
            variables = variables.args()
        formula = entry.get_arg_with_head(Formula)
        if formula is None:
            raise ValueError("unsupported kind of entry for rewriting")
        formula = formula.args()[0]
        assumptions = entry.get_arg_with_head(Assumptions)
        if assumptions is None:
            assumptions = True_
        else:
            assumptions = assumptions.args()[0]
        if formula is None or formula.head() != Equal or len(formula.args()) != 2:
            raise ValueError("unsupported kind of entry for rewriting")
        lhs, rhs = formula.args()

        def match_local(expr):
            match = self.match(expr, lhs, variables, assumptions)
            if match is not None:
                return rhs.replace(match)
            if expr.is_atom():
                return expr
            head = expr.head()
            args = expr.args()
            return head(*(match_local(arg) for arg in args))

        if recursive:
            return match_local(expr)
        else:    
            match = self.match(expr, lhs, variables, assumptions)
            if match is not None:
                return rhs.replace(match)
            return expr



class FungrimBrain(Brain):
    def __init__(self):
        pass



class TestBrain(object):

    def __init__(self):
        pass

    def run(self):
        for method in dir(self):
            if method.startswith("test_"):
                print(method, "...", end=" ")
                getattr(self, method)()
                print("OK!")

    def test_init(self):
        b = Brain([x,y], And(Element(x, CC), Element(y, SetMinus(QQ, ZZ))))

    def test_domain_inference(self):
        b = Brain([x], Element(x, ZZ))
        assert b.simple(Element(x, ZZ)) == True_
        assert b.simple(Element(x, QQ)) == True_
        assert b.simple(Element(x, RR)) == True_
        assert b.simple(Element(x, CC)) == True_
        assert b.simple(Element(x, AlgebraicNumbers)) == True_
        assert b.simple(Element(x, PP)) == Element(x, PP)

        b = Brain([x], Element(x, QQ))
        assert b.simple(Element(x, QQ)) == True_
        assert b.simple(Element(x, RR)) == True_
        assert b.simple(Element(x, CC)) == True_
        assert b.simple(Element(x, AlgebraicNumbers)) == True_
        assert b.simple(Element(x, ZZ)) == Element(x, ZZ)
        assert b.simple(Element(x, PP)) == Element(x, PP)

        b = Brain([x], Element(x, RR))
        assert b.simple(Element(x, RR)) == True_
        assert b.simple(Element(x, CC)) == True_
        assert b.simple(Element(x, AlgebraicNumbers)) == Element(x, AlgebraicNumbers)
        assert b.simple(Element(x, QQ)) == Element(x, QQ)
        assert b.simple(Element(x, ZZ)) == Element(x, ZZ)
        assert b.simple(Element(x, PP)) == Element(x, PP)

        b = Brain([x], Element(x, AlgebraicNumbers))
        assert b.simple(Element(x, CC)) == True_
        assert b.simple(Element(x, AlgebraicNumbers)) == True_
        assert b.simple(Element(x, QQ)) == Element(x, QQ)
        assert b.simple(Element(x, RR)) == Element(x, RR)
        assert b.simple(Element(x, ZZ)) == Element(x, ZZ)
        assert b.simple(Element(x, PP)) == Element(x, PP)

        b = Brain([x], Element(x, PP))
        assert b.simple(Element(x, PP)) == True_
        assert b.simple(Element(x, ZZ)) == True_
        assert b.simple(Element(x, QQ)) == True_
        assert b.simple(Element(x, RR)) == True_
        assert b.simple(Element(x, CC)) == True_
        assert b.simple(Element(x, AlgebraicNumbers)) == True_

        b = Brain([x], Element(x, SetMinus(RR, QQ)))
        assert b.simple(Element(x, CC)) == True_
        assert b.simple(Element(x, RR)) == True_
        assert b.simple(Element(x, QQ)) == False_
        assert b.simple(NotElement(x, QQ)) == True_

    def test_simple(self):
        b = Brain()
        assert b.simple(Element(Add(3, 5), ZZ)) == True_
        assert b.simple(And(Not(False_), Or(True_, False_))) == True_

    def test_is_positive(self):
        b = Brain()
        assert b.is_positive(Expr(3)) is True
        assert b.is_positive(Pi) is True
        assert b.is_positive(1 + Sqrt(2)) is True
        assert b.is_positive(Expr(-3)) is False
        assert b.is_positive(Pi - 3) is True
        assert b.is_positive(Pi - 4) is False

    def test_is_algebraic(self):
        b = Brain()
        assert b.is_algebraic(ConstI) is True
        assert b.is_algebraic(Sqrt(2)) is True
        assert b.is_algebraic(Sqrt(2)+1) is True
        assert b.is_algebraic(Pi) is False
        assert b.is_algebraic(Exp(2)) is False
        assert b.is_algebraic(Log(2)) is False
        assert b.is_algebraic(Sin(2)) is False
        assert b.is_algebraic(Sin(Sqrt(Pi))) is None
        assert b.is_algebraic(2**Sqrt(2)) is False
        assert b.is_algebraic(Exp(3*ConstI*Pi/7)) is True
        b = Brain([q], And(Element(q, QQ), NotEqual(q, 0)))
        assert b.is_algebraic(Exp(q)) is False
        assert b.is_algebraic(Sin(q)) is False
        assert b.is_algebraic(Log(q)) is None
        assert b.is_algebraic(Pi + ConstE) is None

    def test_element(self):
        b = Brain()
        assert b.element(Expr(3), ZZ) is True
        assert b.element(Expr(3) * Expr(-4) + Pow(5, 2) - Expr(1), ZZ) is True
        assert b.element(Factorial(10**20), ZZ) is True
        assert b.element(Pi, ZZ) is False
        assert b.element(Pi, Set(Pi)) is True
        assert b.element(Pi, Union(ZZ, Set(Pi))) is True
        assert b.element(Pi, SetMinus(RR, QQ)) is True
        assert b.element(Div(3, 2), ZZ) in (False, None)  # todo: implement calculation

        points = [-Infinity, Expr(-3), Expr(0), Expr(3), Infinity, ConstI]
        np = range(len(points))
        bad = points.index(ConstI)
        for ia in np:
            for ib in np:
                # todo: order comparisons with complex numbers -> False consistently?
                v = b.less(points[ia], points[ib])
                if bad in (ia, ib):
                    assert v in (False, None)
                else:
                    assert v == (ia < ib)

                v = b.less_equal(points[ia], points[ib])
                if bad in (ia, ib):
                    assert v in (False, None)
                else:
                    assert v == (ia <= ib)

                v = b.greater(points[ia], points[ib])
                if bad in (ia, ib):
                    assert v in (False, None)
                else:
                    assert v == (ia > ib)

                v = b.greater_equal(points[ia], points[ib])
                if bad in (ia, ib):
                    assert v in (False, None)
                else:
                    assert v == (ia >= ib)

                for ix in np:
                    v = b.element(points[ix], ClosedInterval(points[ia], points[ib]))
                    if bad in (ia, ib):
                        assert v is None
                    elif ix == bad:
                        assert v is False
                    else:
                        assert v == (ia <= ix and ix <= ib)

                    v = b.element(points[ix], OpenInterval(points[ia], points[ib]))
                    if bad in (ia, ib):
                        assert v is None
                    elif ix == bad:
                        assert v is False
                    else:
                        assert v == (ia < ix and ix < ib)

                    v = b.element(points[ix], OpenClosedInterval(points[ia], points[ib]))
                    if bad in (ia, ib):
                        assert v is None
                    elif ix == bad:
                        assert v is False
                    else:
                        assert v == (ia < ix and ix <= ib)

                    v = b.element(points[ix], ClosedOpenInterval(points[ia], points[ib]))
                    if bad in (ia, ib):
                        assert v is None
                    elif ix == bad:
                        assert v is False
                    else:
                        assert v == (ia <= ix and ix < ib)

        assert b.element(Expr(3), ZZGreaterEqual(2)) is True
        assert b.element(Expr(3), ZZGreaterEqual(3)) is True
        assert b.element(Expr(3), ZZGreaterEqual(4)) is False
        assert b.element(Pi, ZZGreaterEqual(4)) is False

        assert b.element(Expr(3), ZZLessEqual(2)) is False
        assert b.element(Expr(3), ZZLessEqual(3)) is True
        assert b.element(Expr(3), ZZLessEqual(4)) is True
        assert b.element(Pi, ZZLessEqual(4)) is False

        assert b.element(Expr(2), Range(2, 5)) is True
        assert b.element(Expr(3), Range(2, 5)) is True
        assert b.element(Expr(5), Range(2, 5)) is True
        assert b.element(Expr(1), Range(2, 5)) is False
        assert b.element(Expr(6), Range(2, 5)) is False
        assert b.element(Pi, Range(2, 5)) is False
        assert b.element(Expr(2), Range(2, 1)) is False

        b = Brain([z], Element(z, CC))
        assert b.element(Log(z), CC) is None
        b = Brain([z], And(Element(z, CC), NotEqual(z, 0)))
        assert b.element(Log(z), CC) is True

    def test_equal(self):
        b = Brain()
        assert b.equal(Pi, Pi) is True
        assert b.equal(x, x) is True
        assert b.equal(1+x, 1+x) is True
        assert b.equal(1+x, x+1) is None
        assert b.equal(Pi, Expr(2)) is False
        assert b.equal(Expr(3), Expr(3)) is True
        assert b.equal(Expr(3), Expr(-3)) is False
        assert b.equal(Expr(3), Pi) is False
        assert b.equal(Expr(3), ConstI) is False

    def test_Sqrt(self):
        b = Brain()
        assert b.simple(Sqrt(0)) == Expr(0)
        assert b.simple(Sqrt(1)) == Expr(1)
        assert b.simple(Sqrt(2)) == Sqrt(2)
        assert b.simple(Sqrt(4)) == Expr(2)
        assert b.simple(Sqrt(-1)) == ConstI
        assert b.simple(Sqrt(-4)) == 2*ConstI
        assert b.simple(Sqrt(Infinity)) == Infinity
        assert b.simple(Sqrt(UnsignedInfinity)) == UnsignedInfinity
        assert b.simple(Sqrt(Undefined)) == Undefined
        assert b.simple(Sqrt(Pi**2)) == Pi
        assert b.simple(Sqrt(Pi**3)) == Sqrt(Pi**3)
        assert b.simple(Sqrt(Pi**4)) == Pi**2
        b = Brain([x], Element(x, ClosedOpenInterval(0, Infinity)))
        assert b.simple(Sqrt(x**2)) == x
        assert b.simple(Sqrt(x**4)) == x**2
        b = Brain([x], Element(x, RR))
        assert b.simple(Sqrt(x**2)) == Sqrt(x**2)
        # todo: check element (...)

    def test_Abs(self):
        b = Brain()
        assert b.simple(Abs(0)) == Expr(0)
        assert b.simple(Abs(1)) == Expr(1)
        assert b.simple(Abs(2)) == Expr(2)
        assert b.simple(Abs(-2)) == Expr(2)
        assert b.simple(Abs(-Pi)) == Pi
        assert b.simple(Abs(Infinity)) == Infinity
        assert b.simple(Abs(-Infinity)) == Infinity
        assert b.simple(Abs(UnsignedInfinity)) == Infinity
        assert b.simple(Abs(ConstI*UnsignedInfinity)) == Infinity
        assert b.simple(Abs(2*ConstI)) == b.simple(-ConstI*(2*ConstI))   # XXX
        assert b.simple(Abs(-2*ConstI)) == b.simple(ConstI*(-2*ConstI))   # XXX
        assert b.simple(Abs(Exp(ConstI*Pi/7))) == Expr(1)
        b = Brain([x], Element(x, OpenInterval(0, Infinity)))
        assert b.simple(Abs(x)) == x
        b = Brain([x], Element(x, OpenClosedInterval(0, Infinity)))
        assert b.simple(Abs(x)) == x
        b = Brain([x], Element(x, OpenInterval(-Infinity, 0)))
        assert b.simple(Abs(x)) == -x
        b = Brain([x], Element(x, OpenClosedInterval(-Infinity, 0)))
        assert b.simple(Abs(x)) == -x

    def test_Add(self):
        b = Brain()
        assert b.simple(Add(2, 3)) == Expr(5)
        assert b.simple(Add(-1, 1)) == Expr(0)
        assert b.simple(Add(0, 0, 0)) == Expr(0)
        assert b.simple(Add(0, 0, 1)) == Expr(1)
        assert b.simple(Add(-1, Pi, 1)) == Pi
        assert b.simple(Add(3*Pi, 5*Pi/7, Pi/2, Pi/3, 2*Pi, -Div(191,42)*Pi)) == Mul(2, Pi)

    def test_Mul(self):
        b = Brain()
        assert b.simple(Pi**2 / Pi) == Pi
        assert b.simple(Pi / Pi**2) == 1/Pi
        assert b.simple(Pi**2 / (Pi - 2*Pi)**2) == Expr(1)
        assert b.simple(Pi**2 / (Pi - 2*Pi)**3) == b.simple(-1/Pi)

    def test_fungrim(self):
        b = Brain(fungrim=True)
        assert b.simple(RiemannZeta(2) / Pi**2) == Div(1,6)
        assert b.simple((1+Sqrt(5))/2) == GoldenRatio
        assert b.simple(Sin(1)**2 + Cos(1)**2) == Expr(1)
        assert b.simple(Erf(Sin(1)**2 + Cos(1)**2) + Erfc(1)) == Expr(1)
        assert b.simple(2 * Integral(1/(2*x+3)**Div(3,2), For(x, 1, Infinity))) == b.simple(2 * Pow(5, Div(-1, 2)))

