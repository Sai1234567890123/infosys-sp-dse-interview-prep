
// Study plan (per-viewer ticks in localStorage)
(function(){
  const KEY = 'infosys-plan-v1';
  let done = {};
  try { done = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) {}
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) {} };
  const cfUrl = id => { const m = id.match(/^(\d+)([A-Z]\d?)$/); return m ? 'https://codeforces.com/problemset/problem/' + m[1] + '/' + m[2] : ''; };
  const start = new Date(2026, 9, 23), exam = new Date(2026, 10, 22);
  const days = Math.round((exam - start) / 864e5) + 1;
  $('plan-left').textContent = days - 1 + ' days until the exam on 22 November 2026';
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const list = $('plan-list');
  for (let d = 0; d < days; d++) {
    const date = new Date(start); date.setDate(start.getDate() + d);
    const tasks = [];
    for (let k = 0; k < 3; k++) {
      const q = top[d * 3 + k];
      if (q) tasks.push({ id: 'cf' + (d * 3 + k), text: 'CF ' + q.cf_id + ' ' + q.name + ' (' + q.rating + ')', url: cfUrl(q.cf_id) });
    }
    tasks.push({ id: 'lc' + d, text: '1 LeetCode problem, submitted on leetcode.com' });
    if (date.getDay() === 2 || date.getDay() === 6) tasks.push({ id: 'mock' + d, text: 'Timed set: 3 Infosys-style questions, then explain aloud and compare with the dry run' });
    if (d === 0) tasks.push({ id: 'low', text: 'Review low-confidence entries in the Greedy tab first (they have no C++)' });
    const card = el('div', 'card plan-day' + (date.getTime() === today.getTime() ? ' today' : ''));
    card.append(el('b', '', date.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' })));
    tasks.forEach(t => {
      const row = el('label', 'plan-task');
      const cb = document.createElement('input'); cb.type = 'checkbox'; cb.checked = !!done[t.id];
      cb.addEventListener('change', () => { done[t.id] = cb.checked; save(); });
      row.append(cb);
      if (t.url) { const a = el('a', '', t.text); a.href = t.url; a.target = '_blank'; a.rel = 'noopener'; row.append(a); }
      else row.append(el('span', '', t.text));
      card.append(row);
    });
    list.append(card);
  }
})();
