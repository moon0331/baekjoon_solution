import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    query = int(sys.stdin.readline())
    if query == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, query)