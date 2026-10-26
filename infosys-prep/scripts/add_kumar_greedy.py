"""Add the Kumar K list (sheet 1q-90q) to the Greedy and Kumar K greedy tabs of website/index.html.

Each sheet record gets the study notes from sheet_1q_25q/kumar_k_notes_{a,b,c}.py (rating, patterns,
key idea, steps, complexity, dry run), the scores from sheet_1q_25q/kumar_k_scores.json (run
scripts/score_kumar_k.py first), and the C++ or Python cut from the sheet_* solution files.
Records are stored under D.kgreedy. Re-running replaces the previous kgreedy data and scripts.
Usage: python3 scripts/add_kumar_greedy.py   (run from infosys-prep/)
"""
import glob, json, re, sys

sys.path.insert(0, 'sheet_1q_25q')
from kumar_k_notes_a import NOTES as NA
from kumar_k_notes_b import NOTES as NB
from kumar_k_notes_c import NOTES as NC

KG_CONTROLS = '''      <input id="kg-q" type="search" placeholder="Search id, brief, pattern, nearest Infosys question…">
      <select id="kg-pat"><option value="">All patterns</option></select>
      <select id="kg-rat"><option value="">Any rating</option><option value="0">Under 1400</option><option value="1400">1400–1600</option><option value="1700">1700–1900</option><option value="2000">2000–2200</option></select>
      <select id="kg-sort"><option value="list">Sort: sheet order</option><option value="pred">Sort: prediction index</option><option value="match">Sort: match %</option><option value="rating">Sort: rating</option></select>
'''

HTML = 'website/index.html'


def cpp_snippets():
    out = {}
    for f in sorted(glob.glob('sheet_*/*.cpp')):
        lines = open(f).read().split('\n')
        main = next((i for i, l in enumerate(lines) if l.startswith('int main')), len(lines))
        hdr = [(i, m.group(1)) for i, l in enumerate(lines[:main]) if (m := re.match(r'^// (\d+q(?:-b)?)\b', l))]
        for k, (i, sid) in enumerate(hdr):
            end = hdr[k + 1][0] if k + 1 < len(hdr) else main
            chunk = '\n'.join(lines[i:end]).rstrip()
            if chunk.count('\n') >= 2:
                out.setdefault(sid, ('C++', chunk, f))
    # 1q has three parts in its own file; 36q shares 35q's routine.
    out['1q'] = ('C++', open('sheet_1q_25q/1q.cpp').read().rstrip(), 'sheet_1q_25q/1q.cpp')
    if '35q' in out:
        out['36q'] = out['35q']
    return out


def py_snippets():
    out = {}
    singles = {'8q': 'sheet_1q_25q/8q_atlassian_islands.py', '13q': 'sheet_1q_25q/13q_selling_products.py',
               '15q': 'sheet_1q_25q/15q_goblet_of_fire.py', '20q': 'sheet_1q_25q/20q_bny_three_problems.py'}
    multi = ['sheet_1q_25q/6q_22q_tests.py', 'sheet_1q_25q/26q_33q_tests.py']

    def strip(text):
        # keep solution functions, drop brute-force checkers and the test harness
        keep, skip = [], False
        for l in text.split('\n'):
            if re.match(r'^(if __name__|random\.seed|for _ in range|def test|def main)', l):
                break
            if re.match(r'^def \w*brute', l):
                skip = True
                continue
            if skip and (l.startswith('def ') or l.startswith('#')):
                skip = False
            if not skip:
                keep.append(l)
        return '\n'.join(keep).strip()

    for sid, f in singles.items():
        out[sid] = ('Python', strip(open(f).read()), f)
    for f in multi:
        lines = open(f).read().split('\n')
        hdr = [(i, m.group(1)) for i, l in enumerate(lines) if (m := re.match(r'^# (\d+q(?:-b)?)\b', l))]
        for k, (i, sid) in enumerate(hdr):
            end = hdr[k + 1][0] if k + 1 < len(hdr) else len(lines)
            out[sid] = ('Python', strip('\n'.join(lines[i:end])), f)
    return out


def short_status(s):
    t = (s or '').lower()
    if 'not a problem' in t: return 'n/a'
    if t.startswith('open') or 'open:' in t: return 'OPEN'
    if t.startswith('dup') or 'duplicate of' in t: return 'DUP'
    if 'statement incomplete' in t or t == 'partial': return 'Partial'
    return 'Solved'


def main():
    h = open(HTML).read()
    m = re.search(r'(<script id="data" type="application/json">)(.*?)(</script>)', h, re.S)
    D = json.loads(m.group(2))
    code = {**py_snippets(), **cpp_snippets()}
    notes = {**NA, **NB, **NC}
    scores = json.load(open('sheet_1q_25q/kumar_k_scores.json'))
    kg = []
    for r in D['sheet']:
        sid = r['sheet_id']
        n, sc = notes[sid], scores[sid]
        own = sorted({p.strip() for x in r.get('patterns', []) for p in x.split(',') if p.strip() and p.strip() != 'n/a'})
        lang, src, f = code.get(sid, ('', '', ''))
        kg.append({**r, 'sheet_patterns': own, 'is_greedy': any('greedy' in p.lower() for p in own),
                   'patterns': n['pats'], 'topics': n['topics'], 'rating': n['rating'] or 0,
                   'match_pct': sc['match_pct'], 'prediction_index': sc['prediction_index'],
                   'nearest_infosys_question': sc['nearest_infosys_question'],
                   'key_idea': n['key'], 'steps': n['steps'], 'complexity': n['cx'], 'dry_run': n['dry'],
                   'state': short_status(r.get('status')), 'code_lang': lang, 'code': src, 'code_file': f})
    D['kgreedy'] = kg
    h = h[:m.start(2)] + json.dumps(D, ensure_ascii=False).replace('</', '<\\/') + h[m.end(2):]

    # Greedy tab: source filter and intro text
    h = h.replace('<div class="count" style="margin-bottom:8px">Greedy problems from your Codeforces list (1400–2100). Kept separate from the DP set.</div>',
                  '<div class="count" style="margin-bottom:8px">Greedy problems: the Kumar K list (sheet 1q–90q, shown first) and your Codeforces list (1400–2100). Kept separate from the DP set.</div>')
    if 'id="gr-src"' not in h:
        h = h.replace('<input id="gr-q" type="search" placeholder="Search name, pattern, nearest Infosys question…">',
                      '<select id="gr-src"><option value="">All sources</option><option value="kk">Kumar K list (1q–90q)</option><option value="cf">Codeforces list</option></select>\n'
                      '      <input id="gr-q" type="search" placeholder="Search name, pattern, nearest Infosys question…">')

    # Rating filter: add an "under 1400" band for the easier sheet items
    h = h.replace('<select id="gr-rat"><option value="">Any rating</option><option value="1400">',
                  '<select id="gr-rat"><option value="">Any rating</option><option value="0">Under 1400</option><option value="1400">')
    # Kumar K greedy tab: same controls as the Codeforces DP tab
    h = re.sub(r'      <input id="kg-q"[^\n]*\n(      <select id="kg-[^\n]*\n)*', lambda _: KG_CONTROLS, h)
    h = h.replace('Every greedy-pattern problem from the Kumar K list (sheet items 1q–90q). Same records as the Sheet tab, filtered to greedy.',
                  'Every greedy-pattern problem from the Kumar K list (sheet items 1q–90q), with rating, match %, prediction index, key idea, steps, complexity, dry run and code, like the Codeforces DP tab.')

    # The Greedy block runs up to the Sheet tab; the Kumar K block is replaced by its own file.
    old_js = re.search(r'// Greedy tab \(separate section\)[^\n]*\n.*?(?=\n// Sheet tab)', h, re.S)
    h = h[:old_js.start()] + open('scripts/greedy_tab.js').read().rstrip('\n') + '\n' + h[old_js.end():]
    old_kg = re.search(r'// Kumar K greedy tab[^\n]*\n\(function\(\)\{.*?\n\}\)\(\);\n', h, re.S)
    h = h[:old_kg.start()] + open('scripts/kumar_k_tab.js').read() + h[old_kg.end():]
    open(HTML, 'w').write(h)
    st = {}
    for r in kg: st[r['state']] = st.get(r['state'], 0) + 1
    print(len(kg), 'records;', st, '; with code:', sum(1 for r in kg if r['code']))


main()
