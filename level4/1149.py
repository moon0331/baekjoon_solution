import sys

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = [val for val in cost[0]]

# step
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1])+cost[i][2]

print(min(dp[-1]))