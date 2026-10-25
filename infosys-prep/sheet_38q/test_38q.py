"""Random test of sol_38q.cpp vs brute force over an integer grid. Usage: python3 test_38q.py <binary>"""
import random, subprocess, sys
BIN = sys.argv[1]
R = random.Random(3)

def dist_seg(px, py, x1, y1, x2, y2):
    # Manhattan distance from point to segment: min over segment points (integer-or-not doesn't matter for axis segments)
    best = None
    lo_x, hi_x = min(x1, x2), max(x1, x2)
    lo_y, hi_y = min(y1, y2), max(y1, y2)
    cx = min(max(px, lo_x), hi_x)
    cy = min(max(py, lo_y), hi_y)
    return abs(px - cx) + abs(py - cy)

def brute(lines):
    xs = [v for l in lines for v in (l[0], l[2])]
    ys = [v for l in lines for v in (l[1], l[3])]
    best = None
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            s = sum(dist_seg(x, y, *l) for l in lines)
            key = (s, x, y)
            if best is None or key < best:
                best = key
    return best[1], best[2]

bad = 0
for _ in range(400):
    n = R.randint(1, 5)
    lines = []
    for _ in range(n):
        if R.random() < 0.5:
            y = R.randint(-4, 4); x1 = R.randint(-4, 4); x2 = R.randint(-4, 4)
            lines.append([x1, y, x2, y])
        else:
            x = R.randint(-4, 4); y1 = R.randint(-4, 4); y2 = R.randint(-4, 4)
            lines.append([x, y1, x, y2])
    text = f"{n}\n" + "".join(" ".join(map(str, l)) + "\n" for l in lines)
    got = subprocess.run([BIN], input=text, capture_output=True, text=True).stdout.split()
    exp = brute(lines)
    if (int(got[0]), int(got[1])) != exp:
        bad += 1
        if bad <= 3:
            print("MISMATCH", lines, "expected", exp, "got", got)
print("38q random cases: 400, mismatches:", bad)
