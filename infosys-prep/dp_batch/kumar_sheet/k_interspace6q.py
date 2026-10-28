"""6q: longest k-interspace substring.

Start a new window whenever two adjacent characters differ by more than k (by alphabet position).
Keep the longest window; on a tie the first one wins.
Example from the paste: word = "ababbaca", k = 1 -> "ababba".
Time O(N), memory O(1) beyond the answer."""
import random
import sys


def longest_k_interspace(word, k):
    if not word:
        return ''
    best_l, best_len = 0, 1
    l = 0
    for r in range(1, len(word)):
        if abs(ord(word[r]) - ord(word[r - 1])) > k:
            l = r
        if r - l + 1 > best_len:
            best_l, best_len = l, r - l + 1
    return word[best_l:best_l + best_len]


def brute(word, k):
    best = word[:1]
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            sub = word[i:j]
            if all(abs(ord(sub[t]) - ord(sub[t - 1])) <= k for t in range(1, len(sub))) and len(sub) > len(best):
                best = sub
    return best


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        assert longest_k_interspace('ababbaca', 1) == 'ababba'
        rng = random.Random(6)
        for _ in range(2000):
            n = rng.randint(1, 8)
            w = ''.join(rng.choice('abcde') for _ in range(n))
            k = rng.randint(0, 3)
            assert len(longest_k_interspace(w, k)) == len(brute(w, k)), (w, k)
        print('ok: sample and 2000 random cases (length match)')
    else:
        word = sys.stdin.readline().strip()
        k = int(sys.stdin.readline())
        print(longest_k_interspace(word, k))
