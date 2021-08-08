import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

box = []
for _ in range(H):
    box.append([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

visited = [[[True if box[i][j][k] == -1 else False for k in range(M)] for j in range(N)] for i in range(H)]

print(box)
print(visited)

q = deque([(0, 0, 0, 0)]) # x, y, z, when visited

possible_move = ((-1, 0, 0), (1, 0, 0), 
                (0, -1, 0), (0, 1, 0), 
                (0, 0, -1), (0, 0, 1))

while q:
    x, y, z, visit_num = q.popleft()
    for dx, dy, dz in possible_move: # -1 처리 어떻게?
        newx, newy, newz = x+dx, y+dy, z+dz
        if 0<=newx<H and 0<=newy<N and 0<=newz<M: # inbound
            if not visited[newx][newy][newz]: # nonvisit
                visited[newx][newy][newz] = True  
                q.append((newx, newy, newz, visit_num+1)) 
                if box[newx][newy][newz] == 0: # 익음
                    box[newx][newy][newz] = 1

for line in box:
    for line2 in line:
        if 0 in line2:
            print(-1)
            exit(0)
print(visit_num)