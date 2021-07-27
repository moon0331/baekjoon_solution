from collections import deque

# 시간초과 -> visited set으로 변경해보기

def getConnectedComponent(g):
    visited = [False for i in range(len(g)+1)]
    n_comp = 0
    while all(visited[1:]) != True:
        q = deque()
        nonvisited = [i for i in range(1, len(visited)) if visited[i] == False]
        q.append(nonvisited[0])
        while q:
            node = q.popleft()
            if not visited[node]:
                visited[node] = True
                q.extend(g[node])
        n_comp += 1
    return n_comp


N, M = map(int, input().split())

graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(getConnectedComponent(graph))