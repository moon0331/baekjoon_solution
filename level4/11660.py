import sys

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    