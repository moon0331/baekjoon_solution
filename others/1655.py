import heapq
import sys

N = int(sys.stdin.readline())

h = []
l = []

for i in range(N):
    val = int(sys.stdin.readline())
    heapq.heappush(h, val)
    l.append(val)
    heapq.heapify(l)
    print(l)
    h_len = len(h)
    tmp = []
    print_idx = int((h_len-1)/2)
    for j in range(h_len):
        val = heapq.heappop(h)
        tmp.append(val)
        # if j == print_idx:
        #     print(val)
    for x in tmp:
        heapq.heappush(h, x)
    # heapq.heappush(h, int(sys.stdin.readline()))
    # print('====')

    # tmp = []
    # for j in range(len(h)):
    #     val = heapq.heappop(h)
    #     print('popped val =', val)
    #     middle = len(h)//2
    #     if j == middle:
    #         print(val)
    #     heapq.heappush(h, val)