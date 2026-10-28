"""31q (Uber SDE intern OA): array A of size N. Choose at most x blocks of size 1, at most y blocks of size 2 and at most z
blocks of size 3, all non-overlapping. Maximise the sum of the chosen elements (choosing nothing is allowed)."""
import random
from functools import lru_cache

def max_sum(A, x, y, z):
    n = len(A)
    # dp[i][j][k][l]: best sum using only A[0..i-1] with <= j blocks of size 1, <= k of size 2, <= l of size 3
    dp = [[[[0] * (z + 1) for _ in range(y + 1)] for _ in range(x + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        a = A[i - 1]
        for j in range(x + 1):
            for k in range(y + 1):
                for l in range(z + 1):
                    best = dp[i - 1][j][k][l]                                   # skip A[i]
                    if j >= 1:
                        best = max(best, a + dp[i - 1][j - 1][k][l])            # block of size 1
                    if i >= 2 and k >= 1:
                        best = max(best, a + A[i - 2] + dp[i - 2][j][k - 1][l]) # block of size 2
                    if i >= 3 and l >= 1:
                        best = max(best, a + A[i - 2] + A[i - 3] + dp[i - 3][j][k][l - 1])  # block of size 3
                    dp[i][j][k][l] = best
    return dp[n][x][y][z]

def brute(A, x, y, z):
    n = len(A); best = [0]
    def rec(i, cx, cy, cz, total):
        if total > best[0]: best[0] = total
        if i >= n: return
        rec(i + 1, cx, cy, cz, total)                              # skip
        if cx < x: rec(i + 1, cx + 1, cy, cz, total + A[i])
        if cy < y and i + 2 <= n: rec(i + 2, cx, cy + 1, cz, total + A[i] + A[i + 1])
        if cz < z and i + 3 <= n: rec(i + 3, cx, cy, cz + 1, total + A[i] + A[i + 1] + A[i + 2])
    rec(0, 0, 0, 0, 0)
    return best[0]

if __name__ == '__main__':
    rng = random.Random(31); bad = 0
    for _ in range(1500):
        n = rng.randint(1, 8)
        A = [rng.randint(-10, 10) for _ in range(n)]
        x, y, z = rng.randint(0, 3), rng.randint(0, 3), rng.randint(0, 3)
        bad += max_sum(A, x, y, z) != brute(A, x, y, z)
    print('mismatches over 1500 random cases:', bad)
