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


from formulas import *

topics_referencing_entry = {}
entries_referencing_symbol = {}
all_used_symbols = set()

for entry in all_entries:
    for symbol in entry.all_symbols():
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
                for symbol in entry.all_symbols():
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
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.css" integrity="sha384-dbVIfZGuN1Yq7/1Ocstc1lUEm+AT+/rCkibIcC/OmWo5f0EA48Vf8CytHzGrSwbQ" crossorigin="anonymous">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style type="text/css">
body { margin: 0; padding: 0; font-family: roboto, arial, sans-serif; background-color:#eee; color:#111; }
h1 { text-align:center; color:#256; margin-top: 0; }
h2, h3 { text-align: center; margin-bottom: 0.5em; margin-top: 0.7em; }
h3 { font-size: 1em; font-weight: bold; color:#633; }
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
  if (x.style.height == "140px")
  {
    x.src = bigurl;
    x.style.height = "500px";
    x.style.width = "auto";
  }
  else
  {
    x.src = smallurl;
    x.style.height = "140px";
    x.style.width = "auto";
  }
}
</script>
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
<h1 style="margin-top: 0.5em">The Mathematical Functions Grimoire</h1>

<p style="text-align:center; color:red"><b>Pre-alpha version</b></p>

<p style="margin:1em">
Welcome! The Mathematical Functions Grimoire (<i>Fungrim</i>) is an open source library of formulas for mathematical functions.
Fungrim currently consists of %%NUMSYMBOLS%% <i>symbols</i> (named mathematical objects), %%NUMENTRIES%% <i>entries</i> (definitions, formulas, tables, plots), and %%NUMTOPICS%% <i>topics</i> (listings of entries).
All data in Fungrim is represented in symbolic, semantic form designed to be usable by computer algebra software.
Fungrim is also fully viewable online, with a permanent ID and URL for each entry, symbol or topic. This is one formula entry:
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
        self.filepath = "build/html/entry/%s.html" % self.id
        self.pagetitle = "Entry %s - Fungrim: The Mathematical Functions Grimoire" % self.id

    def entry(self, id):
        html = entries_dict[id].entry_html(single=True)
        self.fp.write(html)
        self.fp.write("<h2>Topics using this entry</h2>")
        self.fp.write("<ul>")
        for title in topics_referencing_entry[id]:
            self.fp.write("""<li><a href="../topic/%s.html">%s</a></li>""" % (escape_title(title), title))
        self.fp.write("</ul>")

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%; margin-top: 0.2em;"><a href="../index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>Fungrim entry: %s</h1>""" % self.id)

    def write(self):
        self.start()
        self.entry(self.id)
        self.end()

def escape_title(name):
    # paren = name.find("(")
    # if paren >= 0:
    #     name = name[:paren].rstrip(" ")
    return name.replace(" ", "_")

class TopicPage(Webpage):

    def __init__(self, title):
        self.filepath = "build/html/topic/" + escape_title(title) + ".html"
        self.title = title
        self.pagetitle = title + " - Fungrim: The Mathematical Functions Grimoire"

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%; margin-top: 0.2em;em"><a href="../index.html">Fungrim home page</a></p>""")
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
                rel_strs = ["""<a href="%s.html">%s</a>""" % (escape_title(rel._text), rel._text) for rel in arg.args()]
                self.fp.write("""<p style="text-align:center">Related topics: %s</p>""" % ", ".join(rel_strs))
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
        self.filepath = "build/html/symbol/%s.html" % self.symbol
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
            self.fp.write("""<li><a href="../topic/%s.html">%s</a> (in %i entries)</li>""" % (escape_title(topic), topic, count))
        self.fp.write("""</div>""")

        self.fp.write("""<h2>Entries using this symbol</h2>""")
        num = len(entries_referencing_symbol[symbol])
        self.fp.write("""<p style="margin-left:1em">The symbol <tt>%s</tt> appears in %i entries:</p>""" % (symbol, num))
        cols = min(max(1, num // 8), 5)
        self.fp.write("""<div style="columns: %i"><ul>""" % cols)
        for entry in entries_referencing_symbol[symbol]:
            id = entry
            self.fp.write("""<li><a href="../entry/%s.html">%s</a></li>""" % (id, id))
        self.fp.write("""</ul></div>""")

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%"><a href="../index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>Fungrim symbol: %s</h1>""" % self.symbol)

    def write(self):
        self.start()
        self.content(self.symbol)
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

#def index_link(symbol):
#    s = """<a href="%s.html">%s</a> &nbsp; (%i entries)""" % described_symbols

frontpage = FrontPage()
frontpage.start()
frontpage.entry("9ee8bc")
frontpage.fp.write("""<p style="margin: 1em">Click "Details" to show an expanded view of an entry, or click the ID (9ee8bc) to show the expanded view on its own page.</p>""")
frontpage.section("Browse by topic")

def writetopic(s):
    frontpage.fp.write("""<li><a href="topic/%s.html">%s</a></li>""" % (escape_title(s), s))

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
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Elementary functions<ul>""")
writetopic("Complex parts")
writetopic("Exponential function")
writetopic("Natural logarithm")
writetopic("Square roots")
writetopic("Powers")
writetopic("Sine")
writetopic("Inverse tangent")
writetopic("Lambert W-function")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Combinatorial and integer functions<ul>""")
writetopic("Greatest common divisor")
writetopic("Factorials and binomial coefficients")
writetopic("Prime numbers")
writetopic("Partition function")
writetopic("Bernoulli numbers and polynomials")
writetopic("Stirling numbers")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Hypergeometric functions<ul>""")
writetopic("Gamma function")
writetopic("Confluent hypergeometric functions")
writetopic("Error functions")
writetopic("Airy functions")
writetopic("Bessel functions")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Orthogonal polynomials<ul>""")
writetopic("Legendre polynomials")
writetopic("Chebyshev polynomials")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Zeta and L-functions<ul>""")
writetopic("Riemann zeta function")
writetopic("Zeros of the Riemann zeta function")
frontpage.fp.write("""</ul></li>""")

frontpage.fp.write("""<li>Modular and elliptic functions<ul>""")
writetopic("Modular transformations")
writetopic("Jacobi theta functions")
writetopic("Dedekind eta function")
writetopic("Modular j-invariant")
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

frontpage.section("General")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="definitions.html">Table of defined symbols</a> &nbsp;(%i total entries)</li>""" % len(described_symbols))
frontpage.fp.write("""</ul>""")

frontpage.end()

print("The grimoire was built successfully!")

try:
    with open("build/katex_cache.pickle", "wb") as fp:
        pickle.dump(katex_cache, fp, protocol=pickle.HIGHEST_PROTOCOL)
except IOError:
    print("Error writing katex_cache")

