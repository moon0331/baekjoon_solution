import sys
from collections import defaultdict, deque

network = defaultdict(list)

n_com = int(sys.stdin.readline())
n_connect = int(sys.stdin.readline())
infected = [False for _ in range(n_com+1)]

for _ in range(n_connect):
    x, y = map(int, sys.stdin.readline().split())
    network[x].append(y)
    network[y].append(x)

q = deque()
q.append(1)
ans = 0
while q:
    com = q.popleft()
    if not infected[com]:
        ans += 1
        infected[com] = True
        next_com = [x for x in network[com] if not infected[x]]
        q.extend(next_com)

print(ans)