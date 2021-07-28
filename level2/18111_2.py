import sys

def relu(x):
    return x if x >= 0 else 0

N, M, B = map(int, sys.stdin.readline().split())

land = []

min_land, max_land = 257, -1    # 땅의 최소 높이, 최대 높이

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    min_land, max_land = min(min_land, min(row)), max(max_land, max(row))
    land.append(row)

n_step = []
for h in range(min_land, max_land+1):
    #print('=============={}=============='.format(h))
    n_up, n_down = 0, 0
    for row in land:
        #print(sum(relu(h-x) for x in row), "needed to up\t", h, row)
        n_up += sum(relu(h-x) for x in row)
        #print(sum(relu(x-h) for x in row), "needed to down", h, row)
        n_down += sum(relu(x-h) for x in row)
    time = 2 * n_down + n_up
    if B >= n_up:
        n_step.append((h, n_up, n_down, time))

n_step.sort(key=lambda x:(x[-1], -x[0])) # time 오름차순, h 내림차순

ans = n_step[0]

print(ans[-1], ans[0])