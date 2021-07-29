import sys
from collections import deque

def BFS(maze, visited):
    visited[0][0] = 1
    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        val = visited[i][j]
        if visited[x][y] == -1:
            visited[x][y] = val + 1
            if x == N-1 and y == M-1:
                return visited[x][y]

N, M = map(int, sys.stdin.readline().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, [c for c in sys.stdin.readline().split()])))

print(maze)