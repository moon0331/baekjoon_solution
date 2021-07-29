x = int(input())

dp = [0, 1, 3]

for i in range(x-2):
    dp[0], dp[1] = dp[1], dp[2]
    dp[2] = (2*dp[0] + dp[1]) % 10007

if x == 1:
    print(1)
elif x == 2:
    print(3)
else:
    print(dp[2])