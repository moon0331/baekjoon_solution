import heapq
from math import inf

def preprocessing(N, road):
    g = {i:{j:inf for j in range(1, N+1)} for i in range(1, N+1)}
    for a, b, c in road:
        g[a][b] = min(g[a][b], c)
        g[b][a] = min(g[b][a], c)
    return g

def dij(N, g):
    h = [(0, 1)] # (거리, 노드)
    way = {i:inf for i in range(1, N+1)}
    while h:
        dist, node = heapq.heappop(h)
        # print(node, 'popped')
        way[node] = min(way[node], dist)
        for nextnode in range(1, N+1):
            if g[node][nextnode] != inf:
                # cost 계산
                cost = dist + g[node][nextnode]
                if cost < way[nextnode]:
                    # print(f'dist={dist}, nextnode={nextnode}, cost = {cost}')
                    # heap에 넣기
                    heapq.heappush(h, (cost, nextnode))
    return way


def solution(N, road, K):
    graph = preprocessing(N, road) # 연결하는 도로 여러개일 시 최단경로만 사용
    way = dij(N, graph)
    return sum(map(lambda x: x<=K, way.values()))

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3) == 4)
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4) == 4)

