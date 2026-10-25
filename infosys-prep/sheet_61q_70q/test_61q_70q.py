"""Random tests of sol_61q_70q.cpp against brute force. Usage: python3 test_61q_70q.py <binary>"""
import heapq, itertools, random, subprocess, sys
BIN = sys.argv[1]
R = random.Random(5)

def run(item, text):
    return subprocess.run([BIN, item], input=text, capture_output=True, text=True).stdout.split("\n")

def brute61(a, b):
    best = None
    for x in a:
        for y in b:
            if y >= x and (best is None or y - x < best):
                best = y - x
    return -1 if best is None else best

def brute62(X, Y, Z):
    best = None
    for x in X:
        for y in Y:
            for z in Z:
                if z >= y >= x:
                    v = (z - y) + (y - x)
                    if best is None or v < best: best = v
    return -1 if best is None else best

def brute63(A, B, C):
    best = None
    for a, b, c in itertools.product(A, B, C):
        v = abs(a - b) + abs(b - c) + abs(c - a)
        if best is None or v < best: best = v
    return best

def brute64(A, B, S, T):
    # Dijkstra over strings; ops: rotate left (cost A), change one position to any letter in the alphabet (cost B)
    alpha = sorted(set(S + T))
    n = len(S)
    dist = {S: 0}
    pq = [(0, S)]
    while pq:
        d, s = heapq.heappop(pq)
        if s == T: return d
        if d > dist.get(s, 1 << 60): continue
        nxt = [(s[1:] + s[:1], A)]
        for i in range(n):
            for c in alpha:
                if c != s[i]:
                    nxt.append((s[:i] + c + s[i + 1:], B))
        for ns, w in nxt:
            if d + w < dist.get(ns, 1 << 60):
                dist[ns] = d + w
                heapq.heappush(pq, (d + w, ns))
    return None

def brute65(X, a):
    n = len(a); best = None
    for comp in itertools.product(range(X + 1), repeat=n):
        if sum(comp) != X: continue
        v = sum(a[i] * (-1) ** comp[i] for i in range(n))
        if best is None or v > best: best = v
    return best

def brute67(nums, q):
    nums = list(nums)
    for t, a, b in q:
        if t == 1:
            nums = [max(x, a) for x in nums]
        else:
            nums[a] = b
    return nums

def bad_count(name, trials, cases, exp_fn, text_fn, parse):
    b = 0
    for _ in range(trials):
        c = cases()
        got = parse(run(name, text_fn(c)))
        if got != exp_fn(c):
            b += 1
            if b <= 2: print(name, "MISMATCH", c, "exp", exp_fn(c), "got", got)
    print(f"{name}: {trials} cases, {b} mismatches")
    return b

tot = 0
def g61():
    return [R.randint(1, 9) for _ in range(R.randint(1, 6))], [R.randint(1, 9) for _ in range(R.randint(1, 6))]
# 61q needs equal sizes: fix by generating equal lengths
def g61e():
    n = R.randint(1, 6)
    return [R.randint(1, 9) for _ in range(n)], [R.randint(1, 9) for _ in range(n)]
tot += bad_count("61q", 300, g61e, lambda c: brute61(*c),
    lambda c: f"{len(c[0])}\n" + " ".join(map(str, c[0])) + "\n" + " ".join(map(str, c[1])) + "\n",
    lambda o: int(o[0]))

def g62():
    n = R.randint(1, 4)
    return [R.randint(1, 9) for _ in range(n)], [R.randint(1, 9) for _ in range(n)], [R.randint(1, 9) for _ in range(n)]
tot += bad_count("62q", 400, g62, lambda c: brute62(*c),
    lambda c: f"{len(c[0])}\n" + "".join(" ".join(map(str, x)) + "\n" for x in c),
    lambda o: int(o[0]))

def g63():
    n = R.randint(1, 4)
    return [R.randint(1, 20) for _ in range(n)], [R.randint(1, 20) for _ in range(n)], [R.randint(1, 20) for _ in range(n)]
tot += bad_count("63q", 400, g63, lambda c: brute63(*c),
    lambda c: f"{len(c[0])}\n" + "".join(" ".join(map(str, x)) + "\n" for x in c),
    lambda o: int(o[0]))

def g64():
    n = R.randint(1, 4)
    S = "".join(R.choice("abc") for _ in range(n))
    T = "".join(R.choice("abc") for _ in range(n))
    return R.randint(0, 6), R.randint(0, 6), S, T
def t64(c):
    A, B, S, T = c
    return f"1\n{len(S)} {A} {B}\n{S}\n{T}\n"
tot += bad_count("64q", 300, g64, lambda c: brute64(*c), t64, lambda o: int(o[0]))

def g65():
    n = R.randint(1, 4)
    return R.randint(0, 4), [R.randint(-6, 6) for _ in range(n)]
def t65(c):
    X, a = c
    return f"1\n{len(a)} {X}\n" + " ".join(map(str, a)) + "\n"
tot += bad_count("65q", 400, g65, lambda c: brute65(*c), t65, lambda o: int(o[0]))

def g67():
    n = R.randint(1, 6)
    nums = [R.randint(1, 9) for _ in range(n)]
    q = []
    for _ in range(R.randint(1, 6)):
        if R.random() < 0.5:
            q.append((1, R.randint(0, 10), -1))
        else:
            q.append((2, R.randint(0, n - 1), R.randint(0, 10)))
    return nums, q
def t67(c):
    nums, q = c
    return f"{len(nums)}\n" + " ".join(map(str, nums)) + f"\n{len(q)}\n" + "".join(f"{a} {b} {c2}\n" for a, b, c2 in q)
def p67(o):
    return [int(x) for x in o[0].split()]
tot += bad_count("67q", 400, g67, lambda c: brute67(*c), t67, p67)
print("TOTAL MISMATCHES:", tot)
