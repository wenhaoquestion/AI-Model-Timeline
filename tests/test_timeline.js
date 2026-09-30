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
c=model([{m:'Dated',d:'2026-09-01'},{m:'Month only',d:'2026-09',verification:'unverified'},{m:'Undated',d:null,verification:'unverified'}]);
assert.equal(c.items.length,3);
assert.equal(c.items[1].s,null);assert.equal(c.items[2].s,null);
assert.equal(c.structure[0].rows.flatMap(r=>r.items).length,1);
assert.equal(c.items[0].next,null);

const packingCode=template.split('// ---------- layout (depends on zoom) ----------')[1].split('var hoverLine')[0];
const packing={};vm.runInNewContext(packingCode,packing);
// A 0/1/7-day release must keep its label, regardless of time scale or viewport width.
for (const viewWidth of [375,390,720,1188,1440]) {
  for (const ppd of [0.12,(viewWidth-108)/1460,14]) {
    const entries=[{x:0,width:110},{x:ppd,width:125},{x:7*ppd,width:110},{x:27*ppd,width:130}];
    const packed=packing.packLabels(entries);
    assert.equal(packed.slots.length,entries.length);
    for(let i=0;i<entries.length;i++)for(let j=i+1;j<entries.length;j++){
      if(packed.slots[i]===packed.slots[j]) assert.ok(entries[i].x+entries[i].width+8<=entries[j].x);
    }
  }
}
assert.ok(!template.includes('color: transparent; padding: 0'));
assert.ok(!template.includes('if (bw >= 26) text'));

const searchCode=template.split('function searchKey(text)')[1].split('function visible(it)')[0];
const search={state:{q:'GPT6Sol'},CO:{test:{name:'OpenAI',sub:'GPT'}}};
vm.runInNewContext('function searchKey(text)'+searchCode,search);
assert.equal(search.matchQ({c:'test',m:'GPT-6 Sol',lane:'GPT Sol',aliases:[]}),true);
search.state.q='GPT-6 Sol / Luna';
assert.equal(search.matchQ({c:'test',m:'GPT-6 Sol',lane:'GPT Sol',aliases:['GPT-6 Sol / Luna']}),true);
assert.match(template,/tl\.scrollTop \+= br\.top - tr\.top - 64/);
assert.match(template,/if \(it.unverified\) ops.push\(\{ k: "b"/);
assert.match(template,/ctx.setLineDash\(\[3, 2\]\)/);
assert.match(template,/stroke-dasharray="3 2"/);
assert.ok(template.indexOf('.bar.dim {')>template.indexOf('.bar.unverified {'));
new vm.Script(template.split('<script>')[1].split('</script>')[0]);
console.log('Timeline succession, undated catalog, label collision packing at mobile/desktop widths, search aliases, export labels and JS syntax: passed');
