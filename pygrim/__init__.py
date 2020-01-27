# -*- coding: utf-8 -*-

from .expr import *
from .brain import *

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
    formula.test(variables, assumptions, num=num)

def test():
    TestBrain().run()

