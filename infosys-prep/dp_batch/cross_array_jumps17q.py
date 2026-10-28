"""17q (Goldman OA): array b (1-indexed). Start at index 1 (its cost is paid). Moves: +2 forward or -1 backward.
Landing on an index adds its cost. Each index may be visited at most once. Reach index n or jump past it; minimise total."""
import sys
from functools import lru_cache

def min_cost_bruteforce(b):
    n = len(b)
    best = [None]
    def dfs(pos, visited, cost, last_back):
        if pos > n:                       # crossed the array
            best[0] = cost if best[0] is None else min(best[0], cost); return
        if pos == n:
            best[0] = cost if best[0] is None else min(best[0], cost)
        for step, back in ((2, False), (-1, True)):
            nxt = pos + step
            if back and last_back: continue      # no consecutive backward moves
            if nxt < 1: continue
            if nxt <= n and nxt in visited: continue
            if nxt > n:
                dfs(nxt, visited, cost, back)  # crossing ends the walk
            else:
                dfs(nxt, visited | {nxt}, cost + b[nxt - 1], back)
    dfs(1, frozenset({1}), b[0], False)
    return best[0]

if __name__ == '__main__':
    print('example [2,5,8] ->', min_cost_bruteforce([2, 5, 8]), 'expect 10 (cost = 10 on the screenshot)')
    print('example [2,-100,8,5,0] ->', min_cost_bruteforce([2, -100, 8, 5, 0]), 'expect -85')
    print('example [2,10,8,-5,-10,5] ->', min_cost_bruteforce([2, 10, 8, -5, -10, 5]), 'expect 0')
