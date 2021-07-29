x = int(input())

dp = [0, 1, 2, 3]

for i in range(x-3):
    dp[1], dp[2] = dp[2], dp[3]
    dp[3] = (dp[1] + dp[2]) % 10007

if x == 1:
    print(1)
elif x == 2:
    print(2)
else:
    print(dp[3])