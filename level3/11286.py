import heapq
import sys

read = sys.stdin.readline

h = []

N = int(read())

for _ in range(N):
    cmd = int(read())
    if cmd:
        heapq.heappush(h, (abs(cmd), cmd))
    else:
        if h:
            print(heapq.heappop(h)[-1])
        else:
            print(0)
