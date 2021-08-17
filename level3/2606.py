import sys
from collections import deque

read = sys.stdin.readline

N = int(read())

g = {i:set() for i in range(1, N+1)}
visited = [False for i in range(N+1)]

n_connect = int(read())
for _ in range(n_connect):
    x, y = map(int, read().split())
    g[x].add(y)
    g[y].add(x)

q = deque([1])
while q:
    com = q.popleft()
    for next_com in g[com]:
        if not visited[next_com]:
            q.append(next_com)
            visited[next_com] = True

print(sum([1 for c in visited if c])-1)