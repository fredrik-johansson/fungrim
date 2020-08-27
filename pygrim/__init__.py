# -*- coding: utf-8 -*-

from .expr import *
from .brain import *

# this should maybe not be exported, but it's currently
# useful for development
try:
    from flint import *
    from .algebraic import alg, gaussian_integer
    from .values import *
except ImportError:
    pass

def fungrim_entry(id):
    from .formulas import entries_dict
    return entries_dict[id]

def test_fungrim_entry(id, num=100):
    from .formulas import entries_dict
    entry = entries_dict[id]
    formula = entry.get_arg_with_head(Formula)
    if formula is None:
        print("no Formula() in entry")
        return
    formula = formula.args()[0]
    print("Formula: ", formula)
    variables = entry.get_arg_with_head(Variables)
    if variables is None:
        variables = []
    else:
        variables = variables.args()
    assumptions = entry.get_arg_with_head(Assumptions)
    if assumptions is None:
        assumptions = True_
    else:
        # todo: multiple args to Assumptions()
        assumptions = assumptions.args()[0]
    print("Variables: ", variables)
    print("Assumptions: ", assumptions)
    return formula.test(variables, assumptions, num=num)

def test_fungrim(nstart=0, nend=10**9, num=100, filter=None):
    from .formulas import entries_dict
    effective = 0
    ineffective = 0
    truly_effective = 0
    for n, eid in enumerate(sorted(entries_dict)):
        if n >= nstart and n <= nend:
            entry = entries_dict[eid]
            if filter is not None:
                if set(entry.symbols()).isdisjoint(set(filter)):
                    continue
            print("-------------------------------------------------------------------")
            print(eid, n, len(entries_dict))
            info = test_fungrim_entry(eid, num)
            if info is not None:
                if info["Total"] > 0:
                    effective += 1
                else:
                    ineffective += 1
                if info["True"] > 0:
                    truly_effective += 1
    print("Tested", effective, "formulas and", truly_effective, "truly effective; unable to satisfy assumptions for", ineffective, "formulas")

def test():
    import doctest

    print("----------------------------------------------------------")
    print("expr")
    print("----------------------------------------------------------")
    doctest.testmod(expr, verbose=True, raise_on_error=False, optionflags=doctest.ELLIPSIS)
    expr.TestExpr().run()

    print("----------------------------------------------------------")
    print("algebraic")
    print("----------------------------------------------------------")
    doctest.testmod(algebraic, verbose=True, raise_on_error=True, optionflags=doctest.ELLIPSIS)
    algebraic.TestAlgebraic().run()

    print("----------------------------------------------------------")
    print("brain")
    print("----------------------------------------------------------")
    doctest.testmod(brain, verbose=True, raise_on_error=True, optionflags=doctest.ELLIPSIS)
    TestBrain().run()

