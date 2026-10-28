"""30q (LeetCode 'Paint House IV'): n houses (n even), 3 colours, cost[i][c].
Adjacent houses must differ; houses i and n-1-i (mirror pairs) must differ. Minimise the total cost."""
import itertools, random

INF = float('inf')

def min_cost(n, cost):
    rows = n // 2
    dp = [[[INF] * 3 for _ in range(3)] for _ in range(rows)]
    for i in range(3):
        for j in range(3):
            if i != j:
                dp[0][i][j] = cost[0][i] + cost[n - 1][j]
    for row in range(1, rows):
        for i in range(3):
            for j in range(3):
                if i == j: continue
                best = INF
                for i1 in range(3):
                    for j1 in range(3):
                        if i1 != i and j1 != j and i1 != j1:
                            best = min(best, dp[row - 1][i1][j1])
                dp[row][i][j] = best + cost[row][i] + cost[n - row - 1][j]
    return min(dp[rows - 1][i][j] for i in range(3) for j in range(3) if i != j)

def brute(n, cost):
    best = INF
    for colours in itertools.product(range(3), repeat=n):
        if any(colours[i] == colours[i + 1] for i in range(n - 1)): continue
        if any(colours[i] == colours[n - 1 - i] for i in range(n // 2)): continue
        best = min(best, sum(cost[i][colours[i]] for i in range(n)))
    return best

if __name__ == '__main__':
    rng = random.Random(30); bad = 0
    for _ in range(600):
        n = rng.choice((2, 4, 6, 8))
        cost = [[rng.randint(1, 20) for _ in range(3)] for _ in range(n)]
        b = brute(n, cost)
        if b == INF: continue
        bad += min_cost(n, cost) != b
    print('mismatches over random even-n cases:', bad)
