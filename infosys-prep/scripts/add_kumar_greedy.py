"""Add the Kumar K list (sheet 1q-90q) to the Greedy tab of website/index.html.

Each sheet record gets a `code` field (C++ or Python cut from the sheet_* solution files)
and is stored under D.kgreedy. Re-running replaces the previous kgreedy data and script.
Usage: python3 scripts/add_kumar_greedy.py   (run from infosys-prep/)
"""
import glob, json, re

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
    kg = []
    for r in D['sheet']:
        pats = sorted({p.strip() for x in r.get('patterns', []) for p in x.split(',') if p.strip() and p.strip() != 'n/a'})
        lang, src, f = code.get(r['sheet_id'], ('', '', ''))
        kg.append({**r, 'patterns': pats, 'state': short_status(r.get('status')),
                   'code_lang': lang, 'code': src, 'code_file': f})
    D['kgreedy'] = kg
    h = h[:m.start(2)] + json.dumps(D, ensure_ascii=False).replace('</', '<\\/') + h[m.end(2):]

    # Greedy tab: source filter and intro text
    h = h.replace('<div class="count" style="margin-bottom:8px">Greedy problems from your Codeforces list (1400–2100). Kept separate from the DP set.</div>',
                  '<div class="count" style="margin-bottom:8px">Greedy problems: the Kumar K list (sheet 1q–90q, shown first) and your Codeforces list (1400–2100). Kept separate from the DP set.</div>')
    if 'id="gr-src"' not in h:
        h = h.replace('<input id="gr-q" type="search" placeholder="Search name, pattern, nearest Infosys question…">',
                      '<select id="gr-src"><option value="">All sources</option><option value="kk">Kumar K list (1q–90q)</option><option value="cf">Codeforces list</option></select>\n'
                      '      <input id="gr-q" type="search" placeholder="Search name, pattern, nearest Infosys question…">')

    old_js = re.search(r'// Greedy tab \(separate section\)[^\n]*\n\(function\(\)\{.*?\n\}\)\(\);\n', h, re.S)
    h = h[:old_js.start()] + open('scripts/greedy_tab.js').read() + h[old_js.end():]
    open(HTML, 'w').write(h)
    st = {}
    for r in kg: st[r['state']] = st.get(r['state'], 0) + 1
    print(len(kg), 'records;', st, '; with code:', sum(1 for r in kg if r['code']))


main()
