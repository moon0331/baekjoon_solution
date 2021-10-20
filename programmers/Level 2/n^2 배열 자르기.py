# def solution(n, left, right):
#     two_d = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(i+1):
#             two_d[i][j] = i+1
#             two_d[j][i] = i+1

#     return [item for line in two_d for item in line][left:right+1]

def value(n, x):
    row, col = x//n, x%n
    return max(row, col)+1

def solution(n, left, right):
    val = [value(n, x) for x in range(left, right+1)]
    return val


wxyz = [(3, 2, 5, [3,2,2,3]), (4,7,14,[4,3,3,3,4,4,4,4])]

for w, x, y, z in wxyz:
    print(solution(w,x,y) == z)