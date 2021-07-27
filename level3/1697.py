from collections import deque, defaultdict

def BFS(x, y):
    q = deque()
    visited = defaultdict(int)
    q.append(x)
    while q:
        moved = q.popleft()
        n_step = visited[moved]
        if moved == y:
            break
        next_possible = (moved-1, moved+1, 2*moved)
        for next_step in next_possible:
            if next_step > 4*y: continue
            if not visited[next_step] or n_step + 1 < visited[next_step]:
                q.append(next_step)
                visited[next_step] = n_step + 1
    print(n_step)

BFS(*map(int, input().split()))