// Kumar K greedy tab: greedy-pattern sheet records, with the same filters and cards as the Codeforces DP tab
(function(){
  const G = KK.filter(r => r.is_greedy);
  const kp = document.getElementById('kg-pat');
  fillPatterns(kp, G);
  const st = {q: '', pat: '', rat: '', sort: 'list'};
  let pager = null;
  function refresh() { pager = paged(document.getElementById('kg-list'), document.getElementById('kg-count'), document.getElementById('kg-more'), sortBy(G.filter(r => kkMatch(r, st)), st.sort), renderKk); }
  document.getElementById('kg-more').addEventListener('click', () => pager.reset());
  document.getElementById('kg-q').addEventListener('input', e => { st.q = e.target.value.trim().toLowerCase(); refresh(); });
  kp.addEventListener('change', e => { st.pat = e.target.value; refresh(); });
  document.getElementById('kg-rat').addEventListener('change', e => { st.rat = e.target.value; refresh(); });
  document.getElementById('kg-sort').addEventListener('change', e => { st.sort = e.target.value; refresh(); });
  refresh();
})();
