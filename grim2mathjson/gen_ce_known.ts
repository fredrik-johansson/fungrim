// M4: generate ce-known-symbols.txt — the oracle of symbol names the
// Compute Engine already defines, used by shells.py to decide which corpus
// heads need a shell declaration (plan §4 "Filtering").
//
// Candidates are every string occurring anywhere in the emitted corpus +
// properties JSON (heads, atoms, variables alike; {"str"./"num".} payloads
// excluded). A name is "CE-known" iff ce.lookupDefinition(name) finds a
// definition in a fresh engine. The output keeps the two repos decoupled:
// shells.py only reads the text file, never the CE source.
//
// Run (from anywhere):
//   npx tsx /Users/arno/dev/fungrim-master/grim2mathjson/gen_ce_known.ts
import { ComputeEngine } from '/Users/arno/dev/compute-engine/src/compute-engine';
import * as fs from 'node:fs';
import * as path from 'node:path';

const OUT_DIR = path.join(__dirname, 'out');
const TARGET = path.join(__dirname, 'ce-known-symbols.txt');

const names = new Set<string>();

function scan(x: unknown): void {
  if (typeof x === 'string') {
    names.add(x);
  } else if (Array.isArray(x)) {
    for (const y of x) scan(y);
  } else if (x && typeof x === 'object') {
    for (const [k, v] of Object.entries(x)) {
      // {"str": ...} text and {"num": ...} digit payloads are not symbols;
      // metadata string values (ids, topics, reasons, ...) are filtered by
      // scanning only expression-bearing fields below.
      if (k === 'str' || k === 'num') continue;
      scan(v);
    }
  }
}

const EXPR_FIELDS = [
  'formula',
  'assumptions',
  'assumptionAlternatives',
  'expr',
  'domain',
  'point',
  'path',
  'condition',
  'value',
];

for (const file of fs.readdirSync(path.join(OUT_DIR, 'corpus'))) {
  const data = JSON.parse(
    fs.readFileSync(path.join(OUT_DIR, 'corpus', file), 'utf8')
  );
  for (const e of data.entries)
    for (const f of EXPR_FIELDS) if (f in e) scan(e[f]);
}
{
  const props = JSON.parse(
    fs.readFileSync(path.join(OUT_DIR, 'properties.json'), 'utf8')
  );
  for (const e of props.entries) {
    for (const f of EXPR_FIELDS) if (f in e) scan(e[f]);
    if (e.operator) names.add(e.operator);
  }
}

const ce = new ComputeEngine();
const known: string[] = [];
for (const name of [...names].sort()) {
  try {
    if (ce.lookupDefinition(name) !== undefined) known.push(name);
  } catch {
    /* not a valid symbol name — not known */
  }
}

fs.writeFileSync(TARGET, known.join('\n') + '\n');
console.log(
  `ce-known-symbols.txt: ${known.length} known of ${names.size} candidates`
);
