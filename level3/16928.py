import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

rule = {}

for _ in range(N+M):
    x, y = map(int ,sys.stdin.readline().split())
    rule[x] = y

q = deque()
q.append(1)
visited = [False for _ in range(101)]
visited[1] = 0
while q:
    n = q.popleft()
    n_step = visited[n]
    if n == 100:
        break
    for dice in (1, 2, 3, 4, 5, 6):
        next_n = n + dice
        if next_n in rule:
            next_n = rule[next_n]
        if next_n > 100:
            continue
        if not visited[next_n]:
            visited[next_n] = n_step + 1
            q.append(next_n)


print(visited[100]) 