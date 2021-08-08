import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

chicken_loc = []
house_loc = []

for y in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for x in range(len(line)):
        if line[x] == 1:
            house_loc.append((y, x))
        elif line[x] == 2:
            chicken_loc.append((y, x)) # n_chicken 확인하고 안더함

n_chicken = len(chicken_loc)
n_house = len(house_loc)

c_distance = [[0 for _ in range(n_chicken)] for _ in range(len(house_loc))]

# print('house_loc', house_loc)
# print('chicken_loc', chicken_loc)
# print('chicken_idx', n_chicken)
# print('chicken_distance', c_distance)

for h_num in range(n_house):
    for c_num in range(n_chicken):
        c_y, c_x = chicken_loc[c_num]
        h_y, h_x = house_loc[h_num]
        c_distance[h_num][c_num] = abs(c_y - h_y) + abs(c_x - h_x)

# print('chicken_distance', c_distance)  # c_distance[집번호][치킨집번호]

minval = float('inf')
for valid_c_idxs in combinations(range(n_chicken), M): # 선택된 치킨집
    val = 0
    min_dist_for_all_house = 0
    for h_dist_lst in c_distance:
        dist_list = [h_dist_lst[i] for i in range(len(h_dist_lst)) if i in valid_c_idxs]
        # print(valid_c_idxs, dist_list)
        min_dist_for_all_house += min(dist_list)
    minval = min(minval, min_dist_for_all_house)

print(minval)