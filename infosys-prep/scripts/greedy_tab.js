// Greedy tab (separate section): Kumar K list (sheet 1q–90q) first, then the Codeforces list
const KK = D.kgreedy || [];
const kkStateCls = {Solved: 'ok', OPEN: 'warn', Partial: 'warn'};
function kkTitle(r) { return r.brief.length > 70 ? r.brief.slice(0, 67).replace(/\s+\S*$/, '') + '…' : r.brief; }
function renderKk(r) {
  const d = el('details', 'item');
  const s = el('summary');
  s.append(el('span', 'badge', r.sheet_id), el('span', 't', kkTitle(r)));
  if (r.rating) s.append(el('span', 'badge', 'Rating ' + r.rating), el('span', 'badge', 'Match ' + r.match_pct + '%'), el('span', 'badge', 'Pred ' + r.prediction_index));
  s.append(el('span', 'badge', 'Kumar K'), el('span', 'badge ' + (kkStateCls[r.state] || ''), r.state));
  d.append(s);
  const b = el('div', 'body');
  if (r.topics.length) b.append(el('p', 'meta', 'Topics: ' + r.topics.join(', ') + (r.rating ? ' · Rating is an estimate on the Codeforces scale' : '')));
  if (r.patterns.length) b.append(el('p', 'meta', 'Patterns: ' + r.patterns.join(', ')));
  if (r.nearest_infosys_question) b.append(el('p', 'meta', 'Closest Infosys question: ' + r.nearest_infosys_question));
  section(b, 'Brief', r.brief);
  section(b, 'Key idea', r.key_idea);
  section(b, 'Solution steps', r.steps);
  section(b, 'Complexity', r.complexity);
  section(b, 'Dry run', r.dry_run, true);
  if (r.code) {
    section(b, r.code_lang, r.code, true);
    b.append(el('p', 'meta', 'From ' + r.code_file + ' in the repo.'));
  } else if (r.state === 'Solved') {
    b.append(el('p', 'meta', 'No separate code file for this item.'));
  }
  section(b, 'How it was checked', r.verification);
  section(b, 'Mapping', 'External: ' + r.external_mapping + '\nInfosys DB: ' + r.infosys_mapping);
  section(b, 'Status', r.status);
  d.append(b);
  return d;
}
function ratingOk(v, rat) {
  if (rat === '') return true;
  if (!v) return false;
  if (rat === '0') return v < 1400;
  const lo = +rat; return v >= lo && v < lo + 200;
}
function kkMatch(r, st) {
  if (st.pat && !r.patterns.includes(st.pat)) return false;
  if (!ratingOk(r.rating, st.rat)) return false;
  if (st.q && ![r.sheet_id, r.brief, r.patterns, r.sheet_patterns, r.nearest_infosys_question, r.external_mapping, r.status].join(' ').toLowerCase().includes(st.q)) return false;
  return true;
}
function sortBy(list, how) {
  if (how === 'pred') return list.slice().sort((a, b) => b.prediction_index - a.prediction_index);
  if (how === 'match') return list.slice().sort((a, b) => b.match_pct - a.match_pct);
  if (how === 'rating') return list.slice().sort((a, b) => (a.rating || 1e9) - (b.rating || 1e9));
  return list;
}
function fillPatterns(sel, items) {
  [...new Set(items.flatMap(q => q.patterns))].sort().forEach(p => { const o = el('option', '', p); o.value = p; sel.append(o); });
}

(function(){
  const G = D.greedy;
  const gp = document.getElementById('gr-pat');
  fillPatterns(gp, G.concat(KK));
  const st = {q: '', pat: '', rat: '', sort: 'list', src: ''};
  function filt() {
    const kk = st.src === 'cf' ? [] : KK.filter(r => kkMatch(r, st));
    const cf = st.src === 'kk' ? [] : G.filter(q => {
      if (st.pat && !q.patterns.includes(st.pat)) return false;
      if (!ratingOk(+q.rating, st.rat)) return false;
      if (st.q && !(q.cf_id + ' ' + q.name + ' ' + q.patterns + ' ' + q.nearest_infosys_question + ' ' + q.tags).toLowerCase().includes(st.q)) return false;
      return true;
    });
    return sortBy(kk.concat(cf), st.sort);
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
