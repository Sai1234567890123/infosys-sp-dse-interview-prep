import itertools, random, heapq
from collections import Counter

# 26q: delete occurrences so that all remaining value-frequencies lie within a window of width K.
# Optimal: pick a lower bound L (a frequency value). Frequencies below L are removed entirely (cost f),
# frequencies above L+K are cut down to L+K (cost f-(L+K)). Answer = min over L (and "remove all").
def freq_within_k(a, K):
    f = list(Counter(a).values())
    n = len(a)
    best = n
    for L in set(f):
        cost = sum(x for x in f if x < L) + sum(x - (L + K) for x in f if x > L + K)
        best = min(best, cost)
    return best

def freq_brute(a, K):
    n = len(a); best = n
    vals = list(Counter(a).keys())
    for r in range(n + 1):
        for dele in itertools.combinations(range(n), r):
            rem = [a[i] for i in range(n) if i not in dele]
            f = list(Counter(rem).values())
            if not f or max(f) - min(f) <= K:
                best = min(best, r)
    return best

# 27q: choose P elements from L to minimize max-min.
def find_min_difference(L, P):
    s = sorted(L)
    return min(s[i + P - 1] - s[i] for i in range(len(s) - P + 1))

def fmd_brute(L, P):
    return min(max(c) - min(c) for c in itertools.combinations(L, P))

# 28q: rearrange msg letters to minimize sum of |value differences| of adjacent letters = sorted values.
def min_sum_security(values, msg):
    v = sorted(values[ord(c) - ord('a')] for c in msg)
    return sum(v[i] - v[i - 1] for i in range(1, len(v)))

def security_brute(values, msg):
    best = None
    for p in set(itertools.permutations(msg)):
        s = sum(abs(values[ord(p[i]) - 97] - values[ord(p[i - 1]) - 97]) for i in range(1, len(p)))
        best = s if best is None or s < best else best
    return best

# 30q (k max priority): top-K subset sums of B. Max = sum of positives; then subsets of |values| by smallest sum.
def top_k_subset_sums(B, K):
    mx = sum(x for x in B if x > 0)
    a = sorted(abs(x) for x in B)
    out = [mx]
    heap = [(a[0], 0)] if a else []   # (sum of absolute subset, last index)
    while heap and len(out) < K:
        s, i = heapq.heappop(heap)
        out.append(mx - s)
        if i + 1 < len(a):
            heapq.heappush(heap, (s + a[i + 1], i + 1))
            heapq.heappush(heap, (s - a[i] + a[i + 1], i + 1))
    return out[:K]

def top_k_brute(B, K):
    sums = []
    n = len(B)
    for m in range(1 << n):
        sums.append(sum(B[i] for i in range(n) if m >> i & 1))
    return sorted(sums, reverse=True)[:K]

# 30q-b (min memory): remove m contiguous processes; return minimum memory remaining.
def min_memory(v, m):
    s = sum(v); w = sum(v[:m]); best = w
    for i in range(m, len(v)):
        w += v[i] - v[i - m]; best = max(best, w)
    return s - best

def min_memory_brute(v, m):
    return min(sum(v) - sum(v[i:i + m]) for i in range(len(v) - m + 1))

# 31q: code as pasted (distinct elements, each x can become x-k, x or x+k). Statement not in paste; verified only against itself.
def distinct_elements(A, k):
    A = sorted(A); used = set(); ans = 0
    for x in A:
        for y in (x - k, x, x + k):
            if y not in used:
                used.add(y); ans += 1; break
    return ans

# 32q: LC 2522 partition string into substrings with value <= k; minimal count; -1 if impossible.
def min_partition(s, k):
    cnt = 0; temp = ''
    for ch in s:
        if int(ch) > k: return -1
        if temp and int(temp + ch) <= k:
            temp += ch
        else:
            cnt += 1; temp = ch
    return cnt

def partition_brute(s, k):
    n = len(s); best = None
    for m in range(1 << (n - 1)):
        parts = []; cur = s[0]
        for i in range(1, n):
            if m >> (i - 1) & 1: parts.append(cur); cur = s[i]
            else: cur += s[i]
        parts.append(cur)
        if all(int(p) <= k for p in parts):
            best = len(parts) if best is None else min(best, len(parts))
    return -1 if best is None else best

random.seed(21)
bad = Counter()
for _ in range(1500):
    n = random.randint(1, 7); a = [random.randint(1, 3) for _ in range(n)]; K = random.randint(0, 3)
    if freq_within_k(a, K) != freq_brute(a, K): bad['26q'] += 1
    m = random.randint(1, n); L = [random.randint(1, 20) for _ in range(n)]
    if n >= m and find_min_difference(L, m) != fmd_brute(L, m): bad['27q'] += 1
    vals = [random.randint(1, 9) for _ in range(26)]; msg = ''.join(random.choice('abcdef') for _ in range(random.randint(1, 6)))
    if min_sum_security(vals, msg) != security_brute(vals, msg): bad['28q'] += 1
    B = [random.randint(-9, 9) for _ in range(random.randint(1, 6))]; K2 = random.randint(1, 8)
    if top_k_subset_sums(B, K2) != top_k_brute(B, K2)[:K2] and len(top_k_brute(B, K2)) >= K2: bad['30q'] += 1
    v = [random.randint(1, 20) for _ in range(random.randint(2, 7))]; m3 = random.randint(1, len(v))
    if min_memory(v, m3) != min_memory_brute(v, m3): bad['30qb'] += 1
    s = ''.join(random.choice('123456789') for _ in range(random.randint(1, 6))); kk = random.randint(1, 99)
    if min_partition(s, kk) != partition_brute(s, kk): bad['32q'] += 1
print("mismatches:", dict(bad) or 'none')
print("26q sample [5,8,8,10,10,10,10,10] K=3 ->", freq_within_k([5,8,8,10,10,10,10,10],3), "(expect 1)")
print("27q sample [3,4,1,9,56,7,9,12,13] P=5 ->", find_min_difference([3,4,1,9,56,7,9,12,13],5), "(expect 6)")
print("28q sample afeb ->", min_sum_security([1,2,1,3,1,3,5,7,1,1,5,5,8,10,11,1,23,2,3,7,8,9,1,6,5,9],'afeb'), "(expect 2 via eabf/fbae; afeb gives 5 by hand)")
print("30q sample [10,4,8,13,20]->min memory m=2 ->", min_memory([10,4,8,13,20],2), "(expect 22)")
print("32q sample 165462 k=60 ->", min_partition('165462',60), "(expect 4); 238182 k=5 ->", min_partition('238182',5), "(expect -1)")
print("33q=19q sample reward check skipped (duplicate of LC 2611)")
