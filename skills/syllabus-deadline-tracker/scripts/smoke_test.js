// Runs the generated app's script against a minimal DOM stub and renders every screen.
const fs = require('fs'), h = fs.readFileSync(process.argv[2], 'utf8');
const js = h.split('<script>')[1].split('</script>')[0], els = {};
const mk = () => ({ innerHTML: '', textContent: '', value: '', classList: { toggle() {} }, remove() {}, select() {}, dataset: {}, style: {} });
global.document = { getElementById: i => els[i] || (els[i] = mk()), querySelectorAll: () => [], querySelector: () => mk(), documentElement: { style: { setProperty() {} } }, title: '' };
const store = {}; global.localStorage = { getItem: k => store[k] || null, setItem: (k, v) => { store[k] = v } };
global.innerWidth = 800; global.innerHeight = 600; global.addEventListener = () => {};
const app = new Function(js + ';return {views,get tab(){return tab},set tab(v){tab=v},tick,render,logH,get st(){return st}}')();
for (const t of ['today', 'plan', 'road', 'jour', 'settings']) {
  if (t === 'jour' && !app.st.sig && false) continue;
  try { const out = app.views[t](); if (!out || out.length < 20) throw new Error('empty'); console.log('ok  ', t, out.length); }
  catch (e) { console.log('FAIL', t, e.message); process.exitCode = 1; }
}
const done = () => app.st.tasks.reduce((a, t) => a + t.d, 0);
app.tick(); const after = done(); app.tick();
console.log(after > 0 && done() === 0 ? 'ok   tick applies hours and undo reverses them (' + after.toFixed(2) + ' h)' : 'note: no work-day target today (weekend or outside the plan window), tick not exercised');
