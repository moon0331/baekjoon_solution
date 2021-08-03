import sys

N, M, B = map(int, sys.stdin.readline().split())

land = []

for _ in range(N):
    land.append(list(map(int, sys.stdin.readline().split())))

ans_height = -1
ans_time = float('inf') #sys.maxint
for height in range(256+1):
    h_down = h_up = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] > height:
                h_down += land[i][j] - height
            else:
                h_up += height - land[i][j]
    if h_up - h_down > B:
        continue
    h_time = 2 * h_down + h_up
    if h_time <= ans_time:
        ans_height = height
        ans_time = h_time

print(ans_time, ans_height)

# 올라가는 것과 내려가는 것이 가중치가 다르기 때문에
# 무조건 옵티멀이 최소 최대 사이가 아닐 수 있다