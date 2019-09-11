from .expr import *

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


class Ordner(object):
    def __init__(self):
        pass

    def build(self, entries):
        from flint import ctx, arb, acb
        from . import formulas

        digits = 30
        eval_digits = 40
        count = 0
        excluded = set([Parentheses, Brackets, Braces])
        ctx.dps = eval_digits   # for local manipulations

        # expr -> arb/acb value
        expressions_values = {}
        # expr -> entries containing expr (with repetitions!)
        expressions_entries = {}

        def insert(expr, val, eid):
            expressions_values[expr] = val
            if expr in expressions_entries:
                expressions_entries[expr] += (eid,)
            else:
                expressions_entries[expr] = (eid,)

        def insert_real(expr, val, eid):
            if val == 0:
                insert(expr, val, eid)
            if val != 0:
                if val < 0:
                    insert(Neg(expr), -val, eid)
                else:
                    insert(expr, val, eid)

        for entry in entries:
            eid = entry.id()
            for expr in entry.subexpressions():
                if expr == Exp:
                    insert_real(Expr("Indirect use of e: Exp(...)"), ConstE.n(eval_digits, as_arb=True), eid)
                if expr.head() not in excluded:
                    if expr in expressions_values:
                        val = expressions_values[expr]
                    else:
                        try:
                            val = expr.n(eval_digits, as_arb=True)
                        except (ValueError, NotImplementedError):
                            continue
                    if isinstance(val, arb):
                        insert_real(expr, val, eid)
                    else:
                        a = val.real
                        b = val.imag
                        if a != 0:
                            insert_real(Re(expr), a, eid)
                        if b != 0:
                            insert_real(Im(expr), b, eid)
                        if a != 0 and b != 0:
                            insert_real(Abs(expr), abs(val), eid)
                            insert_real(Arg(expr), val.arg(), eid)
                        #if not (a != 0 or b != 0):
                        #    insert_real(Abs(expr), abs(val), eid)
                        #    insert_real(Arg(expr), val.arg(), eid)

        # expr -> str(expr) ?
        expressions_values = dict((str(expr), val) for (expr, val) in expressions_values.items())
        expressions_entries = dict((str(expr), val) for (expr, val) in expressions_entries.items())

        # xxx: missing .is_int / .is_integer method
        def _arb_isint(x):
            return arb(x) == arb(x).floor() or arb(x) > 10**digits

        integer_values = set()

        # convert arb/acb values to decimal keys
        for expr in expressions_values:
            val = expressions_values[expr]
            # save integerness
            isint = _arb_isint(val)
            if val == 0:
                val = "0.0" + "0" * (digits-2)
            else:
                val = val.str(digits, radius=False)
            expressions_values[expr] = val
            if isint:
                integer_values.add(val)

        # reverse the table
        values_expressions = {}

        # some rankings
        values_frequency = {}
        values_diversity = {}
        for expr, val in expressions_values.items():
            if val in values_frequency:
                values_frequency[val] += len(expressions_entries[expr])
            else:
                values_frequency[val] = len(expressions_entries[expr])

            if val in values_diversity:
                values_diversity[val] += 1
            else:
                values_diversity[val] = 1

            if val in values_expressions:
                values_expressions[val].add(expr)
            else:
                values_expressions[val] = set([expr])

        values_ordered = list(values_expressions.keys())
        values_ordered.sort(key=lambda d: arb(d))

        values_ordered_frequency = list(values_expressions.keys())
        values_ordered_frequency.sort(key=lambda d: values_frequency[d], reverse=True)
        values_ordered_diversity = list(values_expressions.keys())
        values_ordered_diversity.sort(key=lambda d: values_diversity[d], reverse=True)

        self.integer_values = integer_values
        self.values_expressions = values_expressions
        self.values_frequency = values_frequency
        self.values_diversity = values_diversity
        self.values_ordered = values_ordered
        self.values_ordered_frequency = values_ordered_frequency
        self.values_ordered_diversity = values_ordered_diversity
        self.expressions_values = expressions_values
        self.expressions_entries = expressions_entries

    def html_table(self, write, num=None, between=None, sort=None, integers=True, entrypath="../../entry/", max_entries=10, max_expressions=10):

        write("""<div style="margin-left:1em; margin-right:1em">""")
        write("""<table style="margin-left:auto; margin-right:auto">""")

        write("""<tr>""")
        write("""<th>Decimal</th>""")
        write("""<th style="max-width:25%">Expression [entries]</th>""")
        write("""<th>Frequency</th>""")
        write("""</tr>""")

        frequency_order = {}
        for i, val in enumerate(self.values_ordered_frequency):
            frequency_order[val] = i

        if sort == "frequency":
            values = self.values_ordered_frequency
        elif sort == "expressions":
            values = self.values_ordered_diversity
        else:
            values = self.values_ordered

        if between is not None:
            values = values[between[0] : between[1] + 1]

        allcount = 0
        for decimal in values:
            expressions = self.values_expressions[decimal]

            if not integers and (decimal in self.integer_values):
                continue

            allcount += 1
            if num is not None and allcount > num:
                break

            num_expr = len(expressions)
            num_shown = min(num_expr, max_expressions)
            #if num_expr <= 15:
            #    num_shown = num_expr
            #else:
            #    num_shown = 10

            exprs = sorted(self.values_expressions[decimal], key=lambda expr: len(str(expr)))

            nmax = max_entries

            want_details = num_shown < num_expr
            for i, expr in enumerate(exprs[:num_shown]):
                eids = set(self.expressions_entries[expr])
                if len(eids) > nmax:
                    want_details = True

            write("""<tr>""")

            write("""<td valign="top">""")
            if want_details and len(values) != 1:
                write("""<a href="../%s/"><b><tt>%s</tt></b></a>""" % (decimal, decimal))
            else:
                write("""<tt>%s</tt>""" % (decimal))
            write("""</td>""")

            write("""<td valign="top">""")

            for i, expr in enumerate(exprs[:num_shown]):
                write("""<tt>%s</tt> """ % str(expr))
                count = 0
                write("""&nbsp;&nbsp;&nbsp;&nbsp;[""")
                eids = set(self.expressions_entries[expr])
                for eid in list(eids)[:nmax]:
                    write("""<a href="%s"><tt>%s</tt></a>""" % (entrypath + eid + "/", eid))
                    count += 1
                    if count < min(nmax, len(eids)):
                        write(" ")

                if len(eids) > nmax:
                    #write("""<tt> ... (%i omitted)</tt>""" % (len(eids) - nmax))
                    write("""&nbsp;<span style="font-size:0.85em; color:#666"> ... %i of %i shown</span>""" % (nmax, len(eids)))
                write("""]""")
                write("""<br/>""")

            if want_details and len(values) != 1:
                write("""<div style="font-size:0.85em; margin-top:0.4em; color:#666">%i of %i expressions shown</div>""" % (num_shown, num_expr))

            write("""</td>""")
            write("""<td valign="top">%i (#%i)</td>""" % (self.values_frequency[decimal], frequency_order[decimal] + 1))

            write("""</tr>""")

        write("</table>")
        write("</div>")

