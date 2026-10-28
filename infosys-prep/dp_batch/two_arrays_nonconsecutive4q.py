"""4q (DP Set-3): two arrays a1, a2 of size n. Choose a subset of elements (at most one per index, from either array),
no two chosen indices consecutive (index i and i+1 cannot both be chosen). Maximise the sum (empty allowed)."""
import itertools, random

def solve(a1, a2):
    n = len(a1)
    m = [max(a1[i], a2[i]) for i in range(n)]
    dp = [0] * (n + 1)                        # dp[k] = best for first k indices (1-based dp used below)
    if n >= 1: dp[1] = max(0, m[0])
    if n >= 2: dp[2] = max(dp[1], m[1])
    for i in range(3, n + 1):
        dp[i] = max(m[i - 1] + dp[i - 2], dp[i - 1])
    return dp[n]

def brute(a1, a2):
    n = len(a1); best = 0
    for choice in itertools.product((0, 1, 2), repeat=n):   # 0 none, 1 from a1, 2 from a2
        chosen = [i for i in range(n) if choice[i]]
        if any(chosen[k + 1] - chosen[k] == 1 for k in range(len(chosen) - 1)): continue
        best = max(best, sum((a1, a2)[choice[i] - 1][i] for i in chosen))
    return best

if __name__ == '__main__':
    print('sample ->', solve([1, 5, 3, 21234], [-4509, 200, 3, 40]), 'expect 21434')
    rng = random.Random(14); bad = 0
    for _ in range(2000):
        n = rng.randint(1, 7)
        a1 = [rng.randint(-20, 20) for _ in range(n)]; a2 = [rng.randint(-20, 20) for _ in range(n)]
        bad += solve(a1, a2) != brute(a1, a2)
    print('mismatches over 2000 random cases:', bad)
