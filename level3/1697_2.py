import sys
from collections import deque

N, K = map(int, input().split())

visited = {x:999999 for x in range(100001)} # K+1로 하면 안됨

q = deque([N])
visited[N] = 0
while q:
    loc = q.popleft()
    val = visited[loc]
    for nextloc in (loc+1, loc-1, 2*loc):
        if nextloc in range(100001) and visited[nextloc] == 999999:
            q.append(nextloc)
            visited[nextloc] = val + 1
    if visited[K] != 999999:
        print(visited[K])
        break