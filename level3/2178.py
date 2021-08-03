import sys
from collections import deque

NOT_VISITED = float('inf')

def BFS(maze, N, M): # 닿는 최소의 칸

    def available_index(y, x):
        return 0 <= y < N and 0 <= x < M

    def should_visit(maze, visited, y, x):
        return maze[y][x] == 1 and visited[y][x] == NOT_VISITED

    q = deque([(0, 0)])
    visited = [[NOT_VISITED for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        loc = visited[y][x]
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            newy, newx = y+dy, x+dx
            if available_index(newy, newx) and should_visit(maze, visited, newy, newx):
                q.append((newy, newx))
                visited[newy][newx] = loc + 1
                if visited[N-1][M-1] != NOT_VISITED:
                    return visited[N-1][M-1]
    return -1 # not reached


N, M = map(int, sys.stdin.readline().split())

maze = []

for _ in range(N):
    maze.append([int(c) for c in sys.stdin.readline().strip()])

print(BFS(maze, N, M))