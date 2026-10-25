import itertools, random

def min_reachable(n, c, a):
    """a is 0-indexed list of importance values; island 1 is a[0]. Returns min islands Jordan can visit."""
    total = sum(a)
    rest = sorted(a[1:])                      # islands 2..N
    m = len(rest)
    pre = [0]
    for x in rest: pre.append(pre[-1] + x)
    best = n                                  # no cuts: all n islands
    for k in range(1, m + 1):                 # cut off k islands (never island 1)
        lo = pre[k]                           # k smallest
        hi = pre[m] - pre[m - k]              # k largest
        cost = min(lo * (total - lo), hi * (total - hi))
        if cost <= c:
            best = min(best, n - k)
    return best

def brute(n, c, a):
    total = sum(a)
    best = n
    idx = list(range(1, n))
    for k in range(1, n):
        for S in itertools.combinations(idx, k):
            Y = sum(a[i] for i in S)
            if Y * (total - Y) <= c:
                best = min(best, n - k)
    return best

random.seed(1)
bad = 0
for _ in range(3000):
    n = random.randint(1, 7)
    a = [random.randint(1, 9) for _ in range(n)]
    c = random.randint(0, 400)
    if min_reachable(n, c, a) != brute(n, c, a):
        bad += 1
        if bad < 4: print("mismatch", n, c, a, min_reachable(n,c,a), brute(n,c,a))
print("mismatches:", bad)
# video example: values 2,3,4,5 (node 1 = 2)
for C in (0, 50, 160, 105, 1000):
    print("C =", C, "->", min_reachable(4, C, [2, 3, 4, 5]), "brute", brute(4, C, [2, 3, 4, 5]))
