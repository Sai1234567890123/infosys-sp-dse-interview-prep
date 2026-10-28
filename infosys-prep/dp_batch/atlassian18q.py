"""18q Atlassian: start with 1, B ops in order, each op may be skipped: +x, -x, *x, /x (x>=1, truncating), N (negate).
Maximize final value. DP keeps best max and min reachable value after each prefix of operations."""
import itertools, random

def trunc_div(a, b):
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b > 0) else -q

def atlassian(ops):
    mx = mn = 1
    for op, x in ops:
        if op == '+': cands = [mx + x, mn + x]
        elif op == '-': cands = [mx - x, mn - x]
        elif op == '*': cands = [mx * x, mn * x]
        elif op == '/': cands = [trunc_div(mx, x), trunc_div(mn, x)]
        else: cands = [-mx, -mn]                      # N: negate, max comes from -min, min from -max
        nmx = max(mx, *cands)
        nmn = min(mn, *cands)
        mx, mn = nmx, nmn
    return mx

def brute(ops):
    best = None
    for mask in range(1 << len(ops)):
        v = 1
        for i, (op, x) in enumerate(ops):
            if mask >> i & 1:
                if op == '+': v += x
                elif op == '-': v -= x
                elif op == '*': v *= x
                elif op == '/': v = trunc_div(v, x)
                else: v = -v
        best = v if best is None else max(best, v)
    return best

if __name__ == '__main__':
    rng = random.Random(3)
    bad = 0
    for _ in range(3000):
        b = rng.randint(1, 8)
        ops = []
        for _ in range(b):
            op = rng.choice('+-*/N')
            x = rng.randint(1, 6)
            ops.append((op, x))
        bad += atlassian(ops) != brute(ops)
    print('mismatches over 3000 random cases:', bad)
