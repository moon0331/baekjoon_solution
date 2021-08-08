import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0 for _ in range(len(line))] for line in arr]
dp[0][0] = arr[0][0]

for h in range(1, n):
    dp[h][0] = dp[h-1][0]+arr[h][0]
    dp[h][-1] = dp[h-1][-1]+arr[h][-1]
    for k in range(1, h): # fxxking index
        dp[h][k] = max(dp[h-1][k-1], dp[h-1][k]) + arr[h][k]

print(max(dp[-1]))