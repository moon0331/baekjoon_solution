# floyd

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

g = [[0 if i == j and i != 0 else float('inf') for j in range(n+1)] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a][b] = min(g[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

for i in range(1, n+1):
    print(*[c if c != float('inf') else 0 for c in g[i][1:]])