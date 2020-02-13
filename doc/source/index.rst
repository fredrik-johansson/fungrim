.. pygrim documentation master file, created by
   sphinx-quickstart on Tue Feb 11 14:15:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pygrim
==================================

**Pygrim** is a Python library for working with symbolic mathematical expressions.

It is used to develop the Mathematical Functions Grimoire (Fungrim): http://fungrim.org/

The source repository is: https://github.com/fredrik-johansson/fungrim

Features
--------

* Uses Grim expressions (http://fungrim.org/grim/)
  to represent mathematical formulas and theorems semantically
* Conversion from symbolic expressions to LaTeX
* Code for building the Fungrim website
* Access to the Fungrim formula database from Python
* Symbolic computation (evaluation/simplification of expressions)
* Numerical evaluation of expressions

Module documentation
--------------------

.. toctree::
    :maxdepth: 3
    :caption: Contents:

    expr.rst
    brain.rst
    algebraic.rst

Dependencies
-----------------------------

For building the Fungrim website:

* `node.js <https://nodejs.org/>`_
* `KaTeX <https://www.npmjs.com/package/katex>`_

For building the image files on the Fungrim website:

* `Matplotlib <https://matplotlib.org/>`_
* `mpmath <http://mpmath.org/>`_
* `Python-FLINT <https://github.com/fredrik-johansson/python-flint>`_ and its dependencies (GMP, MPFR, FLINT, Arb)

For symbolic computation:

* `Python-FLINT <https://github.com/fredrik-johansson/python-flint>`_ and its dependencies (GMP, MPFR, FLINT, Arb)

Note: right now, Pygrim requires a git checkout of FLINT and a checkout of the development branch of Python-FLINT

Building the Fungrim website
----------------------------

Run ``python3 fungrim.py`` in the root directory of the ``fungrim`` source repository, and the grimoire will appear in ``build/html/index.html``.

The first build may take several minutes (due to starting ``node.js`` thousands of times to run KaTeX for each formula), but subsequent rebuilds should be fast since this data is cached.

Run ``python fungrim.py img`` to build the image files.

Indices
-------

* :ref:`genindex`

