import sys

T = int(sys.stdin.readline())

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(90)]

for i in range(10, 101):
    dp[i] = dp[i-5] + dp[i-1]

for _ in range(T):
    print(dp[int(sys.stdin.readline())])