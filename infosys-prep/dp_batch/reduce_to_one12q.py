"""12q: from N reduce to 1. Ops: -1 costs y; /7 costs x (if divisible by 7); /3 costs z (if divisible by 3); /5 costs b (if divisible by 5). Minimum total cost."""
import heapq, random

def min_cost(n, y, x, z, b):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        best = dp[i - 1] + y
        if i % 7 == 0: best = min(best, dp[i // 7] + x)
        if i % 3 == 0: best = min(best, dp[i // 3] + z)
        if i % 5 == 0: best = min(best, dp[i // 5] + b)
        dp[i] = best
    return dp[n]

def dijkstra(n, y, x, z, b):
    dist = {n: 0}; pq = [(0, n)]
    while pq:
        d, v = heapq.heappop(pq)
        if v == 1: return d
        if d > dist[v]: continue
        moves = [(v - 1, y)]
        if v % 7 == 0: moves.append((v // 7, x))
        if v % 3 == 0: moves.append((v // 3, z))
        if v % 5 == 0: moves.append((v // 5, b))
        for w, c in moves:
            if w >= 1 and d + c < dist.get(w, 1 << 62):
                dist[w] = d + c; heapq.heappush(pq, (d + c, w))

if __name__ == '__main__':
    print('sample N=15 y=100 x=1 z=500 b=10000000 ->', min_cost(15, 100, 1, 500, 10000000))
    rng = random.Random(6); bad = 0
    for _ in range(2000):
        n = rng.randint(1, 60)
        y, x, z, b = (rng.randint(1, 100) for _ in range(4))
        bad += min_cost(n, y, x, z, b) != dijkstra(n, y, x, z, b)
    print('mismatches over 2000 random cases:', bad)
