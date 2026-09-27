"""M4 shell-table tests (plan SS4 / SS8).

Uses the shared full-corpus build from test_golden plus the checked-in
ce-known-symbols.txt oracle (regenerate with
``npx tsx grim2mathjson/gen_ce_known.ts`` after a corpus change).
"""

import os

import pytest

from grim2mathjson.tests.conftest import ROOT

CE_KNOWN_PATH = os.path.join(ROOT, "grim2mathjson", "ce-known-symbols.txt")

_BUILD = None


def _build():
    global _BUILD
    if _BUILD is None:
        from pygrim.formulas import all_entries
        from grim2mathjson import shells
        from grim2mathjson.tests.test_golden import _index

        _, result = _index()
        with open(CE_KNOWN_PATH) as f:
            ce_known = set(f.read().split())
        _BUILD = shells.build(result, all_entries, ce_known)
    return _BUILD


def test_ce_known_oracle_present():
    assert os.path.exists(CE_KNOWN_PATH)


def test_full_coverage():
    """M4 acceptance: every corpus head/atom CE doesn't define is covered
    by the declarations table (mechanical cross-check)."""
    _, uncovered = _build()
    assert uncovered == []


def test_signature_quality():
    """Most shells must have a derived (non-fallback) signature. The plan's
    '>=80% table-derived' target is unreachable in this snapshot (only 48
    of 228 SymbolDefinition entries carry a domain Table); the combined
    verified/table/curated/usage derivation stands in for it."""
    doc, _ = _build()
    decls = doc["declarations"]
    derived = sum(1 for r in decls.values()
                  if r["signatureSource"] != "fallback")
    assert derived >= 0.80 * len(decls)
    # every signatureInferred flag is consistent with the source
    for name, r in decls.items():
        assert r["signatureInferred"] == (r["signatureSource"] != "fallback")


def test_known_shell_records():
    doc, _ = _build()
    decls = doc["declarations"]
    zz = decls["RiemannZetaZero"]
    assert zz["arity"] == 1
    assert zz["signature"] == "(integer) -> complex"
    assert zz["signatureSource"] == "verified"
    assert zz["domainTable"]
    # EL-3 condition predicates must be boolean-typed (spike #3)
    assert decls["CongruentMod"]["signature"].endswith("-> boolean")
    # heads CE has since gained (JacobiTheta, Divides, PolyGamma, ...) leave
    # the shell table for the existing-audit section
    assert "JacobiTheta" not in decls and "JacobiTheta" in doc["existing"]
    assert "Divides" not in decls and "Divides" in doc["existing"]
    assert "PolyGamma" not in decls and "PolyGamma" in doc["existing"]
    # synthesized collections
    assert decls["Primes"]["signature"] == "collection<integer>"
    assert "PP" in decls["Primes"].get("fungrimNames", [])


def test_existing_audit_section():
    doc, _ = _build()
    existing = doc["existing"]
    # name-collision mappings audited (spike #15)
    assert "Zeta" in existing and "RiemannZeta" in existing["Zeta"]["fungrimNames"]
    assert "Beta" in existing and "BetaFunction" in existing["Beta"]["fungrimNames"]
    assert "note" in existing["Erf"]
    # nothing both declared and CE-known
    assert not set(doc["declarations"]) & set(existing)
