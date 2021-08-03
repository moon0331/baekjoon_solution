import sys
from collections import deque

def BFS(land, n, m):
    has_new_field = False
    q = deque([(n, m)])
    while q:
        y, x = q.popleft()
        # print(y, x, 'found')
        if visited[y][x] == False:
            # print('..not visited')
            visited[y][x] = True
        else:
            continue
        if land[y][x] == 1:
            # print('.. expand')
            has_new_field = True
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newy, newx = y+dy, x+dx
                if 0 <= newy < N and 0 <= newx < M and not visited[newy][newx]:
                    # print('.. expand {} {}'.format(newy, newx))
                    q.append((newy, newx))
    # print('bfs end')
    return 1 if has_new_field else 0

T = int(sys.stdin.readline())

for _ in range(T):

    M, N, K = map(int, sys.stdin.readline().split())

    land = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        land[y][x] = 1

    # for row in land:
    #     print(row)

    ans = 0
    for n in range(N): # 세로
        for m in range(M): # 가로
            ans += BFS(land, n, m)

    print(ans)

    # for row in land:
    #     print(row)