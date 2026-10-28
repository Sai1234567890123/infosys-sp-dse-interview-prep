"""28q: N days, one task per day: easy E[i], medium M[i] or hard H[i] (points).
Rules (from day 3 on, 1-based):
  hard on day i only if day i-2 was easy;
  medium on day i only if day i-1 was easy and day i-2 was medium.
Maximise total points. State = (task of day i-1, task of day i-2)."""
import itertools, random

E, M, H = 'E', 'M', 'H'

def allowed(i, t, prev1, prev2):          # i is 1-based; prev1 = task on day i-1, prev2 = day i-2 (None if absent)
    if i <= 2: return True
    if t == H: return prev2 == E
    if t == M: return prev1 == E and prev2 == M
    return True

def max_points(E_, M_, H_):
    n = len(E_)
    val = {E: E_, M: M_, H: H_}
    f = {}                                # (t1, t2) -> best total; t1 = last task, t2 = the one before
    for t in (E, M, H):
        f[(t, None)] = val[t][0]
    for i in range(2, n + 1):
        g = {}
        for (t1, t2), v in f.items():
            for t in (E, M, H):
                if not allowed(i, t, t1, t2): continue
                nv = v + val[t][i - 1]
                key = (t, t1)
                if nv > g.get(key, float('-inf')): g[key] = nv
        f = g
    return max(f.values())

def brute(E_, M_, H_):
    n = len(E_); val = {E: E_, M: M_, H: H_}; best = None
    for seq in itertools.product((E, M, H), repeat=n):
        ok = True
        for i in range(1, n + 1):
            t = seq[i - 1]
            p1 = seq[i - 2] if i >= 2 else None
            p2 = seq[i - 3] if i >= 3 else None
            if not allowed(i, t, p1, p2): ok = False; break
        if not ok: continue
        s = sum(val[t][i] for i, t in enumerate(seq))
        best = s if best is None else max(best, s)
    return best

if __name__ == '__main__':
    rng = random.Random(28); bad = 0
    for _ in range(1500):
        n = rng.randint(1, 7)
        Es = [rng.randint(0, 20) for _ in range(n)]
        Ms = [rng.randint(0, 20) for _ in range(n)]
        Hs = [rng.randint(0, 20) for _ in range(n)]
        bad += max_points(Es, Ms, Hs) != brute(Es, Ms, Hs)
    print('mismatches over 1500 random cases:', bad)
