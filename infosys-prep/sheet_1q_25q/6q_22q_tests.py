import random

# 6q (CodeChef SHOOT0 as pasted): line of M cells, b[i] in {0,1,2,3}.
# Person X sits at cells with b==1 or b==3, person Y at cells with b==2 or b==3.
# For each blue line position i (1-based), cost = sum of distances of each person to i.
# Output |costX(i) - costY(i)| for every i.
def shoot_brute(b):
    M = len(b); out = []
    X = [i + 1 for i in range(M) if b[i] in (1, 3)]
    Y = [i + 1 for i in range(M) if b[i] in (2, 3)]
    for i in range(1, M + 1):
        cx = sum(abs(i - p) for p in X)
        cy = sum(abs(i - p) for p in Y)
        out.append(abs(cx - cy))
    return out

def shoot_fast(b):
    M = len(b)
    def costs(pos_flags):
        # sum |i-p| for all people p, for every i, via prefix counts and prefix sums
        cnt = [0] * (M + 1); sm = [0] * (M + 1)
        for i in range(1, M + 1):
            f = pos_flags[i - 1]
            cnt[i] = cnt[i - 1] + f
            sm[i] = sm[i - 1] + f * i
        tot_c, tot_s = cnt[M], sm[M]
        res = []
        for i in range(1, M + 1):
            lc, ls = cnt[i], sm[i]              # people at or left of i
            rc, rs = tot_c - lc, tot_s - ls      # people right of i
            res.append((i * lc - ls) + (rs - i * rc))
        return res
    fx = [1 if v in (1, 3) else 0 for v in b]
    fy = [1 if v in (2, 3) else 0 for v in b]
    cx, cy = costs(fx), costs(fy)
    return [abs(x - y) for x, y in zip(cx, cy)]

# 22q (Visa OA as pasted): array of N zeros, Q queries [L,R] add +1, then points y: print value at y.
def visa_brute(n, queries, points):
    arr = [0] * (n + 1)
    for L, R in queries:
        for k in range(L, R + 1): arr[k] += 1
    return [arr[y] for y in points]

def visa_fast(n, queries, points):
    d = [0] * (n + 2)
    for L, R in queries:
        d[L] += 1; d[R + 1] -= 1
    pref = [0] * (n + 1); run = 0
    for i in range(1, n + 1):
        run += d[i]; pref[i] = run
    return [pref[y] for y in points]

random.seed(3)
bad6 = bad22 = 0
for _ in range(2000):
    M = random.randint(1, 8)
    b = [random.randint(0, 3) for _ in range(M)]
    if shoot_brute(b) != shoot_fast(b): bad6 += 1
    n = random.randint(1, 8)
    qs = []
    for _ in range(random.randint(0, 5)):
        L = random.randint(1, n); R = random.randint(L, n); qs.append((L, R))
    pts = [random.randint(1, n) for _ in range(random.randint(1, 4))]
    if visa_brute(n, qs, pts) != visa_fast(n, qs, pts): bad22 += 1
print("6q mismatches:", bad6, " 22q mismatches:", bad22)
print("6q sample b=[1,2,3]:", shoot_fast([1, 2, 3]))
print("22q sample N=8, queries (1,8),(5,8), points 1,5:", visa_fast(8, [(1, 8), (5, 8)], [1, 5]), "(expect [1, 2])")
