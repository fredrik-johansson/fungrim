from flint import *

"""
wishlist:
- factoring
- evaluate at nmod
- evaluate at fmpq

"""

def _canonicalise(p, q):
    g = p.gcd(q)
    if not g.is_one():
        p //= g
        q //= g
    if q.leading_coefficient() < 0:
        p = -p
        q = -q
    return p, q

'''
class fmpz_mpoly_factored:

    def __init__(self, factors):
        if isinstance(factors, fmpz_mpoly_factored):
            self.factors = factors.factors
        elif isinstance(factors, (int, fmpz)):
            if factors == 1:
                self.factors = []
            else:
                self.factors = [(fmpz_mpoly(factors), 1)]
        elif isinstance(factors, fmpz_mpoly):
            if factors == 1:
                self.factors = []
            else:
                self.factors = [(factors, 1)]

    def __repr__(self):
        return repr(self.factors)

    def gcd_fmpz_mpoly(self, poly):
        g = []
        for fac, exp in self.factors:
            div_exp = 0
            while 1:
                fac_gcd = fac.gcd(poly)
                if fac_gcd != 1:
                    poly //= fac_gcd
'''

class fmpz_mpoly_q:

    def __init__(self, p, q=None, canonicalise=True):
        if isinstance(p, fmpz_mpoly_q):
            assert q is None
            p, q = p.p, p.q
        else:
            if not isinstance(p, fmpz_mpoly):
                p = fmpz_mpoly(p)
            if q is None:
                q = fmpz_mpoly(1)
            elif not isinstance(q, fmpz_mpoly):
                q = fmpz_mpoly(q)
            if canonicalise:
                p, q = _canonicalise(p, q)
        self.p = p
        self.q = q

    @staticmethod
    def gens(n):
        gens = fmpz_mpoly.gens(n)
        return tuple(fmpz_mpoly_q(x) for x in gens)

    def __repr__(self):
        return "(" + str(self.p) + ") / (" + str(self.q) + ")"

    def __eq__(self, other):
        self = fmpz_mpoly_q(self)
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        return ap*bq - bp*bq == 0

    def __ne__(self, other):
        return False

    def __neg__(self):
        return fmpz_mpoly_q(-self.p, self.q, canonicalise=False)

    def __add__(self, other):
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        return fmpz_mpoly_q._add(ap, aq, bp, bq)

    def __radd__(self, other):
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        return fmpz_mpoly_q._add(ap, aq, bp, bq)

    def __sub__(self, other):
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        return fmpz_mpoly_q._add(ap, aq, -bp, bq)

    def __rsub__(self, other):
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        return fmpz_mpoly_q._add(-ap, aq, bp, bq)

    def __mul__(self, other):
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        return fmpz_mpoly_q._mul(ap, aq, bp, bq)

    def __rmul__(self, other):
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        return fmpz_mpoly_q._mul(ap, aq, bp, bq)

    @staticmethod
    def _add(ap, aq, bp, bq):
        if aq == bq:
            x = ap + bp
            if not aq.is_one():
                t = x.gcd(aq)
                if not t.is_one():
                    x //= t
                    aq //= t
            return fmpz_mpoly_q(x, aq, canonicalise=False)
        if aq.is_one():
            return fmpz_mpoly_q(ap*bq + bp, bq, canonicalise=False)
        if bq.is_one():
            return fmpz_mpoly_q(bp*aq + ap, aq, canonicalise=False)
        t = aq.gcd(bq)
        if t.is_one():
            return fmpz_mpoly_q(ap*bq + bp*aq, aq*bq, canonicalise=False)
        a = aq // t
        b = bq // t
        x = ap*b + bp*a
        u = x.gcd(t)
        if u.is_one():
            y = aq * b
        else:
            x //= u
            y = (aq // u) * b
        return fmpz_mpoly_q(x, y, canonicalise=False)


    @staticmethod
    def _mul(ap, aq, bp, bq):
        if aq == bq:
            return fmpz_mpoly_q(ap * bp, aq * bq, canonicalise=False)
        if aq.is_one():
            # ap*(bp/bq)
            t = ap.gcd(bq)
            if t.is_one():
                return fmpz_mpoly_q(ap*bp, bq, canonicalise=False)
            else:
                return fmpz_mpoly_q((ap//t)*bp, bq//t, canonicalise=False)
        if bq.is_one():
            # (ap/aq)*bp
            t = bp.gcd(aq)
            if t.is_one():
                return fmpz_mpoly_q(ap*bp, aq, canonicalise=False)
            else:
                return fmpz_mpoly_q(ap*(bp//t), aq//t, canonicalise=False)
        t = ap.gcd(bq)
        u = bp.gcd(aq)
        if t.is_one():
            ap //= t
            bq //= t
        if u.is_one():
            bp //= u
            aq //= u
        return fmpz_mpoly_q(ap*bp, aq*bq, canonicalise=False)

    def __div__(self, other):
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        if not bp:
            raise ZeroDivisionError
        return fmpz_mpoly_q._mul(ap, aq, bq, bp)

    def __rdiv__(self, other):
        other = fmpz_mpoly_q(other)
        ap = self.p
        aq = self.q
        bp = other.p
        bq = other.q
        if not ap:
            raise ZeroDivisionError
        return fmpz_mpoly_q._mul(aq, ap, bp, bq)

    __truediv__ = __div__
    __rtruediv__ = __rdiv__

    def __pow__(self, other):
        other = int(other)
        ap = self.p
        aq = self.q
        if other < 0:
            if not ap:
                raise ZeroDivisionError
            ap, aq = aq, ap
            other = -other
        ap **= other
        aq **= other
        return fmpz_mpoly_q(ap, aq, canonicalise=False)

"""
from pygrim import *
from pygrim.multivariate import *
x, y, z = fmpz_mpoly_q.gens(3)
(x+1)*(x-1)


"""

