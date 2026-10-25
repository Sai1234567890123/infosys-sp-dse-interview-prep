"""Random tests of sol_48q_60q.cpp against brute force. Usage: python3 test_48q_60q.py <binary>"""
import itertools, random, subprocess, sys
BIN = sys.argv[1]
R = random.Random(11)

def run(item, text):
    return subprocess.run([BIN, item], input=text, capture_output=True, text=True).stdout.split()

def inter(a, b):  # closed integer intervals share a point
    return a[0] <= b[1] and b[0] <= a[1]

def brute48(seg):
    n = len(seg); best = 0
    for k in range(1, n + 1):
        for sub in itertools.combinations(range(n), k):
            for i in sub:
                if all(inter(seg[i], seg[j]) for j in sub):
                    best = max(best, k); break
    return n - best

def brute50(en, ex):
    best, t_best = 0, None
    for t in range(min(en), max(ex) + 1):
        c = sum(1 for a, b in zip(en, ex) if a <= t <= b)
        if c > best: best, t_best = c, t
    return f"{best} {t_best}"

def brute51(arr):
    # half-step grid: covered points, gaps are maximal uncovered open runs between covered points
    pts = [x / 2 for x in range(0, 2 * max(b for _, b in arr) + 1)]
    cov = lambda x: any(a <= x <= b for a, b in arr)
    gaps = []
    xs = [x for x in pts if cov(x)]
    for x in xs:
        nxt = [y for y in xs if y > x]
        if nxt and nxt[0] > x + 0.5 + 1e-9 and not any(cov(x + 0.5 * k) for k in range(1, 2 * int(nxt[0] - x))):
            gaps.append((x, nxt[0]))
    # gaps only where something uncovered lies strictly between x and next covered point
    res = []
    for x in xs:
        nxt = [y for y in xs if y > x]
        if nxt and nxt[0] > x + 0.5:
            res.append((x, nxt[0]))
    return res

def brute52(arr):
    n = len(arr); parent = list(range(n))
    def f(x):
        while parent[x] != x: x = parent[x]
        return x
    for i in range(n):
        for j in range(n):
            if inter(arr[i], arr[j]):
                parent[f(i)] = f(j)
    groups = {}
    for i in range(n): groups.setdefault(f(i), []).append(arr[i])
    return sorted((min(a for a, _ in g), max(b for _, b in g)) for g in groups.values())

def brute53(arr):
    n = len(arr); best = 0
    for k in range(n, 0, -1):
        for sub in itertools.combinations(arr, k):
            s = sorted(sub, key=lambda p: p[1])
            if all(s[i][1] <= s[i + 1][0] for i in range(k - 1)):
                return n - k
    return n

def brute54(nums, k):
    from functools import lru_cache
    @lru_cache(None)
    def go(state, k):
        if k == 0 or not any(state): return 0
        best = None
        for i, x in enumerate(state):
            if x == 0: continue
            ns = list(state); ns[i] = (x + 2) // 3
            v = x + go(tuple(sorted(ns)), k - 1)
            best = v if best is None or v > best else best
        return best
    return go(tuple(sorted(nums)), k)

def brute55(jobs):  # max profit over feasible subsets
    n = len(jobs); best = 0
    for mask in range(1 << n):
        sel = [jobs[i] for i in range(n) if mask >> i & 1]
        ds = sorted(d for d, _ in sel)
        if all(ds[i] >= i + 1 for i in range(len(ds))):
            best = max(best, sum(p for _, p in sel))
    return best

def brute56(arr):
    xs = sorted({v for p in arr for v in p})
    for k in range(0, len(arr) + 1):
        for pts in itertools.combinations(xs, k):
            if all(any(a <= x <= b for x in pts) for a, b in arr):
                return k
    return 0

def brute57(clips, T):
    best = None
    for k in range(1, len(clips) + 1):
        for sub in itertools.combinations(clips, k):
            cov = [False] * (T + 1)
            for a, b in sub:
                for x in range(max(a, 0), min(b, T) + 1): cov[x] = True
            # coverage of [0,T] as real interval: check each unit [x,x+1] covered
            ok = all(any(a <= x and x + 1 <= b for a, b in sub) for x in range(T))
            if ok: return k
    return -1

def brute58(tasks, T):
    for k in range(0, T + 1):
        for S in itertools.combinations(range(1, T + 1), k):
            if all(sum(1 for x in S if s <= x <= e) >= d for s, e, d in tasks):
                return k
    return None

bad = {}
def check(name, trials, gen, exp, text):
    b = 0
    for _ in range(trials):
        case = gen()
        got = run(name, text(case))
        e = exp(case)
        if isinstance(e, list):
            ok = [tuple(map(int, got[1 + 2 * i:3 + 2 * i])) for i in range(int(got[0]))] == e if got else False
        else:
            ok = " ".join(got) == str(e) if not isinstance(e, tuple) else " ".join(got) == f"{e[0]} {e[1]}"
        if not ok:
            b += 1
            if b <= 2: print(name, "MISMATCH", case, "exp", e, "got", got)
    print(f"{name}: {trials} cases, {b} mismatches"); bad[name] = b

def gen_seg(n_max=6, lo=0, hi=12):
    n = R.randint(1, n_max)
    out = []
    for _ in range(n):
        a = R.randint(lo, hi); out.append((a, a + R.randint(0, 4)))
    return out

def fmt_seg(arr):
    return f"{len(arr)}\n" + "".join(f"{a} {b}\n" for a, b in arr)

check("48q", 400, lambda: gen_seg(), brute48, fmt_seg)

def gen50():
    n = R.randint(1, 6)
    en = [R.randint(1, 15) for _ in range(n)]
    ex = [e + R.randint(0, 6) for e in en]
    return en, ex
check("50q", 400, gen50, lambda c: brute50(*c),
      lambda c: f"{len(c[0])}\n" + " ".join(map(str, c[0])) + "\n" + " ".join(map(str, c[1])) + "\n")

check("51q", 300, lambda: gen_seg(5, 0, 14), brute51, fmt_seg)
check("52q", 400, lambda: gen_seg(), brute52, fmt_seg)
check("53q", 300, lambda: gen_seg(6, 0, 10), brute53, fmt_seg)

def gen54():
    n = R.randint(1, 4)
    return [R.randint(1, 30) for _ in range(n)], R.randint(0, 4)
check("54q", 300, gen54, lambda c: brute54(c[0], c[1]),
      lambda c: f"{len(c[0])} {c[1]}\n" + " ".join(map(str, c[0])) + "\n")

def gen55():
    n = R.randint(1, 7)
    return [(R.randint(1, 4), R.randint(1, 50)) for _ in range(n)]

# 55q: check profit only (count depends on tie-breaking among equal-profit optima)
b = 0
for _ in range(300):
    jobs = gen55()
    got = run("55q", f"{len(jobs)}\n" + "".join(f"{d} {p}\n" for d, p in jobs))
    if int(got[1]) != brute55(jobs): b += 1
print(f"55q (profit): 300 cases, {b} mismatches"); bad["55q"] = b

check("56q", 300, lambda: gen_seg(6, 0, 12), brute56, fmt_seg)

def gen57():
    T = R.randint(1, 8)
    n = R.randint(1, 5)
    clips = []
    for _ in range(n):
        a = R.randint(0, T); clips.append((a, a + R.randint(0, 4)))
    return clips, T
check("57q", 300, gen57, lambda c: brute57(c[0], c[1]),
      lambda c: f"{len(c[0])} {c[1]}\n" + "".join(f"{a} {b}\n" for a, b in c[0]))

def gen58():
    T = R.randint(1, 6)
    n = R.randint(1, 4)
    tasks = []
    for _ in range(n):
        s = R.randint(1, T); e = R.randint(s, T); d = R.randint(1, e - s + 1)
        tasks.append((s, e, d))
    return tasks, T
b = 0
for _ in range(300):
    tasks, T = gen58()
    got = run("58q", f"{len(tasks)}\n" + "".join(f"{s} {e} {d}\n" for s, e, d in tasks))
    if int(got[0]) != brute58(tasks, T): b += 1
print(f"58q: 300 cases, {b} mismatches"); bad["58q"] = b
print("TOTAL MISMATCHES:", sum(bad.values()))
