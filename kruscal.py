from collections import deque

graph = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n_node = 4

# 0 to 1 : cost 1
# 2 to 3 : cost 8
# 4 nodes (0, 1, 2, 3)

graph.sort(key=lambda x:x[-1])

q = deque(graph)
visited = set()
vertex = []
tot_value = 0

while len(visited) < n_node:
    x, y, val = q.popleft()
    if not (x in visited and y in visited): #??
        vertex.append((x, y))
        visited.add(x)
        visited.add(y)
        tot_value += val

print(vertex, tot_value)