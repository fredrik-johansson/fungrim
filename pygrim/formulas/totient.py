# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Totient function"),
    Section("Definitions"),
    Entries(
        "2c46dc",
    ),
    Section("Tables"),
    Entries(
        "6d37c9",
    ),
    Section("Counting"),
    Entries(
        "c19cd6",
    ),
    Section("Factorization"),
    Entries(
        "b9c50f",
        "081abd",
        "cb410e",
        "1d731f",
        "db4763",
        "56d7fe",
        "05e9ae",
        "c0e088",
        "b9c36d",
        "d1ea57",
        "11a56b",
    ),
    Section("Divisibility"),
    Entries(
        "f0639c",
        "eae0de",
        "8f51dd",
    ),
    Subsection("Euler-Fermat theorem"),
    Entries(
        "a68214",
        "36fe36",
    ),
    Section("Sum representations"),
    Entries(
        "3f5711",
        "93a877",
        "efd378",
        "bb4ce0",
        "a08583",
        "08ff0b",
    ),
    Section("Summation"),
    Entries(
        "cdd7e7",
        "90bb4a",
        "0fdb94",
        "a05466",
        "ea27a7",
    ),
    Section("Generating functions"),
    Entries(
        "1a907e",
        "7f5468",
        "a9a405",
    ),
    Section("Asymptotics"),
    Entries(
        "cd7877",
        "acfc1f",
        "4b5b44",
        "33139b",
        "feb1a0",
        "8d7b3d",
        "9923b7",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "e3005f",
        "485ab6",
        "d0b5a7",
        "b81b45",
        "08fb81",
        "775e10",
        "433a5c",
        "86fcf1",
        "acb28a",
        "0477b3",
    ),
)

# Definitions

make_entry(ID("2c46dc"),
    SymbolDefinition(Totient, Totient(n), "Euler totient function"),
    References("http://oeis.org/A000010"))

# Counting

make_entry(ID("c19cd6"),
    Formula(Equal(Totient(n), Cardinality(Set(k, For(k), And(Element(k, ZZBetween(1, n)), Equal(GCD(n,k), 1)))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# Factorization

make_entry(ID("b9c50f"),
    Formula(Equal(Totient(n), n * PrimeProduct(Parentheses(1-1/p), p, Divides(p, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("081abd"),
    Formula(Equal(Totient(2**n), 2**(n-1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("cb410e"),
    Formula(Equal(Totient(p), p - 1)),
    Variables(p),
    Assumptions(Element(p, PP)))

make_entry(ID("1d731f"),
    Formula(Equal(Totient(p**k), p**(k-1) * (p - 1))),
    Variables(p, k),
    Assumptions(And(Element(p, PP), Element(k, ZZGreaterEqual(1)))))

make_entry(ID("db4763"),
    Formula(Implies(Equal(GCD(m,n), 1), Equal(Totient(m*n), Totient(m)*Totient(n)))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("56d7fe"),
    Formula(Equal(Totient(m*n), (Totient(m) * Totient(n) * GCD(m,n) / Totient(GCD(m,n))))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("05e9ae"),
    Formula(Equal(Totient(m**n), m**(n-1) * Totient(m))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("c0e088"),
    Formula(Equal(Totient(2*n), Cases(Tuple(2*Totient(n), Even(n)), Tuple(Totient(n), Odd(n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("b9c36d"),
    Formula(Equal(Totient(Product(Pow(PrimeNumber(k), Subscript(e, k)), For(k, 1, m))),
        Product(Totient(Pow(PrimeNumber(k), Subscript(e, k))), For(k, 1, m)))),
    Variables(e, m),
    Assumptions(And(Element(Subscript(e, k), ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)))))

make_entry(ID("d1ea57"),
    Formula(Equal(Totient(LCM(m,n))*Totient(GCD(m,n)), Totient(m)*Totient(n))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("11a56b"),
    Formula(Equal(Totient(-n), 0)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Divisibility

make_entry(ID("f0639c"),
    Formula(Cases(Tuple(Odd(Totient(n)), Element(n, Set(1, 2))), Tuple(Even(Totient(n)), Otherwise))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("eae0de"),
    Formula(Implies(Divides(m, n), Divides(Totient(m), Totient(n)))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("8f51dd"),
    Formula(Divides(n, Totient(m**n-1))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("a68214"),
    Formula(CongruentMod(Pow(a,Totient(n)), 1, n)),
    Variables(a, n),
    Assumptions(And(Element(a, ZZ), Element(n, ZZGreaterEqual(1)), Equal(GCD(a,n), 1))))

make_entry(ID("36fe36"),
    Formula(Implies(CongruentMod(x, y, Totient(n)), CongruentMod(a**x, a**y, n))),
    Variables(a, x, y, n),
    Assumptions(And(Element(a, ZZ), Element(n, ZZGreaterEqual(1)), Equal(GCD(a,n), 1), Element(x, ZZGreaterEqual(0)), Element(y, ZZGreaterEqual(0)))))

# Sum representations

make_entry(ID("3f5711"),
    Formula(Equal(Totient(n), Sum(GCD(n,k) * Exp(2*ConstPi*ConstI*k/n), For(k, 1, n)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("93a877"),
    Formula(Equal(Totient(n), Sum(GCD(n,k) * Cos(2*ConstPi*k/n), For(k, 1, n)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("efd378"),
    Formula(Equal(Totient(n), DivisorSum(MoebiusMu(d) * (n/d), d, n))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# todo: better markup for this kind of sum
make_entry(ID("bb4ce0"),
    Formula(Equal(Totient(n), (2/n) * Sum(Cases(Tuple(k, Equal(GCD(n,k), 1)), Tuple(0, Otherwise)), For(k, 1, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# todo: better markup for this kind of sum
make_entry(ID("a08583"),
    Formula(Equal(Totient(n) * DivisorSigma(0,n), Sum(Cases(Tuple(GCD(n,k-1), Equal(GCD(n,k), 1)), Tuple(0, Otherwise)), For(k, 1, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))),
    Description("Menon's identity"))

make_entry(ID("08ff0b"),
    Formula(Equal(Totient(n), n - DivisorSum(Totient(d), d, n, Less(d, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Summation

make_entry(ID("cdd7e7"),
    Formula(Equal(DivisorSum(Totient(d), d, n), n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("90bb4a"),
    Formula(Equal(DivisorSum(Totient(d) * d, d, n), Parentheses((2/n) * Sum(LCM(n, k), For(k, 1, n))) - 1)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("0fdb94"),
    Formula(Equal(DivisorSum(Totient(d) * (n / d), d, n), Sum(GCD(n, k), For(k, 1, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("a05466"),
    Formula(Equal(DivisorSum(Totient(d) * DivisorSigma(k, n/d), d, n), n*DivisorSigma(k-1,n))),
    Variables(k, n),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("ea27a7"),
    Formula(Equal(Sum(Totient(k) * Floor(n/k), For(k, 1, n)), (n*(n+1))/2)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))


# Generating functions

make_entry(ID("1a907e"),
    Formula(Equal(Sum(Totient(n) / n**s, For(n, 1, Infinity)), RiemannZeta(s-1) / RiemannZeta(s))),
    Variables(s),
    Assumptions(And(Element(s, CC), Greater(Re(s), 2))))

make_entry(ID("7f5468"),
    Formula(Equal(Sum((Totient(n) * q**n) / (1-q**n), For(n, 1, Infinity)), q/(1-q)**2)),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("a9a405"),
    Formula(Equal(Sum(Totient(n)/n * Log(1-x**n), For(n, 1, Infinity)), x/(x-1))),
    Variables(x),
    Assumptions(And(Element(x, CC), Less(Abs(x), 1))))

# Asymptotics

make_entry(ID("cd7877"),
    Formula(Equal(SequenceLimitSuperior(Totient(n) / n, Var(n), Infinity), 1)))

make_entry(ID("acfc1f"),
    Formula(Equal(SequenceLimitInferior((Totient(n) * Log(Log(n))) / n, Var(n), Infinity), Exp(-ConstGamma))))

make_entry(ID("4b5b44"),
    Formula(Equal(SequenceLimit(Totient(n) / n**(1-delta), Var(n), Infinity), Infinity)),
    Variables(delta),
    Assumptions(Element(delta, OpenInterval(0, Infinity))))

make_entry(ID("33139b"),
    Formula(Equal(SequenceLimitInferior(Totient(n+1) / Totient(n), Var(n), Infinity), 0)))

make_entry(ID("feb1a0"),
    Formula(Equal(SequenceLimitSuperior(Totient(n+1) / Totient(n), Var(n), Infinity), Infinity)))

make_entry(ID("8d7b3d"),
    Formula(Equal(SequenceLimit(1/N**2 * Sum(Totient(n), For(n, 1, N)), Var(N), Infinity), 3/ConstPi**2)))

make_entry(ID("9923b7"),
    Formula(Equal(SequenceLimit(1/Log(N) * Sum(1/Totient(n), For(n, 1, N)), Var(N), Infinity), (RiemannZeta(2)*RiemannZeta(3) / RiemannZeta(6)))))

# Bounds and inequalities

make_entry(ID("e3005f"),
    Formula(LessEqual(Totient(n), n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("485ab6"),
    Formula(LessEqual(Totient(n), n - 1)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(2))))

make_entry(ID("d0b5a7"),
    Formula(GreaterEqual(Totient(n), Sqrt(n))),
    Variables(n),
    Assumptions(Element(n, SetMinus(ZZGreaterEqual(7)))))

make_entry(ID("b81b45"),
    Formula(Implies(NotElement(n, PP), LessEqual(Totient(n), n - Sqrt(n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(2))))

make_entry(ID("08fb81"),
    Formula(LessEqual(Totient(m*n), m*Totient(n))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("775e10"),
    Formula(LessEqual(Totient(m)*Totient(n), Totient(m*n))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(0)), Element(n, ZZGreaterEqual(0)))))

# ref: Rosser and Schoenfeld
make_entry(ID("433a5c"),
    Formula(Greater(Totient(n), n / (Exp(ConstGamma) * Log(Log(n)) + Decimal("2.50637")/Log(Log(n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(3))))

make_entry(ID("86fcf1"),
    Formula(Equal(Cardinality(Set(n, For(n), And(Element(n, ZZGreaterEqual(1)), Less(Totient(n), n / (Exp(ConstGamma) * Log(Log(n))))))), Cardinality(ZZ))))

make_entry(ID("acb28a"),
    Formula(Less(Totient(n) * DivisorSigma(1, n), n**2)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(2))),
    References("G. H. Hardy and E. M. Wright (1979), An Introduction to the Theory of Numbers (Fifth ed.), Oxford University Press. Theorem 327."))

make_entry(ID("0477b3"),
    Formula(Greater(Totient(n) * DivisorSigma(1, n), (6/ConstPi**2) * n**2)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))),
    References("G. H. Hardy and E. M. Wright (1979), An Introduction to the Theory of Numbers (Fifth ed.), Oxford University Press. Theorem 327."))



# Tables

make_entry(ID("6d37c9"),
    Description("Table of", Totient(n), "for", LessEqual(0, n, 100)),
    Table(
      Var(n),
      TableValueHeadings(n, Totient(n)),
      TableSplit(5),
      List(
    Tuple(0, 0),
    Tuple(1, 1),
    Tuple(2, 1),
    Tuple(3, 2),
    Tuple(4, 2),
    Tuple(5, 4),
    Tuple(6, 2),
    Tuple(7, 6),
    Tuple(8, 4),
    Tuple(9, 6),
    Tuple(10, 4),
    Tuple(11, 10),
    Tuple(12, 4),
    Tuple(13, 12),
    Tuple(14, 6),
    Tuple(15, 8),
    Tuple(16, 8),
    Tuple(17, 16),
    Tuple(18, 6),
    Tuple(19, 18),
    Tuple(20, 8),
    Tuple(21, 12),
    Tuple(22, 10),
    Tuple(23, 22),
    Tuple(24, 8),
    Tuple(25, 20),
    Tuple(26, 12),
    Tuple(27, 18),
    Tuple(28, 12),
    Tuple(29, 28),
    Tuple(30, 8),
    Tuple(31, 30),
    Tuple(32, 16),
    Tuple(33, 20),
    Tuple(34, 16),
    Tuple(35, 24),
    Tuple(36, 12),
    Tuple(37, 36),
    Tuple(38, 18),
    Tuple(39, 24),
    Tuple(40, 16),
    Tuple(41, 40),
    Tuple(42, 12),
    Tuple(43, 42),
    Tuple(44, 20),
    Tuple(45, 24),
    Tuple(46, 22),
    Tuple(47, 46),
    Tuple(48, 16),
    Tuple(49, 42),
    Tuple(50, 20),
    Tuple(51, 32),
    Tuple(52, 24),
    Tuple(53, 52),
    Tuple(54, 18),
    Tuple(55, 40),
    Tuple(56, 24),
    Tuple(57, 36),
    Tuple(58, 28),
    Tuple(59, 58),
    Tuple(60, 16),
    Tuple(61, 60),
    Tuple(62, 30),
    Tuple(63, 36),
    Tuple(64, 32),
    Tuple(65, 48),
    Tuple(66, 20),
    Tuple(67, 66),
    Tuple(68, 32),
    Tuple(69, 44),
    Tuple(70, 24),
    Tuple(71, 70),
    Tuple(72, 24),
    Tuple(73, 72),
    Tuple(74, 36),
    Tuple(75, 40),
    Tuple(76, 36),
    Tuple(77, 60),
    Tuple(78, 24),
    Tuple(79, 78),
    Tuple(80, 32),
    Tuple(81, 54),
    Tuple(82, 40),
    Tuple(83, 82),
    Tuple(84, 24),
    Tuple(85, 64),
    Tuple(86, 42),
    Tuple(87, 56),
    Tuple(88, 40),
    Tuple(89, 88),
    Tuple(90, 24),
    Tuple(91, 72),
    Tuple(92, 44),
    Tuple(93, 60),
    Tuple(94, 46),
    Tuple(95, 72),
    Tuple(96, 32),
    Tuple(97, 96),
    Tuple(98, 42),
    Tuple(99, 60),
    Tuple(100, 40),
    )))

