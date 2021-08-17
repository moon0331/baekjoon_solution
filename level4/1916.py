import heapq 

#DIJ 복습하기

def DIJ(g, dist_list, start, end):
    h = []
    visited = set()

    for i in range(len(dist_list)):
        if dist_list[i] != float('inf'):
            heapq.heappush(h, (dist_list[i], i)) #(거리, 노드)
    
    while h:
        val, node = heapq.heappop(h)
        next_nodes = [i for i in range(len(g)) if g[node][i] != float('inf')]
        for nn in next_nodes:
            dist_list[nn] = min(dist_list[nn], dist_list[node] + g[node][nn])
        

    return dist_list[end]


read = __import__('sys').stdin.readline

N = int(read())
M = int(read())

g = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    x, y, val = map(int, read().split())
    g[x][y] = val

start, end = map(int, read().split())

dist_list = [float('inf') for _ in range(N+1)]
dist_list[start] = 0

print(DIJ(g, dist_list, start, end))

# https://justkode.kr/algorithm/python-dijkstra