import sys

n = int(sys.stdin.readline())

juice = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0 for _ in range(n)]

try:
    dp[0] = juice[0]
    dp[1] = juice[0] + juice[1]
    dp[2] = max(juice[0]+juice[2], juice[1]+juice[2], juice[0]+juice[1])
except:
    pass

for x in range(3, n):
    dp[x] = max(dp[x-3]+juice[x-1]+juice[x], dp[x-2]+juice[x])
    dp[x] = max(dp[x], dp[x-1])

print(dp[-1])