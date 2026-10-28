"""Add the DP items (sections 1q-27q of the DesiQnA paste) to the Kumar K list in website/index.html.

Records go under D.kdp, shown in a 'Kumar K DP' tab with the same cards and filters as the greedy tab.
Rating and match/prediction scores are left empty (not estimated), so those badges are hidden.
Usage: python3 scripts/add_kumar_dp.py   (run from infosys-prep/)
"""
import json, re, os

HTML = 'website/index.html'
DP = 'dp_batch'

SHARED = ('dp_batch1.py', 'dp_batch1b.py', 'dp_batch2_screenshots.py')

def rec(sid, brief, patterns, key, steps, cx, dry, verification, state, code_file=None, code_lang='Python'):
    code = ''
    if code_file and code_file.endswith(SHARED):
        code = '# Solver is in ' + code_file + ' together with other sections; see its brute-force check.'
    elif code_file and os.path.exists(code_file):
        code = open(code_file).read().rstrip()
    return {'sheet_id': sid, 'kind': 'dp', 'brief': brief, 'patterns': patterns, 'sheet_patterns': [],
            'topics': ['Dynamic programming'], 'is_greedy': False, 'rating': None, 'match_pct': None,
            'prediction_index': None, 'nearest_infosys_question': '', 'key_idea': key, 'steps': steps,
            'complexity': cx, 'dry_run': dry, 'verification': verification, 'state': state,
            'external_mapping': 'DesiQnA DP paste, section ' + sid, 'infosys_mapping': 'not checked',
            'status': 'solved from the paste text; verified against brute force' if state == 'Solved' else state,
            'code_lang': code_lang if code else '', 'code': code, 'code_file': code_file or ''}

R = []
R.append(rec('1q', 'Range-sum queries on an array (1, i)', ['Prefix sums'],
             'pre[i] = pre[i-1] + a[i]; answer each query in O(1).',
             '1. Build pre[0..n].\n2. Answer query i with pre[i].',
             'O(N + Q) time, O(N) space',
             'a = {4,5,3,2,1} -> prefix 4, 9, 12, 14, 15 (same as the paste).',
             'checked by hand against the paste values', 'Solved'))
R.append(rec('2q', 'Prefix-sum code sample with queries', ['Prefix sums'],
             'Same prefix-sum idea as 1q, in C++ (the paste code is 0-based, so query 0 must give 0).',
             '1. pre[0] = 0, pre[i] = pre[i-1] + a[i].\n2. Query q -> pre[q].',
             'O(N + Q) time, O(N) space',
             'a = {6,7,3,2,2}, queries 0,3,4,2 -> 0, 16, 18, 13.',
             'checked against the direct sum on 2000 random cases', 'Solved'))
R.append(rec('3q', 'Max sum subset, no two adjacent (empty allowed)', ['1D DP', 'Take or skip'],
             'dp[i] = max(dp[i-1], a[i] + dp[i-2]).',
             '1. dp[0] = 0, dp[1] = max(0, a[1]).\n2. For i >= 2: dp[i] = max(dp[i-1], a[i] + dp[i-2]).',
             'O(N) time, O(1) space', 'Paste example {2,4,6,7,8} -> 16 (2 + 6 + 8).',
             'brute force on random cases (dp_batch1.py)', 'Solved', f'{DP}/dp_batch1.py'))
R.append(rec('4q', 'Two arrays, max subset with no consecutive index', ['1D DP', 'Two choices per index'],
             'dp[i] = max(max(a1[i], a2[i]) + dp[i-2], dp[i-1]).',
             '1. m[i] = max(a1[i], a2[i]).\n2. dp[1], dp[2] from the base cases.\n3. dp[i] = max(m[i] + dp[i-2], dp[i-1]).',
             'O(N) time, O(N) space', 'a1 = {1,5,3,21234}, a2 = {-4509,200,3,40} -> 21434.',
             'brute force over 3-choice assignments, 2000 random cases', 'Solved', f'{DP}/two_arrays_nonconsecutive4q.py'))
R.append(rec('5q', 'Min cost to reach city N, jumps of 1 or 3', ['1D DP', 'Min over predecessors'],
             'dp[i] = min(dp[i-1] + |A[i] - A[i-1]|, dp[i-3] + |A[i] - A[i-3]|).',
             '1. dp[1] = 0.\n2. For i >= 2 take the cheaper of the +1 and +3 transitions.',
             'O(N) time, O(N) space', 'A = {1,2,3,4,5} -> 4.',
             'brute force over all flight paths, 3000 random cases', 'Solved', f'{DP}/minimum_cost_destination5q.py'))
R.append(rec('6q', 'Longest k-interspace substring', ['Sliding window'],
             'Start a new window whenever two adjacent characters differ by more than k.',
             '1. Keep the window start l.\n2. For each r, if |word[r] - word[r-1]| > k, set l = r.\n3. Track the longest window (first one wins).',
             'O(N) time, O(1) space', 'word = "ababbaca", k = 1 -> "ababba" (screenshot, sample case 1).',
             'checked against the screenshot samples', 'Solved'))
R.append(rec('7q', 'Frog 1: jumps of 1 or 2, cost |h_i - h_j|', ['1D DP', 'Min over predecessors'],
             'dp[i] = min(dp[i-1] + |h[i]-h[i-1]|, dp[i-2] + |h[i]-h[i-2]|).',
             '1. dp[1] = 0.\n2. Fill dp left to right.',
             'O(N) time, O(N) space', 'Recurrence checked (dp_batch1b.py brute force).',
             'brute force (dp_batch1b.py)', 'Solved', f'{DP}/dp_batch1b.py'))
R.append(rec('8q', 'Jumps of 1, 3 or 5; maximise visited sum', ['1D DP', 'Max over predecessors'],
             'dp[i] = a[i] + max(dp[i-1], dp[i-3], dp[i-5]) over the valid predecessors.',
             '1. Start from index 1 with its value.\n2. Fill dp with the three jump sizes.',
             'O(N) time, O(N) space', 'Recurrence checked (dp_batch1.py brute force).',
             'brute force (dp_batch1.py)', 'Solved', f'{DP}/dp_batch1.py'))
R.append(rec('9q', 'Jump i -> j (i < j <= i+K) costs a[i]·a[j]', ['1D DP', 'Sliding minimum'],
             'dp[j] = min over i in [j-K, j-1] of dp[i] + a[i]·a[j].',
             '1. dp[0] = 0.\n2. For each j, take the minimum over the last K positions.',
             'O(N·K) time (O(N) with a deque)', 'Recurrence checked (dp_batch1.py brute force).',
             'brute force (dp_batch1.py)', 'Solved', f'{DP}/dp_batch1.py'))
R.append(rec('10q', 'Three activities per day, no repeat in a row', ['1D DP', 'State = last choice'],
             'dp[i][t] = happiness[i][t] + max(dp[i-1][u]) over u != t.',
             '1. Keep three states (activity of the last day).\n2. Transition to the two other activities.',
             'O(N) time, O(1) space', 'Recurrence checked (dp_batch1.py brute force).',
             'brute force (dp_batch1.py)', 'Solved', f'{DP}/dp_batch1.py'))
R.append(rec('11q', 'Count journeys with odd sum (steps +1 or +2)', ['Counting DP', 'Parity'],
             'Count journeys ending at i by parity of their sum.',
             '1. cnt[i][parity] from cnt[i-1] and cnt[i-2].\n2. Answer is cnt[n][odd].',
             'O(N) time, O(N) space', 'Recurrence checked (dp_batch1.py brute force).',
             'brute force (dp_batch1.py)', 'Solved', f'{DP}/dp_batch1.py'))
R.append(rec('12q', 'Reduce N to 1 with -1 (y), /7 (x), /3 (z), /5 (b)', ['1D DP', 'Min over moves'],
             'dp[i] = min(dp[i-1] + y, dp[i/7] + x if 7 | i, dp[i/3] + z if 3 | i, dp[i/5] + b if 5 | i).',
             '1. dp[1] = 0.\n2. For i from 2 to N take the cheapest allowed move.',
             'O(N) time, O(N) space', 'N = 15, y=100, x=1, z=500, b=10000000 -> 201 (15 -> 14 -> 2 -> 1).',
             'matches Dijkstra on 2000 random cases', 'Solved', f'{DP}/reduce_to_one12q.py'))
R.append(rec('13q', 'Two-array journeys: pick one array per index (parity)', ['Counting DP', 'Two arrays'],
             'Track the last array used and the parity of the sum.',
             '1. State = (last array, parity).\n2. Extend each state by one index.',
             'O(N) time, O(1) space', 'Recurrence checked (dp_batch1.py brute force).',
             'brute force (dp_batch1.py)', 'Solved', f'{DP}/dp_batch1.py'))
R.append(rec('14q', 'Minimum steps to reduce N to 1 with -1, /2, /3', ['1D DP', 'Min over moves'],
             'dp[i] = 1 + min(dp[i-1], dp[i/2] if 2 | i, dp[i/3] if 3 | i).',
             '1. dp[1] = 0.\n2. Fill dp up to N.',
             'O(N) time, O(N) space', 'Recurrence checked (dp_batch1.py brute force).',
             'brute force (dp_batch1.py)', 'Solved', f'{DP}/dp_batch1.py'))
R.append(rec('15q', 'Gallery Heist, part 1: max non-adjacent sum', ['1D DP', 'Take or skip'],
             'take = skip_prev + x; skip = max(take_prev, skip_prev).',
             '1. Keep take and skip states.\n2. Update per gallery.',
             'O(N) time, O(1) space', '[3, 2, 7, 10] -> 13.',
             'brute force on 1500 random cases (gallery_heist15q.py)', 'Solved', f'{DP}/gallery_heist15q.py'))
R.append(rec('16q', 'Gallery Heist, parts 2–4: exactly k, penalty P, two thieves', ['2D DP', 'Exactly k'],
             'Part 2: dp[i][j] = max(dp[i-1][j], a[i] + dp[i-2][j-1]). Part 3: track whether i is taken, with penalty P. Part 4: states A, B, X.',
             '1. Part 2 uses exact-count states.\n2. Part 3 adds last-taken state and penalty.\n3. Part 4 uses three states.',
             'O(N·k) time (parts 2–3), O(N) (part 4)', 'Checked on 1500 random cases (gallery_heist15q.py).',
             'brute force on 1500 random cases (gallery_heist15q.py)', 'Solved', f'{DP}/gallery_heist15q.py'))
R.append(rec('17q', 'Cost-jump array: +2 or -1, visit each index once', ['1D DP', 'Block transitions'],
             'Walks are built from a +2 jump or a zig-zag p -> p+2 -> p+1 -> p+3.',
             '1. f[1] = b[1].\n2. From p: +2 jump, or zig-zag when p+2 < n.\n3. Cross the end from the last landing.',
             'O(N) time, O(N) space', 'b = [2,5,8] -> 10; [2,-100,8,5,0] -> -85; [2,10,8,-5,-10,5] -> 0.',
             'matches exhaustive search on 3000 random cases', 'Solved', f'{DP}/cross_array_dp17q.py'))
R.append(rec('18q', 'Atlassian: +x, -x, *x, /x, N with optional ops', ['1D DP', 'Max and min states'],
             'Keep the best and worst reachable value; N swaps them.',
             '1. mx = mn = 1.\n2. For each op update mx and mn from both candidates; for N use -mn and -mx.',
             'O(N) time, O(1) space', 'Matches brute force (3000 random cases).',
             'brute force on 3000 random cases (atlassian18q.py)', 'Solved', f'{DP}/atlassian18q.py'))
R.append(rec('19q', 'Two arrays, switching costs a gap', ['1D DP', 'Two arrays'],
             'Track the last array; a switch needs the gap.',
             '1. State = last array.\n2. Extend with the switch rule.',
             'O(N) time, O(1) space', 'Recurrence checked (dp_batch1b.py brute force).',
             'brute force (dp_batch1b.py)', 'Solved', f'{DP}/dp_batch1b.py'))
R.append(rec('20q', 'Uber: two arrays, no three picks in a row from one array', ['1D DP', 'Run length'],
             'State = (array of last pick, run length 1 or 2).',
             '1. Start with the first pick from either array.\n2. Extend; drop a state if the run would reach 3.',
             'O(N) time, O(1) space', 'B = [5,3,4], C = [10,10,10] -> 25.',
             'brute force on 3000 random cases (uber20q.py)', 'Solved', f'{DP}/uber20q.py'))
R.append(rec('21q', 'Barclays: easy / hard / no task, hard only after rest', ['1D DP', 'State machine'],
             'States: easy today, hard today (only after rest), rest today.',
             '1. Start with the day-1 options.\n2. Hard requires the previous day to be rest.',
             'O(N) time, O(1) space', 'Stephen example: 33.',
             'brute force on 500 random cases (dp_batch2_screenshots.py)', 'Solved', f'{DP}/dp_batch2_screenshots.py'))
R.append(rec('23q', 'Compositions of y from {1,2,4,6}, 4 used at most twice', ['Counting DP', 'Limited use'],
             'Count sequences by the last part and how many 4s are used.',
             '1. Track the number of 4s used.\n2. Sum over the four parts.',
             'O(y·3) time', 'Recurrence checked (dp_batch1.py brute force).',
             'brute force (dp_batch1.py)', 'Solved', f'{DP}/dp_batch1.py'))
R.append(rec('24q', 'Visiting order: A/B/C by neighbours visited first', ['Edge orientation DP'],
             'Orient each edge by which endpoint is visited first; the value of i depends on in-degree.',
             '1. Walk the edges, keeping the orientation of the last edge.\n2. Add A, B or C by in-degree.',
             'O(N) time, O(1) space', 'Matches brute force over all orders (1500 random cases).',
             'brute force over all orders (journey_order24q.py)', 'Solved', f'{DP}/journey_order24q.py'))
R.append(rec('25q', 'AirBnB stones: remove cost depends on neighbours', ['Interval / removal DP'],
             'Removal cost b[i] if both neighbours remain, a[i] if one, 0 if none.',
             '1. Set up the recurrence on removal order.\n2. Fill intervals.',
             'O(N^3) or better, see the solver', 'Recurrence checked (dp_batch1b.py brute force).',
             'brute force (dp_batch1b.py)', 'Solved', f'{DP}/dp_batch1b.py'))
R.append(rec('26q', 'Phonepe OA: Thieves and Houses (blocks of 2 or 3)', ['1D DP', 'Block gaps'],
             'f[i][s] = block sum + best earlier block with the required gap (1 if both size 2, else 2).',
             '1. Prefix max of block ends by size.\n2. Each block adds its sum to the best valid predecessor.\n3. Multi-test input wrapper in thieves_houses_io.py.',
             'O(N) time, O(N) space', 'Samples 0, 3, 6, 9, 16, 15 (screenshots).',
             'brute force on 500 random cases; 0.3 s for N = 1e5', 'Solved', f'{DP}/thieves_houses_io.py'))
R.append(rec('27q', 'Split into k parts, alternating-sign sums', ['2D DP', 'Parts and sign'],
             'State = (parts opened, sign of the last element).',
             '1. Start part 1 with +.\n2. Continue with the opposite sign, or open a new part with +.',
             'O(N·k) time, O(k) space', '[1, -2, 3], k = 2 -> 6.',
             'brute force over all k-part splits on 3000 random cases', 'Solved', f'{DP}/alternating_parts27q.py'))

HTML_TAB = '''  <section id="tab-kdp" class="hidden">
    <div class="count" style="margin-bottom:8px">DP problems from the DesiQnA paste (sections 1q–27q): the same cards as the Kumar K greedy tab, with brief, key idea, steps, complexity, dry run, verification and code. Ratings and match % are not estimated yet.</div>
    <div class="controls">
      <input id="kd-q" type="search" placeholder="Search section, brief, pattern…">
      <select id="kd-pat"><option value="">All patterns</option></select>
    </div>
    <div class="count" id="kd-count"></div>
    <div id="kd-list"></div>
    <div class="more"><button id="kd-more">Show more</button></div>
  </section>

'''

JS_TAB = '''// Kumar K DP tab: DP items from the DesiQnA paste, same cards as the greedy tab
(function(){
  const K = D.kdp || [];
  const kp = document.getElementById('kd-pat');
  fillPatterns(kp, K);
  const st = {q: '', pat: '', rat: '', sort: 'list'};
  let pager = null;
  function refresh() { pager = paged(document.getElementById('kd-list'), document.getElementById('kd-count'), document.getElementById('kd-more'), K.filter(r => kkMatch(r, st)), renderKk); }
  document.getElementById('kd-more').addEventListener('click', () => pager.reset());
  document.getElementById('kd-q').addEventListener('input', e => { st.q = e.target.value.trim().toLowerCase(); refresh(); });
  kp.addEventListener('change', e => { st.pat = e.target.value; refresh(); });
  refresh();
})();
'''

def main():
    h = open(HTML).read()
    m = re.search(r'(<script id="data" type="application/json">)(.*?)(</script>)', h, re.S)
    D = json.loads(m.group(2))
    D['kdp'] = R
    h = h[:m.start(2)] + json.dumps(D, ensure_ascii=False).replace('</', '<\\/') + h[m.end(2):]
    if 'id="tab-kdp"' not in h:
        h = h.replace('  <section id="tab-top" class="hidden">', HTML_TAB + '  <section id="tab-top" class="hidden">', 1)
        h = h.replace('<button role="tab" data-tab="kgreedy" aria-selected="false">Kumar K greedy</button>',
                      '<button role="tab" data-tab="kgreedy" aria-selected="false">Kumar K greedy</button>\n    <button role="tab" data-tab="kdp" aria-selected="false">Kumar K DP</button>', 1)
        h = h.replace("['start','inf','cf','greedy','sheet','kgreedy','top','plan','method']",
                      "['start','inf','cf','greedy','sheet','kgreedy','kdp','top','plan','method']", 1)
        js_anchor = '// Kumar K greedy tab'
        i = h.index(js_anchor)
        h = h[:i] + JS_TAB + h[i:]
    # Missing match/prediction scores must not show as 0 or break sorting
    h = h.replace("if (r.rating) s.append(el('span', 'badge', 'Rating ' + r.rating), el('span', 'badge', 'Match ' + r.match_pct + '%'), el('span', 'badge', 'Pred ' + r.prediction_index));",
                  "if (r.rating) s.append(el('span', 'badge', 'Rating ' + r.rating));\n  if (r.match_pct != null) s.append(el('span', 'badge', 'Match ' + r.match_pct + '%'), el('span', 'badge', 'Pred ' + r.prediction_index));", 1)
    open(HTML, 'w').write(h)
    print(len(R), 'DP records added; with code:', sum(1 for r in R if r['code']))

if __name__ == '__main__':
    main()
