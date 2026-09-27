"""Golden tests: hand-checked entry translations (plan §2.1 / M1-M2).

Each file in golden/ is {"kind": "corpus"|"property"|"skip", "record": ...}
where record is the full emitted record for that entry, hand-verified against
SPIKE-DECISIONS.md (same entry IDs as the M0 spike candidates where
applicable, incl. d4b0b6 matching the FUNGRIM.md / plan §3.2 example).

Run with:  uv run --with pytest pytest grim2mathjson/tests
(or any environment that has pytest; the translator itself is stdlib-only).
"""

import glob
import json
import os

import pytest

GOLDEN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "golden")
GOLDEN_FILES = sorted(glob.glob(os.path.join(GOLDEN_DIR, "*.json")))

_INDEX = None


def _index():
    """Translate the full corpus once (fast: < 1 s) and index records by id."""
    global _INDEX
    if _INDEX is None:
        from pygrim.formulas import all_entries
        from grim2mathjson import emit
        from grim2mathjson.tests.conftest import ROOT

        result = emit.build(all_entries,
                            os.path.join(ROOT, "pygrim", "formulas"))
        idx = {}
        for records in result["corpus"].values():
            for r in records:
                idx[r["id"]] = ("corpus", r)
        for r in result["properties"]:
            idx[r["id"]] = ("property", r)
        for r in result["skipped"]:
            if r["id"]:
                idx[r["id"]] = ("skip", r)
        _INDEX = (idx, result)
    return _INDEX


def test_golden_coverage():
    assert len(GOLDEN_FILES) >= 20, "need at least 20 golden entries"
    ids = {os.path.basename(f)[:-5] for f in GOLDEN_FILES}
    assert "d4b0b6" in ids


@pytest.mark.parametrize(
    "path", GOLDEN_FILES, ids=[os.path.basename(f)[:-5] for f in GOLDEN_FILES])
def test_golden(path):
    with open(path) as f:
        expected = json.load(f)
    eid = os.path.basename(path)[:-5]
    idx, _ = _index()
    assert eid in idx, f"entry {eid} not produced by the translator"
    kind, record = idx[eid]
    assert kind == expected["kind"]
    assert record == expected["record"]


def test_d4b0b6_matches_plan_example():
    """d4b0b6 must match the FUNGRIM.md §2 / plan §3.2 example structure."""
    idx, _ = _index()
    kind, record = idx["d4b0b6"]
    assert kind == "corpus"
    assert record["formula"] == [
        "Equal",
        ["Sin", ["Arctan", "z"]],
        ["Divide", "z", ["Sqrt", ["Add", 1, ["Power", "z", 2]]]],
    ]
    assert record["variables"] == ["z"]
    assert record["assumptions"] == [
        "Element", "z",
        ["SetMinus", "ComplexNumbers",
         ["Set", ["Negate", "ImaginaryUnit"], "ImaginaryUnit"]],
    ]
    assert record["heads"] == ["Arctan", "Sin"]
    assert record["topics"] == ["atan"]
    # M3 annotations (plan SS3.2 example: identity / complex-domain)
    assert record["class"] == "identity"
    assert record["guardLevel"] == "complex-domain"


def test_0d8e03_assumption_alternatives():
    """Multi-arg Assumptions(...) states ALTERNATIVE assumption sets (pygrim
    renders args past the first as "Alternative assumptions"). They must not
    be And-joined: sqrt/0d8e03's sets are mutually contradictory
    (b in (0, oo) vs b in CC \\ (-oo, 0]). The first set is the primary
    `assumptions`; the rest go to `assumptionAlternatives`; guardLevel is
    computed from the primary set only."""
    idx, _ = _index()
    kind, record = idx["0d8e03"]
    assert kind == "corpus"
    assert record["assumptions"] == [
        "And",
        ["Element", "a", "ComplexNumbers"],
        ["Element", "b", ["Interval", ["Open", 0],
                          ["Open", "PositiveInfinity"]]],
    ]
    alts = record["assumptionAlternatives"]
    assert len(alts) == 2
    assert alts[0] == [
        "And",
        ["Element", "a", ["Interval", 0, ["Open", "PositiveInfinity"]]],
        ["Element", "b", ["SetMinus", "ComplexNumbers",
                          ["Interval", ["Open", "NegativeInfinity"], 0]]],
    ]
    assert alts[1][0] == "And" and len(alts[1]) == 4
    assert record["guardLevel"] == "complex-domain"


def test_no_record_joins_alternatives_with_and():
    """Regression: every corpus record with assumptionAlternatives keeps the
    primary set free of the alternative sets (27 entries upstream)."""
    _, result = _index()
    n = 0
    for records in result["corpus"].values():
        for r in records:
            alts = r.get("assumptionAlternatives")
            if not alts:
                continue
            n += 1
            for alt in alts:
                assert alt != r["assumptions"]
    assert n == 27


# Hand-checked class + guardLevel assertions (M3 acceptance). Each row was
# audited against the translated formula/assumptions:
#   d4b0b6  Sin(Arctan z) closed form; z in CC minus {-i, i}
#   591d64  Beta(1/2, 1/2) = pi, no variables
#   9b0994  Arctan(-i) = -i*oo, no variables (directed infinity)
#   0888b3  EulerGamma = Limit(...), no assumptions
#   3ab92d  Sum over DirichletGroup(q) = Which(...); q, n integer-typed
#           (the structural domain is in the formula, not the assumptions)
#   8f5e66  Euler product over Primes; Re(s) > 1 is a complex-inspection guard
#   622772  Erfi integral representation; z in CC
#   08ff0b  divisor-sum identity; n a positive integer
#   c33e2b  Element(...) statement (logical); integer guards
#   2a8ec9  Implies + piecewise (logical); Element(a_(k), ...) family
#           membership is implicitly quantified -> undischargeable
#   987e3c  Implies statement; z in CC
#   162ecf  AGM inequality; a, b in [0, oo) real interval -> real-simple
M3_GOLDEN = {
    "d4b0b6": ("identity", None, "complex-domain"),
    "591d64": ("specific-value", None, "none"),
    "9b0994": ("specific-value", None, "none"),
    "0888b3": ("representation", "limit", "none"),
    "3ab92d": ("representation", "series", "real-simple"),
    "8f5e66": ("representation", "product", "complex-domain"),
    "622772": ("representation", "integral", "complex-domain"),
    "08ff0b": ("identity", None, "real-simple"),
    "c33e2b": ("logical", None, "real-simple"),
    "2a8ec9": ("logical", None, "undischargeable"),
    "987e3c": ("logical", None, "complex-domain"),
    "162ecf": ("inequality", None, "real-simple"),
}


@pytest.mark.parametrize("eid", sorted(M3_GOLDEN), ids=sorted(M3_GOLDEN))
def test_m3_class_and_guard_level(eid):
    idx, _ = _index()
    kind, record = idx[eid]
    assert kind == "corpus"
    cls, subclass, guard = M3_GOLDEN[eid]
    assert record["class"] == cls
    assert record["subclass"] == subclass
    assert record["guardLevel"] == guard


def test_m3_distribution_within_tolerance():
    """M3 acceptance: class distribution within +-10% of the FUNGRIM.md SS1
    measured taxonomy (properties live in properties.json, not the corpus)."""
    from collections import Counter
    _, result = _index()
    counts = Counter()
    for records in result["corpus"].values():
        for r in records:
            counts[r["class"]] += 1
    expected = {
        "identity": 1185,
        "specific-value": 437,
        "representation": 424,
        "inequality": 248,
        "logical": 194,
    }
    for cls, exp in expected.items():
        assert abs(counts[cls] - exp) <= 0.10 * exp, (
            f"{cls}: got {counts[cls]}, expected {exp} +-10%")
    assert counts["other"] <= 5  # near-zero (upstream source artifacts)


def test_totality_and_skip_budget():
    """Plan §2.4: every entry lands somewhere; zero unknown heads; skip
    ledger <= ~10% of formula entries."""
    _, result = _index()
    corpus_count = sum(len(v) for v in result["corpus"].values())
    n = (corpus_count + len(result["properties"]) + len(result["skipped"]))
    assert n == result["totalEntries"]
    unknown = [r for r in result["skipped"] if r["reason"] == "unknown-head"]
    assert unknown == []
    formula_skips = [r for r in result["skipped"]
                     if r["reason"] != "symbol-definition"]
    assert len(formula_skips) <= 0.10 * result["formulaEntries"]
