import random

def advance(a, b):
    """Count wizards with no other wizard strictly greater in both skills. O(N log N)."""
    n = len(a)
    order = sorted(range(n), key=lambda i: a[i])
    ans = 0
    best = -1                      # max b among wizards with strictly greater a (seen so far from the right)
    j = n - 1
    while j >= 0:
        k = j
        while k - 1 >= 0 and a[order[k - 1]] == a[order[j]]:
            k -= 1
        group = order[k:j + 1]     # all wizards with the same primary skill
        for i in group:
            if not (best > b[i]):  # nobody with strictly greater a has strictly greater b
                ans += 1
        for i in group:
            best = max(best, b[i])
        j = k - 1
    return ans

def brute(a, b):
    n = len(a); c = 0
    for i in range(n):
        if not any(a[j] > a[i] and b[j] > b[i] for j in range(n)): c += 1
    return c

random.seed(11)
bad = 0
for _ in range(5000):
    n = random.randint(1, 8)
    a = [random.randint(1, 4) for _ in range(n)]
    b = [random.randint(1, 4) for _ in range(n)]
    if advance(a, b) != brute(a, b): bad += 1
print("mismatches:", bad)
print("sample 1: a=[1,2] b=[2,3] ->", advance([1, 2], [2, 3]), "(expect 1)")
print("sample 2: a=[1,2,3] b=[3,2,1] ->", advance([1, 2, 3], [3, 2, 1]), "(expect 3)")
