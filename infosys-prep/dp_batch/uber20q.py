"""20q Uber OA: arrays B and C (size N). At each index pick one element from B or C. No 3 consecutive picks from the same array. Maximize sum."""
import itertools, random

def uber(B, C):
    n = len(B)
    NEG = float('-inf')
    # state (arr, run): arr 0 = picked from B, 1 = from C; run = how many consecutive picks from arr (1 or 2)
    best = {(0, 1): B[0], (1, 1): C[0]}
    for i in range(1, n):
        nb = {}
        for (a, r), v in best.items():
            for arr in (0, 1):
                val = (B if arr == 0 else C)[i]
                if arr == a:
                    if r == 2: continue           # would make 3 in a row
                    key, nv = (arr, 2), v + val
                else:
                    key, nv = (arr, 1), v + val
                if nv > nb.get(key, NEG): nb[key] = nv
        best = nb
    return max(best.values())

def brute(B, C):
    n = len(B); best = None
    for picks in itertools.product((0, 1), repeat=n):
        ok = all(not (picks[i] == picks[i+1] == picks[i+2]) for i in range(n - 2))
        if not ok: continue
        s = sum((B if p == 0 else C)[i] for i, p in enumerate(picks))
        best = s if best is None else max(best, s)
    return best

if __name__ == '__main__':
    print('sample', uber([5, 3, 4], [10, 10, 10]), 'expect 25')
    rng = random.Random(9); bad = 0
    for _ in range(3000):
        n = rng.randint(1, 9)
        B = [rng.randint(1, 20) for _ in range(n)]; C = [rng.randint(1, 20) for _ in range(n)]
        bad += uber(B, C) != brute(B, C)
    print('mismatches over 3000 random cases:', bad)
