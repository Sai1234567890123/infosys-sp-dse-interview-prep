"""51q (Google OA, prime string): count the ways to split a digit string into parts whose
numeric values are prime. Parts have at most 6 digits (the largest value in the paste's
window is below 10^6), so every part is checked with a sieve.

dp[i] = sum over k in 1..6 of dp[i-k] when the last k digits form a prime number.
Time O(N * 6) after an O(M log log M) sieve, with M = 10^6. Memory O(N + M).
Assumption: a part may not start with '0' (no leading zeros). Without this rule a part such
as '0000003' would be longer than six digits and the six-digit window would miss it.
"""
import random
import sys


def sieve(limit):
    is_p = bytearray([1]) * (limit + 1)
    is_p[0:2] = b'\x00\x00'
    for p in range(2, int(limit ** 0.5) + 1):
        if is_p[p]:
            is_p[p * p::p] = bytearray(len(is_p[p * p::p]))
    return is_p


PRIME = sieve(10 ** 6)


def count_prime_partitions(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        total = 0
        for k in range(1, min(6, i) + 1):
            v = int(s[i - k:i])
            if s[i - k] != '0' and v <= 10 ** 6 - 1 and PRIME[v] and dp[i - k]:
                total += dp[i - k]
        dp[i] = total
    return dp[n]


def brute(s):
    n = len(s)
    if n == 0:
        return 1
    total = 0
    for mask in range(1 << (n - 1)):
        cuts = [0] + [i + 1 for i in range(n - 1) if mask >> i & 1] + [n]
        ok = True
        for a, b in zip(cuts, cuts[1:]):
            v = int(s[a:b])
            if s[a] == '0' or not (v < 10 ** 6 and PRIME[v]):
                ok = False
                break
        total += ok
    return total


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        rng = random.Random(51)
        for _ in range(2000):
            n = rng.randint(1, 9)
            s = ''.join(rng.choice('0123456789') for _ in range(n))
            assert count_prime_partitions(s) == brute(s), s
        print('ok: 2000 random digit strings match brute force')
    else:
        print(count_prime_partitions(sys.stdin.readline().strip()))
