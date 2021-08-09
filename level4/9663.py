ans = 0

def DFS(chess, row, N):
    global ans
    if row == N:
        ans += 1
        print(chess)
        return
    next_row = row + 1
    for next_col in range(N):
        for prev_row, prev_col in enumerate(chess):
            # print('({}, {}) - ({}, {})'.format(prev_row, prev_col, next_row, next_col), end='')
            if prev_col == next_col or abs(prev_row-next_row) == abs(prev_col-next_col):
                # print('X')
                break
        else:
            DFS(chess+[next_col], next_row, N)

N = int(input())

for i in range(N):
    DFS([i], 0, N)

print(ans)