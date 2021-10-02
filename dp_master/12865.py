N, K = map(int, input().split())

WV = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)] # value

for i, (wi, vi) in zip(range(1, N+1), WV): # i th item, 무게 wi, 값 vi
    for w_limit in range(K+1): # 0 to K : 무게 제한
        if wi > w_limit:
            dp[i][w_limit] = dp[i-1][w_limit]
        else:
            dp[i][w_limit] = max(vi + dp[i-1][w_limit - wi], dp[i-1][w_limit])

print(dp[-1][-1])

#knapsack