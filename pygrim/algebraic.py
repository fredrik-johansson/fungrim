from flint import ctx, arb, acb, fmpz, fmpq, fmpz_poly, fmpq_poly, fmpq_series, fmpz_mat, fmpq_mat
import operator

_fmpz_poly_x = fmpq_poly([0,1])

# algorithm borrowed from sage
def composed_op(P1, P2, operation):
    d1 = P1.degree()
    d2 = P2.degree()
    # print("compose", d1, d2)
    assert d1 >= 1 and d2 >= 1
    cap = d1*d2 + 1
    if operation == operator.truediv:
        P2 = list(P2)
        if P2[0] == 0:
            raise ZeroDivisionError
        P2 = fmpq_poly(P2[::-1])
    if operation == operator.sub:
        P2 = list(P2)
        for i in range(1,len(P2),2):
            P2[i] = -P2[i]
        P2 = fmpq_poly(P2)
    orig_cap = ctx.cap
    try:
        ctx.cap = cap
        P1rev = list(P1)[::-1]
        P1drev = list(P1.derivative())[::-1]
        P2rev = list(P2)[::-1]
        P2drev = list(P2.derivative())[::-1]
        NP1 = fmpq_series(P1drev) / fmpq_series(P1rev)
        NP2 = fmpq_series(P2drev) / fmpq_series(P2rev)
        if operation in (operator.add, operator.sub):
            c = fmpq(1)
            a1, a2 = [NP1[0]], [NP2[0]]
            for j in range(1, cap):
                c *= j
                a1.append(NP1[j] / c)
                a2.append(NP2[j] / c)
            NP1E = fmpq_series(a1)
            NP2E = fmpq_series(a2)
            NP3E = NP1E*NP2E
            c = fmpq(-1)
            a3 = [fmpq(0)]
            for j in range(1, cap):
                a3.append(NP3E[j] * c)
                c *= j
            NP = fmpq_series(a3)
            Q = NP
        else:
            NP = fmpq_series([-NP1[j]*NP2[j] for j in range(1, cap)])
            Q = NP.integral()
        Q = Q.exp()
        Q = fmpq_poly([Q[i] for i in range(cap)][::-1])
        Q = Q.p
        return Q
    finally:
        # print("end compose")
        ctx.cap = orig_cap

def test_composed_op():
    from random import randrange
    for N in range(100):
        while 1:
            D1 = randrange(10)
            D2 = randrange(10)
            F = fmpz_poly([randrange(-2,3) for n in range(D1)])
            G = fmpz_poly([randrange(-2,3) for n in range(D2)])
            if F.degree() >= 1 and G.degree() >= 1:
                break
        H = composed_op(F, G, operator.add)
        for x, r in F.roots():
            for y, r in G.roots():
                v = H(x+y)
                assert v.contains(0)
        H = composed_op(F, G, operator.sub)
        for x, r in F.roots():
            for y, r in G.roots():
                v = H(x-y)
                assert v.contains(0)
        H = composed_op(F, G, operator.mul)
        for x, r in F.roots():
            for y, r in G.roots():
                v = H(x*y)
                assert v.contains(0)
        if G[0] != 0:
            H = composed_op(F, G, operator.truediv)
            for x, r in F.roots():
                for y, r in G.roots():
                    v = H(x/y)
                    assert v.contains(0)

_alg_degree_limit = [None]
_alg_bits_limit = [None]

def alg_get_degree_limit():
    return _alg_degree_limit[0]

def alg_set_degree_limit(lim):
    _alg_degree_limit[0] = lim

def alg_get_bits_limit():
    return _alg_bits_limit[0]

def alg_set_bits_limit(lim):
    _alg_bits_limit[0] = lim

def check_degree_limit(deg):
    degree_limit = alg_get_degree_limit()
    if degree_limit is not None:
        if deg > degree_limit:
            raise ValueError("degree limit exceeded")

def check_bits_limit(bits):
    bits_limit = alg_get_bits_limit()
    if bits_limit is not None:
        if bits > bits_limit:
            raise ValueError("bits limit exceeded")

class alg(object):
    """
    A type representing algebraic numbers.

        >>> phi = (alg(5).sqrt() + 1)/2
        >>> phi
        1.61803 (deg 2)
        >>> y = ((phi**100 - (1-phi)**100) / alg(5).sqrt())
        >>> y
        3.54225e+20 (deg 1)
        >>> y.is_integer()
        True
        >>> y.fmpz()
        354224848179261915075

    """
    def __init__(self, v=0, _minpoly=None, _enclosure=None):
        """
        An *alg* instance can be created from an existing *alg*
        (this creates a copy), from a Python integer, or from
        a FLINT *fmpz* or *fmpq*:

            >>> alg(3)
            3.00000 (deg 1)
            >>> alg(alg(3))
            3.00000 (deg 1)
            >>> alg(fmpq(2,3))
            0.666667 (deg 1)

        It is also possible to create an *alg* instance *unsafely* from the
        internal representation consisting of a minimal polynomial
        and an enclosure:

            >>> alg(_minpoly=fmpz_poly([-1,-1,1]), _enclosure=arb("1.618 +/- 0.001"))
            1.61803 (deg 2)

        The minimal polynomial must be an *fmpz_poly* that is irreducible and
        normalized (no factors, GCD content removed, positive leading
        coefficient), and the enclosure must isolate a unique root
        of this polynomial. Warning: these properties are *not* checked.
        Providing invalid input will silently produce wrong results
        in subsequent computations.
        """
        if _minpoly is not None:
            assert type(_minpoly) == fmpz_poly
            self._minpoly = _minpoly
            self._enclosure = _enclosure
        elif isinstance(v, (int, fmpz)):
            self._minpoly = fmpz_poly([-v,1])
            self._enclosure = None
        elif isinstance(v, fmpq):
            self._minpoly = fmpz_poly([-v.p, v.q])
            self._enclosure = None
        elif isinstance(v, alg):
            self._minpoly = v._minpoly
            self._enclosure = v._enclosure
        else:
            raise NotImplementedError
        self._hash = None

    def minpoly(self):
        """
        Returns the minimal polynomial of *self* as an *fmpz_poly*.

            >>> ((-alg(2)).sqrt()).minpoly()
            x^2 + 2
            >>> list(_)
            [2, 0, 1]
        """
        return self._minpoly

    def degree(self):
        """
        Returns the degree of *self*, i.e. the degree of the minimal polynomial.

            >>> (alg(1)/3).degree()
            1
            >>> alg(2).root(5).degree()
            5
        """
        return self._minpoly.degree()

    def height(self):
        """
        Returns the height of *self*, i.e. the maximum of the absolute values
        of the coefficients of the minimal polynomial of *self*.

            >>> (alg(5).sqrt() + alg(1)/17).height()
            1444
            >>> (alg(5).sqrt() + alg(1)/17).minpoly()
            289*x^2 + (-34)*x + (-1444)
        """
        return max(abs(c) for c in self.minpoly())

    def index(self):
        """
        Returns the index of *self* among the roots of its minimal polynomial
        in canonical order, counting from 1.
        The index is an integer between 1 and *d* inclusive, where *d* is the
        degree of *self*. The minimal polynomial together with the index
        uniquely identifies this algebraic number.

            >>> x = alg(2).sqrt()
            >>> x.index()
            1
            >>> (-x).index()
            2
            >>> for x, m in alg.polynomial_roots([5,3,1,1]):
            ...     print(x.index())
            ... 
            1
            2
            3
        """
        if self.degree() == 1:
            return 1
        else:
            return self.conjugates().index(self) + 1

    def str(self, digits=6, rep=False, formula=False):
        # fixme: enclosure() with enough precision, if ctx.prec is low...
        if rep:
            return "alg(%s, %s)" % (list(self.minpoly()), self.enclosure())
        elif formula:
            if self.degree() <= 2:
                a, b, c = self.as_quadratic()
                if b == 0:
                    return "%s" % a
                elif b == 1:
                    return "%s + (%s)^(1/2)" % (a, c)
                elif b == -1:
                    return "%s - (%s)^(1/2)" % (a, c)
                elif b < 0:
                    return "%s - %s*(%s)^(1/2)" % (a, -b, c)
                else:
                    return "%s + %s*(%s)^(1/2)" % (a, b, c)
            else:
                return self.str(rep=True)
        else:
            sstr = self.enclosure(pretty=True).str(digits, radius=False)
            #sstr = sstr.replace("j", "*I")
            return "%s (deg %s)" % (sstr, self.degree())

    def __repr__(self):
        return self.str()

    def __str__(self):
        return self.str()

    def __bool__(self):
        return self._minpoly != _fmpz_poly_x

    def is_rational(self):
        return self._minpoly.degree() == 1

    def is_integer(self):
        return self._minpoly.degree() == 1 and self._minpoly[1] == 1

    def fmpq(self):
        if not self.is_rational():
            raise ValueError("fmpq() requires a rational value")
        c0 = self._minpoly[0]
        c1 = self._minpoly[1]
        return fmpq(c0) / (-c1)

    def fmpz(self):
        if not self.is_integer():
            raise ValueError("fmpz() requires an integer value")
        c0 = self._minpoly[0]
        return -c0

    def as_quadratic(self, factor_limit=2**64):
        """
        Assuming that *self* has degree 1 or 2, returns (*a*, *b*, *c*)
        where *a* and *b* are *fmpq* rational numbers and *c* is a *fmpz*
        integer, such that *self* equals `a + b \sqrt{c}`.

        The integer *c* will not be a perfect square, but might not be
        squarefree since ensuring this property requires integer factorization.
        If *|c|* is initially smaller than *factor_limit*, it will be
        completely factored into its squarefree part (with the square content
        moved to *b*); otherwise, only a partial factorization will be performed.

            >>> alg(-23).as_quadratic()
            (-23, 0, 0)
            >>> (2 + alg.i() / 3).as_quadratic()
            (2, 1/3, -1)
            >>> x = (alg(5)/2 + alg(24).sqrt())**5
            >>> x.as_quadratic()
            (353525/32, 36341/8, 6)
            >>> x == alg(353525)/32 + alg(36341)/8 * alg(6).sqrt()
            True
            >>> alg(3 * 29**2 * (10**20+39)**2).sqrt().as_quadratic()
            (0, 2900000000000000001131, 3)
            >>> x = alg(3 * (10**10+1)**3 * (10**15+1)**2).sqrt()
            >>> a, b, c = x.as_quadratic()
            >>> (a, b, c)
            (0, 39340116598834051, 1938429316132524961593868203)
            >>> x == a + b*alg(c).sqrt()
            True
            >>> a, b, c = x.as_quadratic(factor_limit=10**50)
            >>> (a, b, c)
            (0, 10000000001000010000000001, 30000000003)
            >>> x == a + b*alg(c).sqrt()
            True

        """
        poly = self._minpoly
        if poly.degree() == 1:
            return (self.fmpq(), fmpq(), fmpz())
        if poly.degree() != 2:
            raise ValueError
        c, b, a = list(self.minpoly())
        D = b**2 - 4*a*c
        Dsqrt = alg(D).sqrt()
        x = (-b + Dsqrt) / (2*a)
        if self == x:
            bsign = 1
        else:
            x = (-b - Dsqrt) / (2*a)
            bsign = -1        
        a, b, c = fmpq(-b)/(2*a), fmpq(bsign,2*a), D
        if abs(c) >= 4:
            if abs(c) < factor_limit:
                fac = c.factor()
            else:
                fac = c.factor(trial_limit=1000)
                # todo: the partial factoring in flint is wonky;
                # it should at least do a perfect power test or single-word
                # factorisation of the last factor
                rem = fac[-1][0]
                if rem < factor_limit:
                    fac = fac[:-1] + rem.factor()
                elif rem.is_perfect_power():
                    for e in range(64,1,-1):
                        p = rem.root(e)
                        if p**e == rem:
                            if p < factor_limit:
                                fac2 = rem.factor()
                                fac = fac[:-1]
                                for (p, f) in fac2:
                                    fac.append((p, e*f))
                            else:
                                fac = fac[:-1] + [(p, e)]
                            break
            square = fmpz(1)
            squarefree = fmpz(1)
            for p, e in fac:
                if e % 2 == 0:
                    square *= p**(e//2)
                else:
                    square *= p**(e//2)
                    squarefree *= p
            if c < 0:
                squarefree = -squarefree
            b *= square
            c = squarefree
        return a, b, c

    def expr(self):
        from .brain import Brain
        brain = Brain()
        return brain.alg_to_expression(self)

    @staticmethod
    def i():
        return alg(_minpoly=fmpz_poly([1,0,1]), _enclosure=acb(0,1))

    @staticmethod
    def phi():
        return (1+alg(5).sqrt())/2

    @staticmethod
    def complex(a, b):
        return alg(a) + alg(b)*alg.i()

    def __eq__(a, b):
        if a is b:
            return True
        try:
            if type(a) != alg:
                a = alg(a)
            if type(b) != alg:
                b = alg(b)
        except NotImplementedError:
            return NotImplemented
        if a._minpoly != b._minpoly:
            return False
        # rationals have a unique root
        if a._minpoly.degree() == 1:
            return True
        prec = ctx.prec
        ctx.prec = 64
        try:
            while 1:
                ar = a.enclosure()
                br = b.enclosure()
                if not acb(ar).overlaps(br):
                    return False
                z = acb(ar).union(br)
                z2 = alg._validate_root_enclosure(a._minpoly, z)
                if z2 is not None:
                    return True
                ctx.prec *= 2
        finally:
            ctx.prec = prec

    def __ne__(a, b):
        try:
            if type(a) != alg:
                a = alg(a)
            if type(b) != alg:
                b = alg(b)
        except NotImplementedError:
            return NotImplemented
        return not a.__eq__(b)

    def __ge__(a, b):
        try:
            if type(a) != alg:
                a = alg(a)
            if type(b) != alg:
                b = alg(b)
        except NotImplementedError:
            return NotImplemented
        if not (a.is_real() and b.is_real()):
            return False
        if a.is_rational() and b.is_rational():
            return a.fmpq() >= b.fmpq()
        if a._enclosure is not None and b._enclosure is not None:
            if a._enclosure >= b._enclosure:
                return True
            if a._enclosure < b._enclosure:
                return False
        return (a-b).sgn() >= 0

    def __gt__(a, b):
        try:
            if type(a) != alg:
                a = alg(a)
            if type(b) != alg:
                b = alg(b)
        except NotImplementedError:
            return NotImplemented
        if not (a.is_real() and b.is_real()):
            return False
        if a.is_rational() and b.is_rational():
            return a.fmpq() > b.fmpq()
        if a._enclosure is not None and b._enclosure is not None:
            if a._enclosure > b._enclosure:
                return True
            if a._enclosure <= b._enclosure:
                return False
        return (a-b).sgn() > 0

    def __le__(a, b):
        try:
            if type(a) != alg:
                a = alg(a)
            if type(b) != alg:
                b = alg(b)
        except NotImplementedError:
            return NotImplemented
        if not (a.is_real() and b.is_real()):
            return False
        if a.is_rational() and b.is_rational():
            return a.fmpq() <= b.fmpq()
        if a._enclosure is not None and b._enclosure is not None:
            if a._enclosure <= b._enclosure:
                return True
            if a._enclosure > b._enclosure:
                return False
        return (a-b).sgn() <= 0

    def __lt__(a, b):
        try:
            if type(a) != alg:
                a = alg(a)
            if type(b) != alg:
                b = alg(b)
        except NotImplementedError:
            return NotImplemented
        if not (a.is_real() and b.is_real()):
            return False
        if a.is_rational() and b.is_rational():
            return a.fmpq() < b.fmpq()
        if a._enclosure is not None and b._enclosure is not None:
            if a._enclosure < b._enclosure:
                return True
            if a._enclosure >= b._enclosure:
                return False
        return (a-b).sgn() < 0

    def conjugate(self):
        if self.is_rational():
            return self
        if isinstance(self._enclosure, arb) or self._enclosure.imag == 0:
            return self
        y = self._enclosure.conjugate(exact=True)
        return alg(_minpoly=self._minpoly, _enclosure=y)

    @property
    def real(self):
        if self.is_real():
            return self
        return (self + self.conjugate()) / 2

    @property
    def imag(self):
        if self.is_real():
            return alg(0)
        return (self - self.conjugate()) / alg(_minpoly=fmpz_poly([4,0,1]), _enclosure=acb(0,2))

    def __abs__(self):
        if self.is_rational():
            return alg(abs(self.fmpq()))
        if self.is_real():
            if self._enclosure > 0:
                return self
            if self._enclosure < 0:
                return -self
            return self.pow(2).root(2)
        return (self * self.conjugate()).root(2)

    def sgn(self):
        if self.is_rational():
            v = self._minpoly[0]
            if v < 0:
                return alg(1)
            if v > 0:
                return alg(-1)
            return alg(0)
        if self.is_real():
            if self._enclosure > 0:
                return alg(1)
            if self._enclosure < 0:
                return alg(-1)
        return self / abs(self)

    def real_sgn(self):
        if self.is_rational():
            return self.sgn()
        v = self._enclosure
        if v.real > 0:
            return alg(1)
        if v.real < 0:
            return alg(-1)
        return (self * alg.i()).imag_sgn()

    def imag_sgn(self):
        if self.is_real():
            return alg(0)
        orig = ctx.prec
        try:
            ctx.prec = 64
            while 1:
                v = self.enclosure()
                if v.imag > 0:
                    return alg(1)
                if v.imag < 0:
                    return alg(-1)
                ctx.prec *= 2
        finally:
            ctx.prec = orig

    def is_real(self):
        if self.is_rational():
            return True
        if isinstance(self._enclosure, arb):
            return True
        if self._enclosure.imag == 0:
            self._enclosure = self._enclosure.real
            return True
        if isinstance(self._enclosure, acb) and self._enclosure.imag != 0:
            return False
        v = self.conjugate()
        if v == self:
            self._enclosure = self._enclosure.real  # note: exact
            return True
        return False

    def floor(self):
        r = self.real
        if r.is_rational():
            return alg(r.fmpq().floor())
        orig = ctx.prec
        try:
            ctx.prec = 64
            while 1:
                v = self.enclosure()
                v = v.floor().unique_fmpz()
                if v is not None:
                    return alg(v)
                ctx.prec *= 2
        finally:
            ctx.prec = orig

    def ceil(self):
        r = self.real
        if r.is_rational():
            return alg(r.fmpq().ceil())
        orig = ctx.prec
        try:
            ctx.prec = 64
            while 1:
                v = self.enclosure()
                v = v.ceil().unique_fmpz()
                if v is not None:
                    return alg(v)
                ctx.prec *= 2
        finally:
            ctx.prec = orig

    @staticmethod
    def _validate_root_enclosure(poly, x):
        """
        Given x known to be an enclosure of *at least one root of poly*,
        certifies that the enclosure contains a unique root, and in that
        case returns a new (possibly improved) enclosure for the same
        root.

        Returns None if uniqueness cannot be certified.
        """
        if x.is_exact() or poly.degree() == 1:
            return x
        orig = ctx.prec
        try:
            acc = x.rel_accuracy_bits()
            ctx.prec = max(acc, 32) * 2 + 10
            # slightly inflate enclosure - needed e.g. in case of
            # complex interval with one very narrow real/imaginary part
            eps = x.rad() * (1/16.)
            if x.imag == 0:
                x += arb(0,eps)
            else:
                x += acb(arb(0,eps), arb(0,eps))
            # interval Newton steps
            xmid = x.mid()
            y = xmid - poly(xmid) / poly.derivative()(x)
            if x.contains(y):
                return y
            return None
        finally:
            ctx.prec = orig

    def enclosure(self, pretty=False):
        if self.degree() == 1:
            c0 = self._minpoly[0]
            c1 = self._minpoly[1]
            return arb(c0) / (-c1)
        elif pretty:
            z = self.enclosure()
            re = z.real
            im = z.imag
            # detect zero real/imag part
            if z.real.contains(0):
                if self.real_sgn() == 0:
                    re = arb(0)
            if z.imag.contains(0):
                if self.imag_sgn() == 0:
                    im = arb(0)
            # detect exact (dyadic) real/imag parts
            # fixme: extracting real and imag parts and checking if
            # they are exact can be slow at high degree; this is a workaround
            # until that operation can be improved
            scale = fmpz(2)**max(10,ctx.prec-20)
            if not re.is_exact() and (re * scale).unique_fmpz() is not None:
                n = (re * scale).unique_fmpz()
                b = self - fmpq(n, scale)
                if b.real_sgn() == 0:
                    re = arb(fmpq(n, scale))
            if not im.is_exact() and (im * scale).unique_fmpz() is not None:
                n = (im * scale).unique_fmpz()
                b = self - fmpq(n, scale) * alg.i()
                if b.imag_sgn() == 0:
                    im = arb(fmpq(n, scale))
            if im == 0:
                return arb(re)
            else:
                return acb(re, im)
        else:
            orig_prec = ctx.prec
            x = self._enclosure
            if x.rel_accuracy_bits() >= orig_prec - 2:
                return x
            # Try interval newton refinement
            f = self._minpoly
            g = self._minpoly.derivative()
            try:
                ctx.prec = max(x.rel_accuracy_bits(), 32) + 10
                for step in range(40):
                    ctx.prec *= 2
                    if ctx.prec > 1000000:
                        raise ValueError("excessive precision")
                    # print("root-refinement prec", ctx.prec)
                    # print(x.mid().str(10), x.rad().str(10))
                    xmid = x.mid()
                    y = xmid - f(xmid) / g(x)
                    if y.rel_accuracy_bits() >= 1.1 * orig_prec:
                        self._enclosure = y
                        return y
                    if y.rel_accuracy_bits() < 1.5 * x.rel_accuracy_bits() + 1:
                        # print("refinement failed -- recomputing roots")
                        roots = self._minpoly.roots()
                        near = [r for (r, mult) in roots if acb(r).overlaps(x)]
                        if len(near) == 1:
                            y = near[0]
                            if y.rel_accuracy_bits() >= 1.1 * orig_prec:
                                self._enclosure = y
                                return y
                    x = y
                raise ValueError("root refinement did not converge")
            finally:
                ctx.prec = orig_prec

    @staticmethod
    def gaussian_integer(a, b):
        if b == 0:
            return alg(a)
        a = fmpz(a)
        b = fmpz(b)
        orig = ctx.prec
        ctx.prec = 64
        try:
            z = acb(a, b)
        finally:
            ctx.prec = orig
        res = alg(_minpoly=fmpz_poly([a**2 + b**2, -2*a, 1]), _enclosure=z)
        return res

    @staticmethod
    def exp_two_pi_i(x):
        x = fmpq(x)
        poly = fmpz_poly.cyclotomic(x.q)
        prec = ctx.prec
        ctx.prec = 64
        try:
            while 1:
                a = arb.cos_pi_fmpq(2 * x)
                b = arb.sin_pi_fmpq(2 * x)
                z = acb(a, b)
                z2 = alg._validate_root_enclosure(poly, z)
                if z2 is not None:
                    return alg(_minpoly=poly, _enclosure=z2)
                ctx.prec *= 2
        finally:
            ctx.prec = prec

    @staticmethod
    def exp_pi_i(x):
        x = fmpq(x)
        return alg.exp_two_pi_i(x / 2)

    @staticmethod
    def cos_pi(x, monic=False):
        x = fmpq(x)
        x2 = x / 2
        poly = fmpz_poly.cos_minpoly(x2.q)
        prec = ctx.prec
        ctx.prec = 64
        try:
            while 1:
                z = 2 * arb.cos_pi_fmpq(x)
                z2 = alg._validate_root_enclosure(poly, z)
                if z2 is not None:
                    v = alg(_minpoly=poly, _enclosure=z2)
                    if not monic:
                        v /= 2
                    return v
                ctx.prec *= 2
        finally:
            ctx.prec = prec

    @staticmethod
    def sin_pi(x, monic=False):
        return alg.cos_pi(fmpq(1,2) - x, monic=monic)

    @staticmethod
    def tan_pi(x):
        a = alg.sin_pi(x, monic=True)
        b = alg.cos_pi(x, monic=True)
        return a / b

    @staticmethod
    def cot_pi(x):
        a = alg.cos_pi(x, monic=True)
        b = alg.sin_pi(x, monic=True)
        return a / b

    @staticmethod
    def sec_pi(x):
        a = alg.cos_pi(x, monic=True)
        return 2 / a

    @staticmethod
    def csc_pi(x):
        a = alg.sin_pi(x, monic=True)
        return 2 / a

    @staticmethod
    def _binop(a, b, operation):
        if type(a) != alg:
            a = alg(a)
        if type(b) != alg:
            b = alg(b)
        F = a._minpoly
        G = b._minpoly
        check_degree_limit(F.degree() * G.degree())
        check_bits_limit(F.height_bits() + G.height_bits())
        H = composed_op(F, G, operation)
        # print("begin factoring", H.degree())
        c, factors = H.factor()
        # print("end factoring")
        prec = 64
        orig_prec = ctx.prec
        try:
            while 1:
                # print("trying prec", prec)
                ctx.prec = prec
                x = a.enclosure()
                y = b.enclosure()
                z = operation(x, y)
                maybe_root = [fac for fac, mult in factors if fac(z).contains(0)]
                if len(maybe_root) == 1:
                    fac = maybe_root[0]
                    z2 = alg._validate_root_enclosure(fac, z)
                    if z2 is not None:
                        return alg(_minpoly=fac, _enclosure=z2)
                prec *= 2
        finally:
            ctx.prec = orig_prec

    def pow(self, n):
        if self.is_rational():
            c0 = self._minpoly[0]
            c1 = self._minpoly[1]
            if abs(n) > 2:
                check_bits_limit(c0.height_bits() * n)
                check_bits_limit(c1.height_bits() * n)
            if n >= 0:
                return alg(fmpq(c0**n) / (-c1)**n)
            else:
                return alg((-c1)**n / fmpq(c0**n))
        if n == 0:
            return alg(1)
        if n == 1:
            return self
        if n == 2:
            return self * self
        if n < 0:
            return (1 / self).pow(-n)
        v = self.pow(n // 2)
        v = v * v
        if n % 2:
            v *= self
        return v

    def sqrt(self):
        return self.root(2)

    def root(self, n):
        assert n >= 0
        if n == 0:
            raise ZeroDivisionError
        if n == 1:
            return self
        F = self._minpoly
        d = F.degree()
        check_degree_limit(d * n)
        H = [0] * (d * n + 1)
        H[::n] = list(F)
        H = fmpz_poly(H)
        c, factors = H.factor()
        prec = 64
        orig_prec = ctx.prec
        try:
            while 1:
                ctx.prec = prec
                x = self.enclosure(pretty=True)
                z = acb(x).root(n)
                #if not z.imag == 0:
                #    eps = arb(0, z.rad())
                #    z += acb(eps,eps)
                maybe_root = [fac for fac, mult in factors if fac(z).contains(0)]
                if len(maybe_root) == 1:
                    fac = maybe_root[0]
                    z2 = alg._validate_root_enclosure(fac, z)
                    if z2 is not None:
                        return alg(_minpoly=fac, _enclosure=z2)
                prec *= 2
        finally:
            ctx.prec = orig_prec




    # optimize!
    def __neg__(self):
        return 0 - self

    def __add__(a, b):
        return alg._binop(a, b, operator.add)

    def __radd__(a, b):
        return alg._binop(a, b, operator.add)

    def __sub__(a, b):
        return alg._binop(a, b, operator.sub)

    def __rsub__(a, b):
        return alg._binop(b, a, operator.sub)

    def __mul__(a, b):
        return alg._binop(a, b, operator.mul)

    def __rmul__(a, b):
        return alg._binop(a, b, operator.mul)

    def __div__(a, b):
        return alg._binop(a, b, operator.truediv)

    def __rdiv__(a, b):
        return alg._binop(b, a, operator.truediv)

    def __truediv__(a, b):
        return alg._binop(a, b, operator.truediv)

    def __rtruediv__(a, b):
        return alg._binop(b, a, operator.truediv)

    def __pow__(a, b):
        if type(b) in (int, fmpz):
            return a.pow(int(b))
        if type(b) == fmpq:
            p = b.p
            q = b.q
            return a.root(q) ** p
        if type(b) == alg:
            if b.is_rational():
                return a ** b.fmpq()
        raise ValueError("power of algebraic number requires a rational exponent")

    def __rpow__(a, b):
        b = alg(b)
        return b ** a

    @staticmethod
    def guess(z, deg=None, verbose=False, try_smaller=True, check=True):
        """
        Use LLL to try to find an algebraic number matching the real or
        complex enclosure *z* (given as a *flint.arb* or *flint.acb*).
        Returns *None* if unsuccessful.

        To determine the number of bits to use in the LLL matrix, the
        algorithm accounts for the accuracy of the input as well as the
        current Arb working precision (*flint.ctx.prec*).

        The maximum degree is determined by the *deg* parameter.
        By default the degree is set to roughly the square root of the working
        precision.
        If *try_smaller* is set, then the guessing is attempted recursively
        with lower degree bounds to speed up detection of lower-degree
        numbers.

        If *check* is True (default), the algorithm verifies that the
        result is contained in the complex interval *z*. (At high precision,
        this reduces the likelihood of spurious results.)

        """
        z = acb(z)
        if not z.is_finite():
            return None
        if deg is None:
            deg = max(1, int(ctx.prec ** 0.5))
        if try_smaller and deg > 8:
            g = alg.guess(z, deg // 4, verbose=verbose, try_smaller=True, check=check)
            if g is not None:
                return g
        # todo: early detect exact (dyadic) real and imaginary parts?
        # (avoid reliance on enclosure(pretty=True)
        prec = ctx.prec
        z = acb(z)
        zpow = [z**i for i in range(deg+1)]
        magn = max(abs(t) for t in zpow)
        if magn >= arb(2)**prec:
            return None   # too large
        magnrad = max(abs(t.rad()) for t in zpow)
        if magnrad >= 0.125:
            return None   # too imprecise
        magnrad = max(2**(max(1,prec//20)) * magnrad, arb(2)**(-2*prec))
        scale = 1 / magnrad
        nonreal = z.imag != 0
        A = fmpz_mat(deg + 1, deg + 2 + nonreal)
        for i in range(deg+1):
            A[i,i] = 1
        for i in range(deg+1):
            v = zpow[i] * scale
            # fixme: don't use unique_fmpz
            A[i,deg + 1] = v.real.mid().floor().unique_fmpz()
            if nonreal:
                A[i,deg + 2] = v.imag.mid().floor().unique_fmpz()
        A = A.lll()
        poly = fmpz_poly([A[0,i] for i in range(deg+1)])
        if verbose:
            print("LLL-reduced matrix:")
            print(A)
            print("poly(z) =", poly(z))
        if not check:
            candidates = alg.polynomial_roots(poly) or [(alg(0), 1)]
            return min([cand for (cand, mult) in candidates], key=lambda x: abs(x.enclosure()-z).mid())
        if not poly(z).contains(0):
            return None
        orig = ctx.prec
        try:
            candidates = alg.polynomial_roots(poly)
            while ctx.prec <= 16 * orig:
                for cand, mult in candidates:
                    r = cand.enclosure(pretty=True)
                    if z.contains(r):
                        return cand
                ctx.prec *= 2
        finally:
            ctx.prec = orig
        return None

    @staticmethod
    def polynomial_roots(poly, canonical_order=True):
        """
        Returns all the roots of the given *fmpz_poly* or *fmpq_poly*,
        or list of coefficients that can be converted to an *fmpq_poly*.
        (At this time, this function does not support algebraic coefficients.)

        The output is a list of pairs (*root*, *m*) where root
        is an algebraic number and *m* >= 1 is its multiplicity.

        With *canonical_order* set to *True*, the roots are sorted in
        a mathematically well-defined way, ensuring a consistent
        ordering of algebraic numbers.
        """
        poly = fmpq_poly(poly).numer()
        # todo: flag to assume irreducible?
        c, factors = poly.factor()
        roots = []
        orig = ctx.prec
        maxprec = 64
        try:
            for fac, mult in factors:
                if fac.degree() == 1:
                    a, b = list(fac)
                    roots.append((alg(fmpq(-a,b)), mult))
                    continue
                ctx.prec = 64
                while 1:
                    fac_roots = fac.roots()
                    checked_roots = []
                    for r, _ in fac_roots:
                        r = alg._validate_root_enclosure(fac, r)
                        if r is not None:
                            checked_roots.append(r)
                        else:
                            break
                    if len(checked_roots) == len(fac_roots):
                        for i in range(len(fac_roots)):
                            a = alg(_minpoly=fac, _enclosure=checked_roots[i])
                            roots.append((a, mult))
                        break
                    ctx.prec *= 2
                    maxprec = max(maxprec, ctx.prec)
            if len(roots) > 1 and canonical_order:
                from functools import cmp_to_key
                real = []
                nonreal = []
                ctx.prec = 64
                for (r, m) in roots:
                    if r.is_real():
                        real.append((r, m))
                    else:
                        z = r.enclosure()
                        if z.imag > 0:
                            nonreal.append((r, m))
                        else:
                            assert z.imag < 0
                def complex_algebraic_cmp(a, b):
                    a, _ = a
                    b, _ = b
                    ctx.prec = 64
                    while 1:
                        ac = a.enclosure()
                        bc = b.enclosure()
                        ac = ac.real + ac.imag * arb.pi()
                        bc = bc.real + bc.imag * arb.pi()
                        if ac.overlaps(bc):
                            ctx.prec *= 2
                        else:
                            if ac < bc:
                                return -1
                            else:
                                return 1
                roots = sorted(real, reverse=True)
                nonreal = sorted(nonreal, key=cmp_to_key(complex_algebraic_cmp), reverse=True)
                for r, m in nonreal:
                    roots.append((r, m))
                    roots.append((r.conjugate(), m))
        finally:
            ctx.prec = orig
        return roots

    @staticmethod
    def matrix_eigenvalues(mat):
        mat = fmpq_mat(mat)
        return alg.polynomial_roots(mat.charpoly())

    def conjugates(self):
        """
        Returns a list of the set of algebraic conjugates of *self*.
        The list includes *self*.
        """
        roots = alg.polynomial_roots(self.minpoly())
        return [r for (r, m) in roots]

    def __hash__(self):
        if self._hash is None:
            if self.is_rational():
                x = self.fmpq()
                self._hash = hash(x)
            poly = tuple(self._minpoly)
            orig = ctx.prec
            try:
                ctx.prec = 64
                while 1:
                    z = self.enclosure()
                    v = ((z.real / arb.pi() + z.imag * arb.pi()) * 1e15)
                    v = v.floor()
                    n = v.unique_fmpz()
                    if n is not None:
                        self._hash = hash((poly, n))
                        break
                    ctx.prec *= 2
            finally:
                ctx.prec = orig
        return self._hash

    def continued_fraction(self, N=None):
        """
        Generates the terms in the continued fraction expansion of *self*,
        up to the first *N* coefficients. If *N* is *None* (default), it
        iterates forever (unless the continued fraction expansion terminates).

        The coefficients are output as *fmpz* integers.

        **Examples**

            >>> list(alg(2).sqrt().continued_fraction(10))
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            >>> list((-alg(2).root(3)).continued_fraction(10))
            [-2, 1, 2, 1, 5, 1, 1, 4, 1, 1]
            >>> list((alg(31415926535) / 10**10).continued_fraction())
            [3, 7, 15, 1, 292, 1, 1, 6, 2, 13, 3, 1, 12, 3]

        """
        if not self.is_real():
            raise ValueError
        b = self
        a = b.floor().fmpz()
        yield a
        b = b - a
        num = 1
        while b:
            if N is not None and num >= N:
                break
            b = 1 / b
            a = b.floor().fmpz()
            yield a
            b = b - a
            num += 1

class TestAlgebraic:

    def run(self):
        from time import time
        import sys
        for method in dir(self):
            if method.startswith("test_"):
                mname = method +  " ..."
                print(mname.ljust(40), end=" ")
                sys.stdout.flush()
                t1 = time()
                getattr(self, method)()
                t2 = time()
                print("OK!       %.3f s" % (t2 - t1))

    def test_examples(self):
        assert sum(1/alg(n) for n in range(1,101)) == fmpq.harmonic(100)
        sqrt = lambda n: alg(n).sqrt()
        x = sqrt(2*sqrt(3)*sqrt(2*sqrt(10) + 7) + 2*sqrt(10) + 10)
        y = sqrt(2) + sqrt(3) + sqrt(5)
        assert x == y
        def R(a,n):
            return alg(a).root(n)
        assert R(2,1) + R(2,2) - R(2,2) - R(2,1) == 0
        assert R(2,1) + R(2,2) + R(2,3) - R(2,2) - R(2,1) - R(2,3) == 0
        assert R(2,4) + R(2,1) + R(2,2) + R(2,3) - R(2,2) - R(2,1) - R(2,3) - R(2,4) == 0
        assert 7 < sum(R(2,n) for n in [1,2,3,4,5]) < fmpq(702,100)

    def test_nested_radicals(self):
        # https://en.wikipedia.org/wiki/Nested_radical
        def R(a,n):
            return alg(a).root(n)
        a = R(3+2*R(2,2),2)
        b = 1 + R(2,2)
        assert a == b
        a = R(5+2*R(6,2),2)
        b = R(2,2) + R(3,2)
        assert a == b
        x = R(5,4)
        a = R((3 + 2*x) / (3 - 2*x), 4)
        b = (x + 1) / (x - 1)
        c = (3 + x + R(5,2) + R(125,4))/2
        assert a == b
        assert a == c
        assert b == c
        a = R(R(28,3) - R(27,3), 2)
        b = (R(98,3) - R(28,3) - 1)/3
        assert a == b

    def test_sage_examples(self):
        # from the sage qqbar docs
        rt17 = alg(17).sqrt()
        rt2 = alg(2).sqrt()
        eps = (17 + rt17).sqrt()
        epss = (17 - rt17).sqrt()
        delta = rt17 - 1
        alpha = (34 + 6*rt17 + rt2*delta*epss - 8*rt2*eps).sqrt()
        beta = 2*(17 + 3*rt17 - 2*rt2*eps - rt2*epss).sqrt()
        x = rt2*(15 + rt17 + rt2*(alpha + epss)).sqrt()/8
        y = rt2*(epss**2 - rt2*(alpha + epss)).sqrt()/8
        cx, cy = alg(1), alg(0)
        #for i in range(34):    # slow
        for i in range(3):
            cx, cy = x*cx-y*cy, x*cy+y*cx
        ax = fmpz_poly([0,1])
        x2 = alg.polynomial_roots(256*ax**8 - 128*ax**7 - 448*ax**6 + 192*ax**5 + 240*ax**4 - 80*ax**3 - 40*ax**2 + 8*ax + 1)[0][0]
        y2 = (1-x2**2).sqrt()
        assert x == x2
        assert y == y2

    def test_sage_examples_slow(self):
        if 0:
            x = fmpz_poly([0,1])
            pol = x**10 + x**9 - x**7 - x**6 - x**5 - x**4 - x**3 + x + 1
            root = arb("[1.17628081825991751 +/- 3.46e-18]")
            alpha = alg(_minpoly=pol, _enclosure=root)
            lhs = alpha**630 - 1
            rhs_num = (alpha**315 - 1) * (alpha**210 - 1) * (alpha**126 - 1)**2 * (alpha**90 - 1) * (alpha**3 - 1)**3 * (alpha**2 - 1)**5 * (alpha - 1)**3
            rhs_den = (alpha**35 - 1) * (alpha**15 - 1)**2 * (alpha**14 - 1)**2 * (alpha**5 - 1)**6 * alpha**68
            rhs = rhs_num / rhs_den
            assert lhs == rhs

    def test_guess(self):
        assert alg.guess(arb(123)/3789, 1) == alg(123)/3789
        assert alg.guess(arb(5) + acb(2).sqrt()*1j, 2) == alg(5) + alg(2).sqrt() * alg.i()
        assert alg.guess(arb(5)/64 + acb(0,37)/256, 2) == alg(5)/64 + (alg(37)/256) * alg.i()
        orig = ctx.prec
        try:
            ctx.dps = 200
            assert alg.guess(arb(2).root(6) + arb(3).root(5), 30) == alg(2).root(6) + alg(3).root(5)
        finally:
            ctx.prec = orig
        assert alg.guess(arb("3.1415926535897932 +/- 1e-5"), 1, check=False) == alg(22)/7
        assert alg.guess(arb("3.1415926535897932 +/- 1e-8"), 1, check=False) == alg(355)/113

    def test_misc_bugs(self):
        x = ((1/(alg(3).sqrt() + alg(5).sqrt()) + 1).root(3) + 1)**2 + fmpq(1,3)
        x + alg.i()
        u = (x+alg.i()).root(3)

