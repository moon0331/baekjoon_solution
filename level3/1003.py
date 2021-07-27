import sys

def fib(n, cnt):
    if n==0:
        cnt[0] += 1
        return 0
    elif n == 1:
        cnt[1] += 1
        return 1
    else:
        return fib(n-1, cnt) + fib(n-2, cnt)

T = int(sys.stdin.readline())

dp = [[0, 0] for _ in range(41)]
dp[0][:] = [1, 0]
dp[1][:] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-2][0] + dp[i-1][0]
    dp[i][1] = dp[i-2][1] + dp[i-1][1]
    # dp[i] = list(map(sum, zip(dp[i-2], dp[i-1]))) # 왜 더 느린지

for _ in range(T):
    N = int(sys.stdin.readline())
    print(*dp[N])