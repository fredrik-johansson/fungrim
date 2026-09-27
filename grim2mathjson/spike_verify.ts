// M0 spike verifier: box every candidate in spike_candidates.json against
// the live Compute Engine. Run from the compute-engine repo:
//   npx tsx /Users/arno/dev/fungrim-master/grim2mathjson/spike_verify.ts
import { ComputeEngine } from '/Users/arno/dev/compute-engine/src/compute-engine';
import * as fs from 'node:fs';
import * as path from 'node:path';

const data = JSON.parse(
  fs.readFileSync(path.join(__dirname, 'spike_candidates.json'), 'utf8')
);

function hasError(e: any): boolean {
  if (e.operator === 'Error') return true;
  if (e.ops) return e.ops.some(hasError);
  return false;
}

let pass = 0;
let fail = 0;

for (const c of data.candidates) {
  // Fresh engine per candidate: avoids cross-candidate declaration clashes.
  const ce = new ComputeEngine();
  for (const [name, type] of Object.entries(data.shells))
    ce.declare(name, type as string);
  if (c.declare)
    for (const [name, type] of Object.entries(c.declare))
      ce.declare(name, type as string);

  try {
    const canon = ce.box(c.json).canonical;
    const err = hasError(canon);
    const rt = ce.box(canon.json);
    const rtOk = rt.isSame(canon);
    const ok = !err && rtOk;
    ok ? pass++ : fail++;
    console.log(
      `#${String(c.item).padStart(2)} ${ok ? 'PASS' : 'FAIL'} [${c.entry}] ${c.label}`
    );
    if (!ok)
      console.log(
        `        canonical: ${JSON.stringify(canon.json).slice(0, 220)}${rtOk ? '' : '  [ROUNDTRIP-DIFF]'}`
      );
  } catch (e: any) {
    fail++;
    console.log(
      `#${String(c.item).padStart(2)} THROW [${c.entry}] ${c.label}: ${e.message?.slice(0, 140)}`
    );
  }
}

console.log('\n--- numeric compatibility (#15) ---');
{
  const ce = new ComputeEngine();
  for (const n of data.numericChecks) {
    const v = ce.box(n.json).N().re;
    const rel = Math.abs(v - n.expect) / Math.abs(n.expect);
    console.log(
      `${rel < 1e-10 ? 'PASS' : 'WARN'} ${n.label}: got ${v} (expected ${n.expect}, rel.err ${rel.toExponential(2)})`
    );
  }
}

console.log(`\n${pass} passed, ${fail} failed of ${data.candidates.length}`);
process.exitCode = fail > 0 ? 1 : 0;
