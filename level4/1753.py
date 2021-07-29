import sys
from collections import defaultdict

g = defaultdict(dict)

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    g[u][v] = w

d = [99999 for _ in range(V+1)]
d[K] = 0