# -*- coding: utf-8 -*-

from formulas import *

import os
if not os.path.exists("build"):
    os.makedirs("build")
if not os.path.exists("build/html"):
    os.makedirs("build/html")
if not os.path.exists("build/html/entry"):
    os.makedirs("build/html/entry")

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
timestamp = str(datetime.datetime.now())

html_start = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>%%PAGETITLE%%</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.1/dist/katex.min.css" integrity="sha384-dbVIfZGuN1Yq7/1Ocstc1lUEm+AT+/rCkibIcC/OmWo5f0EA48Vf8CytHzGrSwbQ" crossorigin="anonymous">
<style type="text/css">
body { margin:0.5em; font-family: roboto; background-color: #fafafa; color: black; }
h1 { text-align:center; color:#256; }
h2, h3 { text-align: center; }
p { line-height:1.5em; }
pre { white-space: pre-wrap; background-color: #ffffff; border: 1px solid #cccccc; padding: 0.5em; margin: 0.1em; }
.entry { border:1px solid #bbb; padding-left:0.4em; padding-right:0.4em; padding-top:0em; padding-bottom:0em; margin-left:0; margin-right:0; margin-bottom:0.5em; background-color: #fff; overflow: hidden; }
.entrysubhead { font-weight: bold; padding-bottom: 0.1em; padding-top: 0.6em; }
table { border-collapse:collapse; background-color:#fff; }
table, th, td { border: 1px solid #aaa; }
th, td { padding:0.2em; }
td { min-width: 30px; }
th { background-color: #f0f0f0; }
tr:nth-child(odd) { background-color: #fafafa; }
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
</script>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> 
</head>
<body>
"""

html_end = """
<div style="margin:2em">
<p style="text-align:center">Copyright (C) <a href="http://fredrikj.net">Fredrik Johansson</a> and <a href="https://github.com/fredrik-johansson/fungrim/graphs/contributors">contributors</a>.
Fungrim is provided under the
<a href="https://github.com/fredrik-johansson/fungrim/blob/master/LICENSE">MIT license</a>.
The <a href="https://github.com/fredrik-johansson/fungrim">source code is on GitHub</a>.
</p></div>
<p style="text-align:center">%%TIMESTAMP%%</p></div>
</body>
</html>
"""

html_end = html_end.replace("%%TIMESTAMP%%", timestamp)

index_text = """
<h1>The Mathematical Functions Grimoire</h1>

<p style="text-align:center; color:red"><b>Pre-alpha version</b></p>

<p style="margin:1em">Welcome! The Mathematical Functions Grimoire (<i>Fungrim</i>) is an open source library of formulas for mathematical functions. The data is fully symbolic (designed for use by computer algebra software) and the whole library can be browsed online, with a permanent ID and URL for each entry. There are currently %%NUMTOTAL%% entries in Fungrim; see one example below. Click "Details" to show an expanded view of an entry, or click the ID to show the expanded view on its own page. You can <a href="https://github.com/fredrik-johansson/fungrim">contribute on GitHub</a>.
</p>
"""

index_text = index_text.replace("%%NUMTOTAL%%", str(len(all_entries)))

def makeurl(id):
    return "fungrim/entry/%s" % id

def write_definitions_table(fp, symbols, center=False):
    fp.write(Expr.definitions_table_html(symbols, center))

entries_dict = {}
for entry in all_entries:
    if entry.id() in entries_dict:
        raise ValueError("duplicated ID %s" % entry.id())
    entries_dict[entry.id()] = entry

class Webpage:

    def start(self):
        self.fp = open(self.filepath, "w")
        self.fp.write(html_start.replace("%%PAGETITLE%%", self.title))

    def entry(self, id):
        html = entries_dict[id].entry_html(single=False)
        self.fp.write(html)

    def section(self, title):
        self.fp.write("""<h2>%s</h2>""" % title)

    def end(self):
        self.fp.write(html_end)
        self.fp.close()

class FrontPage(Webpage):

    def __init__(self):
        self.filepath = "build/html/index.html"
        self.title = "Fungrim: the Mathematical Functions Grimoire"

    def start(self):
        Webpage.start(self)
        self.fp.write(index_text)

class EntryPage(Webpage):

    def __init__(self, id):
        self.id = id
        self.filepath = "build/html/entry/%s.html" % self.id
        self.title = "Entry %s - Fungrim" % self.id

    def entry(self, id):
        html = entries_dict[id].entry_html(single=True)
        self.fp.write(html)

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center"><a href="../index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>Fungrim entry: %s</h1>""" % self.id)

    def write(self):
        self.start()
        self.entry(self.id)
        self.end()

class IndexPage(Webpage):

    def __init__(self, url, title, sections_ids):
        self.filepath = "build/html/%s.html" % url
        self.title = title
        self.sections_ids = sections_ids

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center"><a href="index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>%s</h1>""" % self.title)

    def write(self):
        count = 0
        self.start()
        for sect, ids in self.sections_ids:
            self.section(sect)
            for id in ids:
                self.entry(id)
                count += 1
        self.end()
        return count

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
        write_definitions_table(self.fp, described_symbols, center=True)
        self.end()

for entry in all_entries:
    print("processing " + str(entry.id()))
    EntryPage(entry.id()).write()


count_ConstPi = IndexPage(*index_ConstPi).write()
count_ConstGamma = IndexPage(*index_ConstGamma).write()
count_Exp = IndexPage(*index_Exp).write()
count_Log = IndexPage(*index_Log).write()
count_GammaFunction = IndexPage(*index_GammaFunction).write()
count_LegendrePolynomial = IndexPage(*index_LegendrePolynomial).write()
count_RiemannZeta = IndexPage(*index_RiemannZeta).write()
count_DedekindEta = IndexPage(*index_DedekindEta).write()
count_PartitionsP = IndexPage(*index_PartitionsP).write()
DefinitionsPage().write()

frontpage = FrontPage()
frontpage.start()
frontpage.entry("9ee8bc")
frontpage.section("Browse by function")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="ConstPi.html">The constant pi (3.14...)</a> &nbsp;(%i total entries)</li>""" % count_ConstPi)
frontpage.fp.write("""<li><a href="ConstGamma.html">The constant gamma (0.577...)</a> &nbsp;(%i total entries)</li>""" % count_ConstGamma)
frontpage.fp.write("""<li><a href="Exp.html">Exponential function</a> &nbsp;(%i total entries)</li>""" % count_Exp)
frontpage.fp.write("""<li><a href="Log.html">Natural logarithm</a> &nbsp;(%i total entries)</li>""" % count_Log)
frontpage.fp.write("""<li><a href="GammaFunction.html">Gamma function</a> &nbsp;(%i total entries)</li>""" % count_GammaFunction)
frontpage.fp.write("""<li><a href="LegendrePolynomial.html">Legendre polynomial</a> &nbsp;(%i total entries)</li>""" % count_LegendrePolynomial)
frontpage.fp.write("""<li><a href="RiemannZeta.html">Riemann zeta function</a> &nbsp;(%i total entries)</li>""" % count_RiemannZeta)
frontpage.fp.write("""<li><a href="DedekindEta.html">Dedekind eta function</a> &nbsp;(%i total entries)</li>""" % count_DedekindEta)
frontpage.fp.write("""<li><a href="PartitionsP.html">Integer partition function</a> &nbsp;(%i total entries)</li>""" % count_PartitionsP)
frontpage.fp.write("""</ul>""")
frontpage.section("General")
frontpage.fp.write("""<ul>""")
frontpage.fp.write("""<li><a href="definitions.html">All symbol definitions</a> &nbsp;(%i total entries)</li>""" % len(described_symbols))
frontpage.fp.write("""</ul>""")
frontpage.end()

print("The grimoire was built successfully!")

try:
    with open("build/katex_cache.pickle", "wb") as fp:
        pickle.dump(katex_cache, fp, protocol=pickle.HIGHEST_PROTOCOL)
except IOError:
    print("Error writing katex_cache")

