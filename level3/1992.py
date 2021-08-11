import sys

def isAtomic(arr, r, c, l):
    val = arr[r][c]
    for row in range(r, r+l):
        for col in range(c, c+l):
            if val != arr[row][col]:
                # not same
                # divide
                return False
    return True
    

def quad(arr, r, c, l): # (r, c)에서 시작하는 한 변의 길이가 l인 배열
    if l == 1 or isAtomic(arr, r, c, l):
        return str(arr[r][c])
    else:
        half_l = l//2
        str_1 = quad(arr, r, c, half_l)
        str_2 = quad(arr, r, c+half_l, half_l)
        str_3 = quad(arr, r+half_l, c, half_l)
        str_4 = quad(arr, r+half_l, c+half_l, half_l)
        concat_str = '(' + str_1 + str_2 + str_3 + str_4 + ')'
        return concat_str

N = int(sys.stdin.readline())
arr = [list(map(int, [c for c in sys.stdin.readline().strip()])) for _ in range(N)]

print(quad(arr, 0, 0, N))