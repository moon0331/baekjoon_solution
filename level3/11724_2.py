import sys
from collections import deque

def BFS(g, x, visited):
    q = deque([x])
    while q:
        val = q.popleft()
        visited[val] = True
        #print(val, g[x], list(nextnode for nextnode in g[val] if not visited[nextnode]))
        for nextnode in g[val]:
            if not visited[nextnode]:
                q.append(nextnode)
        # q.extend(nextnode for nextnode in g[val] if not visited[nextnode])

N, M = map(int, sys.stdin.readline().split())

# g = {i:set() for i in range(1, N+1)}
g = [[]*N for _ in range(N+1)]
# visited = {i:False for i in range(1, N+1)}
visited = [False for i in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    g[x].append(y)
    g[y].append(x)
    # g[x].add(y)
    # g[y].add(x)

ans = 0
for x in range(1, N+1):
    if not visited[x]: ans += 1
    BFS(g, x, visited)

print(ans)