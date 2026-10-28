"""24q (Meesho OA, as summarized in the paste): visit every index 1..n exactly once in some order.
When index i is visited, its value is A[i] if neither neighbour (i-1, i+1) was visited before it,
B[i] if exactly one was, C[i] if both were. Maximize the total.
Model: each edge (i, i+1) is oriented by which endpoint is visited first. Index i's value depends on
how many of its edges point into it, so a DP over edge orientations gives the maximum."""
import itertools, random

def journey(A, B, C):
    n = len(A)                              # arrays are 0-based here: A[0..n-1]
    NEG = float('-inf')
    # e = orientation of edge (i, i+1): True = i visited before i+1
    # dp[e] = best value of indices 0..i-1 plus nothing else, given edge (i-1, i) has orientation e
    def val(i, inc):                        # inc = number of neighbours visited before i
        return (A, B, C)[inc][i]
    if n == 1: return A[0]
    best = {}
    for e in (True, False):                 # edge (0,1) orientation; index 0 has only edge (0,1)
        inc0 = 0 if e else 1                # if 0 before 1, 0 has no earlier neighbour
        best[e] = val(0, inc0)
    # wait: val needs lists; fix below
    return None

def journey_dp(A, B, C):
    n = len(A)
    lists = (A, B, C)
    if n == 1: return A[0]
    # prev maps the orientation of edge (i-1, i-2) (None before any edge) to the best total of indices 0..i-2
    # o = True means the left index is visited first on that edge
    prev = {None: 0}
    for i in range(1, n):
        cur = {}
        for o_new in (True, False):              # orientation of edge (i-1, i)
            for o_old, v in prev.items():        # orientation of edge (i-2, i-1)
                inc = (1 if o_old else 0) + (1 if not o_new else 0)   # neighbours of i-1 visited before it
                cand = v + lists[inc][i - 1]
                if cand > cur.get(o_new, float('-inf')): cur[o_new] = cand
        prev = cur
    best = float('-inf')
    for o, v in prev.items():                    # last index n-1: only left edge
        inc = 1 if o else 0
        best = max(best, v + lists[inc][n - 1])
    return best

def brute(A, B, C):
    n = len(A); lists = (A, B, C); best = float('-inf')
    for perm in itertools.permutations(range(n)):
        pos = {v: k for k, v in enumerate(perm)}
        s = 0
        for i in range(n):
            inc = sum(1 for j in (i - 1, i + 1) if 0 <= j < n and pos[j] < pos[i])
            s += lists[inc][i]
        best = max(best, s)
    return best

if __name__ == '__main__':
    rng = random.Random(2); bad = 0
    for _ in range(1500):
        n = rng.randint(1, 7)
        A = [rng.randint(-20, 20) for _ in range(n)]
        B = [rng.randint(-20, 20) for _ in range(n)]
        C = [rng.randint(-20, 20) for _ in range(n)]
        bad += journey_dp(A, B, C) != brute(A, B, C)
    print('mismatches over 1500 random cases:', bad)
