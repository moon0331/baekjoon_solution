N = int(input())

dp = [1, 2, 3]

for _ in range(N-3):
    dp[0], dp[1] = dp[1], dp[2]
    dp[2] = (dp[0] + dp[1]) % 15746

if N <= 3:
    print(N)
else:
    print(dp[2])