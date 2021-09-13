def DFS(n, computers, start_node, visited):
    stack = [start_node]
    while stack:
        node = stack.pop()
        for next_node in range(n):
            if not visited[next_node] and computers[node][next_node] == 1:
                stack.append(next_node)
                visited[next_node] = True


def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    for start_node in range(n):
        if visited[start_node]:
            continue
        DFS(n, computers, start_node, visited)
        answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1)