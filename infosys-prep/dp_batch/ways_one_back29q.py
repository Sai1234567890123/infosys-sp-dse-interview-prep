"""29q: array A (1-indexed, values 1 or 2). Start at index 1, end at index N. From i you move forward by 1..A[i],
and you may move back by 1 at most once in the whole walk. Each index is visited at most once.
Count the walks from 1 that end at N (N is the last index visited).

d0[i]: walks reaching i with no backward step. d1[i]: walks reaching i with the backward step used.
"""
import itertools, random


def count_ways(A):
    n = len(A)
    b = lambda i: A[i - 1]
    if n == 1:
        return 1
    d0 = [0] * (n + 1)
    d1 = [0] * (n + 1)
    d0[1] = 1
    d0[2] = 1
    for i in range(3, n + 1):
        d0[i] = d0[i - 1] + (d0[i - 2] if b(i - 2) == 2 else 0)
        d1[i] = (d1[i - 1] + (d1[i - 2] if b(i - 2) == 2 else 0)
                 + (d0[i - 3] if b(i - 3) == 2 and b(i - 2) == 2 else 0))
    return d0[n] + d1[n]


def brute(A):
    n = len(A)
    count = [0]

    def dfs(pos, visited, back_used):
        if pos == n:
            count[0] += 1
            return
        for d in range(1, A[pos - 1] + 1):
            nxt = pos + d
            if nxt <= n and nxt not in visited:
                dfs(nxt, visited | {nxt}, back_used)
        if not back_used and pos - 1 >= 1 and pos - 1 not in visited:
            dfs(pos - 1, visited | {pos - 1}, True)

    dfs(1, frozenset({1}), False)
    return count[0]


if __name__ == '__main__':
    rng = random.Random(3)
    bad = 0
    for _ in range(2000):
        n = rng.randint(1, 8)
        A = [rng.choice((1, 2)) for _ in range(n)]
        bad += count_ways(A) != brute(A)
    print('mismatches over 2000 random cases:', bad)
    print('A=[1,2,1,1,2] ->', count_ways([1, 2, 1, 1, 2]), 'brute', brute([1, 2, 1, 1, 2]))
