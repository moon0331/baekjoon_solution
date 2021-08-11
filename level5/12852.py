from collections import deque

def BFS(N, visited): # 반대방향으로 고치기
    q = deque([1])
    visited[1] = 0
    while q:
        x = q.popleft()
        if x == N:
            break
        if 3*x <= N and visited[3*x] == False:
            q.append(3*x)
            visited[3*x] = x
        if 2*x <= N and visited[2*x] == False:
            q.append(2*x)
            visited[2*x] = x
        if x+1 <= N and visited[x+1] == False:
            q.append(x+1)
            visited[x+1] = x
    path = [N]
    loc = N
    while loc>1:
        path.append(visited[loc])
        loc = visited[loc]
    print(len(path)-1)
    print(*path)
        

N = int(input())
visited = [False for _ in range(N+1)]
BFS(N, visited)