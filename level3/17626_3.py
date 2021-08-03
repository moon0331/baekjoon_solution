n = int(input())

dp = [99999 for _ in range(n+1)]
dp[0], dp[1] = 0, 1

for i in range(2, n+1):
    k = 1
    while True:
        if k**2 > i:
            break
        dp[i] = min(dp[i], 1 + dp[i-k**2])
        k += 1

print(dp[n])