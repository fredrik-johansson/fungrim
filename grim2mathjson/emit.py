"""Per-topic JSON corpus emission with deterministic ordering.

Output layout (plan §3.1):

    <out>/corpus/<topic>.json    one file per pygrim/formulas source module
    <out>/properties.json        analytic-property records (spike #12)
    <out>/skipped.json           skip ledger (plan §2.4 totality)
    <out>/report.json            summary statistics (report.py)

Determinism: stable key order (dict insertion), entries sorted by ID within
topic, topics sorted by name, indent=1, ASCII-only, "\\n" line endings,
trailing newline -- regeneration is byte-identical when nothing changed.
"""

import json
import os
import re

from . import classify
from . import mapping
from . import properties
from . import walker
from . import __version__

GENERATOR = f"grim2mathjson {__version__}"


# ---------------------------------------------------------------------------
# Entry access helpers (pygrim Entry args)
# ---------------------------------------------------------------------------

def _get_part(entry, head_name):
    for a in entry.args():
        if not a.is_atom():
            h = a.head()
            if h.is_atom() and h.is_symbol() and h._symbol == head_name:
                return a
    return None


def entry_id(entry):
    part = _get_part(entry, "ID")
    return part.args()[0]._text if part is not None else None


# ---------------------------------------------------------------------------
# Topic attribution: entry id -> defining module / referencing modules
# ---------------------------------------------------------------------------

_HEX_RE = re.compile(r'"([0-9a-f]{6})"')
_TITLE_RE = re.compile(r'Title\("([^"]*)"\)')


def module_index(formulas_dir, valid_ids):
    """Scan pygrim/formulas/*.py sources. Returns (home, refs, titles):
    home[id] = defining module (the one containing ID("id")),
    refs[id]  = set of modules whose def_Topic blocks reference id,
    titles[m] = first Title("...") in module m."""
    home, refs, titles = {}, {}, {}
    id_re = re.compile(r'ID\("([0-9a-f]{6})"\)')
    for fname in sorted(os.listdir(formulas_dir)):
        if not fname.endswith(".py") or fname == "__init__.py":
            continue
        mod = fname[:-3]
        with open(os.path.join(formulas_dir, fname)) as f:
            text = f.read()
        for m in id_re.finditer(text):
            home[m.group(1)] = mod
        for m in _HEX_RE.finditer(text):
            if m.group(1) in valid_ids:
                refs.setdefault(m.group(1), set()).add(mod)
        tm = _TITLE_RE.search(text)
        titles[mod] = tm.group(1) if tm else None
    return home, refs, titles


# ---------------------------------------------------------------------------
# Per-entry translation
# ---------------------------------------------------------------------------

def translate_entry(entry, eid, topic, topics):
    """Translate one pygrim Entry. Returns a 4-tuple
    ("corpus"|"property"|"skip", record_dict, ctx_or_None, warning_or_None)."""
    formula_part = _get_part(entry, "Formula")
    if formula_part is None:
        return ("skip", _skip_record(eid, topic, "symbol-definition", [], ""),
                None, None)
    formula = formula_part.args()[0]

    assumptions_part = _get_part(entry, "Assumptions")
    references_part = _get_part(entry, "References")
    variables_part = _get_part(entry, "Variables")

    references = None
    if references_part is not None:
        references = [a._text for a in references_part.args() if a.is_text()]

    # --- property route (spike #12) ----------------------------------------
    if properties.is_property_entry(formula):
        ctx = walker.Ctx()
        try:
            rec = properties.route_property_entry(formula, ctx)
            assumptions, alternatives = _walk_assumptions(assumptions_part,
                                                          ctx)
        except walker.TranslationSkip as exc:
            return ("skip", _skip_record(eid, topic, exc.reason, exc.heads,
                                         str(formula)), None, None)
        except walker.UnknownHeadError as exc:
            return ("skip", _skip_record(eid, topic, "unknown-head",
                                         [exc.head], str(formula)), None, None)
        record = {"id": eid}
        record.update(rec)
        record["assumptions"] = assumptions
        if alternatives:
            record["assumptionAlternatives"] = alternatives
        record["topics"] = topics
        return ("property", record, ctx, None)

    # --- corpus route -------------------------------------------------------
    fctx = walker.Ctx()
    try:
        formula_json = walker.walk(formula, fctx)
    except walker.TranslationSkip as exc:
        return ("skip", _skip_record(eid, topic, exc.reason, exc.heads,
                                     str(formula)), None, None)
    except walker.UnknownHeadError as exc:
        return ("skip", _skip_record(eid, topic, "unknown-head", [exc.head],
                                     str(formula)), None, None)

    actx = walker.Ctx()
    try:
        assumptions_json, alternatives_json = \
            _walk_assumptions(assumptions_part, actx)
    except walker.TranslationSkip as exc:
        rec = _skip_record(eid, topic, exc.reason, exc.heads,
                           str(assumptions_part))
        rec["in"] = "assumptions"
        return ("skip", rec, None, None)
    except walker.UnknownHeadError as exc:
        rec = _skip_record(eid, topic, "unknown-head", [exc.head],
                           str(assumptions_part))
        rec["in"] = "assumptions"
        return ("skip", rec, None, None)

    variables, var_warning = _entry_variables(formula, variables_part)

    # The annotation flags describe the whole entry: merge the assumptions
    # context into the formula context (heads stays formula-only).
    for fl in actx.flavors:
        fctx.add_flavor(fl)
    fctx.directed_infinity |= actx.directed_infinity
    fctx.indexed_families |= actx.indexed_families

    flavor = None
    if len(fctx.flavors) == 1:
        flavor = fctx.flavors[0]
    elif fctx.flavors:
        flavor = list(fctx.flavors)

    # M3 annotations. Classifier errors are deliberate hard failures: a new
    # head must be added to the classify.py tables, never guessed.
    # guardLevel describes the PRIMARY assumption set only (alternatives are
    # informative; consumers wanting them must classify per-alternative).
    entry_class, subclass = classify.classify_class(formula_json, variables)
    guard_level = classify.classify_guard_level(assumptions_json)

    record = {
        "id": eid,
        "formula": formula_json,
        "variables": variables,
        "assumptions": assumptions_json,
        "class": entry_class,
        "subclass": subclass,
        "heads": sorted(fctx.heads - walker.NOISE_HEADS),
        "guardLevel": guard_level,
        "flavor": flavor,
        "references": references,
        "topics": topics,
    }
    if alternatives_json:
        # Optional field, inserted after "assumptions" for schema locality.
        items = list(record.items())
        i = [k for k, _ in items].index("assumptions") + 1
        items.insert(i, ("assumptionAlternatives", alternatives_json))
        record = dict(items)
    if fctx.directed_infinity:
        record["directedInfinity"] = True
    if fctx.indexed_families:
        record["indexedFamilies"] = sorted(fctx.indexed_families)

    # merge shell usage for the report
    fctx.shells |= actx.shells
    return ("corpus", record, fctx, var_warning)


def _walk_assumptions(assumptions_part, ctx):
    """Translate an Assumptions(...) part. Returns (primary, alternatives).

    Fungrim's ``Assumptions(expr, alt_expr, ...)`` with multiple args states
    ALTERNATIVE assumption sets (pygrim renders args past the first as
    "Alternative assumptions"; see FUNGRIM.md SS1) -- the formula holds under
    each set independently. They must NOT be joined with And: 16 entries
    (e.g. sqrt/0d8e03) produce genuinely contradictory conjunctions that way.
    The first set is the entry's primary ``assumptions``; the rest are
    emitted under the optional ``assumptionAlternatives`` field.
    """
    if assumptions_part is None or not assumptions_part.args():
        return (None, None)
    walked = [walker.walk(a, ctx) for a in assumptions_part.args()]
    return (walked[0], walked[1:] or None)


def _entry_variables(formula, variables_part):
    """Variables from free_variables(), cross-checked against the declared
    Variables(...). Returns (sorted names, warning_or_None)."""
    declared = []
    if variables_part is not None:
        declared = [walker.sym_name(v) for v in variables_part.args()
                    if v.is_atom() and v.is_symbol()]
    try:
        fv = sorted(walker.sym_name(v) for v in formula.free_variables()
                    if v.is_symbol())
    except Exception:
        return (sorted(set(declared)), "free-variables-failed")
    warning = None
    if set(fv) != set(declared):
        warning = (f"variables mismatch: declared={sorted(set(declared))} "
                   f"free={fv}")
    return (fv, warning)


def _skip_record(eid, topic, reason, heads, source):
    return {
        "id": eid,
        "topic": topic,
        "reason": reason,
        "heads": sorted(set(heads or [])),
        "source": source,
    }


# ---------------------------------------------------------------------------
# Corpus build + write
# ---------------------------------------------------------------------------

def build(entries, formulas_dir, only_topic=None):
    """Translate every entry. Returns a result dict consumed by report.py
    and write()."""
    valid_ids = set()
    for e in entries:
        eid = entry_id(e)
        if eid:
            valid_ids.add(eid)
    home, refs, titles = module_index(formulas_dir, valid_ids)

    corpus = {}      # topic -> [entry records]
    props = []
    skipped = []
    shells = set()
    warnings = []
    n_formula = 0

    for e in entries:
        eid = entry_id(e)
        topic = home.get(eid, "_unattributed")
        if only_topic is not None and topic != only_topic:
            continue
        topics = sorted(refs.get(eid, {topic}))
        if _get_part(e, "Formula") is not None:
            n_formula += 1
        kind, record, ctx, warning = translate_entry(e, eid, topic, topics)
        if warning:
            warnings.append(f"{eid}: {warning}")
        if ctx is not None:
            shells |= ctx.shells
        if kind == "skip":
            skipped.append(record)
        elif kind == "property":
            props.append(record)
        else:
            corpus.setdefault(topic, []).append(record)

    for topic in corpus:
        corpus[topic].sort(key=lambda r: r["id"])
    props.sort(key=lambda r: r["id"])
    skipped.sort(key=lambda r: (r["id"] or ""))

    return {
        "corpus": corpus,
        "properties": props,
        "skipped": skipped,
        "shells": sorted(shells),
        "warnings": sorted(warnings),
        "titles": titles,
        "formulaEntries": n_formula,
        "totalEntries": sum(1 for e in entries
                            if only_topic is None
                            or home.get(entry_id(e)) == only_topic),
    }


def _dump(path, obj):
    with open(path, "w", newline="\n") as f:
        json.dump(obj, f, indent=1, ensure_ascii=True)
        f.write("\n")


def write(result, outdir):
    corpus_dir = os.path.join(outdir, "corpus")
    os.makedirs(corpus_dir, exist_ok=True)
    for topic in sorted(result["corpus"]):
        _dump(os.path.join(corpus_dir, f"{topic}.json"), {
            "topic": topic,
            "title": result["titles"].get(topic),
            "source": f"pygrim/formulas/{topic}.py",
            "generator": GENERATOR,
            "entries": result["corpus"][topic],
        })
    _dump(os.path.join(outdir, "properties.json"), {
        "generator": GENERATOR,
        "entries": result["properties"],
    })
    _dump(os.path.join(outdir, "skipped.json"), {
        "generator": GENERATOR,
        "skipped": result["skipped"],
    })
