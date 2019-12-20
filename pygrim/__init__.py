# -*- coding: utf-8 -*-

from .expr import *

def test():
    from .simplification import TestSimplification
    TestSimplification().run()

