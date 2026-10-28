"""Minimum cost to merge an array into one number (38q).

Each operation merges two adjacent numbers into their sum; the cost is that sum.
dp[i][j] = min cost to merge a[i..j] into one number.
    dp[i][i] = 0
    dp[i][j] = min over k in [i, j-1] of dp[i][k] + dp[k+1][j] + sum(a[i..j])
The sum term is paid once for every merge that creates a block, and the last
merge of a[i..j] always costs sum(a[i..j]). O(n^3) time, O(n^2) memory.
"""
import functools
import random
import sys


def min_merge_cost(a):
    n = len(a)
    if n == 0:
        return 0
    pre = [0] * (n + 1)
    for i, x in enumerate(a):
        pre[i + 1] = pre[i] + x
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total = pre[j + 1] - pre[i]
            dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j)) + total
    return dp[0][n - 1]


def brute(a):
    @functools.lru_cache(maxsize=None)
    def go(t):
        if len(t) == 1:
            return 0
        best = None
        for i in range(len(t) - 1):
            merged = t[:i] + (t[i] + t[i + 1],) + t[i + 2:]
            cand = t[i] + t[i + 1] + go(merged)
            best = cand if best is None or cand < best else best
        return best
    return go(tuple(a))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        assert min_merge_cost([5, 5, 8]) == 28
        assert min_merge_cost([5, 8, 2]) == 25
        assert min_merge_cost([5, 8]) == 13
        assert min_merge_cost([5, 8, 2, 10]) == brute([5, 8, 2, 10])
        rng = random.Random(38)
        for _ in range(1000):
            n = rng.randint(1, 7)
            a = [rng.randint(1, 20) for _ in range(n)]
            assert min_merge_cost(a) == brute(a), a
        print('samples ok, 1000 random cases match brute force')
    else:
        nums = list(map(int, sys.stdin.read().split()))
        print(min_merge_cost(nums[1:]) if nums and len(nums) == nums[0] + 1 else min_merge_cost(nums))
