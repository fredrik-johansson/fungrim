from .expr import *

def grim_to_sympy(expr, **kwargs):
    import sympy
    assert isinstance(expr, Expr)
    if expr.is_integer():
        return sympy.sympify(int(expr))
    if expr.is_symbol():
        if expr == Pi:
            return sympy.pi
        if expr == ConstI:
            return sympy.I
        if expr == ConstE:
            return sympy.E
        return sympy.Symbol(str(expr))
    head = expr.head()
    args = [grim_to_sympy(x, **kwargs) for x in expr.args()]
    if head in (Pos, Parentheses, Brackets, Braces, AngleBrackets, Logic):
        x, = args
        return x
    if expr.head() == Add:
        return sympy.Add(*args)
    if expr.head() == Mul:
        return sympy.Mul(*args)
    if expr.head() == Neg:
        x, = args
        return -x
    if expr.head() == Sub:
        a, b = args
        return a - b
    if expr.head() == Div:
        p, q = args
        return p / q
    if expr.head() == Pow:
        b, e = args
        return b ** e
    if expr.head() == Sqrt:
        x, = args
        return sympy.sqrt(x)
    raise NotImplementedError("converting %s to SymPy", expr.head())

def sympy_to_grim(expr, **kwargs):
    import sympy
    assert isinstance(expr, sympy.Expr)
    if expr.is_Integer:
        return Expr(int(expr))
    if expr.is_Symbol:
        return Expr(symbol_name=expr.name)
    if expr is sympy.pi:
        return Pi
    if expr is sympy.E:
        return ConstE
    if expr is sympy.I:
        return ConstI
    if expr.is_Add:
        args = [sympy_to_grim(x, **kwargs) for x in expr.args]
        return Add(*args)
    if expr.is_Mul:
        args = [sympy_to_grim(x, **kwargs) for x in expr.args]
        return Mul(*args)
    if expr.is_Pow:
        args = [sympy_to_grim(x, **kwargs) for x in expr.args]
        b, e = args
        return Pow(b, e)
    raise NotImplementedError("converting %s to Grim", type(expr))

