"""grim2mathjson — Fungrim (pygrim) Expr → MathJSON translator.

Sibling package to `pygrim` so that `from pygrim.formulas import all_entries`
works unmodified. Plain python3 + stdlib only (no third-party deps; the test
suite needs pytest: run `uv run --with pytest pytest grim2mathjson/tests`).

Usage:
    python3 -m grim2mathjson --out <dir> [--topic atan] [--strict]

Modules (per FUNGRIM-PLAN-1-TRANSLATOR.md §2.1):
  mapping.py     SYMBOL_MAP / SHELL_HEADS / SKIP_HEADS / METADATA_HEADS /
                 VARIABLE_RENAMES data tables
  walker.py      Expr -> MathJSON recursive translator core
  structural.py  Where/Def, For/ForElement, Cases, chains, Subscript,
                 intervals, integer sets, quantifiers, optima, ... (spike
                 decisions implemented; see SPIKE-DECISIONS.md)
  properties.py  top-level analytic-property routing -> properties.json
  emit.py        per-topic JSON writers, deterministic ordering
  report.py      skip/failure ledger, summary statistics, report.json
  cli.py         command-line entry point
  (M3+) classify.py (class/guardLevel annotations), shells.py
        (declarations.json) are future milestones.

M0 artifacts:
  SPIKE-DECISIONS.md   verification-backed decisions for the 15 risk items
  spike_verify.py      generates candidate MathJSON for the spike entries
  spike_verify.ts      boxes the candidates against the live Compute Engine
                       (run from the compute-engine repo:
                        npx tsx /Users/arno/dev/fungrim-master/grim2mathjson/spike_verify.ts)
"""

__version__ = "0.1.0"
