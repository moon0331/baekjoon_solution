def find_minimum(x):
    if x == 1:
        return 0
    elif x == 2 or x == 3:
        return 1
    dp = [0 for _ in range(N+1)]
    dp[1] = 0
    dp[2] = dp[3] = 1

    for idx in range(4, N+1):
        available = [dp[idx-1]]
        if idx % 2 == 0:
            available.append(dp[int(idx/2)])
        if idx % 3 == 0:
            available.append(dp[int(idx/3)])
        dp[idx] = min(available) + 1
    
    return dp[x]

N = int(input())

print(find_minimum(N))