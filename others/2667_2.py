from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

visited = '2'

N = int(input())
apart = []
for _ in range(N):
    apart.append([x for x in input()])

answer = []
for i in range(N):
    for j in range(N):
        if apart[i][j] == '1': # 방이 있고 방문하지 않음
            q = deque()
            q.append((i, j)) # ㅇㅋ 넣음 
            print(i, j, 'visited')
            k = 0
            while q:
                x, y = q.popleft() # 뽑을때 체크
                if apart[x][y] != '1':
                    continue
            # if apart[x][y] == '1':
                k += 1
                apart[x][y] = visited # 방문함
                print(x, y, 'visited')
                for xx, yy in zip(dx, dy):
                    newx, newy = x+xx, y+yy
                    if newx < 0 or newy < 0:
                        continue
                    elif newx >= N or newy >= N:
                        continue
                    if apart[newx][newy] == '1':
                        print((newx, newy))
                        q.append((newx,newy))  
            #print(k)
            answer.append(k)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)