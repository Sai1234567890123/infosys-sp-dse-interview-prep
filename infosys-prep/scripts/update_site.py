import csv, json, re
from openpyxl import load_workbook
csv.field_size_limit(10**9)
D = "/mnt/project-files/infosys-prep/"
OUT = D + "website/index.html"

# greedy problem IDs from the three pasted pages
greedy_ids = []
for f in ["cf/greedy_1400_2100_page1.tsv", "cf/greedy_1400_2100_page2.tsv", "cf/greedy_1500_2100_page3.tsv", "cf/greedy_1600_page4a.tsv", "cf/greedy_1700_page5a.tsv", "cf/greedy_1800_page6a.tsv", "cf/greedy_1900_page7a.tsv", "cf/greedy_remaining_489.tsv"]:
    for l in open(D + f, encoding="utf-8"):
        p = l.split("\t")
        if p and p[0].strip(): greedy_ids.append(p[0].strip())
gset = set(greedy_ids)

def pl(s): return [x.strip() for x in (s or "").split(",") if x.strip()]
keep = ["cf_id","name","rating","tags","patterns","match_pct","nearest_infosys_question","prediction_index","brief","key_idea","solution","complexity","dry_run","cpp","confidence","solved","url"]
rows = []
for q in csv.DictReader(open(D + "cf_dp_scored.csv", encoding="utf-8")):
    r = {k: q.get(k, "") or "" for k in keep}
    r["patterns"] = pl(r["patterns"])
    for k in ("rating", "match_pct", "prediction_index"):
        try: r[k] = int(float(r[k]))
        except Exception: r[k] = 0
    rows.append(r)
dp_ids = {q["cf_id"] for q in csv.DictReader(open(D + "cf/cf_dp_list.csv", encoding="utf-8"))}
cf_rows = [r for r in rows if r["cf_id"] in dp_ids]
greedy_rows = [r for r in rows if r["cf_id"] in gset]
# keep the greedy order from the pasted pages
order = {i: n for n, i in enumerate(greedy_ids)}
greedy_rows.sort(key=lambda r: order.get(r["cf_id"], 10**6))

wb = load_workbook(D + "infosys_sp_dse_prep_full.xlsx", read_only=True)
rec = {}
for row in wb["Summary"].iter_rows(min_row=6, values_only=True):
    if row[0] and isinstance(row[1], (int, float)): rec[str(row[0])] = int(row[1])

html = open(OUT, encoding="utf-8").read()
m = re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S)
data = json.loads(m.group(1).replace("<\\/", "</"))
data["cf"] = cf_rows
data["greedy"] = greedy_rows
data["recurrence"] = rec
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = html[:m.start(1)] + blob + html[m.end(1):]

if 'id="tab-greedy"' not in html:
    # nav button after the Codeforces DP button
    html = html.replace('<button role="tab" data-tab="cf" aria-selected="false">Codeforces DP</button>',
        '<button role="tab" data-tab="cf" aria-selected="false">Codeforces DP</button>\n    <button role="tab" data-tab="greedy" aria-selected="false">Greedy</button>', 1)
    section = '''  <section id="tab-greedy" class="hidden">
    <div class="count" style="margin-bottom:8px">Greedy problems from your Codeforces list (1400–2100). Kept separate from the DP set.</div>
    <div class="controls">
      <input id="gr-q" type="search" placeholder="Search name, pattern, nearest Infosys question…">
      <select id="gr-pat"><option value="">All patterns</option></select>
      <select id="gr-rat"><option value="">Any rating</option><option value="1400">1400–1600</option><option value="1700">1700–1900</option><option value="2000">2000–2200</option></select>
      <select id="gr-sort"><option value="list">Sort: your list order</option><option value="pred">Sort: prediction index</option><option value="match">Sort: match %</option><option value="rating">Sort: rating</option></select>
    </div>
    <div class="count" id="gr-count"></div>
    <div id="gr-list"></div>
    <div class="more"><button id="gr-more">Show more</button></div>
  </section>

  <section id="tab-top"'''
    html = html.replace('  <section id="tab-top"', section, 1)
    html = html.replace("['start','inf','cf','top','method'].forEach", "['start','inf','cf','greedy','top','method'].forEach", 1)
    js = '''
// Greedy tab (separate section)
(function(){
  const G = D.greedy;
  const gp = document.getElementById('gr-pat');
  const pats = [...new Set(G.flatMap(q => q.patterns))].sort();
  pats.forEach(p => { const o = document.createElement('option'); o.value = p; o.textContent = p; gp.append(o); });
  const st = {q: '', pat: '', rat: '', sort: 'list'};
  function filt() {
    let r = G.filter(q => {
      if (st.pat && !q.patterns.includes(st.pat)) return false;
      if (st.rat) { const lo = +st.rat, v = +q.rating; if (v < lo || v >= lo + 200) return false; }
      if (st.q) { const h = (q.name + ' ' + q.patterns + ' ' + q.nearest_infosys_question + ' ' + q.tags).toLowerCase(); if (!h.includes(st.q)) return false; }
      return true;
    });
    if (st.sort === 'pred') r = r.slice().sort((a, b) => b.prediction_index - a.prediction_index);
    if (st.sort === 'match') r = r.slice().sort((a, b) => b.match_pct - a.match_pct);
    if (st.sort === 'rating') r = r.slice().sort((a, b) => a.rating - b.rating);
    return r;
  }
  let pager = null;
  function refresh() { pager = paged(document.getElementById('gr-list'), document.getElementById('gr-count'), document.getElementById('gr-more'), filt(), renderCf); }
  document.getElementById('gr-more').addEventListener('click', () => pager.reset());
  document.getElementById('gr-q').addEventListener('input', e => { st.q = e.target.value.trim().toLowerCase(); refresh(); });
  gp.addEventListener('change', e => { st.pat = e.target.value; refresh(); });
  document.getElementById('gr-rat').addEventListener('change', e => { st.rat = e.target.value; refresh(); });
  document.getElementById('gr-sort').addEventListener('change', e => { st.sort = e.target.value; refresh(); });
  refresh();
})();
'''
    html = html.replace("})();\n</script>", js + "})();\n</script>", 1)
open(OUT, "w", encoding="utf-8").write(html)
print("cf", len(cf_rows), "greedy", len(greedy_rows), "bytes", len(html.encode()))
