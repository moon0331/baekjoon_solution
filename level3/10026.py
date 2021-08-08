import sys
from collections import deque

def BFS(land, j, i, N, visited):
    if visited[j][i] == 0:
        return 0
    q = deque([(j, i)])
    search_color = visited[j][i]
    visited[j][i] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            newy, newx = y+dy, x+dx
            if 0<=newy<N and 0<=newx<N:
                if visited[newy][newx] == search_color:
                    q.append((newy, newx))
                    visited[newy][newx] = 0
    return 1

N = int(sys.stdin.readline())

land = [sys.stdin.readline().strip() for _ in range(N)]
land_rb = [['B' if c=='B' else 'R' for c in row] for row in land]

color_dict={'R':1, 'B':2, 'G':3}
visited = [[color_dict[c] for c in row] for row in land]
visited_rb = [[color_dict[c] for c in row] for row in land_rb]

ans = ans_rb = 0
for j in range(N):
    for i in range(N):
        ans += BFS(land, j, i, N, visited)
        ans_rb += BFS(land_rb, j, i, N, visited_rb) # 적록색약

print(ans, ans_rb)