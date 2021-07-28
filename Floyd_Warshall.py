import sys
from collections import defaultdict

node = []

N = int(sys.stdin.readline())
g = {i:{j:99999 for j in range(1, N+1)} for i in range(1, N+1)}
for k in g:
    g[k][k] = 0

while True:
    ans = sys.stdin.readline().strip()
    if not ans:
        break
    x, y, val = map(int, ans.split())
    g[x][y] = val
    
for k in g:
    print(list(g[k].values()))

node = list(g.keys())
for k in node:
    for i in node:
        for j in node:
            if i == j or i == k: continue
            print('{}->{}->{}'.format(i, k, j))
            if g[i][j] > g[i][k]+g[k][j]:
                print('g[{}][{}]changed : {} -> {}'.format(i,j, g[i][j], g[i][k]+g[k][j]))
                g[i][j] = g[i][k]+g[k][j]
            # g[i][j] = min(g[i][j], g[i][k]+g[k][j])
    print('--------------------------------------------')

for k in g:
    print(list(g[k].values()))

'''
7
1 2 2
1 6 15
2 1 2
2 4 14
3 4 12
3 5 8 
3 6 5
4 2 14
4 3 12
4 5 10
5 3 8
5 4 10
5 7 1
6 1 15
6 3 5
6 7 6
7 5 1
7 6 6


'''