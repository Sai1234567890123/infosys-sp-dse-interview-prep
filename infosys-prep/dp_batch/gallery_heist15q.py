"""15q/16q Gallery Heist (4 parts). Indices 0-based in code.
Part 1: max sum with no two adjacent picks (may pick nothing).
Part 2: max sum with exactly k picks, no two adjacent (None if impossible).
Part 3: exactly k picks, adjacency allowed, minus P per adjacent pair of picks.
Part 4: two thieves; each gallery taken by at most one; each thief's own picks are non-adjacent. Max total."""
import itertools, random

NEG = float('-inf')

def part1(a):
    take, skip = NEG, 0                       # take: best with last gallery taken; skip: best with last not taken
    best = 0
    for x in a:
        take, skip = skip + x, max(take, skip)
    return max(take, skip, 0)

def part2(a, k):
    n = len(a)
    # f[j][s]: best sum with j picks so far, s = last gallery taken
    f = {(0, False): 0}
    for x in a:
        g = {}
        for (j, s), v in f.items():
            for key, nv in (((j, False), v), ((j + 1, True), v + x if not s else NEG)):
                if nv > g.get(key, NEG): g[key] = nv
        f = g
    vals = [v for (j, s), v in f.items() if j == k]
    return max(vals) if vals and max(vals) > NEG else None

def part3(a, k, P):
    f = {(0, False): 0}                       # (picks, last taken)
    for x in a:
        g = {}
        for (j, s), v in f.items():
            for key, nv in (((j, False), v), ((j + 1, True), v + x - (P if s else 0))):
                if nv > g.get(key, NEG): g[key] = nv
        f = g
    vals = [v for (j, s), v in f.items() if j == k]
    return max(vals) if vals else None

def part4(a):
    NA = NEG
    dA, dB, dX = NEG, NEG, 0                  # state of last gallery: thief A took it, B took it, nobody
    for x in a:
        nA = x + max(dX, dB)
        nB = x + max(dX, dA)
        nX = max(dA, dB, dX)
        dA, dB, dX = nA, nB, nX
    return max(dA, dB, dX)

# ---- brute force checks ----
def brute1(a):
    best = 0
    n = len(a)
    for mask in range(1 << n):
        if mask & (mask >> 1): continue
        best = max(best, sum(a[i] for i in range(n) if mask >> i & 1))
    return best

def brute2(a, k):
    n = len(a); best = None
    for mask in range(1 << n):
        if mask & (mask >> 1) or bin(mask).count('1') != k: continue
        v = sum(a[i] for i in range(n) if mask >> i & 1)
        best = v if best is None else max(best, v)
    return best

def brute3(a, k, P):
    n = len(a); best = None
    for mask in range(1 << n):
        if bin(mask).count('1') != k: continue
        v = sum(a[i] for i in range(n) if mask >> i & 1)
        v -= P * sum(1 for i in range(n - 1) if mask >> i & 1 and mask >> (i + 1) & 1)
        best = v if best is None else max(best, v)
    return best

def brute4(a):
    n = len(a); best = NEG
    for assign in itertools.product((0, 1, 2), repeat=n):     # 0 none, 1 thief A, 2 thief B
        ok = all(not (assign[i] and assign[i] == assign[i + 1]) for i in range(n - 1))
        if not ok: continue
        best = max(best, sum(a[i] for i in range(n) if assign[i]))
    return best

if __name__ == '__main__':
    rng = random.Random(8); bad = [0, 0, 0, 0]
    for _ in range(1500):
        n = rng.randint(1, 8)
        a = [rng.randint(-10, 10) for _ in range(n)]
        k = rng.randint(0, n)
        P = rng.randint(0, 5)
        bad[0] += part1(a) != brute1(a)
        bad[1] += part2(a, k) != brute2(a, k)
        bad[2] += part3(a, k, P) != brute3(a, k, P)
        bad[3] += part4(a) != brute4(a)
    print('mismatches per part (1..4) over 1500 cases:', bad)
    print('sample part1 [3,2,7,10] ->', part1([3, 2, 7, 10]), 'expect 13')
