def minecraft(land, n_item):
    minval = 257
    maxval = -1

    for r in land:
        minval = min(minval, min(r))
        maxval = max(maxval, max(r))

    # 땅 높이기, 하나씩 세다가 깎는게 더 많아지면 바로 자르기
    cost_upper = cost_under = 0
    for r in land:
        cost_upper += sum(maxval-h for h in r)
        cost_under += sum(h-minval for h in r)
    
    cost_upper_time = cost_upper
    cost_under_time = 2 * cost_under

    if cost_upper <= n_item and cost_upper_time <= cost_under_time:
        return (cost_upper_time, maxval) # 
    else:
        return (cost_under_time, minval)
    

import sys

N, M, B = map(int, sys.stdin.readline().split())

land = []

for _ in range(N):
    land.append(list(map(int, sys.stdin.readline().split())))

print(*minecraft(land, B))