# Fungrim

Is it a reference book? Is it a computer algebra system? No, it's the Mathematical Functions Grimoire! 

Early view at https://fungrim.org/

## Dependencies

* [node.js](https://nodejs.org/)
* [KaTeX](https://www.npmjs.com/package/katex)

## Usage

Just run `python fungrim.py`, and the grimoire will appear in `build/html/index.html`.

## Todo

* More formulas!
* Website up and running
* Content pages to browse the formulas in a structured way (e.g. function category -> function -> formula type...) -- maybe want a combination of hand-compiled pages and automatically generated index pages
* Definition entries for all builtin functions and symbols
* Domain and codomain definitions for functions (may be multiple)
* Other basic function properties: symmetries, holomorphicity, zeros and poles, branch points and branch cuts
* Complete and improve the TeX output
* Hyperlinked function definitions in the detailed view
* Review and freeze the core language / builtin function names (after adding many more formulas to get a feel for what looks good)
* Print S-expressions as a(b, c) or (a, b, c)?
* Improve look and usability of the pages
* Table (and plot?) entries in addition to regular formula entries
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
