'''
A~G : 0~6
'''

def getNextNode(d, visited): # 문제점 찾기
    idx = -1
    minval = 99999
    for i in range(len(d)):
        if d[i] < minval and i not in visited:
            minval = d[i]
            idx = i
    return idx

node_to_idx = 'ABCDEFG'
A, B, C, D, E, F, G = 0, 1, 2, 3, 4, 5, 6

N = len(node_to_idx)

g = [[0 for _ in range(N)] for _ in range(N)]

g[A][B] = 2
g[A][F] = 15
g[B][D] = 14
g[C][D] = 12
g[C][E] = 8
g[C][F] = 5
g[D][B] = 14
g[D][C] = 12
g[D][E] = 10
g[E][C] = 8
g[E][D] = 10
g[E][G] = 1
g[F][A] = 15
g[F][C] = 5
g[F][G] = 6
g[G][E] = 1
g[G][F] = 6

d = [99999 for _ in range(N)]
d[0] = 0
visited = set()

next_node = A
while len(visited) < N:
    next_node = getNextNode(d, visited)
    for n in range(N):
        if g[next_node][n] in (0, 99999): continue
        d[n] = min(d[n], d[next_node]+g[next_node][n])
    # visited 처리
    print(node_to_idx[next_node], d)
    visited.add(next_node)