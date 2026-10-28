"""Problems from the screenshots in the last message: Thieves and Houses (26q), Stephen's internship salary, and the cost-jump array."""
import itertools, random

MOD = 10**9 + 7
NEG = float('-inf')

# Thieves and Houses (26q, screenshot): blocks of exactly 2 or exactly 3 consecutive houses.
# Gap between adjacent blocks: >= 1 house if both are size 2; >= 2 houses if either is size 3.
# f[i][s] = best total when a block of size s ends at index i (0-based).
# PM[t][k] = best f[j][t] over block ends j <= k, so the previous block must end at j <= st - 1 - need.
def thieves(H):
    n = len(H)
    f = [{2: NEG, 3: NEG} for _ in range(n)]
    PM = [{2: NEG, 3: NEG} for _ in range(n)]
    best = 0
    for i in range(n):
        for s in (2, 3):
            st = i - s + 1
            if st < 0:
                continue
            block = sum(H[st:i + 1])
            cand = block                              # this block may be the first one
            for t in (2, 3):
                need = 1 if (t == 2 and s == 2) else 2
                k = st - 1 - need
                if k >= 0 and PM[k][t] != NEG:
                    cand = max(cand, PM[k][t] + block)
            f[i][s] = cand
        for t in (2, 3):
            PM[i][t] = max(f[i][t], PM[i - 1][t] if i > 0 else NEG)
        best = max(best, f[i][2], f[i][3])
    return best % MOD

def thieves_brute(H):
    n = len(H)
    best = 0
    def rec(i, prev_end, prev_size, total):
        nonlocal best
        best = max(best, total)
        for st in range(i, n):
            for s in (2, 3):
                if st + s > n:
                    continue
                if prev_end is not None:
                    gap = st - prev_end - 1
                    need = 1 if (prev_size == 2 and s == 2) else 2
                    if gap < need:
                        continue
                rec(st + s, st + s - 1, s, total + sum(H[st:st + s]))
    rec(0, None, None, 0)
    return best % MOD

# Stephen's internship: each day easy or hard or nothing; hard allowed only if no work the previous day.
def stephen(rows):
    worked, idle = NEG, 0          # idle: best with no work on the last day; worked: best with work on last day
    for easy, hard in rows:
        new_idle = max(idle, worked)
        new_worked = max(idle + easy, idle + hard, worked + easy)
        idle, worked = new_idle, new_worked
    return max(idle, worked)

def stephen_brute(rows):
    n = len(rows)
    best = 0
    for choice in itertools.product((0, 1, 2), repeat=n):  # 0 nothing, 1 easy, 2 hard
        ok = True
        total = 0
        for i, c in enumerate(choice):
            if c == 2 and i > 0 and choice[i - 1] != 0:
                ok = False
                break
            total += (0, rows[i][0], rows[i][1])[c]
        if ok:
            best = max(best, total)
    return best

if __name__ == '__main__':
    print('Thieves samples:', [thieves(x) for x in ([1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [4, 1, 1, 5, 6], [1, 5, 5, 5, 1])], 'expect 0 3 6 9 16 15')
    print('Stephen sample:', stephen([(1, 2), (4, 10), (20, 21), (2, 23)]), 'expect 33')
    rng = random.Random(5)
    bad = {'thieves': 0, 'stephen': 0}
    for _ in range(300):
        n = rng.randint(1, 7)
        H = [rng.randint(0, 9) for _ in range(n)]
        bad['thieves'] += thieves(H) != thieves_brute(H)
        rows = [(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(n)]
        rows = [(min(e, h - 1) if h > 1 else e, h) for e, h in rows]
        rows = [(e, max(h, e + 1)) for e, h in rows]
        bad['stephen'] += stephen(rows) != stephen_brute(rows)
    print('mismatches', bad)
