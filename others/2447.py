# 별 찍기 - 10

def star(star_map, n):
    if n == 3:
        star_map[0][:3] = [1, 1, 1]
        star_map[1][:3] = [1, 0, 1]
        star_map[2][:3] = [1, 1, 1]
        return
    
    a = n // 3 # n을 3으로 나눈 
    star(star_map, a)
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            for k in range(a): # 3 9 27 ...
                star_map[a*i+k][a*j:a*(j+1)] = star_map[k][:a]



N = int(input())

star_map = [[0 for _ in range(N)] for _ in range(N)]

star(star_map, N)

for line in star_map:
    print(*('*' if c == 1 else ' ' for c in line))