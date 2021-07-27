import sys

N = int(input())

dots = []

for _ in range(N):
    dots.append(tuple(map(int, sys.stdin.readline().split())))

dots.sort(key=lambda x:x[1])
dots.sort(key=lambda x:x[0])

for val in dots:
    print(*val)