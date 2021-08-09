import sys
from collections import deque

OPENED = 2
CHEESE = 1
CLOSED = 0

def check_opened_space(arr):
    movement = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque([(0, 0)])
    visited = set([(0, 0)])
    arr[0][0] = OPENED
    while q:
        row, col = q.popleft()
        for dr, dc in movement:
            nr, nc = row+dr, col+dc
            if not (nr, nc) in visited: 
                if 0<=nr<N and 0<=nc<M and arr[nr][nc] != CHEESE:
                    arr[nr][nc] = OPENED
                    q.append((nr, nc))
                    visited.add((nr, nc))
    
    # for row in arr:
    #     print(*[str(c) for c in row])


def melting(arr):
    movement = ((-1, 0), (1, 0), (0, -1), (0, 1))
    n_melted_cheese = 0
    melting = list()
    for row in range(1, N-1):
        for col in range(1, M-1):
            if arr[row][col] == 1:
                n_adj = sum([1 for dr, dc in movement if arr[row+dr][col+dc] == OPENED])
                if n_adj >= 2:
                    melting.append((row, col))
                    n_melted_cheese += 1
    for r, c in melting:
        # print(r, c, 'opened')
        arr[r][c] = OPENED
    return n_melted_cheese

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 치즈 안의 공간 전처리 with BFS
# 바깥공간 0 처리, 안공간 2처리


n_cheese = 0
for row in range(1, N-1):
    for col in range(1, M-1):
        if arr[row][col] == 1:
            n_cheese += 1

n_time = 0

# print('-'*50)
while n_cheese:
    check_opened_space(arr)
    # print('='*50)
    n_cheese -= melting(arr)
    # print('='*50)
    n_time += 1

print(n_time)