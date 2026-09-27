"""CLI: python3 -m grim2mathjson --out <dir> [--topic atan] [--strict]"""

import argparse
import os
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="grim2mathjson",
        description="Translate the Fungrim corpus (pygrim) to MathJSON.")
    parser.add_argument(
        "--out",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "out"),
        help="output directory (default: grim2mathjson/out)")
    parser.add_argument(
        "--topic",
        default=None,
        help="restrict to one topic module (e.g. atan)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail (exit 1) if any entry hits the catch-all unknown-head"
             " or the shell table leaves a corpus head uncovered")
    parser.add_argument(
        "--ce-known",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "ce-known-symbols.txt"),
        help="CE-known-symbols oracle (regenerate with"
             " `npx tsx grim2mathjson/gen_ce_known.ts`); declarations.json"
             " is skipped when the file is missing")
    args = parser.parse_args(argv)

    # Make the Fungrim snapshot importable regardless of cwd.
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root not in sys.path:
        sys.path.insert(0, root)

    from pygrim.formulas import all_entries  # noqa: E402 (slow import)
    from . import emit, report

    formulas_dir = os.path.join(root, "pygrim", "formulas")
    result = emit.build(all_entries, formulas_dir, only_topic=args.topic)

    if args.topic is not None and not result["corpus"] \
            and not result["properties"] and not result["skipped"]:
        print(f"error: no entries found for topic '{args.topic}'",
              file=sys.stderr)
        return 2

    os.makedirs(args.out, exist_ok=True)
    emit.write(result, args.out)

    # M4 shell-declaration table (full runs only: the census must see the
    # whole corpus to be authoritative).
    uncovered = []
    if args.topic is not None:
        print("note: --topic run, skipping declarations.json")
    elif not os.path.exists(args.ce_known):
        print(f"warning: {args.ce_known} not found -- skipping "
              "declarations.json", file=sys.stderr)
    else:
        from . import shells
        with open(args.ce_known) as f:
            ce_known = set(f.read().split())
        doc, uncovered = shells.build(result, all_entries, ce_known)
        shells.write(doc, args.out)
        ssum = shells.summarize(doc)
        print(f"  declarations:   {ssum['shellCount']} shells"
              f" ({ssum['withDomainTable']} with domain tables),"
              f" {ssum['existingCount']} CE-known heads audited")
        print(f"    signature sources: "
              + ", ".join(f"{k} {v}"
                          for k, v in ssum["signatureSources"].items()))
        if uncovered:
            print(f"  UNCOVERED HEADS ({len(uncovered)}):"
                  f" {', '.join(uncovered)}")

    summary = report.summarize(result)
    report.write_report(summary, args.out)
    report.print_summary(summary)

    if args.strict and summary["unknownHeads"]:
        print("strict mode: unknown heads present -- failing", file=sys.stderr)
        return 1
    if args.strict and uncovered:
        print("strict mode: uncovered shell heads present -- failing",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
