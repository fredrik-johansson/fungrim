// M4 verification (plan §8): load declarations.json, ce.declare() every
// entry (must raise no errors), then ce.box() a deterministic sample of 20
// corpus entries that use shell heads (no exceptions, no ["Error", ...]
// subexpressions in the canonical form).
//
// Per SPIKE-DECISIONS.md cross-cutting finding #2, entry variables are
// declared with a type inferred from the entry's Element assumptions
// before boxing (symbolic derivative orders / JacobiTheta 4th arguments
// need `integer`).
//
// Run (from anywhere):
//   npx tsx /Users/arno/dev/fungrim-master/grim2mathjson/verify_declarations.ts
import { ComputeEngine } from '/Users/arno/dev/compute-engine/src/compute-engine';
import * as fs from 'node:fs';
import * as path from 'node:path';

const OUT_DIR = path.join(__dirname, 'out');
const decls = JSON.parse(
  fs.readFileSync(path.join(OUT_DIR, 'declarations.json'), 'utf8')
);

// --- stage 1: full declare() pass -----------------------------------------
{
  const ce = new ComputeEngine();
  let ok = 0;
  const failures: string[] = [];
  for (const [name, rec] of Object.entries<any>(decls.declarations)) {
    try {
      ce.declare(name, rec.signature);
      ok++;
    } catch (e: any) {
      failures.push(`${name} (${rec.signature}): ${e.message?.slice(0, 100)}`);
    }
  }
  console.log(
    `declare pass: ${ok}/${Object.keys(decls.declarations).length} ok`
  );
  for (const f of failures) console.log(`  FAIL ${f}`);
  if (failures.length > 0) process.exit(1);
}

// --- stage 2: box a 20-entry sample that uses shell heads ------------------
const shellNames = new Set(Object.keys(decls.declarations));

type Entry = {
  id: string;
  formula: unknown;
  variables: string[];
  assumptions: unknown;
  heads: string[];
};

const entries: Entry[] = [];
for (const file of fs.readdirSync(path.join(OUT_DIR, 'corpus')).sort()) {
  const data = JSON.parse(
    fs.readFileSync(path.join(OUT_DIR, 'corpus', file), 'utf8')
  );
  for (const e of data.entries)
    if (e.heads.some((h: string) => shellNames.has(h))) entries.push(e);
}
entries.sort((a, b) => a.id.localeCompare(b.id));
// deterministic spread: every floor(n/20)-th entry
const step = Math.floor(entries.length / 20);
const sample = Array.from({ length: 20 }, (_, i) => entries[i * step]);

function inferType(dom: unknown): string {
  if (typeof dom === 'string') {
    if (
      [
        'Integers',
        'NonNegativeIntegers',
        'PositiveIntegers',
        'NonPositiveIntegers',
        'Primes',
      ].includes(dom)
    )
      return 'integer';
    if (dom === 'RationalNumbers') return 'rational';
    if (dom === 'RealNumbers') return 'real';
    return 'complex';
  }
  if (Array.isArray(dom)) {
    if (dom[0] === 'Interval') return 'real';
    if (dom[0] === 'Range' || dom[0] === 'Divisors') return 'integer';
    if (dom[0] === 'SetMinus') return inferType(dom[1]);
  }
  return 'complex';
}

function varTypes(e: Entry): Record<string, string> {
  const types: Record<string, string> = {};
  const walk = (x: unknown): void => {
    if (!Array.isArray(x)) return;
    if (x[0] === 'Element' && typeof x[1] === 'string' && x.length >= 3)
      types[x[1]] ??= inferType(x[2]);
    for (const y of x) walk(y);
  };
  walk(e.assumptions);
  walk(e.formula);
  return types;
}

function hasError(e: any): boolean {
  if (e.operator === 'Error') return true;
  if (e.ops) return e.ops.some(hasError);
  return false;
}

let pass = 0;
let fail = 0;
for (const e of sample) {
  // fresh engine per entry: per-entry variable declarations must not clash
  const ce = new ComputeEngine();
  for (const [name, rec] of Object.entries<any>(decls.declarations))
    ce.declare(name, rec.signature);
  const types = varTypes(e);
  for (const v of e.variables) {
    try {
      ce.declare(v, types[v] ?? 'complex');
    } catch {
      /* CE-known inert names (m, s, ...) may reject redeclaration */
    }
  }
  try {
    const canonF = ce.box(e.formula as any).canonical;
    const errF = hasError(canonF);
    let errA = false;
    if (e.assumptions != null)
      errA = hasError(ce.box(e.assumptions as any).canonical);
    const ok = !errF && !errA;
    ok ? pass++ : fail++;
    console.log(`${ok ? 'PASS' : 'FAIL'} [${e.id}] heads: ${e.heads.join(', ')}`);
    if (!ok)
      console.log(
        `     canonical: ${JSON.stringify(canonF.json).slice(0, 220)}`
      );
  } catch (err: any) {
    fail++;
    console.log(`THROW [${e.id}]: ${err.message?.slice(0, 140)}`);
  }
}
console.log(`\nbox sample: ${pass}/${pass + fail} pass`);
process.exit(fail > 0 ? 1 : 0);
