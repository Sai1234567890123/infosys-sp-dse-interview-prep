import itertools, random, string

# 20q-1 Longest Work Slot: nurses 0..25 (ids 'a'..'z'); shifts [employee, leaveTime] sorted by leaveTime.
# Each shift starts when the previous one ends (time 0 at start). Return id of the nurse with the longest single shift.
def longest_work_slot(shifts):
    prev = 0; best = -1; who = None
    for emp, end in shifts:
        dur = end - prev
        if dur > best:
            best, who = dur, emp
        prev = end
    return chr(ord('a') + who)

def longest_brute(shifts):
    prev = 0; best = -1; who = None
    for emp, end in shifts:
        d = end - prev
        if d > best: best, who = d, emp
        prev = end
    return chr(ord('a') + who)

# 20q-2 Closest Numbers: distinct integers; print all pairs with minimum absolute difference, ascending.
def closest_numbers(nums):
    a = sorted(nums)
    diffs = [a[i+1] - a[i] for i in range(len(a) - 1)]
    m = min(diffs)
    return [(a[i], a[i+1]) for i in range(len(diffs)) if diffs[i] == m]

def closest_brute(nums):
    best = min(abs(x - y) for x, y in itertools.combinations(nums, 2))
    pairs = sorted((min(x, y), max(x, y)) for x, y in itertools.combinations(nums, 2) if abs(x - y) == best)
    return pairs

# 20q-3 Sum of Arrays: rearrange arr1 and arr2 to maximize sum i*(arr2[i]-arr1[i]), i = 1..n; answer mod 1e9+7.
MOD = 10**9 + 7
def max_sum_of_array(arr1, arr2):
    a = sorted(arr1, reverse=True)   # minimize sum i*arr1[i]: big values at small indices
    b = sorted(arr2)                  # maximize sum i*arr2[i]: big values at big indices
    s = sum((i + 1) * (b[i] - a[i]) for i in range(len(a)))
    return s % MOD                    # Python gives a non-negative residue

def sum_brute(arr1, arr2):
    best = None
    for p in itertools.permutations(arr1):
        for q in itertools.permutations(arr2):
            s = sum((i + 1) * (q[i] - p[i]) for i in range(len(p)))
            best = s if best is None or s > best else best
    return best % MOD

random.seed(9)
bad = [0, 0, 0]
for _ in range(1500):
    n = random.randint(1, 6)
    emps = [random.randint(0, 25) for _ in range(n)]
    ends = sorted(random.sample(range(1, 60), n))
    shifts = list(zip(emps, ends))
    if longest_work_slot(shifts) != longest_brute(shifts): bad[0] += 1
    m = random.randint(2, 7)
    nums = random.sample(range(-30, 30), m)
    if closest_numbers(nums) != closest_brute(nums): bad[1] += 1
    k = random.randint(1, 5)
    x1 = [random.randint(1, 9) for _ in range(k)]
    x2 = [random.randint(1, 9) for _ in range(k)]
    if max_sum_of_array(x1, x2) != sum_brute(x1, x2): bad[2] += 1
print("mismatches (longest slot, closest, sum of arrays):", bad)
print("slot sample [[0,3],[2,5],[0,9],[1,15]] ->", longest_work_slot([(0,3),(2,5),(0,9),(1,15)]), "(expect b)")
print("slot sample [[0,2],[1,3],[0,7]] ->", longest_work_slot([(0,2),(1,3),(0,7)]), "(expect a)")
print("slot sample [[0,1],[0,3],[4,5],[5,6],[4,10]] ->", longest_work_slot([(0,1),(0,3),(4,5),(5,6),(4,10)]), "(expect e)")
print("closest [6,2,4,10] ->", closest_numbers([6,2,4,10]), "(expect (2,4),(4,6))")
print("closest [4,2,1,3] ->", closest_numbers([4,2,1,3]), "(expect (1,2),(2,3),(3,4))")
print("sum sample arr1=[1,2,3], arr2=[10,10,10] ->", max_sum_of_array([1,2,3],[10,10,10]), "(expect 50)")
print("sum sample arr1=[3,1,2,6], arr2=[2,8,4,9] ->", max_sum_of_array([3,1,2,6],[2,8,4,9]), "(expect 48)")
print("sum example arr1=[2,1,3,4], arr2=[2,3,2,3] ->", max_sum_of_array([2,1,3,4],[2,3,2,3]), "(expect 7)")
