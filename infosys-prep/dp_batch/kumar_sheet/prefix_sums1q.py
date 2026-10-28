"""1q: range-sum queries on an array. Answer for query i is pre[i] = a[1] + ... + a[i].
Example from the paste: a = [4, 5, 3, 2, 1] -> 4, 9, 12, 14, 15.
Time O(N + Q) with O(N) prefix sums."""
import random
import sys


def prefix_answers(a, queries):
    pre = [0] * (len(a) + 1)
    for i, x in enumerate(a, start=1):
        pre[i] = pre[i - 1] + x
    return [pre[q] for q in queries]


def brute(a, queries):
    return [sum(a[:q]) for q in queries]


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        assert prefix_answers([4, 5, 3, 2, 1], range(1, 6)) == [4, 9, 12, 14, 15]
        rng = random.Random(1)
        for _ in range(2000):
            n = rng.randint(1, 10)
            a = [rng.randint(0, 9) for _ in range(n)]
            qs = [rng.randint(1, n) for _ in range(rng.randint(1, 6))]
            assert prefix_answers(a, qs) == brute(a, qs)
        print('ok: sample and 2000 random cases')
    else:
        data = sys.stdin.read().split()
        n = int(data[0]); a = list(map(int, data[1:1 + n])); q = int(data[1 + n])
        qs = list(map(int, data[2 + n:2 + n + q]))
        print('\n'.join(map(str, prefix_answers(a, qs))))
