def solution(triangle):
    dp = [[0 for _ in line] for line in triangle]
    len_triangle = len(triangle)
    dp[0][0] = triangle[0][0]
    for n in range(1, len(triangle)):
        dp[n][0] = dp[n-1][0] + triangle[n][0]
        for k in range(1, n):
            dp[n][k] = max(dp[n-1][k-1], dp[n-1][k]) + triangle[n][k]
        dp[n][-1] = dp[n-1][-1] + triangle[n][-1]
    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30)

'''

dp[n][0] = dp[n-1][0] + arr[n][0]
dp[n][n] = dp[n-1][n] + arr[n][n]
dp[n][k] = min(dp[n-1][k-1], dp[n-1][k]) + arr[n][k]

'''