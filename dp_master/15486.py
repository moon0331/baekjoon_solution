import sys

N = int(sys.stdin.readline())
T = []
P = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    tval, pval = map(int, sys.stdin.readline().split())
    T.append(tval)
    P.append(pval)

for i in reversed(range(N)):
    if i+T[i] <= N:
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
    else:
        dp[i] = dp[i+1]
    print(i, P[i], T[i], dp)


# print(dp)
print(dp[0])