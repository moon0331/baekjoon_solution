from collections import deque

N = 7 
apart = [
    "0 1 1 0 1 0 0".split(), 
    "0 1 1 0 1 0 1".split(), 
    "1 1 1 0 1 0 1".split(), 
    "0 0 0 0 1 1 1".split(), 
    "0 1 0 0 0 0 0".split(),
    "0 1 1 1 1 1 0".split(),
    "0 1 1 1 0 0 0".split()
    ]

print(apart)
for row in apart:
    print("".join(row))

visited = 2

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

class LeftIndexError(IndexError):
    pass

class RightIndexError(IndexError):
    pass

answer = []
for i in range(7):
    for j in range(7):
        if apart[i][j] == '1': # 방이 있고 방문하지 않음
            q = deque()
            q.append((i, j)) # ㅇㅋ 넣음 
            k = 0
            while q:
                x, y = q.popleft() # 뽑을때 체크
                if apart[x][y] == '1':
                    k += 1
                    apart[x][y] = '2' # 방문함
                    #print(x, y, 'visited')
                for d in range(4):
                    try:
                        newx, newy = x+dx[d], y+dy[d]
                        if newx * newy < 0:
                            raise LeftIndexError
                        elif newx >=7 or newy >=7:
                            raise RightIndexError
                        if apart[newx][newy] == '1':
                            #print((newx, newy))
                            q.append((newx,newy))  
                    except IndexError: # -1
                        pass
            #print(k)
            answer.append(k)

print(len(answer))
for ans in answer:
    print(ans)