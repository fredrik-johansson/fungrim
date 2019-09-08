# Fungrim

Possible taglines:

* Is it a reference book? Is it a computer algebra system? No, it's the Mathematical Functions Grimoire! 
* Enabling open sourcery in mathematics

Early view at http://fungrim.org/

## Dependencies

* [node.js](https://nodejs.org/)
* [KaTeX](https://www.npmjs.com/package/katex)

## Usage

### Building the website

Just run `python fungrim.py`, and the grimoire will appear in `build/html/index.html`.

The first build may take several minutes (due to starting node.js thousands of times to run KaTeX for each formula), but subsequent rebuilds should be fast since this data is cached.

Run `python fungrim.py img` to build the image files (requires `matplotlib`, `mpmath` and `python-flint`).

### Using the Python library

Run `python setup.py install` to install the `pygrim` Python library. This is the symbolic library used to build the Fungrim website. As currently implemented, all formulas are part of the library (but built data such as images are not).

    >>> import pygrim
    >>> pygrim.Equal
    Equal
    >>> pygrim.ConstPi
    ConstPi
    >>> pygrim.Equal(pygrim.ConstPi - pygrim.ConstPi, 0)
    Equal(Sub(ConstPi, ConstPi), 0)
    >>> import pygrim.formulas
    >>> e = pygrim.formulas.entries_dict["590136"]
    >>> e
    Entry(ID("590136"),
        Formula(Equal(ConstPi, Neg(Mul(ConstI, Log(-1))))))
    >>> e.args()[1].args()[0].head()
    Equal
    >>> e.args()[1].args()[0].args()
    (ConstPi, Neg(Mul(ConstI, Log(-1))))

The Python library is a work in progress and the API will certainly change.

## What is the Mathematical Functions Grimoire (Fungrim)?

A *grimoire* is a book of magic formulas. Formulas for [special functions](https://en.wikipedia.org/wiki/Special_functions) are essentially magic incantations useful to mathematicians and mathematical scientists.

Fungrim is meant to work both as an encyclopedia for human readers and as a computational tool. Unlike a traditional text-based reference work such as the [DLMF](https://dlmf.nist.gov/), all formulas are available in a semantic, compute-friendly S-expression format.

Fungrim provides a computer-readable database of knowledge about mathematical functions, separate from other features of computer algebra systems. Such a database could be used for code generation or could be imported into computer algebra systems at runtime, instead of implementing the same knowledge about mathematical functions in an ad-hoc way in each system. Less ambitiously, Fungrim could be used for testing existing mathematical software.

Fungrim is inspired by Wolfram Mathematica and the [Wolfram Functions site](http://functions.wolfram.com/), but does not use the Wolfram language. Unlike both the DLMF and the Wolfram projects, Fungrim is an open source community project.

### Structure of the library

Each entry (formula) in Fungrim is assigned a permanent identifier, currently in the form of a random 6-digit hexadecimal string. By design, the identifiers are nondescript and the Fungrim database is conceptually just a flat list of all the entries so that many separate categorizations of the entries are possible. Index pages are currently written by hand; this should be complemented by automatically generated index pages in the future. Entries in Fungrim will citable by a permanent URL. **Note that because this is a pre-alpha version, URLs are not yet final.**

### Strict assumptions

An intended feature of Fungrim is that all formulas will be accompanied by explicit sufficient conditions of validity for the functions and variables. Under the stated assumptions, all functions occurring in a formula should be total functions and variable substitution should be valid through all sub-expressions, including possible corner cases. This is to minimize ambiguity about real versus complex (or even p-adic, noncommutative...) variables, infinities, removable singularities, limits, branch cuts, and the like. It is in contrast to most computer algebra systems which have poorly-specified or self-inconsistent substitution rules and default assumptions, and in contrast to traditional reference works which often make the context implicit or leave out conditions altogether.

### What Fungrim is not

Fungrim is not an attempt to encode arbitrary mathematical knowledge. It focuses on (but is not strictly limited to) special function identities in classical analysis, and it focuses on formulas that are useful for symbolic or numerical computational applications. The scope may be expanded in the future if this approach turns out to be fruitful. For example, it could provide more general coverage of differential equations and functional analysis.

Fungrim is not a collection of formally proved (computer-certified) mathematics (like [Metamath](https://en.wikipedia.org/wiki/Metamath)), nor a research project into computational foundations of mathematics or a project to generate formulas automatically from first principles (like the [DDMF](http://ddmf.msr-inria.inria.fr)). It is simply a library of useful formulas compiled by hand, although some amount of computer generation may be involved behind the scenes. The drawback of automatic and computer-certified approaches is that the mathematical content that can be derived by such methods currently is very limited compared to the existing informal mathematical literature, and the presentation also typically suffers. Naturally, it would be terrific if the Fungrim library could be integrated in some way with formal proof software in the future.

### Formula language

The formula language is still being developed as more formulas are added, and it will probably be revised significantly before a stable version of Fungrim is available.

Fungrim formulas are encoded in a custom symbolic language essentially just consisting of raw S-expressions together with a vocabulary of builtin symbol names for common mathematical concepts. By default, S-expressions are printed in function-call notation; for example, the S-expression for `3x+5` which might be written as `(+ (* 3 x) 5)` in Lisp notation is printed as
`Add(Mul(3, x), 5)`. The specifics are not too important since formulas are easy to convert to any other symbolic language (Mathematica, Maple, SymPy, etc.). In the future, functionality to export formulas to different languages could be added. The database itself currently consists of Python scripts that generate the formulas, but it will probably be converted to a pure declarative format in the near future.

Unlike most computer algebra systems, there is no notion of automatic simplification or canonical form built into the Fungrim formula language. Most computer algebra systems automatically flatten nested associative arithmetic operations, rewrite `x / y` as `x y^{-1}`, reorder commuting terms lexicographically, etc., and when such rewriting is undesirable, it must be overridden manually by the user. We avoid imposing any canonical forms to keep the formula language simple to understand and implement, and to maintain flexibility, deferring design choices related to term rewriting to higher-level applications.

## Todo

* More formulas!
* Definition entries for all builtin functions and symbols
* Domain and codomain definitions for functions (may be multiple)
* Complete and improve the TeX output
* Hyperlinked function definitions in the detailed view
* Review and freeze the core language / builtin function names (after adding many more formulas to get a feel for what looks good)
* Print S-expressions as a(b, c) or (a, b, c)?
* Improve look and usability of the pages
* Plot entries?
* More metadata for entries?
* Change database from Python code to a purely declarative format (for formula development, have a function that converts Python-built expression -> database entry source code)
* Partial rebuilds
* Batch invoke KaTeX (even with cache, first build is slooooooow)
* Functionality to search formulas
* Functionality to export to SymPy, etc.
* Dynamic web application with search etc.
* Automatic "type-checking" of formulas (match assumptions and function signatures)
* Applications using the library for simplification, code generation, ...
* Automatic numerical testing
* More ideas for this list

