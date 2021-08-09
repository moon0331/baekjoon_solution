def solve(arr):
    row, col = len(arr), len(arr[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]

    try:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]
    except:
        pass

    if col == 1:
        return max(dp[0][0], dp[1][0])
    elif col == 2:
        return max(dp[1][0], dp[1][1])
    
    ans = max(dp[0][0], dp[0][1], dp[1][0], dp[1][1])
    for c in range(2, col):
        for r in range(row):
            dp[1-r][c] = max(dp[r][c-1]+arr[1-r][c], 
                            dp[1-r][c-2]+arr[1-r][c], 
                            dp[r][c-2]+arr[1-r][c])
            ans = max(dp[1-r][c], ans)
    return ans


read = __import__('sys').stdin.readline

T = int(read())
for _ in range(T):
    n = int(read())
    arr = [list(map(int, read().split())) for _ in range(2)]
    print(solve(arr))