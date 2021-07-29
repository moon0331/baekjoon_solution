import sys

N, M = map(int, sys.stdin.readline().split())

users = list(range(1, N+1))

g = [[99999 for _ in range(N+1)] for _ in range(N+1)]

for i in users:
    g[i][i] = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    g[A][B] = g[B][A] = 1

for k in users:
    for i in users:
        for j in users:
            if i==j or i==k: continue
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])

g_sum = [sum(row) for row in g]

print(g_sum.index(min(g_sum)))