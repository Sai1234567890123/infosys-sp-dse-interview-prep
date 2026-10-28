"""LeetCode 647 Palindromic Substrings (33q).

Count the palindromic substrings of s.
dp[i][j] = True when s[i..j] is a palindrome:
    dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i+1][j-1])
Each True cell is one palindromic substring. Runs in O(n^2) time and memory.
"""
import random
import sys


def count_palindromic_substrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                count += 1
    return count


def brute(s):
    n = len(s)
    return sum(
        1
        for i in range(n)
        for j in range(i + 1, n + 1)
        if s[i:j] == s[i:j][::-1]
    )


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        assert count_palindromic_substrings('abc') == 3
        assert count_palindromic_substrings('aaa') == 6
        rng = random.Random(33)
        for _ in range(3000):
            n = rng.randint(1, 12)
            s = ''.join(rng.choice('ab') for _ in range(n))
            assert count_palindromic_substrings(s) == brute(s), s
        print('samples ok, 3000 random cases match brute force')
    else:
        print(count_palindromic_substrings(sys.stdin.readline().strip()))
