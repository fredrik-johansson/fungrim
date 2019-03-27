# -*- coding: utf-8 -*-

from formulas import *

import os
if not os.path.exists("build"):
    os.makedirs("build")
if not os.path.exists("build/html"):
    os.makedirs("build/html")
if not os.path.exists("build/html/entry"):
    os.makedirs("build/html/entry")
if not os.path.exists("build/html/topic"):
    os.makedirs("build/html/topic")

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
body { margin: 0; padding: 0; font-family: roboto; background-color:#eee; color: black; }
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
<div style="margin:0; padding:0.1em 0.5em 0.5em 0.5em; background-color: #fafafa;">
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
<p style="text-align:center">%%TIMESTAMP%%</p></div>
</div>
</div>
</body>
</html>
"""

html_end = html_end.replace("%%TIMESTAMP%%", timestamp)

index_text = """
<h1>The Mathematical Functions Grimoire</h1>

<p style="text-align:center; color:red"><b>Pre-alpha version</b></p>

<p style="margin:1em">
Welcome! The Mathematical Functions Grimoire (<i>Fungrim</i>) is an open source library of mathematical functions.
Fungrim currently consists of %%NUMSYMBOLS%% <i>symbols</i> (named mathematical objects), %%NUMENTRIES%% <i>entries</i> (formulas or tables), and %%NUMTOPICS%% <i>topics</i> (listings of entries and related topics).
All data in Fungrim is represented in symbolic, semantic form (usable by computer algebra software) and also viewable online, with a permanent ID and URL for each entry, symbol or topic.
</p>
"""

len(all_builtins)

index_text = index_text.replace("%%NUMSYMBOLS%%", str(len(all_builtins)))
index_text = index_text.replace("%%NUMENTRIES%%", str(len(all_entries)))
index_text = index_text.replace("%%NUMTOPICS%%", str(len(all_topics)))

def write_definitions_table(fp, symbols, center=False):
    fp.write(Expr.definitions_table_html(symbols, center))

class Webpage:

    def start(self):
        self.fp = open(self.filepath, "w")
        self.fp.write(html_start.replace("%%PAGETITLE%%", self.title))

    def entry(self, id):
        html = entries_dict[id].entry_html(single=False, entrydir="../entry/")
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

    def entry(self, id):
        html = entries_dict[id].entry_html(single=False, entrydir="entry/")
        self.fp.write(html)

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
        self.fp.write("""<p style="text-align:center; font-size:85%"><a href="../index.html">Fungrim home page</a></p>""")
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
        self.fp.write("""<p style="text-align:center; font-size:85%"><a href="index.html">Fungrim home page</a></p>""")
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

def escape_title(name):
    # paren = name.find("(")
    # if paren >= 0:
    #     name = name[:paren].rstrip(" ")
    return name.replace(" ", "_")

class TopicPage(Webpage):

    def __init__(self, title):
        self.filepath = "build/html/topic/" + escape_title(title) + ".html"
        self.title = title
        self.pagetitle = title

    def start(self):
        Webpage.start(self)
        self.fp.write("""<p style="text-align:center; font-size:85%"><a href="../index.html">Fungrim home page</a></p>""")
        self.fp.write("""<h1>%s</h1>""" % self.title)

    def write(self):
        self.start()
        topic = topics_dict[self.title]
        for arg in topic.args():
            #if arg.head() is DefinitionsTable:
            #    self.fp.write("""<h2>Main symbols</h2>""")
            #    write_definitions_table(self.fp, arg.args(), center=True)
            if arg.head() is Section:
                self.fp.write("""<h2>%s</h2>""" % arg.args()[0]._text)
            if arg.head() is Entries:
                for id in arg.args():
                    self.entry(id._text)
            if arg.head() is SeeTopics:
                for rel in arg.args():
                    if rel._text not in topics_dict:
                        print("WARNING: linked topic page '%s' missing" % rel._text)
                rel_strs = ["""<a href="%s.html">%s</a>""" % (escape_title(rel._text), rel._text) for rel in arg.args()]
                self.fp.write("""<p style="text-align:center">See: %s</p>""" % ", ".join(rel_strs))
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
        write_definitions_table(self.fp, described_symbols, center=True)
        self.end()


for entry in all_entries:
    print("entry " + str(entry.id()))
    EntryPage(entry.id()).write()

for topic in all_topics:
    print("topic " + str(topic.title()))
    TopicPage(topic.title()).write()


DefinitionsPage().write()

#def index_link(symbol):
#    s = """<a href="%s.html">%s</a> &nbsp; (%i entries)""" % described_symbols

frontpage = FrontPage()
frontpage.start()
frontpage.entry("9ee8bc")
frontpage.fp.write("""<p style="margin: 1em">Click "Details" to show an expanded view of an entry, or click the ID to show the expanded view on its own page.</p>""")
frontpage.section("Browse by topic")

def writetopic(s):
    frontpage.fp.write("""<li><a href="topic/%s.html">%s</a></li>""" % (escape_title(s), s))

frontpage.fp.write("""<ul>""")
writetopic("Pi")
writetopic("Euler's constant")
writetopic("Exponential function")
writetopic("Natural logarithm")
writetopic("Gamma function")
writetopic("Legendre polynomials")
writetopic("Airy functions")
writetopic("Riemann zeta function")
writetopic("Zeros of the Riemann zeta function")
writetopic("Dedekind eta function")
writetopic("Partition function")
writetopic("Stirling numbers")
writetopic("General analytic functions")
writetopic("Gaussian quadrature")
writetopic("Definite integrals")
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

