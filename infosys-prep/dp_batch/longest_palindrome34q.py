"""GfG Longest Palindromic Substring (34q).

Return the longest palindromic substring of s. If several have the same
length, return the one that appears first (smallest start index).

Expansion from centre: every odd centre (i, i) and even centre (i, i+1)
is expanded outward while the ends match. Ties are resolved by start index.
O(n^2) time, O(1) extra space.
"""
import random
import sys


def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ''
    best_start, best_len = 0, 1
    for centre in range(n):
        for lo, hi in ((centre, centre), (centre, centre + 1)):
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            length = hi - lo - 1
            start = lo + 1
            if length > best_len or (length == best_len and start < best_start):
                best_start, best_len = start, length
    return s[best_start:best_start + best_len]


def brute(s):
    n = len(s)
    best = ''
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
    return best or (s[:1])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        assert longest_palindrome('forgeeksskeegfor') == 'geeksskeeg'
        assert longest_palindrome('Geeks') == 'ee'
        assert longest_palindrome('abc') == 'a'
        rng = random.Random(34)
        for _ in range(3000):
            n = rng.randint(1, 12)
            s = ''.join(rng.choice('abc') for _ in range(n))
            assert longest_palindrome(s) == brute(s), s
        print('samples ok, 3000 random cases match brute force')
    else:
        print(longest_palindrome(sys.stdin.readline().rstrip('\n')))
