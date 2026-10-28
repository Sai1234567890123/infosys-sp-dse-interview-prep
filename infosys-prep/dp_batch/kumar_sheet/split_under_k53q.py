"""53q (TechGig semifinal DP): count the ways to split a digit string into parts whose values are
all <= K. Assumption: a part may not start with '0' (the paste does not say).

dp[i] = sum over parts s[j..i-1] of dp[j], where the part is valid (no leading zero, value <= K).
A part with value <= K has at most len(str(K)) digits, so the inner loop is short.
Time O(N * len(K)), memory O(N).
Examples from the paste: "123" (K large) -> 4; "125", K = 24 -> 2 (1|2|5 and 12|5).
"""
import random
import sys


def count_splits(s, K):
    n = len(s)
    maxlen = len(str(K))
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        total = 0
        for k in range(1, min(maxlen, i) + 1):
            j = i - k
            part = s[j:i]
            if part[0] == '0' or int(part) > K:
                continue
            total += dp[j]
        dp[i] = total
    return dp[n]


def brute(s, K):
    n = len(s)
    total = 0
    for mask in range(1 << (n - 1)):
        cuts = [0] + [i + 1 for i in range(n - 1) if mask >> i & 1] + [n]
        ok = True
        for a, b in zip(cuts, cuts[1:]):
            if s[a] == '0' or int(s[a:b]) > K:
                ok = False
                break
        total += ok
    return total


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        assert count_splits('123', 1000) == 4
        assert count_splits('125', 24) == 2
        rng = random.Random(53)
        for _ in range(2000):
            n = rng.randint(1, 9)
            s = ''.join(rng.choice('0123456789') for _ in range(n))
            K = rng.randint(1, 500)
            assert count_splits(s, K) == brute(s, K), (s, K)
        print('ok: examples and 2000 random cases match brute force')
    else:
        data = sys.stdin.read().split()
        print(count_splits(data[0], int(data[1])))
