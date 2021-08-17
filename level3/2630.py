import sys
read = sys.stdin.readline

def only_one(arr, r, c, l):
    val = arr[r][c]
    for row in range(r, r+l):
        for col in range(c, c+l):
            if val != arr[row][col]:
                return False
    return True

def paper(arr, r, c, l, ans): # l == 한 변 길이
    # print('r={}, c={}, base_val={}, N={}'.format(r, c, base_val, l))
    if l == 1 or only_one(arr, r, c, l):
        ans[arr[r][c]] += 1
        return
    else:
        half_l = l//2
        # 1사분면
        paper(arr, r, c, half_l, ans)
        # 2사분면
        paper(arr, r+half_l, c, half_l, ans)
        # 3사분면
        paper(arr, r, c+half_l, half_l, ans)
        # 4사분면
        paper(arr, r+half_l, c+half_l, half_l, ans)

N = int(read())
arr = [list(map(int, read().split())) for _ in range(N)]
ans = [0, 0]

paper(arr, 0, 0, N, ans)

print(*ans, sep='\n')