def solution(board):
    row, col = len(board), len(board[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        dp[i][0] = board[i][0]
    for j in range(col):
        dp[0][j] = board[0][j]

    maxval = -1

    for i in range(1, row):
        for j in range(1, col):
            if board[i][j]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            maxval = max(maxval, dp[i][j])

    return maxval**2

brds = [[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]], [[0,0,1,1],[1,1,1,1]]]
anss = [9, 4]

for b, a in zip(brds, anss):
    print(solution(b) == a)