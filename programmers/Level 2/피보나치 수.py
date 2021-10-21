def solution(n):
    dp = [None for _ in range(n+1)]
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1] % 1234567

print(solution(3) == 2)
print(solution(2) == 1)

# cache로 구현 가능 (recursion + memoization)