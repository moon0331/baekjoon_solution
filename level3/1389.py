import sys

def DFS(relation):
    pass

N, M = map(int, sys.stdin.readline().split())

relationship = {i:[] for i in range(1, N+1)}

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    if not y in relationship[x]:
        relationship[x].append(y)
        relationship[y].append(x)

