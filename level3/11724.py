from collections import deque

def BFS(g, i, visited):
    if visited[i]:
        return 0
    q = deque([i])
    visited[i] = True
    while q:
        x = q.popleft()
        for next_node in g[x]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
    return 1


read = __import__('sys').stdin.readline

N, M = map(int, read().split())

g = {i:set() for i in range(1, N+1)}
visited = [False for i in range(N+1)]

for _ in range(M):
    x, y = map(int, read().split())
    g[x].add(y)
    g[y].add(x)

ans = 0
for node in g:
    ans += BFS(g, node, visited)

print(ans)