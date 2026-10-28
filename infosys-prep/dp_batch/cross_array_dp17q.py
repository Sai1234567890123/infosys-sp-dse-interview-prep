"""17q Goldman cost-jump array: start at index 1 (cost paid). Moves +2 or -1; landing adds that index's cost; each index visited once; no two backward moves in a row. Stop when you reach index n or jump past it. Minimise total cost.

A back move always comes right after landing on i by +2 (from i-2), so the walk is made of two block types:
  +2  : p -> p+2
  zig : p -> p+2 -> p+1 -> p+3   (land p+2, back to p+1, then +2 to p+3)
f[p] = min cost of a walk that has landed on p and has not visited p+1 or beyond."""
import random

def min_cost_dp(b):
    n = len(b)
    cost = lambda i: b[i - 1]            # 1-indexed
    INF = float('inf')
    f = [INF] * (n + 4)
    f[1] = cost(1)
    best = INF
    for p in range(1, n + 1):
        if f[p] == INF: continue
        if p == n:
            best = min(best, f[p]); continue
        if p + 2 <= n:
            f[p + 2] = min(f[p + 2], f[p] + cost(p + 2))
            if p + 2 < n:                            # landing on n ends the walk, so zig only if p+2 < n
                c = f[p] + cost(p + 2) + cost(p + 1)  # zig: land p+2, back to p+1
                if p + 3 <= n:
                    f[p + 3] = min(f[p + 3], c + cost(p + 3))
                else:
                    best = min(best, c)              # then jump past the end from p+1
        else:
            best = min(best, f[p])                   # +2 jumps past the end
    return best

def brute(b):
    n = len(b); best = [float('inf')]
    def dfs(pos, visited, total, last_back):
        if pos >= n:                                 # reached or passed the end
            best[0] = min(best[0], total); return
        for step, back in ((2, False), (-1, True)):
            if back and last_back: continue
            nxt = pos + step
            if nxt < 1 or nxt in visited: continue
            if nxt > n:
                dfs(nxt, visited, total, back)
            else:
                dfs(nxt, visited | {nxt}, total + b[nxt - 1], back)
    dfs(1, frozenset({1}), b[0], False)
    return best[0]

if __name__ == '__main__':
    for ex, exp in (([2, 5, 8], 10), ([2, -100, 8, 5, 0], -85), ([2, 10, 8, -5, -10, 5], 0)):
        print(ex, 'dp', min_cost_dp(ex), 'brute', brute(ex), 'expect', exp)
    rng = random.Random(12); bad = 0
    for _ in range(3000):
        n = rng.randint(1, 9)
        b = [rng.randint(-20, 20) for _ in range(n)]
        bad += min_cost_dp(b) != brute(b)
    print('mismatches vs brute over 3000 random cases:', bad)
