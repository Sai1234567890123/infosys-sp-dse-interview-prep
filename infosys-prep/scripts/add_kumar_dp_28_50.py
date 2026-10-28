"""Add Kumar K DP sections 28q-50q to D.kdp in website/index.html (after 1q-27q; 22q is inside 13q).

Code comes from infosys-prep/dp_batch/kumar_sheet/ when a solver file is committed there; otherwise the
record has no code and says so. Usage (from the repo root): python3 infosys-prep/scripts/add_kumar_dp_28_50.py
"""
import json, os, re

HTML = 'infosys-prep/website/index.html'
CODE = 'infosys-prep/dp_batch/kumar_sheet'
SRC = 'DesiQnA/Kumar K DP paste (thread), section '

# (sheet_id, brief, patterns, key_idea, steps, complexity, dry_run, verification, code_file, lang)
ITEMS = [
 ('22q', 'Same problem as 13q (selling products, shared solver)', ['Prefix sums', 'Subarray DP'],
  'Same solver as 13q; see 13q.', 'See 13q.', 'See 13q.', 'Same answers as 13q.', 'see 13q', '', ''),
 ('28q', 'Tasks with easy, medium and hard levels and a day-gap rule', ['1D DP', 'State = last two choices'],
  'State = (last task, task before). A hard task needs day i-2 to be easy; a medium task needs day i-1 easy and day i-2 medium.',
  '1. Keep the two previous task types as state.\n2. Transition only when the gap rule holds.\n3. Answer = max over valid end states.',
  'O(N) time, O(1) space', 'Paste examples, as in the thread.', 'brute force on random schedules', 'tasks28q.py', 'Python'),
 ('29q', 'Count ways with a two-type gap rule', ['1D DP', 'Two states'],
  'd0[i] = d0[i-1] + [A[i-2]==2]*d0[i-2]; d1[i] = d1[i-1] + [A[i-2]==2]*d1[i-2] + [A[i-3]==2 and A[i-2]==2]*d0[i-3]. Answer d0[n] + d1[n].',
  '1. d0[1] = d0[2] = 1.\n2. Fill d0 and d1 together.\n3. Print d0[n] + d1[n].',
  'O(N) time, O(1) space', 'Recurrence verified on small inputs.', 'brute force on random inputs (ways29q_check)', 'ways29q.py', 'Python'),
 ('30q', 'Paint House IV: paint mirror pairs with distinct colours', ['DP over pairs', 'State = two colours'],
  'Go over mirror pairs with state (left colour, right colour). The transition needs i1 != i, j1 != j and i1 != j1.',
  '1. Process pairs from the centre outward.\n2. Keep the best cost per (left, right) colour pair.\n3. Add the middle cell for odd n.',
  'O(N * 9) time', 'Checked against the LeetCode examples in the thread.', 'brute force on small grids (paint30q)', 'paint30q.py', 'Python'),
 ('31q', 'Select at most x, y, z non-overlapping subarrays of sizes 1, 2 and 3', ['3D DP', 'Max with counts'],
  'dp[i][j][k][l] = max(skip, a + dp[i-1][j-1][k][l], a + A[i-2] + dp[i-2][j][k-1][l], a + A[i-2] + A[i-3] + dp[i-3][j][k][l-1]).',
  '1. Index the four counts (j, k, l) as state.\n2. Take the best of skip and the three block transitions.',
  'O(N * x * y * z) time', 'Bounds from the paste: N up to 200, limits up to 20; still to confirm against the original.', 'brute force on random arrays (subarrays31q)', 'subarrays31q.py', 'Python'),
 ('32q', 'Strings over a, b, c, d with forbidden neighbours, odd count of a', ['DP over strings', 'State = last char and parity'],
  'State = (last character, parity of the count of a). Forbidden pairs: ab, ba, bc, cb, cd, dc.',
  '1. Start with single characters.\n2. Extend with allowed next characters, flipping parity for a.\n3. Sum the states with odd parity.',
  'O(N) time, O(1) space', 'Rules give 1, 4, 11, 30, 82 for N = 1..5. The paste sample 29 (N=4) conflicts; see the thread.',
  'brute force over all strings (alpha32q)', 'alpha32q.py', 'Python'),
 ('33q', 'LeetCode 647: count palindromic substrings', ['Palindrome table', 'Interval DP'],
  'dp[i][j] = (s[i] == s[j]) and (length <= 2 or dp[i+1][j-1]); count the true cells.',
  '1. Fill dp by length.\n2. Count the palindromes.',
  'O(N^2) time and memory', 'Examples abc -> 3, aaa -> 6, abcba -> 7; 3000 random cases.', 'brute force over substrings', 'palindromic_substrings33q.py', 'Python'),
 ('34q', 'GfG: longest palindromic substring (first occurrence on ties)', ['Expand around centre'],
  'Expand from each odd and even centre. Ties go to the smaller start index.',
  '1. For each centre, expand while ends match.\n2. Keep the longest; on a tie keep the earlier start.',
  'O(N^2) time, O(1) extra space', 'forgeeksskeegfor -> geeksskeeg; Geeks -> ee; abc -> a; 3000 random cases.', 'brute force over substrings', 'longest_palindrome34q.py', 'Python'),
 ('35q', 'GfG: count palindromic subsequences', ['Interval DP'],
  'dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1 if s[i]==s[j]; otherwise dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1].',
  '1. dp[i][i] = 1.\n2. Fill by length.\n3. Answer dp[0][n-1].',
  'O(N^2) time and memory', 'abcd -> 4, aab -> 4, geeksforgeeks -> 81; 3000 random cases.', 'brute force over subsets', 'palindromic_subsequences35q.py', 'Python'),
 ('36q', 'Ordered non-overlapping palindrome pairs and triples', ['Interval DP', 'Prefix sums over starts'],
  'A[j] = palindromes starting at >= j; W[l] = sum of A[r+1] over palindromes [l..r]; g2 = suffix sums of W; the triple step repeats with g2.',
  '1. Build the palindrome table.\n2. Compute A, W, g2.\n3. Repeat for triples.',
  'O(N^2) time and memory', 'Matches GfG examples aaa -> 5 and abacaba -> 36. The paste "bbaa = 10" conflicts with the definition (11).', 'brute force over spans', 'palindrome_chains36q.py', 'Python'),
 ('37q', 'Longest palindromic subsequence, and with at most K operations (LeetCode 3472)', ['Interval DP', 'Extra dimension for operations'],
  'Plain: dp[i][j] = max(dp[i][j-1], dp[i+1][j]) or 2 + dp[i+1][j-1] when the ends match. With K operations, the cost of matching s[i] and s[j] is min(d, 26-d) and the state adds the operation count.',
  '1. Plain LPS by interval DP.\n2. Add the operation count and the cyclic letter cost.',
  'O(N^2 * K) time', 'Plain LPS: 2000 random cases, 0 mismatches. k-operations: 1500 random cases, 0 mismatches; wrap-around confirmed from the statement.', 'brute force over subsequences', '', ''),
 ('38q', 'Merge adjacent numbers into one, cost = sum of the two', ['Interval DP', 'Merge cost'],
  'dp[i][j] = min over k of dp[i][k] + dp[k+1][j] + sum(a[i..j]).',
  '1. dp[i][i] = 0.\n2. Fill by length with the sum term.\n3. Answer dp[0][n-1].',
  'O(N^3) time, O(N^2) memory', '[5,5,8] -> 28; [5,8,2] -> 25; [5,8] -> 13; [5,8,2,10] -> 50; 1000 random cases.', 'brute force over merge orders', 'merge_cost38q.py', 'Python'),
 ('39q', 'Count palindromic substrings in a range [l, r], many queries', ['Palindrome table', 'Prefix-style counts'],
  'cnt[i][j] = cnt[i][j-1] + cnt[i+1][j] - cnt[i+1][j-1] + dp[i][j].',
  '1. Fill dp and cnt by length.\n2. Answer each query with cnt[l][r].',
  'O(N^2 + Q) time, O(N^2) memory', 'abba [0,3] -> 6, [1,2] -> 3; 300 strings x 10 ranges.', 'brute force over substrings', 'palindromic_substrings_range39q.cpp', 'C++'),
 ('40q', 'LeetCode 312: Burst Balloons', ['Interval DP', 'Last balloon burst'],
  'dp[i][j] = max over k of g[i-1]*g[k]*g[j+1] + dp[i][k-1] + dp[k+1][j], with padded 1s at both ends.',
  '1. Pad the array with 1s.\n2. Fill by length.\n3. Answer dp[1][n].',
  'O(N^3) time, O(N^2) memory', '[3,1,5,8] -> 167; [1,5] -> 10; 400 random arrays.', 'brute force over burst orders', '', ''),
 ('41q', 'Maximum XOR score over subarrays in range queries', ['Interval DP', 'XOR recurrence'],
  'score(i..j): f[i][j] = f[i][j-1] XOR f[i+1][j]. Query answer = max over subarrays inside [l, r]: best[i][j] = max(f, best[i][j-1], best[i+1][j]).',
  '1. Fill f and best by length.\n2. Answer each query with best[l][r].',
  'O(N^2 + Q) time, O(N^2) memory', 'Easy and hard versions; 300 arrays x 8 queries each.', 'brute force over pairwise XOR reduction', 'max_xor_score_queries41q.cpp', 'C++'),
 ('42q', 'Microsoft OA: equal-sum moves, maximum number of moves', ['Interval DP', 'Fix the sum first'],
  'The first move fixes the sum S from three candidates (first two, last two, first + last). dp[i][j][type] is the most moves inside [i..j] that all have sum S.',
  '1. Try each candidate sum.\n2. Fill dp for each interval.\n3. Take the max over candidates.',
  'O(N^2) time', '1 5 6 1 5 1 5 -> 3; 400 random arrays.', 'brute force game search', '', ''),
 ('43q', 'Partition into parts with sum <= M, and exactly k parts', ['1D DP', 'Count with a part-count dimension'],
  'dp[i] = sum over j of dp[j-1] where sum(b[j..i]) <= M; the exactly-k version adds the part count to the state.',
  '1. Unrestricted: sum over valid last parts.\n2. Exactly k: dp[i][p] from dp[j-1][p-1].',
  'O(N^2 K) time', '[1 2 3 4 4], M = 5 -> 3 in total (2 with 4 parts, 1 with 5); 400 random cases.', 'brute force over splits', '', ''),
 ('44q', 'Partition into parts of size >= 2, cost a[i] - a[j]; maximise', ['1D DP', 'Running max'],
  'dp[i] = max over j <= i-2 of dp[j] + a[j+1] - a[i]; keep the running max of dp[j] + a[j+1].',
  '1. dp[0] = 0.\n2. For each i, update the running max and set dp[i].',
  'O(N) time, O(N) space', '[5 10 5 10 1 1 8 2] -> max 15 (min -11); 400 random arrays.', 'brute force over splits', 'partition_cost44q.cpp', 'C++'),
 ('45q', 'LeetCode 2767: split a binary string into powers of 5, fewest parts', ['1D DP', 'Divisor check'],
  'dp[i+1] = min over j of dp[j] + 1 when s[j..i] is a power of 5. Check with 15625 % value == 0 (values up to 15 bits).',
  '1. dp[0] = 0.\n2. For each end, try all starts with a leading 1.',
  'O(N^2) time', '1011 -> 2; 111 -> 3; 500 random strings.', 'brute force over partitions', '', ''),
 ('46q', 'Exactly k parts, minimise the sum of each part maximum', ['2D DP', 'Exactly k parts'],
  'dp[i][p] = min over j of dp[j-1][p-1] + max(a[j..i]). Base case dp[0][0] = 0 only, so parts are never empty.',
  '1. dp[0][0] = 0; every other dp[0][p] = INF.\n2. Fill dp[i][p] with a running max.',
  'O(N^2 K) time, O(N K) space', '5 2 / 1 2 3 4 5 -> 6; 400 random arrays. The pasted base case dp[0][*] = 0 allowed empty parts (255 of 400 wrong).', 'brute force over exact-k splits', 'minimize_max_sum46q.cpp', 'C++'),
 ('47q', 'Minimum substring partition into parts with equal character frequency', ['1D DP', 'Validity check'],
  'dp[i] = min over j of dp[j-1] + 1 when every character in s[j..i] has the same count.',
  '1. dp[1] = 1.\n2. For each i, extend j downward and keep a 26-count array.',
  'O(N^2 * 26) time', 'ababaaaaaaaa -> 2; abcabc -> 1; a -> 1; 500 random strings.', 'brute force over partitions', '', ''),
 ('48q', 'Cisco OA: parts of size >= K with max - min <= M, fewest parts', ['1D DP', 'Min over valid parts'],
  'dp[i] = min over valid starts j of dp[j-1] + 1; the part is valid when its length is >= K and max - min <= M.',
  '1. dp[0] = 0.\n2. For each i, extend the part leftward with running max and min.',
  'O(N^2) time, O(N) space', '6 2 1 / 1 2 3 4 5 6 -> 3; 500 random inputs. Input and output format are assumed (confirm with the original).', 'brute force over splits', 'cisco_partition48q.cpp', 'C++'),
 ('49q', 'Google OA: single parts cost A[i], groups of 2+ cost the sum of B', ['1D DP', 'Three states'],
  's0 = A[i] + min(s2, s0); s1 = B[i] + min(s0, s1); s2 = B[i] + B[i-1] + min(s0, s1) two back. Answer min(s0[n], s2[n]).',
  '1. Keep three states per prefix.\n2. Fill left to right.',
  'O(N) time, O(N) space', 'Sample 12 elements -> 84; 500 random cases.', 'brute force over partitions', 'partition_cost49q.cpp', 'C++'),
 ('50q', 'Same problem as 49q (Google OA partition)', ['1D DP', 'Three states'],
  'Same statement and code as 49q; see 49q.',
  'See 49q.', 'O(N) time, O(N) space', 'Sample 84 (same as 49q).', 'see 49q', 'partition_cost49q.cpp', 'C++'),
]

CODE_FILES = {
 '37q': ('lps_k_ops37q.cpp', 'C++'), '40q': ('burst_balloons40q.cpp', 'C++'),
 '42q': ('equal_sum_moves42q.cpp', 'C++'), '43q': ('partition_sum_k43q.cpp', 'C++'),
 '45q': ('power_of_five45q.cpp', 'C++'), '47q': ('equal_freq_partition47q.cpp', 'C++'),
}

def rec(sid, brief, patterns, key, steps, cx, dry, verification, code_file, lang):
    code = ''
    if code_file and os.path.exists(os.path.join(CODE, code_file)):
        code = open(os.path.join(CODE, code_file)).read().rstrip()
    else:
        code_file = ''
        lang = ''
    return {'sheet_id': sid, 'kind': 'dp', 'brief': brief, 'patterns': patterns, 'sheet_patterns': [],
            'topics': ['Dynamic programming'], 'is_greedy': False, 'rating': None, 'match_pct': None,
            'prediction_index': None, 'nearest_infosys_question': '', 'key_idea': key, 'steps': steps,
            'complexity': cx, 'dry_run': dry, 'verification': verification, 'state': 'Solved',
            'external_mapping': SRC + sid, 'infosys_mapping': 'not checked',
            'status': 'solved from the paste text; verified against brute force' if code else
                      'solved and verified in the thread; code not committed to the repo yet',
            'code_lang': lang if code else '', 'code': code, 'code_file': code_file}

def main():
    h = open(HTML, encoding='utf-8').read()
    m = re.search(r'(<script id="data" type="application/json">)(.*?)(</script>)', h, re.S)
    D = json.loads(m.group(2))
    ids = {it[0] for it in ITEMS}
    kept = [r for r in D.get('kdp', []) if r['sheet_id'] not in ids]
    added = []
    for it in ITEMS:
        sid, brief, patterns, key, steps, cx, dry, ver, cf, lang = it
        if sid in CODE_FILES:
            cf, lang = CODE_FILES[sid]
        added.append(rec(sid, brief, patterns, key, steps, cx, dry, ver, cf, lang))
    D['kdp'] = sorted(kept + added, key=lambda r: int(re.match(r'\d+', r['sheet_id']).group()))
    h = h[:m.start(2)] + json.dumps(D, ensure_ascii=False).replace('</', '<\\/') + h[m.end(2):]
    h = h.replace('(sections 1q–27q)', '(sections 1q–50q)')
    open(HTML, 'w', encoding='utf-8').write(h)
    print('rebuilt', len(added), 'records; total', len(D['kdp']), '; with code', sum(1 for r in D['kdp'] if r['code']))

if __name__ == '__main__':
    main()
