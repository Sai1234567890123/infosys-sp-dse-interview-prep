// Greedy tab (separate section): Kumar K list (sheet 1q–90q) first, then the Codeforces list
(function(){
  const G = D.greedy, K = D.kgreedy || [];
  const gp = document.getElementById('gr-pat');
  const pats = [...new Set(G.concat(K).flatMap(q => q.patterns))].sort();
  pats.forEach(p => { const o = document.createElement('option'); o.value = p; o.textContent = p; gp.append(o); });
  const st = {q: '', pat: '', rat: '', sort: 'list', src: ''};
  const stateCls = {Solved: 'ok', OPEN: 'warn', Partial: 'warn'};
  function renderKk(r) {
    const d = el('details', 'item');
    const s = el('summary');
    const title = r.brief.length > 70 ? r.brief.slice(0, 67).replace(/\s+\S*$/, '') + '…' : r.brief;
    s.append(el('span', 'badge', r.sheet_id), el('span', 't', title));
    s.append(el('span', 'badge', 'Kumar K'), el('span', 'badge ' + (stateCls[r.state] || ''), r.state));
    d.append(s);
    const b = el('div', 'body');
    if (r.patterns.length) b.append(el('p', 'meta', 'Patterns: ' + r.patterns.join(', ')));
    section(b, 'Brief', r.brief);
    section(b, 'Solution', r.solution);
    section(b, 'Check', r.verification);
    section(b, 'Mapping', 'External: ' + r.external_mapping + '\nInfosys DB: ' + r.infosys_mapping);
    section(b, 'Status', r.status);
    if (r.code) {
      section(b, r.code_lang, r.code, true);
      b.append(el('p', 'meta', 'From ' + r.code_file + ' in the repo.'));
    } else if (r.state === 'Solved') {
      b.append(el('p', 'meta', 'No separate code file for this item.'));
    }
    d.append(b);
    return d;
  }
  function hit(text) { return text.toLowerCase().includes(st.q); }
  function filt() {
    let kk = st.src === 'cf' || st.rat ? [] : K.filter(r => {
      if (st.pat && !r.patterns.includes(st.pat)) return false;
      if (st.q && !hit([r.sheet_id, r.brief, r.patterns, r.external_mapping, r.infosys_mapping, r.status].join(' '))) return false;
      return true;
    });
    let cf = st.src === 'kk' ? [] : G.filter(q => {
      if (st.pat && !q.patterns.includes(st.pat)) return false;
      if (st.rat) { const lo = +st.rat, v = +q.rating; if (v < lo || v >= lo + 200) return false; }
      if (st.q && !hit(q.cf_id + ' ' + q.name + ' ' + q.patterns + ' ' + q.nearest_infosys_question + ' ' + q.tags)) return false;
      return true;
    });
    if (st.sort === 'pred') cf = cf.slice().sort((a, b) => b.prediction_index - a.prediction_index);
    if (st.sort === 'match') cf = cf.slice().sort((a, b) => b.match_pct - a.match_pct);
    if (st.sort === 'rating') cf = cf.slice().sort((a, b) => a.rating - b.rating);
    return kk.concat(cf);
  }
  let pager = null;
  function refresh() { pager = paged(document.getElementById('gr-list'), document.getElementById('gr-count'), document.getElementById('gr-more'), filt(), x => x.sheet_id ? renderKk(x) : renderCf(x)); }
  document.getElementById('gr-more').addEventListener('click', () => pager.reset());
  document.getElementById('gr-q').addEventListener('input', e => { st.q = e.target.value.trim().toLowerCase(); refresh(); });
  gp.addEventListener('change', e => { st.pat = e.target.value; refresh(); });
  document.getElementById('gr-rat').addEventListener('change', e => { st.rat = e.target.value; refresh(); });
  document.getElementById('gr-sort').addEventListener('change', e => { st.sort = e.target.value; refresh(); });
  document.getElementById('gr-src').addEventListener('change', e => { st.src = e.target.value; refresh(); });
  refresh();
})();
