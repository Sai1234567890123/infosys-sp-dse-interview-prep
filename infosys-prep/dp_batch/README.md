# DP batch 1 (message.md, sections 1q–27q)

Solutions and brute-force checks for the DP questions in the pasted DesiQnA tutorial (`message_dp_paste.md`).

Processed (solver + brute-force check, Python):
- 3q: max subset sum, no two adjacent
- 7q: AtCoder Frog 1 (jumps of 1 or 2, cost |h_i - h_j|)
- 8q: jumps of 1, 3 or 5, maximise visited sum (sample 131)
- 9q: jumps up to K, cost a[i]*a[j]
- 10q: AtCoder Vacation (no same activity twice in a row)
- 11q: count odd-sum journeys with steps of 1 or 2
- 13q and 22q: two arrays, count even/odd journeys (sample 4 even, 4 odd)
- 14q: min steps to reduce N to 1 (-1, /2, /3)
- 19q: two arrays, switching array costs a skipped index (tutorial recurrence; brute uses the same rule)
- 23q: ordered ways to make y from {1,2,4,6}, 4 used at most twice
- 25q: AirBnB stones, removal cost depends on neighbours (orientation DP)

Not processed yet: 1q, 2q, 4q (tutorial text only), 5q/12q/24q (no section), 6q (same as the k-interspace problem, already solved), 15q/16q/17q (statements in images), 18q (queries; statement ambiguous), 20q (code only), 21q (link only), 26q (rule is ambiguous), 27q (empty).

Run: `python3 -I dp_batch1.py && python3 -I dp_batch1b.py`
