# -*- coding: utf-8 -*-

import sys
if len(sys.argv) > 1 and sys.argv[1] == "ids":
    import random
    prev, prev2 = "x", "y"
    for n in range(15):
        while 1:
            s = "".join(random.choice("0123456789abcdef") for i in range(6))
            if s[0] not in (prev[0], prev2[0]):
                print(s)
                prev, prev2 = s, prev
                break
    sys.exit(0)

if len(sys.argv) > 1 and sys.argv[1] == "img":
    import os
    if not os.path.exists("build/html/img"):
        os.makedirs("build/html/img")
    import source_scripts.xray
    source_scripts.xray.plots("build/html/img")
    sys.exit(0)

ordner_ = None
if len(sys.argv) > 1 and sys.argv[1] == "ordner":
    import pygrim
    import pygrim.formulas
    import pickle
    import os
    print("building Ordner...")
    from pygrim.ordner import Ordner
    ordner = Ordner()
    ordner.build(pygrim.all_entries)
    if not os.path.exists("build"):
        os.makedirs("build")
    with open("build/ordner.pickle", "wb") as fp:
        pickle.dump(ordner, fp, protocol=pickle.HIGHEST_PROTOCOL)
    print("success!")
    sys.exit(0)

try:
    import pickle
    with open("build/ordner.pickle", "rb") as fp:
        ordner_ = pickle.load(fp, encoding="utf-8")
except FileNotFoundError:
    print("Ordner database not found -- skipping ordner output")

    # ordner.html()
    # sys.exit(0)

from pygrim import *
from pygrim.formulas import *

topics_referencing_entry = {}
entries_referencing_symbol = {}
all_used_symbols = set()

for entry in all_entries:
    for symbol in entry.symbols(unique=True):
        all_used_symbols.add(symbol)
        if symbol in entries_referencing_symbol:
            entries_referencing_symbol[symbol].add(entry.id())
        else:
            entries_referencing_symbol[symbol] = set([entry.id()])

topics_referencing_symbol = {}

for topic in all_topics:
    title = topic.title()
    for arg in topic.args():
        if arg.head() is Entries:
            for id in arg.args():
                entry = entries_dict[id._text]
                if id._text in topics_referencing_entry:
                    topics_referencing_entry[id._text].append(title)
                else:
                    topics_referencing_entry[id._text] = [title]
                for symbol in entry.symbols(unique=True):
                    if symbol not in topics_referencing_symbol:
                        topics_referencing_symbol[symbol] = {title:0}
                    if title not in topics_referencing_symbol[symbol]:
                        topics_referencing_symbol[symbol][title] = 1
                    else:
                        topics_referencing_symbol[symbol][title] += 1

import os
if not os.path.exists("build"):
    os.makedirs("build")
if not os.path.exists("build/html"):
    os.makedirs("build/html")
if not os.path.exists("build/html/entry"):
    os.makedirs("build/html/entry")
if not os.path.exists("build/html/topic"):
    os.makedirs("build/html/topic")
if not os.path.exists("build/html/symbol"):
    os.makedirs("build/html/symbol")
if not os.path.exists("build/html/ordner"):
    os.makedirs("build/html/ordner")

from shutil import copyfile
copyfile("favicon.png", "build/html/favicon.png")
copyfile("fungrim.svg", "build/html/fungrim.svg")


import pickle
katex_cache = {}

import subprocess

try:
    with open("build/katex_cache.pickle", "rb") as fp:
        katex_cache = pickle.load(fp)
except UnicodeDecodeError as e:
    with open("build/katex_cache.pickle", "rb") as fp:
        katex_cache = pickle.load(fp, encoding="utf-8")
except (IOError, ValueError):
    print("Unable to read katex_cache")

def katex(string, display=True):
    if (string, display) in katex_cache:
        return katex_cache[(string, display)]
    s = subprocess.check_output(["node", "katex.js",
                                 {True:"display",False:"inline"}[display], string],
                                universal_newlines=True)
    katex_cache[(string, display)] = s
    return s

katex_function.append(katex)

import datetime
datestamp = str(datetime.date.today())
timestamp = str(datetime.datetime.utcnow())

html_start = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>%%PAGETITLE%%</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.css" integrity="sha384-yFRtMMDnQtDRO8rLpMIKrtPCD5jdktao2TV19YiZYWMDkUR5GQZR/NOVTdquEx1j" crossorigin="anonymous">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style type="text/css">
body { margin: 0; padding: 0; font-family: roboto, arial, sans-serif; background-color:#eee; color:#111; }
h1 { text-align:center; color:#256; margin-top: 0; }
h2, h3 { text-align: center; margin-bottom: 0.5em; margin-top: 0.7em; }
h3 { font-size: 1em; font-weight: bold; color:#333; }
 a:link { text-decoration: none; }
 a:visited { text-decoration: none; }
 a:hover { text-decoration: underline; }
 a:active { color:#f60; text-decoration: underline; }
p { line-height:1.3em; }
pre { white-space: pre-wrap; background-color: #ffffff; border: 1px solid #cccccc; padding: 0.5em; margin: 0.1em; }
.entry { border:1px solid #ccc; padding-left:0.2em; padding-right:0.2em; padding-top:0em; padding-bottom:0em; margin-left:0; margin-right:0; margin-bottom:0.3em; background-color: #fff; overflow: hidden; border-radius: 3px; box-shadow: 0px 1px 1px #eee; }
.entrysubhead { font-weight: bold; padding-bottom: 0.1em; padding-top: 0.6em; }
table { border-collapse:collapse; background-color:#fff; }
table, th, td { border: 1px solid #aaa; }
th, td { padding:0.2em; }
td { min-width: 30px; }
th { background-color: #f0f0f0; }
tr:nth-child(odd) { background-color: #fafafa; }
.topiclist { columns: 2 300px; }
.katex { font-size: 1.1em; color: black; }
.katex-display { margin-top:0.0em; margin-bottom:0.0em; padding-top:0.5em; padding-bottom:0.4em; }

@media only screen and (max-width: 500px) {
    .katex { font-size: 1.0em; }
}

.katex-display {
   overflow-x: visible;
   overflow-y: hidden;
}

button {
  cursor:pointer;
  border: none;
  color: #000;
  padding: 0.1em 0.3em;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin: 2px 2px;
  border: 1px solid #999;
  border-radius: 2px;
  background-image: linear-gradient(#fff, #eee);
}
button::-moz-focus-inner {
  border: 0;
}
button:active {
  background-image: linear-gradient(#ccc, #888);
  color: #fff;
  padding: 0.1em 0.3em 0.2em 0.3em;
}
button:focus {
  box-shadow: 0px 0px 2px green;
}

@media print { button { display: none !important; } }
}
</style>
<script type='text/javascript'>
function toggleVisible(id) {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 
function toggleBig(id, smallurl, bigurl) {
  var x = document.getElementById(id);
  if (x.style.width == "140px")
  {
    x.src = bigurl;
    x.style.width = "500px";
  }
  else
  {
    x.src = smallurl;
    x.style.width = "140px";
  }
}
</script>
<link rel="icon" type="image/png" href="/favicon.png">

<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> 
</head>
<body>
<div style="margin:0; padding:0.1em 0.5em 0.5em 0.5em; background-color: #fcfcfc;">
"""

html_end = """
</div>
<div style="margin: 0; padding: 0.5em; border-top: 1px solid #ddd; font-size:85%">
<div style="margin:0;">
<p style="text-align:center">Copyright (C) <a href="http://fredrikj.net">Fredrik Johansson</a> and <a href="https://github.com/fredrik-johansson/fungrim/graphs/contributors">contributors</a>.
Fungrim is provided under the
<a href="https://github.com/fredrik-johansson/fungrim/blob/master/LICENSE">MIT license</a>.
The <a href="https://github.com/fredrik-johansson/fungrim">source code is on GitHub</a>.
</p></div>
<p style="text-align:center">%%TIMESTAMP%% UTC</p>
</div>
</body>
</html>
"""

html_end = html_end.replace("%%TIMESTAMP%%", timestamp)

index_text = """
<h1 style="margin-top:0.3em; margin-bottom:0.35em">The Mathematical Functions Grimoire</h1>
<div style="text-align:center">
<img src="fungrim.svg" alt="Fungrim logo" style="width:140px; height:140px;" />
</div>

<p style="margin:0.6em 1em 1em 1em; font-size:0.9em">
Welcome! The Mathematical Functions Grimoire (<i>Fungrim</i>) is an open source library of formulas and data for special functions.
Fungrim currently consists of %%NUMSYMBOLS%% <i>symbols</i> (named mathematical objects), %%NUMENTRIES%% <i>entries</i> (definitions, formulas, tables, plots), and %%NUMTOPICS%% <i>topics</i> (listings of entries).
This is one example entry:
</p>
"""

len(all_builtins)

index_text = index_text.replace("%%NUMSYMBOLS%%", str(len(all_builtins)))
index_text = index_text.replace("%%NUMENTRIES%%", str(len(all_entries)))
index_text = index_text.replace("%%NUMTOPICS%%", str(len(all_topics)))

def write_definitions_table(fp, symbols, **kwargs):
    fp.write(Expr.definitions_table_html(symbols, **kwargs))

class Webpage:

    def start(self):
        if not os.path.exists(os.path.dirname(self.filepath)):
            os.makedirs(os.path.dirname(self.filepath))
        self.fp = open(self.filepath, "w")
        self.fp.write(html_start.replace("%%PAGETITLE%%", self.pagetitle))

    def entry(self, id, default_visible=False):
        html = entries_dict[id].entry_html(single=False, default_visible=default_visible)
        self.fp.write(html)

    def section(self, title):
        self.fp.write("""<h2>%s</h2>""" % title)

    def end(self):
        self.fp.write(html_end)
        self.fp.close()

class FrontPage(Webpage):

    def __init__(self):
        self.filepath = "build/html/index.html"
        self.pagetitle = "Fungrim: The Mathematical Functions Grimoire"

    def entry(self, id):
        html = entries_dict[id].entry_html(single=False, entry_dir="entry/", symbol_dir="symbol/")
        self.fp.write(html)

    def start(self):
        Webpage.start(self)
        self.fp.write(index_text)

class EntryPage(Webpage):

    def __init__(self, id):
        self.id = id
        self.filepath = "build/html/entry/%s/index.html" % self.id
        self.pagetitle = "Entry %s - Fungrim: The Mathematical Functions Grimoire" % self.id

    def entry(self, id):
        html = entries_dict[id].entry_html(single=True)
        self.fp.write(html)
        self.fp.write("<h2>Topics using this entry</h2>")
        self.fp.write("<ul>")
        for title in topics_referencing_entry[id]:
            self.fp.write("""<li><a href="../../topic/%s/">%s</a></li>""" % (escape_title(title), title))
        self.fp.write("</ul>")

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%; margin-top: 0.2em;"><a href="../../">Fungrim home page</a></p>""")
        self.fp.write("""<h1>Fungrim entry: %s</h1>""" % self.id)

    def write(self):
        self.start()
        self.entry(self.id)
        self.end()

class TopicPage(Webpage):

    def __init__(self, title):
        self.filepath = "build/html/topic/" + escape_title(title) + "/index.html"
        self.title = title
        self.pagetitle = title + " - Fungrim: The Mathematical Functions Grimoire"

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%; margin-top: 0.2em;em"><a href="../../">Fungrim home page</a></p>""")
        self.fp.write("""<h1>%s</h1>""" % self.title)

    def write(self):
        self.start()
        topic = topics_dict[self.title]
        sections = []
        for arg in topic.args():
            if arg.head() is Section:
                sections.append(arg.args()[0]._text)
        if sections:
            self.fp.write("""<p style="text-align:center;">Table of contents: """)
            for i, s in enumerate(sections):
                self.fp.write("""<a href="#%s">%s</a> """ % (escape_title(s), s))
                if i < len(sections) - 1:
                    self.fp.write(""" - """)
            self.fp.write("""</p>""")
        sect_i = 0
        for arg in topic.args():
            if arg.head() is DefinitionsTable:
                # self.fp.write("""<h2>Main symbols</h2>""")
                self.fp.write("""<div style="margin-bottom:1em">""")
                write_definitions_table(self.fp, arg.args(), center=True)
                self.fp.write("""</div>""")
            if arg.head() is Section:
                s = arg.args()[0]._text
                self.fp.write("""<h2 id="%s">%s</h2>""" % (escape_title(s), s))
                sect_i += 1
            if arg.head() is Subsection:
                s = arg.args()[0]._text
                self.fp.write("""<h3>%s</h3>""" % s)
            if arg.head() is Entries:
                for id in arg.args():
                    self.entry(id._text)
            if arg.head() is SeeTopics:
                for rel in arg.args():
                    if rel._text not in topics_dict:
                        print("WARNING: linked topic page '%s' missing" % rel._text)
                rel_strs = ["""<a href="../%s/">%s</a>""" % (escape_title(rel._text), rel._text) for rel in arg.args()]
                self.fp.write("""<p style="text-align:center">Related topics: %s</p>""" % ", ".join(rel_strs))
            if arg.head() is Description:
                self.fp.write(arg.html(display=True))
        self.end()

class DefinitionsPage(Webpage):

    def __init__(self):
        self.filepath = "build/html/definitions.html"
        self.title = "All symbol definitions"
        self.pagetitle = "All symbol definitions"

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center"><a href="index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>%s</h1>""" % self.title)

    def write(self):
        self.start()
        write_definitions_table(self.fp, described_symbols, center=True, symbol_dir="symbol/")
        self.end()

class SymbolPage(Webpage):

    def __init__(self, symbol):
        self.symbol = symbol
        self.filepath = "build/html/symbol/%s/index.html" % self.symbol
        self.pagetitle = "Symbol %s - Fungrim: The Mathematical Functions Grimoire" % self.symbol

    def content(self, symbol):
        if symbol in domain_tables:
            self.entry(domain_tables[symbol]) #, default_visible=True)
        else:
            write_definitions_table(self.fp, [symbol], center=True)
            self.fp.write("""<p style="margin-left:1em">The symbol <tt>%s</tt> does not yet have a definition text. """
                """Please send an angry email to the author and ask for an explanation, or open an issue on GitHub.</p>""" % symbol)

        self.fp.write("""<h2>Topics using this symbol</h2>""")
        topics = topics_referencing_symbol[symbol]
        topics = list(topics.items())
        topics.sort(key=lambda top_count: (top_count[1], top_count[0]), reverse=True)
        num = len(topics)
        cols = min(max(1, num // 8), 3)
        self.fp.write("""<p style="margin-left:1em">The symbol <tt>%s</tt> appears in %i topics:</p>""" % (symbol, num))
        self.fp.write("""<div style="columns: %i"><ul>""" % cols)
        for topic, count in topics:
            self.fp.write("""<li><a href="../../topic/%s/">%s</a> (in %i entries)</li>""" % (escape_title(topic), topic, count))
        self.fp.write("""</div>""")

        self.fp.write("""<h2>Entries using this symbol</h2>""")
        num = len(entries_referencing_symbol[symbol])
        self.fp.write("""<p style="margin-left:1em">The symbol <tt>%s</tt> appears in %i entries:</p>""" % (symbol, num))
        cols = min(max(1, num // 8), 5)
        self.fp.write("""<div style="columns: %i"><ul>""" % cols)
        for entry in entries_referencing_symbol[symbol]:
            id = entry
            self.fp.write("""<li><a href="../../entry/%s/">%s</a></li>""" % (id, id))
        self.fp.write("""</ul></div>""")

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%"><a href="../../">Fungrim home page</a></p>""")
        self.fp.write("""<h1>Fungrim symbol: %s</h1>""" % self.symbol)

    def write(self):
        self.start()
        self.content(self.symbol)
        self.end()

class OrdnerMainPage(Webpage):

    def __init__(self, ordner, index_splits):
        self.ordner = ordner
        self.index_splits = index_splits
        self.filepath = "build/html/ordner/index.html"
        self.title = "Ordner: index of real numbers"
        self.pagetitle = "Ordner: index of real numbers - Fungrim: The Mathematical Functions Grimoire"

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%; margin-top: 0.2em;em"><a href="../">Fungrim home page</a></p>""")
        self.fp.write("""<h1>%s</h1>""" % self.title)

    def write(self):
        self.start()
        write = self.fp.write

        ordner = self.ordner
        count_decimals = len(ordner.values_expressions)
        count_integer_decimals = len(ordner.integer_values)
        count_expressions = len(ordner.expressions_values)

        write("""<p style="margin:1em; font-size:0.9em;">""")
        write("""Welcome to Ordner, a catalog of real numbers in Fungrim. """)
        write("""Ordner is indexed by 30-digit floating-point decimal keys such as <tt>0.707106781186547524400844362105</tt>. """)
        write("""For each key, Ordner lists constant symbolic expressions (for example <tt>Div(1,&nbsp;Sqrt(2))</tt>) with numerical value within &pm;1 <abbr title="unit in the last place">ulp</abbr> of the key. """)
        write("""For each expression <tt>x</tt>, Ordner also links to the Fungrim entries where <tt>x</tt> appears. """)
        write("""Ordner currently contains %i decimal keys (of which %i are integers) and %i symbolic expressions.""" % (count_decimals, count_integer_decimals, count_expressions))
        write("""</p>""")

        write("""<h2>Hall of fame</h2>""")

        write("""<p style="margin:1em; font-size:0.9em;">Find out which real numbers have real significance! <i>Frequency</i> denotes the total number of times any expression matching that decimal key appears in Fungrim, counting repetitions.</p>""")

        write("""<div style="margin: 0 auto;">""")
        write("""<div style="text-align:center">""")
        write("""<div style="display: inline-block;">""")

        write("""<ul style="text-align:left; padding:0; margin-top:0">""")

        write("""<li><a href="top250/">Top 250 real numbers by frequency, excluding integers</a></li>""")
        write("""<li><a href="top250inclusive/">Top 250 real numbers by frequency, including integers</a></li>""")
        write("""<li><a href="top250expr/">Top 250 real numbers by number of expressions</a></li>""")

        write("""</ul>""")
        write("""</div>""")
        write("""</div>""")
        write("""</div>""")

        write("""<h2>All numbers, ordered by magnitude</h2>""")
        write("""<p style="margin:1em; font-size:0.9em;">""")
        write("""Browse [0, &infin;). To keep the page sizes reasonable, the listing is split into intervals with a few hundred keys per page. The splitting points are not permanent and will change when Fungrim is updated.""")
        write("""</p>""")

        write("""<div style="margin: 0 auto;">""")
        write("""<div style="text-align:center">""")
        write("""<div style="display: inline-block;">""")

        write("""<ul style="text-align:left; list-style-type: none; margin:0; padding:0">""")
        for i, (a, b, s) in enumerate(index_splits):
            # write("""<li><a href="index%02i/">%02i: &nbsp; %s</a></li>""" % (i, i, s))
            write("""<li><a href="index%02i/">&nbsp; %s</a></li>""" % (i, s))
        write("""</ul>""")
        write("""</div>""")
        write("""</div>""")
        write("""</div>""")


        write("""<h2>How it works</h2>""")

        write("""<p style="margin:1em; font-size:0.9em;">""")
        write("""Ordner is generated automatically by searching all Fungrim formulas for constant subexpressions that <a href="http://arblib.org">Arb</a> can evaluate numerically. Only expressions that appear explicitly in Fungrim are covered, with the following exceptions. All decimal keys in Ordner are normalized to be nonnegative, so expressions <tt>x</tt> representing negative values are indexed as <tt>Neg(x)</tt> in Ordner. """)
        write("""Complex numbers are indexed by the real and imaginary parts (<tt>Re(x)</tt>, <tt>Im(x)</tt>), as well as the absolute value and complex argument (<tt>Abs(x)</tt>, <tt>Arg(x)</tt>) when both the real and imaginary parts are nonzero. """)
        write("""The number 0 is a special case: a vanishing expression is only included when the numerical evaluation code can prove that the expression exactly represents 0. Some trivially zero-valued expressions are excluded to prevent bloat. """)
        write("""Finally, since the Fungrim formula language normally uses <tt>Exp(x)</tt> instead of <tt>Pow(ConstE, x)</tt> to represent the exponential function, """)
        write("""formulas containing <tt>Exp(...)</tt> are listed under <tt>2.71828182845904523536028747135</tt> as a special case, so as to represent this fundamental constant fairly! """)

        write("""</p>""")

        write("""<p style="margin:1em; font-size:0.9em;">""")
        write("""For some keys, only a decimal literal is listed as a symbolic expression, even when the origin of that quantity is something more meaningful (typically because the decimal appears in a table of numerical values where the corresponding symbolic expressions are only given implicitly). In such cases, the user may look up the entry where the decimal literal appears to find the real meaning. Limitations of this kind will be fixed in the future.""")
        write("""</p>""")

        write("""<p style="margin:1em; font-size:0.9em;">""")
        write("""ORDNER stands for Online Real Decimal Number Encyclopedia Reference.""")
        write("""</p>""")

        self.end()

class OrdnerTablePage(Webpage):

    def __init__(self, ordner, title, dirname, num=10000, sort=None, integers=True, between=None, index_splits=None, max_expressions=4, max_entries=10):
        self.num = num
        self.ordner = ordner
        self.integers = integers
        self.between = between
        self.filepath = "build/html/ordner/" + dirname + "/index.html"
        self.sort = sort
        self.title = title
        self.pagetitle = title + " - Ordner: index to real numbers in Fungrim"
        self.index_splits = index_splits
        self.max_expressions = max_expressions
        self.max_entries = max_entries

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%; margin-top: 0.2em;em"><a href="../../">Fungrim home page</a></p>""")
        self.fp.write("""<h1>%s</h1>""" % self.title)

    def write(self):
        self.start()
        write = self.fp.write
        ordner = self.ordner

        write("""<p style="margin:1em; font-size:0.9em; text-align:center">""")
        write("""From <a href="../">Ordner</a>, a catalog of real numbers in Fungrim. """)
        write("""</p>""")

        if self.between is None:
            write("""<p style="margin:1em; font-size:0.9em;">""")
            if self.sort == "frequency":
                write("""This page lists the top 250 decimal keys in Ordner when ranked by frequency (the total number of times any expression matching the given decimal key appears in Fungrim, counting repetitions). """)
                if self.integers:
                    write("""This page <b>includes</b> integer-valued keys in the list. """)
                else:
                    write("""This page <b>excludes</b> integer-valued keys from the list. """)
            else:
                write("""This page lists the top 250 decimal keys in Ordner when ranked by the number of distinct symbolic expressions in Fungrim matching the key. """)

            links = []
            if not (self.sort == "frequency" and self.integers == False): links.append("""<a href="../top250/">Top 250 real numbers by frequency, excluding integers</a>""")
            if not (self.sort == "frequency" and self.integers == True): links.append("""<a href="../top250inclusive/">Top 250 real numbers by frequency, including integers</a>""")
            if not (self.sort == "expressions"): links.append("""<a href="../top250expr/">Top 250 real numbers by number of expressions</a>""")

            write("See also: ")
            write(links[0])
            write(" and ")
            write(links[1])
            write(".")

            write("""</p>""")
        else:
            for i, (a, b, s) in enumerate(index_splits):
                if (a, b) == self.between:
                    if i != 0:
                        write("""<p style="margin:1em; font-size:0.9em; text-align:center">""")
                        write("""Previous interval: <a href="../index%02i">%s</a>""" % (i-1, index_splits[i-1][2]))
                        write("""</p>""")
                    write("""<p style="margin:1em; font-size:0.9em; text-align:center">""")
                    write("""<span style="font-weight:bold">This interval</span>: %s""" % s)
                    write("""</p>""")
                    if i != len(index_splits) - 1:
                        write("""<p style="margin:1em; font-size:0.9em; text-align:center">""")
                        write("""Next interval: <a href="../index%02i">%s</a>""" % (i+1, index_splits[i+1][2]))
                        write("""</p>""")

        ordner.html_table(write, num=self.num, between=self.between, sort=self.sort, integers=self.integers, max_entries=self.max_entries, max_expressions=self.max_expressions)

        self.end()


for entry in all_entries:
    print("entry " + str(entry.id()))
    EntryPage(entry.id()).write()

for topic in all_topics:
    print("topic " + str(topic.title()))
    TopicPage(topic.title()).write()

for symbol in all_used_symbols:
    print("symbol " + str(symbol))
    SymbolPage(symbol).write()

DefinitionsPage().write()

if ordner_ is not None:
    ordner = ordner_  # the variable was overwritten; make this local...
    print("writing ordner...")
    num = len(ordner.values_ordered)
    index_splits = []
    N = 1
    while num // N > 250:
        N += 1
    num_per_page = (num + N - 1) // N
    for i in range(N):
        a = i * num_per_page
        b = min((i + 1) * num_per_page, len(ordner.values_ordered)-1)
        av = ordner.values_ordered[a]
        bv = ordner.values_ordered[b]
        if i == N - 1:
            s = "[<tt>%s,&nbsp;&infin;</tt>)" % av
        else:
            s = "[<tt>%s,&nbsp;%s</tt>]" % (av, bv)
        index_splits.append((a, b, s))

    for i, val in enumerate(ordner.values_ordered):
        expressions = ordner.values_expressions[val]
        if len(expressions) > 4 or max(len(ordner.expressions_entries[expr]) for expr in expressions) > 10:
            OrdnerTablePage(ordner, val, val, between=(i, i), max_expressions=10000, max_entries=1000).write()

    for i, (a, b, s) in enumerate(index_splits):
        av = ordner.values_ordered[a]
        bv = ordner.values_ordered[b]
        OrdnerTablePage(ordner, "Real numbers from %s" % av, "index%02i" % i, between=(a, b), index_splits=index_splits).write()

    OrdnerTablePage(ordner, "Top 250 real numbers by frequency, excluding integers", "top250", num=250, sort="frequency", integers=False).write()
    OrdnerTablePage(ordner, "Top 250 real numbers by frequency, including integers", "top250inclusive", num=250, sort="frequency", integers=True).write()
    OrdnerTablePage(ordner, "Top 250 real numbers by number of expressions", "top250expr", num=250, sort="expressions", integers=True).write()

    OrdnerMainPage(ordner, index_splits).write()


#def index_link(symbol):
#    s = """<a href="%s.html">%s</a> &nbsp; (%i entries)""" % described_symbols

frontpage = FrontPage()
frontpage.start()
frontpage.entry("9ee8bc")
frontpage.fp.write("""
<p style="margin: 1em; font-size:0.9em">
The Fungrim website provides a permanent ID and URL for each entry, symbol or topic. 
Click "Details" to show an expanded view of an entry, or click the ID (9ee8bc) to show the expanded view on its own page.
All data in Fungrim is represented in semantic form designed to be usable by computer algebra software.
</p>""")
frontpage.section("Browse by topic")

def writetopic(s, highlight=False):
    if highlight:
        frontpage.fp.write("""<li><a href="topic/%s/">%s</a> <span style="color:orange;">&#x2605;</span></li>""" % (escape_title(s), s))
    else:
        frontpage.fp.write("""<li><a href="topic/%s/">%s</a></li>""" % (escape_title(s), s))

frontpage.fp.write("""<div class="topiclist"><ul>""")

frontpage.fp.write("""<li>Fundamentals<ul>""")
writetopic("Elementary logic and set theory")
writetopic("Numbers and infinities")
writetopic("Operators")
writetopic("Complex plane")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Constants<ul>""")
writetopic("Pi")
writetopic("Euler's constant")
writetopic("Golden ratio")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Elementary functions<ul>""")
writetopic("Complex parts")
writetopic("Exponential function")
writetopic("Natural logarithm")
writetopic("Square roots")
writetopic("Powers")
writetopic("Sine", highlight=True)
writetopic("Inverse tangent", highlight=True)
writetopic("Lambert W-function")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Combinatorial and integer functions<ul>""")
writetopic("Greatest common divisor", highlight=True)
writetopic("Totient function")
writetopic("Factorials and binomial coefficients")
writetopic("Fibonacci numbers", highlight=True)
writetopic("Prime numbers")
writetopic("Partition function")
writetopic("Bernoulli numbers and polynomials")
writetopic("Stirling numbers")
writetopic("Landau's function")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Gamma function<ul>""")
writetopic("Gamma function")
writetopic("Beta function")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Hypergeometric functions<ul>""")
writetopic("Gauss hypergeometric function")
writetopic("Confluent hypergeometric functions")
writetopic("Error functions")
writetopic("Airy functions")
writetopic("Bessel functions")
writetopic("Coulomb wave functions")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Orthogonal polynomials<ul>""")
writetopic("Legendre polynomials")
writetopic("Chebyshev polynomials", highlight=True)
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Zeta and L-functions<ul>""")
writetopic("Riemann zeta function")
writetopic("Zeros of the Riemann zeta function")
writetopic("Dirichlet characters")
writetopic("Dirichlet L-functions")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Modular and elliptic functions<ul>""")
writetopic("Modular transformations")
writetopic("Jacobi theta functions", highlight=True)
writetopic("Dedekind eta function")
writetopic("Modular j-invariant")
writetopic("Modular lambda function", highlight=True)
writetopic("Eisenstein series", highlight=True)
writetopic("Weierstrass elliptic functions")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Tables of sums, products, integrals...<ul>""")
writetopic("Definite integrals")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Numerical analysis<ul>""")
writetopic("General analytic functions")
writetopic("Gaussian quadrature")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""</ul></div>""")

frontpage.fp.write("""<p style="margin:1em; text-align:center"><span style="color:orange;">&#x2605;</span> Recommended topic (relatively complete)</p>""")

frontpage.section("Browse by symbol")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="definitions.html">Table of defined symbols</a> &nbsp;(%i total entries)</li>""" % len(described_symbols))
frontpage.fp.write("""</ul>""")

frontpage.section("Browse real numbers (Ordner)")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="ordner/">Ordner: index of real numbers</li>""")
frontpage.fp.write("""</ul>""")


frontpage.end()

print("The grimoire was built successfully!")

try:
    with open("build/katex_cache.pickle", "wb") as fp:
        pickle.dump(katex_cache, fp, protocol=pickle.HIGHEST_PROTOCOL)
except IOError:
    print("Error writing katex_cache")

