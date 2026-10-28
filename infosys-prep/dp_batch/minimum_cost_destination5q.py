"""5q (Amazon summer school, 'Minimum Cost to Reach the Destination'): N cities, from i fly to i+1 or i+3,
cost of a flight i->j is |A[i]-A[j]|. Minimum total cost from city 1 to city N. 1-based indexing."""
import random

def min_cost(A):
    n = len(A)
    dp = [0] * n
    for i in range(1, n):
        best = dp[i - 1] + abs(A[i] - A[i - 1])
        if i >= 3:
            best = min(best, dp[i - 3] + abs(A[i] - A[i - 3]))
        dp[i] = best
    return dp[n - 1]

def brute(A):
    n = len(A); best = [None]
    def go(i, cost):
        if i == n - 1:
            best[0] = cost if best[0] is None else min(best[0], cost); return
        for step in (1, 3):
            j = i + step
            if j < n: go(j, cost + abs(A[j] - A[i]))
    go(0, 0)
    return best[0]

if __name__ == '__main__':
    rng = random.Random(4); bad = 0
    for _ in range(3000):
        n = rng.randint(4, 12)
        A = [rng.randint(1, 50) for _ in range(n)]
        bad += min_cost(A) != brute(A)
    print('mismatches over 3000 random cases:', bad)
    print('example A=[1,2,3,4,5] ->', min_cost([1, 2, 3, 4, 5]))
