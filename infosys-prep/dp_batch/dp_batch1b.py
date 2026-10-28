"""More of DP batch 1: 7q (AtCoder Frog 1), 18q (Atlassian queries, tentative), 19q (two arrays, switch costs a gap), 25q (AirBnB stones)."""
import itertools, random

# 7q: frog on stones 1..N with heights h, jumps of 1 or 2, cost |h_i - h_j|; minimum total cost to reach N.
def q7(h):
    n = len(h)
    dp = [0] * n
    for i in range(1, n):
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]) if i >= 2 else float('inf'))
    return dp[n - 1]

def q7_brute(h):
    n = len(h)
    best = None
    def go(i, c):
        nonlocal best
        if i == n - 1:
            best = c if best is None else min(best, c); return
        for j in (i + 1, i + 2):
            if j < n: go(j, c + abs(h[i] - h[j]))
    go(0, 0)
    return best

# 19q: two arrays a and b, pick elements from index 1 to n in order; switching array from index i to i+2 is allowed,
# switching to the other array directly at i+1 gives nothing (tutorial recurrence):
#   dpA[i] = a[i] + max(dpA[i-1], dpB[i-2]);  dpB[i] = b[i] + max(dpB[i-1], dpA[i-2]).
def q19(a, b):
    n = len(a)
    NEG = float('-inf')
    dA = [NEG] * n; dB = [NEG] * n
    dA[0], dB[0] = a[0], b[0]
    for i in range(1, n):
        dA[i] = a[i] + max(dA[i - 1], dB[i - 2] if i >= 2 else NEG)
        dB[i] = b[i] + max(dB[i - 1], dA[i - 2] if i >= 2 else NEG)
    return max(dA[n - 1], dB[n - 1])

def q19_brute(a, b):
    n = len(a)
    best = None
    # each index is either taken from A, from B, or skipped; consecutive taken indices from different arrays need a gap of >=1 skipped index
    for choice in itertools.product((0, 1, 2), repeat=n):   # 0 skip, 1 A, 2 B
        if choice[0] == 0 or choice[-1] == 0: continue
        ok = True
        s = 0
        last = None  # (index, array)
        for i, c in enumerate(choice):
            if c == 0: continue
            if last is not None:
                li, lc = last
                if lc != c and i - li < 2: ok = False; break
            s += a[i] if c == 1 else b[i]
            last = (i, c)
        if ok and (best is None or s > best): best = s
    return best

# 25q: n stones; removing stone i costs b[i] if both neighbours are still present, a[i] if exactly one is, 0 if none.
# Orientation DP: x_i = 1 if stone i is removed before stone i+1. Stone i has its right neighbour present iff x_i == 1,
# and its left neighbour present iff x_{i-1} == 0. Any orientation of the path is a valid removal order.
def q25(a, b):
    n = len(a)
    if n == 1: return 0
    # dp[x] = min cost of stones 0..i-1 (decided) given x_{i-1} = x (for i >= 1)
    def cost_of(i, left_present, right_present):
        k = left_present + right_present
        return (0, a[i], b[i])[k]
    INF = float('inf')
    # i = 0: no left neighbour; x_0 chooses right neighbour presence
    dp = {1: cost_of(0, 0, 1), 0: cost_of(0, 0, 0)}
    for i in range(1, n - 1):
        nd = {0: INF, 1: INF}
        for xprev, c in dp.items():
            for x in (0, 1):
                left_present = 1 if xprev == 0 else 0     # stone i-1 removed after i
                right_present = x                          # stone i+1 removed after i
                nd[x] = min(nd[x], c + cost_of(i, left_present, right_present))
        dp = nd
    # last stone: right neighbour absent
    best = INF
    for xprev, c in dp.items():
        left_present = 1 if xprev == 0 else 0
        best = min(best, c + cost_of(n - 1, left_present, 0))
    return best

def q25_brute(a, b):
    n = len(a)
    best = None
    for order in itertools.permutations(range(n)):
        present = [True] * n
        total = 0
        for i in order:
            l = i - 1 >= 0 and present[i - 1]
            r = i + 1 < n and present[i + 1]
            k = int(l) + int(r)
            total += (0, a[i], b[i])[k]
            present[i] = False
        best = total if best is None else min(best, total)
    return best

if __name__ == '__main__':
    rng = random.Random(3)
    print('7q sample [10,30,40,20] ->', q7([10, 30, 40, 20]), '(expect 30)')
    print('7q sample [30,10,60,10,60,50] ->', q7([30, 10, 60, 10, 60, 50]), '(expect 40)')
    bad = {'7q': 0, '19q': 0, '25q': 0}
    for _ in range(400):
        n = rng.randint(2, 7)
        h = [rng.randint(1, 20) for _ in range(n)]
        bad['7q'] += q7(h) != q7_brute(h)
        a = [rng.randint(1, 9) for _ in range(n)]
        b = [rng.randint(1, 9) for _ in range(n)]
        bad['19q'] += q19(a, b) != q19_brute(a, b)
    for _ in range(300):
        n = rng.randint(1, 6)
        a = [rng.randint(1, 9) for _ in range(n)]
        b = [rng.randint(1, 9) for _ in range(n)]
        bad['25q'] += q25(a, b) != q25_brute(a, b)
    print('mismatches:', bad)
