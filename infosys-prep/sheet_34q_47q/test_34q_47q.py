"""Random tests: C++ solutions in sol_34q_47q.cpp vs independent Python brute force.
Run: python3 test_34q_47q.py <path-to-compiled-binary>
"""
import itertools
import random
import subprocess
import sys
from collections import deque

BIN = sys.argv[1]


def run(item, text):
    out = subprocess.run([BIN, item], input=text, capture_output=True, text=True, timeout=10)
    return out.stdout.strip()


def powers_cover_min(L, memo={}):
    # min number of powers of two (with repetition) summing to L: coin change, independent of popcount
    if L == 0:
        return 0
    if L not in memo:
        best = None
        p = 1
        while p <= L:
            c = 1 + powers_cover_min(L - p)
            best = c if best is None or c < best else best
            p *= 2
        memo[L] = best
    return memo[L]


def brute_cover(N, segs):
    covered = [False] * (N + 2)
    for l, r in segs:
        for x in range(l, r + 1):
            covered[x] = True
    total, run_len = 0, 0
    for x in range(1, N + 1):
        if not covered[x]:
            run_len += 1
        else:
            total += powers_cover_min(run_len)
            run_len = 0
    total += powers_cover_min(run_len)
    return total


def brute_34(t):
    n = len(t)
    start = '0' * n
    dist = {start: 0}
    q = deque([start])
    while q:
        s = q.popleft()
        for i in range(n):
            ns = s[:i] + ''.join('1' if c == '0' else '0' for c in s[i:])
            if ns not in dist:
                dist[ns] = dist[s] + 1
                q.append(ns)
    return dist[t]


def brute_37(w):
    lst = list(enumerate(w))
    ans = 0
    while lst:
        k = min(range(len(lst)), key=lambda j: (lst[j][1], lst[j][0]))
        ans += lst[k][1]
        rem = {k, k - 1, k + 1}
        lst = [x for j, x in enumerate(lst) if j not in rem or j < 0 or j >= len(lst)]
        # rem may contain out-of-range indices which are simply ignored above
    return ans


def brute_39(k, a, b):
    n = len(a)
    best = None
    rng = range(-k, k + 1)
    for t in itertools.product(rng, repeat=n):
        if sum(abs(x) for x in t) > k:
            continue
        val = sum((a[i] + 2 * t[i]) * b[i] for i in range(n))
        best = val if best is None or val < best else best
    return best


def brute_40(a, b):
    return min(sum(abs(a[i] - p[i]) for i in range(len(a))) for p in itertools.permutations(b))


def brute_41(g, s):
    best = 0
    for k in range(len(g) + 1):
        for gs in itertools.combinations(sorted(g), k):
            for ss in itertools.permutations(s, k):
                if all(ss[i] >= gs[i] for i in range(k)):
                    best = max(best, k)
                    break
    return best


def brute_42(s):
    n = len(s)
    dp = [0] + [10 ** 9] * n
    for i in range(1, n + 1):
        for j in range(i):
            seg = s[j:i]
            if len(set(seg)) == len(seg):
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n]


def brute_43(nums):
    n = len(nums)
    seen = {0}
    q = deque([0])
    while q:
        x = q.popleft()
        for j in range(1, nums[x] + 1):
            y = x + j
            if y < n and y not in seen:
                seen.add(y)
                q.append(y)
    return (n - 1) in seen or n == 1


def brute_44(nums):
    n = len(nums)
    dist = [None] * n
    dist[0] = 0
    q = deque([0])
    while q:
        x = q.popleft()
        for y in range(x + 1, min(n, x + nums[x] + 1)):
            if dist[y] is None:
                dist[y] = dist[x] + 1
                q.append(y)
    return dist[n - 1]


def brute_45(seg):
    best = None
    for i, (Li, Ri, Ci) in enumerate(seg):
        for j, (Lj, Rj, Cj) in enumerate(seg):
            if i != j and Rj < Li:
                v = Ci * Cj
                best = v if best is None or v < best else best
    return best if best is not None else "NONE"


def brute_46(n, a):
    best_h, best_p = None, None
    for p in itertools.permutations(range(1, n + 1)):
        h = sum(1 for i in range(n) if a[i] != p[i])
        if best_h is None or h < best_h or (h == best_h and list(p) < best_p):
            best_h, best_p = h, list(p)
    return best_p


def brute_47(st, en):
    n = len(st)
    cnt = 0
    for x, y, z in itertools.combinations(range(n), 3):
        ivs = sorted([(st[x], en[x]), (st[y], en[y]), (st[z], en[z])])
        if ivs[0][1] < ivs[1][0] and ivs[1][1] < ivs[2][0]:
            cnt += 1
    return cnt


def check(name, trials, gen, brute, fmt):
    bad = 0
    for _ in range(trials):
        case = gen()
        text, expected = fmt(case), brute(*case) if isinstance(case, tuple) else brute(case)
        got = run(name, text)
        if str(expected).lower() != got.lower():
            bad += 1
            if bad <= 2:
                print(name, "MISMATCH", repr(text), "expected", expected, "got", got)
    print(f"{name}: {trials} cases, {bad} mismatches")
    return bad


total_bad = 0
R = random.Random(7)

# 34q
def gen34():
    return ''.join(R.choice('01') for _ in range(R.randint(1, 9)))
total_bad += check("34q", 300, gen34, brute_34, lambda t: t + "\n")

# 35q and 36q: N up to 60, non-overlapping segments in random order
def gen_cover():
    N = R.randint(1, 60)
    k = R.randint(0, 5)
    pts = sorted(R.sample(range(1, N + 1), min(N, 2 * k)))
    segs = []
    for i in range(0, len(pts) - 1, 2):
        segs.append((pts[i], pts[i + 1]))
    R.shuffle(segs)
    return N, segs

def fmt_cover(case):
    N, segs = case
    return f"{N}\n{len(segs)}\n" + "".join(f"{l} {r}\n" for l, r in segs)

total_bad += check("35q", 400, gen_cover, lambda N, s: brute_cover(N, s), fmt_cover)
total_bad += check("36q", 400, gen_cover, lambda N, s: brute_cover(N, s), fmt_cover)

# 37q
def gen37():
    n = R.randint(1, 12)
    return [R.randint(1, 20) for _ in range(n)]

total_bad += check("37q", 400, gen37, brute_37,
                   lambda w: f"{len(w)}\n" + " ".join(map(str, w)) + "\n")

# 39q
def gen39():
    n = R.randint(1, 3)
    k = R.randint(0, 3)
    a = [R.randint(-5, 5) for _ in range(n)]
    b = [R.randint(-5, 5) for _ in range(n)]
    return k, a, b

total_bad += check("39q", 300, gen39, brute_39,
                   lambda c: f"{len(c[1])} {c[0]}\n" + " ".join(map(str, c[1])) + "\n" + " ".join(map(str, c[2])) + "\n")

# 40q
def gen40():
    n = R.randint(1, 6)
    return [R.randint(0, 20) for _ in range(n)], [R.randint(0, 20) for _ in range(n)]

total_bad += check("40q", 300, gen40, brute_40,
                   lambda c: f"{len(c[0])}\n" + " ".join(map(str, c[0])) + "\n" + " ".join(map(str, c[1])) + "\n")

# 41q
def gen41():
    return [R.randint(1, 6) for _ in range(R.randint(1, 5))], [R.randint(1, 6) for _ in range(R.randint(1, 5))]

total_bad += check("41q", 300, gen41, brute_41,
                   lambda c: f"{len(c[0])} {len(c[1])}\n" + " ".join(map(str, c[0])) + "\n" + " ".join(map(str, c[1])) + "\n")

# 42q
def gen42():
    return ''.join(R.choice('abcd') for _ in range(R.randint(1, 12)))

total_bad += check("42q", 300, gen42, brute_42, lambda s: s + "\n")

# 43q
def gen43():
    n = R.randint(1, 8)
    return [R.randint(0, 3) for _ in range(n)]

total_bad += check("43q", 300, gen43, brute_43,
                   lambda a: f"{len(a)}\n" + " ".join(map(str, a)) + "\n")

# 44q: only reachable inputs
def gen44():
    while True:
        a = gen43()
        if brute_43(a):
            return a

total_bad += check("44q", 300, gen44, brute_44,
                   lambda a: f"{len(a)}\n" + " ".join(map(str, a)) + "\n")

# 45q
def gen45():
    n = R.randint(1, 7)
    out = []
    for _ in range(n):
        L = R.randint(1, 20)
        R_ = L + R.randint(0, 5)
        out.append((L, R_, R.randint(-5, 5)))
    return out

total_bad += check("45q", 400, gen45, brute_45,
                   lambda seg: f"{len(seg)}\n" + "".join(f"{l} {r} {c}\n" for l, r, c in seg))

# 46q
def gen46():
    n = R.randint(1, 6)
    return n, [R.randint(1, n + 2) for _ in range(n)]

total_bad += check("46q", 400, gen46, lambda n, a: " ".join(map(str, brute_46(n, a))),
                   lambda c: f"{c[0]}\n" + " ".join(map(str, c[1])) + "\n")

# 47q
def gen47():
    n = R.randint(1, 8)
    st, en = [], []
    for _ in range(n):
        a = R.randint(1, 15)
        st.append(a)
        en.append(a + R.randint(0, 4))
    return st, en

total_bad += check("47q", 400, gen47, brute_47,
                   lambda c: f"{len(c[0])}\n" + " ".join(map(str, c[0])) + "\n" + " ".join(map(str, c[1])) + "\n")

print("TOTAL MISMATCHES:", total_bad)
