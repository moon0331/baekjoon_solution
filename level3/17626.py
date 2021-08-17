import sys
n = int(input())
# n = int(sys.argv[1])

dp = [float('inf') for _ in range(n+1)]
dp[0] = 0

if n >0:
    i = 1
    while True:
        # print(i**2, n+1)
        if i**2 > n:
            break
        dp[i**2] = 1
        i += 1

for i in range(2, n+1):
    # print(i, 'cal', '========================')
    j = 1
    while j**2 < i:
        # print(i-j**2, j**2)
        dp[i] = min(dp[i], dp[i-j**2] + dp[j**2])
        j += 1
    # for div in range(1, i//2+1):
    #     # print(div, dp[div], i-div, dp[i-div])
    #     dp[i] = min(dp[i], dp[div]+dp[i-div])

print(dp[-1])