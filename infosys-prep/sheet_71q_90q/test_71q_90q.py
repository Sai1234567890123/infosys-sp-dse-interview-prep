"""Random tests of sol_71q_90q against brute force. Usage: python3 test_71q_90q.py <binary>"""
import itertools, random, subprocess, sys
from collections import deque

BIN = sys.argv[1]
R = random.Random(7)


def run(item, text):
    out = subprocess.run([BIN, item], input=text, capture_output=True, text=True).stdout.strip()
    return int(out)


def fmt(*parts):
    return "\n".join(" ".join(map(str, p)) if isinstance(p, (list, tuple)) else str(p) for p in parts) + "\n"


# ---- 71q: max count of B[i] > A[i] over permutations B of A
def t71():
    n = R.randint(1, 6)
    A = [R.randint(1, 6) for _ in range(n)]
    best = max(sum(1 for i in range(n) if p[i] > A[i]) for p in itertools.permutations(A))
    return fmt(n, A), best


# ---- 75q: minimal starting y so that some order of pairs can be processed
def feasible(y, order):
    for a, b in order:
        if y < a:
            return False
        y -= b
    return True


def t75():
    n = R.randint(1, 4)
    P = []
    for _ in range(n):
        b = R.randint(1, 6)
        a = b + R.randint(0, 6)
        P.append((a, b))
    best = None
    for y in range(0, sum(a for a, _ in P) + 2):
        if any(feasible(y, o) for o in itertools.permutations(P)):
            best = y
            break
    return fmt(n, *P), best


# ---- 76q: BFS over arrangements of B, moves = move one element to front or back
def t76():
    n = R.randint(1, 6)
    A = list(range(1, n + 1)); R.shuffle(A)
    B = list(range(1, n + 1)); R.shuffle(B)
    start, target = tuple(B), tuple(A)
    dist = {start: 0}
    q = deque([start])
    while q:
        s = q.popleft()
        if s == target:
            break
        for k in range(n):
            x = s[k]
            rest = s[:k] + s[k + 1:]
            for nxt in ((x,) + rest, rest + (x,)):
                if nxt not in dist:
                    dist[nxt] = dist[s] + 1
                    q.append(nxt)
    return fmt(n, A, B), dist[target]


# ---- 77q: longest substring (not whole string) with no letter both inside and outside
def t77():
    n = R.randint(1, 9)
    s = "".join(R.choice("abc") for _ in range(n))
    best = 0
    for l in range(n):
        for r in range(l, n):
            if l == 0 and r == n - 1:
                continue
            inside = set(s[l:r + 1])
            outside = set(s[:l] + s[r + 1:])
            if not (inside & outside):
                best = max(best, r - l + 1)
    return fmt(s), best


# ---- 78q: min ops to break numbers (x+y) so the array becomes non-decreasing (BFS)
def t78():
    n = R.randint(1, 3)
    b = tuple(R.randint(1, 7) for _ in range(n))
    dist = {b: 0}
    q = deque([b])
    goal = None
    while q:
        s = q.popleft()
        if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
            goal = dist[s]
            break
        for i, v in enumerate(s):
            for x in range(1, v):
                nxt = s[:i] + (x, v - x) + s[i + 1:]
                if nxt not in dist:
                    dist[nxt] = dist[s] + 1
                    q.append(nxt)
    return fmt(n, b), goal


# ---- 79q: K-th largest subset sum (empty subset counted), by full enumeration
def t79():
    n = R.randint(1, 7)
    b = [R.randint(-6, 6) for _ in range(n)]
    sums = []
    for mask in range(1 << n):
        sums.append(sum(b[i] for i in range(n) if mask >> i & 1))
    sums.sort(reverse=True)
    K = R.randint(1, min(30, 1 << n))
    return fmt(n, K, b), sums[K - 1]


# ---- 81q: integer points p with sum |p - x_i| <= d
def t81():
    n = R.randint(1, 5)
    x = [R.randint(-8, 8) for _ in range(n)]
    d = R.randint(0, 30)
    cnt = 0
    for p in range(min(x) - d - 2, max(x) + d + 3):
        if sum(abs(p - t) for t in x) <= d:
            cnt += 1
    return fmt(n, d, x), cnt


# ---- 82q: N strings, swap any characters; max number of palindromic strings
def t82():
    n = R.randint(1, 3)
    strs = ["".join(R.choice("ab") for _ in range(R.randint(1, 3))) for _ in range(n)]
    lens = [len(s) for s in strs]
    chars = [c for s in strs for c in s]
    best = 0
    for perm in set(itertools.permutations(chars)):
        pos = 0
        cnt = 0
        for L in lens:
            t = perm[pos:pos + L]
            pos += L
            if t == t[::-1]:
                cnt += 1
        best = max(best, cnt)
    return fmt(n, *strs), best


# ---- 84q: longest joinable chain of tiles (no rotation), brute force over orders
def t84():
    n = R.randint(1, 6)
    tiles = [R.choice(["RR", "GG", "RG", "GR"]) for _ in range(n)]
    best = 0

    def dfs(used, last_right, length):
        nonlocal best
        best = max(best, length)
        for i, t in enumerate(tiles):
            if not used >> i & 1 and (last_right is None or t[0] == last_right):
                dfs(used | 1 << i, t[1], length + 1)

    dfs(0, None, 0)
    return fmt(n, *tiles), best


# ---- 85q: min ops of +1 on subarrays of length <= L to reach b (BFS, values capped)
def t85():
    n = R.randint(1, 4)
    L = R.randint(1, n)
    b = [R.randint(0, 3) for _ in range(n)]
    cap = max(b) + L
    start = tuple([0] * n)
    dist = {start: 0}
    q = deque([start])
    goal = None
    while q:
        s = q.popleft()
        if all(s[i] >= b[i] for i in range(n)):
            goal = dist[s]
            break
        for l in range(n):
            for r in range(l, min(n, l + L)):
                nxt = tuple(s[i] + (1 if l <= i <= r else 0) for i in range(n))
                if max(nxt) <= cap and nxt not in dist:
                    dist[nxt] = dist[s] + 1
                    q.append(nxt)
    return fmt(n, L, b), goal


# ---- 86q: min cost so that all values distinct; cost c_i per +1 on element i
def t86():
    n = R.randint(1, 5)
    a = [R.randint(1, 4) for _ in range(n)]
    c = [R.randint(1, 5) for _ in range(n)]
    best = None
    for f in itertools.product(*[range(a[i], a[i] + n + 1) for i in range(n)]):
        if len(set(f)) == n:
            cost = sum(c[i] * (f[i] - a[i]) for i in range(n))
            best = cost if best is None else min(best, cost)
    return fmt(n, a, c), best


# ---- 90q: min rounds; each b kills at most one a per round; BFS over alive sets
def t90():
    n = R.randint(1, 4)
    m = R.randint(1, 3)
    a = [R.randint(1, 5) for _ in range(n)]
    b = [R.randint(1, 5) for _ in range(m)]
    full = (1 << n) - 1
    dist = {full: 0}
    q = deque([full])
    goal = -1
    while q:
        alive = q.popleft()
        if alive == 0:
            goal = dist[alive]
            break
        idx = [i for i in range(n) if alive >> i & 1]
        for k in range(1, min(len(idx), m) + 1):
            for S in itertools.combinations(idx, k):
                ok = any(all(b[p[j]] >= a[S[j]] for j in range(k))
                         for p in itertools.permutations(range(m), k))
                if ok:
                    nxt = alive
                    for i in S:
                        nxt &= ~(1 << i)
                    if nxt not in dist:
                        dist[nxt] = dist[alive] + 1
                        q.append(nxt)
    if goal == -1:
        return fmt(n, a, m, b), -1
    return fmt(n, a, m, b), goal


TESTS = {"71q": t71, "75q": t75, "76q": t76, "77q": t77, "78q": t78, "79q": t79,
         "81q": t81, "82q": t82, "84q": t84, "85q": t85, "86q": t86, "90q": t90}

if __name__ == "__main__":
    bad = 0
    for item, gen in TESTS.items():
        mism = 0
        for _ in range(300):
            text, want = gen()
            got = run(item, text)
            if got != want:
                mism += 1
                if mism <= 2:
                    print(item, "MISMATCH", repr(text), "want", want, "got", got)
        print(f"{item}: 300 cases, {mism} mismatches")
        bad += mism
    print("TOTAL MISMATCHES", bad)
