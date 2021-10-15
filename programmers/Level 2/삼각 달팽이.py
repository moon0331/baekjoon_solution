def move(i, j, direction):
    return [(i+1, j), (i, j+1), (i-1, j-1)][direction]

def get_direction(arr, i, j, n, move_cntr):
    newi, newj = move(i, j, move_cntr)
    if not (0<=newi<n and 0<=newj<n) or arr[newi][newj]:
        move_cntr = (move_cntr+1)%3
        newi, newj = move(i, j, move_cntr)
    return newi, newj, move_cntr
    
def solution(n):
    arr = [[0 for i in range(i+1)] for i in range(n)]
    i, j = -1, 0
    move_cntr = 0 # 0, 1, 2
    for val in range(1, n*(n+1)//2+1):
        i, j, move_cntr = get_direction(arr, i, j, n, move_cntr)
        arr[i][j] = val

    return sum(arr, [])

testcase = [
    (4, [1,2,9,3,10,8,4,5,6,7]),
    (5, [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]),
    (6, [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11])
]

for n, result in testcase:
    print(solution(n) == result)