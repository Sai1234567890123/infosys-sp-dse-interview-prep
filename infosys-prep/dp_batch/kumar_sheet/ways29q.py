"""29q: array A (1-indexed, values 1 or 2), start at index 1, end at index N.
From index i you can move forward by 1..A[i]; you may also move back by 1 at most once in the whole walk.
Each index visited at most once. Count the walks from 1 that end at N (N is the last index visited)."""
import random

def brute(A):
    n = len(A); count = [0]
    def dfs(pos, visited, back_used):
        if pos == n:
            count[0] += 1; return
        a = A[pos - 1]
        for d in range(1, a + 1):                     # forward moves
            nxt = pos + d
            if nxt <= n and nxt not in visited:
                dfs(nxt, visited | {nxt}, back_used)
        if not back_used and pos - 1 >= 1 and pos - 1 not in visited:   # one backward step of size 1
            dfs(pos - 1, visited | {pos - 1}, True)
    dfs(1, frozenset({1}), False)
    return count[0]

def dp29(A):
    n = len(A)
    b = lambda i: A[i - 1]
    if n == 1: return 1
    d0 = [0] * (n + 1); d1 = [0] * (n + 1)
    # forward-only walks: d0[i] = ways to reach i with no backward step
    d0[1] = 1
    for i in range(2, n + 1):
        d0[i] = d0[i - 1] + (d0[i - 2] if i - 2 >= 1 and b(i - 2) == 2 else 0)
    return None

if __name__ == '__main__':
    rng = random.Random(29); bad = 0
    for _ in range(300):
        n = rng.randint(1, 7)
        A = [rng.choice((1, 2)) for _ in range(n)]
        print_case = None
    print('brute ok; example A=[1,2,1,1,2]:', brute([1, 2, 1, 1, 2]), ' A=[2,2,2]:', brute([2, 2, 2]))
