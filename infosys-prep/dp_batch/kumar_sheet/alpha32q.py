"""32q: strings of length N over {a,b,c,d}. Forbidden adjacent pairs: ab, ba, bc, cb, cd, dc. The number of 'a' must be odd.
Count the valid strings modulo 1e9+7. State = (last character, parity of the count of 'a')."""
import itertools

MOD = 10**9 + 7
CH = 'abcd'
FORBID = {('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'b'), ('c', 'd'), ('d', 'c')}

def count(n):
    if n == 0: return 0
    dp = {(c, 1 if c == 'a' else 0): 1 for c in CH}          # single characters
    for _ in range(n - 1):
        nd = {}
        for (last, par), v in dp.items():
            for c in CH:
                if (last, c) in FORBID: continue
                key = (c, (par + (1 if c == 'a' else 0)) % 2)
                nd[key] = (nd.get(key, 0) + v) % MOD
        dp = nd
    return sum(v for (c, par), v in dp.items() if par == 1) % MOD

def brute(n):
    total = 0
    for s in itertools.product(CH, repeat=n):
        if any((s[i], s[i + 1]) in FORBID for i in range(n - 1)): continue
        if s.count('a') % 2 == 1: total += 1
    return total % MOD

if __name__ == '__main__':
    print('examples N=1..4:', [count(n) for n in range(1, 5)], 'expect [1, 4, 11, 29]')
    print('brute N=1..6:', [brute(n) for n in range(1, 7)], 'dp:', [count(n) for n in range(1, 7)])
    print('N=1e5 mod result:', count(100000))
