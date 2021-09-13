from collections import deque

def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    # print(graph)

    d = [False for _ in range(n+1)]
    d[0] = d[1] = 0

    q = deque([(1,0)])
    while q:
        node, step = q.popleft()
        for next_node in graph[node]:
            if next_node != 1 and d[next_node] == False:
                q.append((next_node, step+1))
                d[next_node] = step+1

    # print(d)
    return sum(1 for x in d if x == max(d))



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3)

# dij