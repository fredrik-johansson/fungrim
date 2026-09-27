"""Skip/failure ledger summary + report.json writer (plan §2.4).

Translation is TOTAL: every entry lands in the corpus, properties.json or
skipped.json. This module aggregates the counts, prints a human summary and
writes <out>/report.json. Under --strict the build fails (exit code 1) if
any entry hit the catch-all ``unknown-head`` reason.
"""

import json
import os
from collections import Counter

from . import __version__


def summarize(result):
    corpus_count = sum(len(v) for v in result["corpus"].values())
    props_count = len(result["properties"])
    skipped = result["skipped"]

    reasons = Counter(rec["reason"] for rec in skipped)
    unknown_heads = sorted({h for rec in skipped
                            if rec["reason"] == "unknown-head"
                            for h in rec["heads"]})
    # symbol-definition records are not formula entries: keep them out of
    # the coverage denominator (plan: skip budget is over formula entries)
    formula_skips = [rec for rec in skipped
                     if rec["reason"] != "symbol-definition"]
    n_formula = result["formulaEntries"]
    translated = corpus_count + props_count

    per_topic = {t: len(v) for t, v in sorted(result["corpus"].items())}

    # M3 annotation distributions
    class_counts = Counter()
    subclass_counts = Counter()
    guard_counts = Counter()
    for records in result["corpus"].values():
        for r in records:
            class_counts[r["class"]] += 1
            if r["subclass"]:
                subclass_counts[r["subclass"]] += 1
            guard_counts[r["guardLevel"]] += 1

    return {
        "generator": f"grim2mathjson {__version__}",
        "totalEntries": result["totalEntries"],
        "formulaEntries": n_formula,
        "corpusEntries": corpus_count,
        "propertyEntries": props_count,
        "skippedFormulaEntries": len(formula_skips),
        "skippedPercentOfFormulas":
            round(100.0 * len(formula_skips) / n_formula, 2)
            if n_formula else 0.0,
        "coveragePercent":
            round(100.0 * translated / n_formula, 2) if n_formula else 0.0,
        "classCounts": dict(sorted(class_counts.items())),
        "representationSubclassCounts": dict(sorted(subclass_counts.items())),
        "guardLevelCounts": dict(sorted(guard_counts.items())),
        "skipReasons": dict(sorted(reasons.items())),
        "unknownHeads": unknown_heads,
        "shellHeadsUsed": result["shells"],
        "variableWarnings": result["warnings"],
        "entriesPerTopic": per_topic,
    }


def print_summary(summary, file=None):
    p = lambda *a: print(*a, file=file)  # noqa: E731
    p(f"grim2mathjson {__version__}")
    p(f"  entries:        {summary['totalEntries']}"
      f" ({summary['formulaEntries']} with Formula)")
    p(f"  corpus:         {summary['corpusEntries']}")
    p(f"  properties:     {summary['propertyEntries']}")
    p(f"  skipped:        {summary['skippedFormulaEntries']}"
      f" formula entries ({summary['skippedPercentOfFormulas']}%)"
      f" -- coverage {summary['coveragePercent']}%")
    if summary["classCounts"]:
        p("  classes:")
        for cls, count in summary["classCounts"].items():
            p(f"    {count:5d}  {cls}")
        if summary["representationSubclassCounts"]:
            subs = ", ".join(f"{k} {v}" for k, v in
                             summary["representationSubclassCounts"].items())
            p(f"           (representation sub-tags: {subs})")
    if summary["guardLevelCounts"]:
        p("  guard levels:")
        order = ["none", "real-simple", "complex-domain", "undischargeable"]
        for lvl in order:
            if lvl in summary["guardLevelCounts"]:
                p(f"    {summary['guardLevelCounts'][lvl]:5d}  {lvl}")
    if summary["skipReasons"]:
        p("  skip reasons:")
        for reason, count in summary["skipReasons"].items():
            p(f"    {count:5d}  {reason}")
    if summary["unknownHeads"]:
        p(f"  UNKNOWN HEADS ({len(summary['unknownHeads'])}):"
          f" {', '.join(summary['unknownHeads'])}")
    p(f"  shell heads used: {len(summary['shellHeadsUsed'])}")
    if summary["variableWarnings"]:
        p(f"  variable-declaration mismatches:"
          f" {len(summary['variableWarnings'])} (see report.json)")


def write_report(summary, outdir):
    path = os.path.join(outdir, "report.json")
    with open(path, "w", newline="\n") as f:
        json.dump(summary, f, indent=1, ensure_ascii=True)
        f.write("\n")
