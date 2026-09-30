// Exercise the actual inline modeling code without adding runtime dependencies.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const template = fs.readFileSync(path.join(__dirname, '../src/template.html'), 'utf8');
const modelCode = template.split('// ---------- model the data ----------')[1].split('// ---------- state ----------')[0];
const DAY = 864e5;
const parse = (s) => Date.parse(s.length === 7 ? s + '-01' : s);
function model(rows) {
  const ctx = { DATA: rows.map(x=>({ c:'test', lane:'test',t:'flagship',...x })),
    COMPANIES:[{k:'test'}],CO:{test:{}},TYPE_NAME:{flagship:'旗舰'},DAY,parse,
    T0:parse('2018-01-01'),TODAY:parse('2026-09-30') };
  vm.runInNewContext(modelCode,ctx);
  return ctx;
}
let c=model([{m:'A',d:'2026-09-01'},{m:'B',d:'2026-09-15',verification:'unverified'},{m:'C',d:'2026-09-20'}]);
assert.equal(c.items[0].next.m,'C');assert.equal(c.items[0].days,19);
c=model([{m:'A',d:'2026-09-01',end:'2026-09-10'},{m:'B',d:'2026-09-15'}]);
assert.equal(c.items[0].next,null);assert.equal(c.items[0].e,parse('2026-09-10'));
c=model([{m:'A',d:'2026-09-01',end:'2026-09-25'},{m:'B',d:'2026-09-15'}]);
assert.equal(c.items[0].next.m,'B');assert.equal(c.items[0].e,parse('2026-09-15'));
c=model([{m:'A',d:'2026-09-01',end:'2026-10-05'}]);
assert.equal(c.items[0].ongoing,true);assert.equal(c.items[0].e,parse('2026-09-30'));
c=model([{m:'A',d:'2026-09-30'},{m:'B',d:'2026-09-30'}]);
assert.equal(c.items[0].days,0);assert.equal(c.structure[0].rows.length,2);
c=model([{m:'A',d:'2026-09-01',lane:'image'},{m:'B',d:'2026-09-15',lane:'video'}]);
assert.equal(c.items[0].ongoing,true);assert.equal(c.items[0].next,null);
assert.match(template,/if \(it.unverified\) ops.push\(\{ k: "b"/);
assert.match(template,/ctx.setLineDash\(\[3, 2\]\)/);
assert.match(template,/stroke-dasharray="3 2"/);
assert.ok(template.indexOf('.bar.dim {')>template.indexOf('.bar.unverified {'));
new vm.Script(template.split('<script>')[1].split('</script>')[0]);
console.log('Timeline succession, same-day siblings, independent lanes, export uncertainty and JS syntax: passed');
