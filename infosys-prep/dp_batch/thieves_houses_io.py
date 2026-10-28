"""Thieves and Houses (screenshots, 17. Thieves and Houses): stdin/stdout version with T test cases.
Reads T, then for each test N and the N values; prints each answer mod 1e9+7 on its own line.
Usage: python3 thieves_houses_io.py < input.txt
"""
import sys
from dp_batch2_screenshots import thieves


def main(data):
    it = iter(data.split())
    T = int(next(it))
    out = []
    for _ in range(T):
        n = int(next(it))
        H = [int(next(it)) for _ in range(n)]
        out.append(str(thieves(H)))
    return '\n'.join(out)


if __name__ == '__main__':
    print(main(sys.stdin.read()))
