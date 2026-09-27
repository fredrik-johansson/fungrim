"""Unit tests for walker atoms / numbers / unknown-head hard error."""

import pytest


def _walk(e):
    from grim2mathjson import walker
    ctx = walker.Ctx()
    return walker.walk(e, ctx), ctx


def test_small_integer():
    from pygrim import expr as pg
    out, _ = _walk(pg.Expr(42))
    assert out == 42
    out, _ = _walk(pg.Expr(-(2**53) + 1))
    assert out == -(2**53) + 1


def test_big_integer_num_object():
    from pygrim import expr as pg
    big = 2**80
    out, _ = _walk(pg.Expr(big))
    assert out == {"num": str(big)}


def test_decimal_literal():
    from pygrim import expr as pg
    out, _ = _walk(pg.Decimal("2.50662827463100050241576528481"))
    assert out == {"num": "2.50662827463100050241576528481"}


def test_constants_and_sets():
    from pygrim import expr as pg
    assert _walk(pg.Pi)[0] == "Pi"
    assert _walk(pg.ConstI)[0] == "ImaginaryUnit"
    assert _walk(pg.Infinity)[0] == "PositiveInfinity"
    assert _walk(pg.Neg(pg.Infinity))[0] == "NegativeInfinity"
    assert _walk(pg.UnsignedInfinity)[0] == "ComplexInfinity"
    assert _walk(pg.Undefined)[0] == "NaN"
    assert _walk(pg.CC)[0] == "ComplexNumbers"
    assert _walk(pg.PP)[0] == "Primes"


def test_variable_collision_renames():
    from pygrim import expr as pg
    # "i" and "e" are CE constants (ImaginaryUnit / ExponentialE aliases):
    # they must be renamed when used as Fungrim variables.
    assert _walk(pg.Expr(symbol_name="i"))[0] == "i_var"
    assert _walk(pg.Expr(symbol_name="e"))[0] == "e_var"
    assert _walk(pg.Expr(symbol_name="pi"))[0] == "pi"  # not a CE symbol


def test_unknown_head_is_hard_error():
    from pygrim import expr as pg
    from grim2mathjson import walker
    ctx = walker.Ctx()
    # "Universe" is a pygrim builtin deliberately absent from every table.
    with pytest.raises(walker.UnknownHeadError):
        walker.walk(pg.Universe, ctx)
    with pytest.raises(walker.UnknownHeadError):
        walker.walk(pg.Universe(pg.Expr(1)), ctx)


def test_skip_heads_raise_translation_skip():
    from pygrim import expr as pg
    from grim2mathjson import walker
    ctx = walker.Ctx()
    with pytest.raises(walker.TranslationSkip) as exc:
        walker.walk(pg.Repeat(pg.Expr(symbol_name="x"), pg.Expr(3)), ctx)
    assert exc.value.reason == "repeat-splice"


def test_family_call_form():
    from pygrim import expr as pg
    z_ = pg.Expr(symbol_name="z_")
    k = pg.Expr(symbol_name="k")
    out, ctx = _walk(z_(k))
    assert out == ["z_", "k"]
    assert "z_" in ctx.indexed_families


def test_subscript_literal_fuses_symbolic_calls():
    from pygrim import expr as pg
    a = pg.Expr(symbol_name="a")
    k = pg.Expr(symbol_name="k")
    assert _walk(pg.Subscript(a, pg.Expr(1)))[0] == "a_1"
    out, ctx = _walk(pg.Subscript(a, k))
    assert out == ["a_", "k"]
    assert "a_" in ctx.indexed_families


def test_directed_infinity_flag():
    from pygrim import expr as pg
    out, ctx = _walk(pg.Mul(pg.ConstI, pg.Infinity))
    assert out == ["Multiply", "ImaginaryUnit", "PositiveInfinity"]
    assert ctx.directed_infinity is True


def test_digamma_polygamma_order():
    from pygrim import expr as pg
    z = pg.Expr(symbol_name="z")
    # 1-arg: plain digamma
    out, ctx = _walk(pg.DigammaFunction(z))
    assert out == ["Digamma", "z"]
    # explicit order 0 folds to the 1-arg form
    out, _ = _walk(pg.DigammaFunction(z, pg.Expr(0)))
    assert out == ["Digamma", "z"]
    # order m != 0 -> CE PolyGamma, order FIRST
    out, ctx = _walk(pg.DigammaFunction(z, pg.Expr(1)))
    assert out == ["PolyGamma", 1, "z"]
    assert "PolyGamma" in ctx.heads
    m = pg.Expr(symbol_name="m")
    out, _ = _walk(pg.DigammaFunction(z, m))
    assert out == ["PolyGamma", "m", "z"]
