import sys
from collections import defaultdict

def getNextNode(d, visited):
    minval = 99999
    idx = -1
    for i in range(1, len(d)):
        if d[i] < minval and i not in visited:
            idx = i
            minval = d[i]
    return idx


g = defaultdict(dict)
node = []

while True:
    ans = sys.stdin.readline().strip()
    if not ans:
        break
    x, y, val = map(int, ans.split())
    g[x][y] = val
    
print(g)

visited = set()
N = len(g)

node = 1 # 1번에서부터 각 노드까지 가는 최단거리
d = [99999 for _ in range(N+1)] # [쓰레기값, A, B, ...]
d[node] = 0

while len(visited) < N:
    # get next node
    node = getNextNode(d, visited)
    for nextnode in g[node]:
        d[nextnode] = min(d[nextnode], d[node]+g[node][nextnode])
    visited.add(node)

print(d)