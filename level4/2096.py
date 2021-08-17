read = __import__('sys').stdin.readline

N = int(read())

arr = [list(map(int, read().split())) for _ in range(N)]

dp_max = [[0 for _ in range(3)] for _ in range(N)]
dp_max[0] = arr[0]

dp_min = [[c for c in line] for line in dp_max]

# print(dp_max)
# print(dp_min)

for row in range(1, N):
    for col in range(3):
        possible_route_max = []
        possible_route_min = []
        tr = row - 1
        for tc in range(col-1, col+2):
            if 0<=tc<3:
                possible_route_max.append(dp_max[tr][tc])
                possible_route_min.append(dp_min[tr][tc])
        #print(row, col, possible_route_max, possible_route_min)
        dp_max[row][col] = max(possible_route_max)+arr[row][col]
        dp_min[row][col] = min(possible_route_min)+arr[row][col]

print(max(dp_max[-1]), min(dp_min[-1]))

# 메모리 줄이기 -> dp 2차원에서 1차원으로?