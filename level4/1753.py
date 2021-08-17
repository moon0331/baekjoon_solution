import sys
from collections import defaultdict
import heapq

g = defaultdict(dict)

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    g[u][v] = w

d = [float('inf') for _ in range(V+1)]
d[K] = 0
for n in g[K]:
    d[n] = g[K][n]

print(g)

h = []
for n in g[K]:
    heapq.heappush(h, (g[K][n], n)) #(가중치, 노드)

while h:
    _, temp_node = heapq.heappop(h)
    print(d, temp_node)
    for node in range(1, V+1):
        if node in g[temp_node]:
            print('determine d[{}]'.format(node))
            d[node] = min(d[node], d[temp_node]+g[temp_node][node])

print(d)