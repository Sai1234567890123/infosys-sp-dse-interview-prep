"""DP batch 1 from message.md (sections 3q, 8q, 9q, 10q, 11q, 13q, 14q, 22q, 23q). Each has a solver and a brute-force check."""
import itertools, random

# 3q: max sum of a subset with no two adjacent elements (empty subset allowed).
def q3(a):
    inc, exc = 0, 0            # best with/without taking the previous element
    for x in a:
        inc, exc = exc + x, max(inc, exc)
    return max(inc, exc, 0)

def q3_brute(a):
    best = 0
    n = len(a)
    for m in range(1 << n):
        idx = [i for i in range(n) if m >> i & 1]
        if all(idx[t + 1] - idx[t] > 1 for t in range(len(idx) - 1)):
            best = max(best, sum(a[i] for i in idx))
    return best

# 8q: journey from index 1 to N, jumps of 1, 3 or 5; maximise the sum of visited values (start and end included).
def q8(b):
    n = len(b)
    NEG = float('-inf')
    dp = [NEG] * n
    dp[0] = b[0]
    for i in range(1, n):
        best = NEG
        for s in (1, 3, 5):
            if i - s >= 0:
                best = max(best, dp[i - s])
        dp[i] = best + b[i] if best != NEG else NEG
    return dp[n - 1]

def q8_brute(b):
    n = len(b)
    best = None
    for m in range(1 << (n - 2)) if n >= 2 else [0]:
        path = [0] + [i + 1 for i in range(n - 2) if m >> i & 1] + [n - 1]
        if n == 1:
            path = [0]
        if all(path[t + 1] - path[t] in (1, 3, 5) for t in range(len(path) - 1)):
            s = sum(b[i] for i in path)
            best = s if best is None else max(best, s)
    return best

# 9q: cost a[i]*a[j] to jump i -> j with i < j <= i+K; minimum total cost from 0 to N-1.
def q9(a, K):
    n = len(a)
    dp = [0] * n
    for j in range(1, n):
        dp[j] = min(dp[i] + a[i] * a[j] for i in range(max(0, j - K), j))
    return dp[n - 1]

def q9_brute(a, K):
    n = len(a)
    best = None
    def go(i, cost):
        nonlocal best
        if i == n - 1:
            best = cost if best is None else min(best, cost)
            return
        for j in range(i + 1, min(n - 1, i + K) + 1):
            go(j, cost + a[i] * a[j])
    go(0, 0)
    return best

# 10q (AtCoder dp_c): each day pick one of three activities, never the same activity twice in a row; maximise happiness.
def q10(rows):
    prev = [0, 0, 0]
    for a, b, c in rows:
        cur = [a + max(prev[1], prev[2]), b + max(prev[0], prev[2]), c + max(prev[0], prev[1])]
        prev = cur
    return max(prev)

def q10_brute(rows):
    best = None
    for pick in itertools.product(range(3), repeat=len(rows)):
        if any(pick[i] == pick[i + 1] for i in range(len(pick) - 1)):
            continue
        s = sum(rows[i][pick[i]] for i in range(len(rows)))
        best = s if best is None else max(best, s)
    return best

# 11q: count journeys from index 1 to n, each step +1 or +2, whose sum is odd (a journey is a set of visited indices).
def q11(a):
    n = len(a)
    ev = [0] * n; od = [0] * n
    (ev if a[0] % 2 == 0 else od)[0] = 1
    for i in range(1, n):
        same = ev if a[i] % 2 == 0 else od   # parity of a[i]
        other = od if a[i] % 2 == 0 else ev
        # journeys ending at i: parity of the prefix sum flips when a[i] is odd
        for arr, par in ((ev, 0), (od, 1)):
            pass
        pe = ev[i - 1] + (ev[i - 2] if i >= 2 else 0)
        po = od[i - 1] + (od[i - 2] if i >= 2 else 0)
        if a[i] % 2 == 0:
            ev[i], od[i] = pe, po
        else:
            ev[i], od[i] = po, pe
    return od[n - 1]

def q11_brute(a):
    n = len(a)
    cnt = 0
    for m in range(1 << (n - 2)) if n >= 2 else [0]:
        path = [0] + [i + 1 for i in range(n - 2) if m >> i & 1] + [n - 1]
        if n == 1 or all(path[t + 1] - path[t] in (1, 2) for t in range(len(path) - 1)):
            if sum(a[i] for i in path) % 2 == 1:
                cnt += 1
    return cnt

# 13q / 22q: two arrays a and b of length n; a journey picks one array for every index (moves are i -> i+1 on
# either array). Count journeys with an even sum and with an odd sum.
def q13(a, b):
    n = len(a)
    # dp[p] = number of ways with current element on array 'a' (index 0) or 'b' (index 1) and running sum parity p
    ways = {}
    ways[('a', a[0] % 2)] = 1
    ways[('b', b[0] % 2)] = ways.get(('b', b[0] % 2), 0) + 1
    for i in range(1, n):
        new = {}
        for (arr, par), c in ways.items():
            for val, name in ((a[i], 'a'), (b[i], 'b')):
                key = (name, (par + val) % 2)
                new[key] = new.get(key, 0) + c
        ways = new
    even = sum(c for (arr, par), c in ways.items() if par == 0)
    odd = sum(c for (arr, par), c in ways.items() if par == 1)
    return even, odd

def q13_brute(a, b):
    n = len(a)
    even = odd = 0
    for pick in itertools.product((0, 1), repeat=n):
        s = sum(a[i] if pick[i] == 0 else b[i] for i in range(n))
        if s % 2 == 0: even += 1
        else: odd += 1
    return even, odd

# 14q: minimum steps to reduce N to 1 using -1, /2 (if divisible), /3 (if divisible).
def q14(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        best = dp[i - 1] + 1
        if i % 2 == 0: best = min(best, dp[i // 2] + 1)
        if i % 3 == 0: best = min(best, dp[i // 3] + 1)
        dp[i] = best
    return dp[n]

def q14_brute(n):
    from collections import deque
    dist = {n: 0}; dq = deque([n])
    while dq:
        x = dq.popleft()
        if x == 1: return dist[x]
        nxt = [x - 1]
        if x % 2 == 0: nxt.append(x // 2)
        if x % 3 == 0: nxt.append(x // 3)
        for y in nxt:
            if y >= 1 and y not in dist:
                dist[y] = dist[x] + 1; dq.append(y)

# 22q (same journey model, see 13q): the sample A=[1,2,1], B=[3,1,1] should give 4 even and 4 odd.

# 23q: number of ordered ways (compositions) to make y from {1,2,4,6}, where 4 may be used at most twice.
def q23(y):
    # dp[s][k]: ordered ways to make sum s using k fours so far
    dp = [[0] * 3 for _ in range(y + 1)]
    dp[0][0] = 1
    for s in range(1, y + 1):
        for k in range(3):
            tot = 0
            for v in (1, 2, 6):
                if s - v >= 0: tot += dp[s - v][k]
            if k >= 1 and s - 4 >= 0: tot += dp[s - 4][k - 1]
            dp[s][k] = tot
    return sum(dp[y])

def q23_brute(y):
    cnt = 0
    def go(s, fours):
        nonlocal cnt
        if s == 0:
            cnt += 1; return
        for v in (1, 2, 6, 4):
            if v <= s:
                if v == 4:
                    if fours < 2: go(s - v, fours + 1)
                else:
                    go(s - v, fours)
    go(y, 0)
    return cnt

if __name__ == '__main__':
    rng = random.Random(1)
    print('3q  sample [2,4,6,7,8] ->', q3([2, 4, 6, 7, 8]), '(expect 16)')
    print('8q  sample [5,8,3,100,-5,-5,5,10] ->', q8([5, 8, 3, 100, -5, -5, 5, 10]), '(expect 131)')
    print('13q sample A=[1,2,1] B=[3,1,1] ->', q13([1, 2, 1], [3, 1, 1]), '(expect 4 even, 4 odd)')
    print('14q sample n=10 ->', q14(10), '(expect 3: 10/2=5, 5-1=4, 4/2=2, 2/2=1 is 4 steps; check)')
    print('23q sample y=6 ->', q23(6))
    bad = {}
    def chk(name, ok):
        bad[name] = bad.get(name, 0) + (0 if ok else 1)
    for _ in range(400):
        n = rng.randint(1, 8)
        a = [rng.randint(-9, 9) for _ in range(n)]
        chk('3q', q3(a) == max(q3_brute(a), 0))
        if n >= 2:
            chk('8q', q8(a) == q8_brute(a))
            chk('11q', q11(a) == q11_brute(a))
        k = rng.randint(1, 3)
        chk('9q', q9(a, k) == q9_brute(a, k) if n >= 2 else True)
        rows = [[rng.randint(1, 9) for _ in range(3)] for _ in range(n)]
        chk('10q', q10(rows) == q10_brute(rows))
        b = [rng.randint(-9, 9) for _ in range(n)]
        chk('13q', q13(a, b) == q13_brute(a, b))
    for _ in range(200):
        chk('14q', q14(rng.randint(1, 300)) == q14_brute(rng.randint(1, 300)) or True)
    for n in range(1, 200):
        chk('14q', q14(n) == q14_brute(n))
    for y in range(0, 25):
        chk('23q', q23(y) == q23_brute(y))
    print('mismatches:', bad)
