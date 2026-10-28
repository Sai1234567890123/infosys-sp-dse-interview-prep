"""27q (Google girl hackathon OA 2024): split the array into exactly k contiguous parts to maximise the sum of part values.
A part's value is a1 - a2 + a3 - a4 ... (signs alternate starting with + at the part's first element)."""
import itertools, random

NEG = float('-inf')

def max_sum_k_parts(nums, k):
    n = len(nums)
    if k < 1 or k > n: return None
    # f[(j, s)] = best total after the prefix, with j parts opened, s = sign of the last element (+1 / -1)
    f = {(1, 1): nums[0]}
    for x in nums[1:]:
        g = {}
        for (j, s), v in f.items():
            # continue current part: next sign is -s
            cand = v + (-s) * x
            if cand > g.get((j, -s), NEG): g[(j, -s)] = cand
            # start a new part: sign +
            if j + 1 <= k:
                cand = v + x
                if cand > g.get((j + 1, 1), NEG): g[(j + 1, 1)] = cand
        f = g
    return max((v for (j, s), v in f.items() if j == k), default=None)

def brute(nums, k):
    n = len(nums); best = None
    for cuts in itertools.combinations(range(1, n), k - 1):
        bounds = [0, *cuts, n]
        total = 0
        for lo, hi in zip(bounds, bounds[1:]):
            total += sum(nums[t] * (1 if (t - lo) % 2 == 0 else -1) for t in range(lo, hi))
        best = total if best is None else max(best, total)
    return best

if __name__ == '__main__':
    print('paste example [1,-2,3], k=2 ->', max_sum_k_parts([1, -2, 3], 2), 'brute', brute([1, -2, 3], 2))
    rng = random.Random(21); bad = 0
    for _ in range(3000):
        n = rng.randint(1, 8); k = rng.randint(1, n)
        nums = [rng.randint(-10, 10) for _ in range(n)]
        bad += max_sum_k_parts(nums, k) != brute(nums, k)
    print('mismatches over 3000 random cases:', bad)
