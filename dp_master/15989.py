N = int(input())
val = [int(input()) for _ in range(N)]

dp = [0 for _ in range(10001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, 10001):
	dp[i] = dp[i-1] + dp[i-2] - dp[i-3]
	if i%3 == 0:
		dp[i] += 1

for x in val:
    print(dp[x])