def solution(m, n, puddles):
    puddles = [(y,x) for x, y in puddles]
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for r in range(1, n+1):
        for c in range(1, m+1):
            if r == c == 1 or (r, c) in puddles: continue
            dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % 1000000007

    return dp[-1][-1]

print(solution(4, 3, [[2, 2]]) == 4)