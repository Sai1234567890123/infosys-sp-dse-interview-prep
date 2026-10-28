"""Count palindromic subsequences (35q), non-empty, duplicates counted separately.

dp[i][j] = number of non-empty palindromic subsequences inside s[i..j].
    if s[i] == s[j]: dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
    else:            dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
(the +1 counts s[i] + s[j] itself; the overlap s[i+1..j-1] is removed when the ends differ)
O(n^2) time and memory.
"""
import itertools
import random
import sys


def count_palindromic_subsequences(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
    return dp[0][n - 1]


def brute(s):
    n = len(s)
    total = 0
    for mask in range(1, 1 << n):
        sub = ''.join(s[k] for k in range(n) if mask >> k & 1)
        if sub == sub[::-1]:
            total += 1
    return total


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        assert count_palindromic_subsequences('abcd') == 4
        assert count_palindromic_subsequences('aab') == 4
        assert count_palindromic_subsequences('geeksforgeeks') == 81
        rng = random.Random(35)
        for _ in range(3000):
            n = rng.randint(1, 10)
            s = ''.join(rng.choice('abc') for _ in range(n))
            assert count_palindromic_subsequences(s) == brute(s), s
        print('samples ok, 3000 random cases match brute force')
    else:
        print(count_palindromic_subsequences(sys.stdin.readline().strip()))
