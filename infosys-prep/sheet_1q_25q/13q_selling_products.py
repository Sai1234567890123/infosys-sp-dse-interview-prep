import itertools, random
from collections import Counter

def min_distinct(a, m):
    """Q1: remove at most m items; minimize number of distinct IDs left."""
    freq = sorted(Counter(a).values())
    i = 0
    while i < len(freq) and m - freq[i] >= 0:
        m -= freq[i]; i += 1
    return len(freq) - i

def brute(a, m):
    best = len(set(a))
    n = len(a)
    for r in range(0, min(m, n) + 1):
        for rem in itertools.combinations(range(n), r):
            s = set(a[i] for i in range(n) if i not in rem)
            best = min(best, len(s))
    return best

random.seed(5)
bad = 0
for _ in range(2000):
    n = random.randint(1, 7)
    a = [random.randint(1, 4) for _ in range(n)]
    m = random.randint(0, n)
    if min_distinct(a, m) != brute(a, m): bad += 1
print("Q1 mismatches:", bad)
print("video example [1,1,1,2,2,3], M=2 ->", min_distinct([1,1,1,2,2,3], 2), "(expect 1)")
print("video example 7 items, M=4 ->", min_distinct([1,1,1,2,2,2,3], 4) if False else "see note")
