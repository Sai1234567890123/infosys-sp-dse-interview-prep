"""Count ordered chains of non-overlapping palindromic substrings (36q).

A pair  is [l1..r1], [l2..r2] with r1 < l2 <= r2, both palindromes.
A triple is [l1..r1], [l2..r2], [l3..r3] with r1 < l2 <= r2 < l3 <= r3.

pal[l][r] = True when s[l..r] is a palindrome (dp[i][j] = s[i]==s[j] and dp[i+1][j-1]).
A[j]  = number of palindromes that start at index >= j        (chains of length 1)
W[l]  = sum over palindromes [l..r] of A[r+1]                 (a palindrome starting at l, then one more)
g2[j] = number of pairs whose first palindrome starts at >= j = suffix sum of W
V[l]  = sum over palindromes [l..r] of g2[r+1]
g3[j] = number of triples whose first palindrome starts at >= j = suffix sum of V

Answer for pairs is g2[0], answer for triples is g3[0]. O(n^2) time and memory.
"""
import itertools
import random
import sys


def palindrome_table(s):
    n = len(s)
    pal = [[False] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length <= 2 or pal[i + 1][j - 1]):
                pal[i][j] = True
    return pal


def chain_counts(s):
    n = len(s)
    pal = palindrome_table(s)
    A = [0] * (n + 1)
    for j in range(n - 1, -1, -1):
        starts = sum(1 for r in range(j, n) if pal[j][r])
        A[j] = A[j + 1] + starts
    W = [0] * (n + 1)
    for l in range(n):
        W[l] = sum(A[r + 1] for r in range(l, n) if pal[l][r])
    g2 = [0] * (n + 2)
    for j in range(n - 1, -1, -1):
        g2[j] = g2[j + 1] + W[j]
    V = [0] * (n + 1)
    for l in range(n):
        V[l] = sum(g2[r + 1] for r in range(l, n) if pal[l][r])
    g3 = [0] * (n + 2)
    for j in range(n - 1, -1, -1):
        g3[j] = g3[j + 1] + V[j]
    return g2[0], g3[0]


def brute(s):
    n = len(s)
    spans = [(l, r) for l in range(n) for r in range(l, n)
             if s[l:r + 1] == s[l:r + 1][::-1]]
    pairs = triples = 0
    for a, b in itertools.product(spans, repeat=2):
        if a[1] < b[0]:
            pairs += 1
    for a, b, c in itertools.product(spans, repeat=3):
        if a[1] < b[0] and b[1] < c[0]:
            triples += 1
    return pairs, triples


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        assert chain_counts('bbaa') == (11, 6)  # statement says 10 pairs; brute force gives 11
        assert chain_counts('aaa')[0] == 5  # GfG non-overlapping palindrome pairs examples
        assert chain_counts('abacaba')[0] == 36
        rng = random.Random(36)
        for _ in range(500):
            n = rng.randint(1, 8)
            s = ''.join(rng.choice('ab') for _ in range(n))
            assert chain_counts(s) == brute(s), s
        print('bbaa: 11 pairs, 6 triples (statement example says 10); 500 random cases match brute force (pairs and triples)')
    else:
        pairs, triples = chain_counts(sys.stdin.readline().strip())
        print(pairs)
        print(triples)
