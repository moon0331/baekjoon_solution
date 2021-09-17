def solution(N, number):
    if number == N:
        return 1

    dp = [[]]
    for i in range(1, 8+1):
        tmp = []
        for x in range(1, i):
            tmp.extend([a+b for a in dp[x] for b in dp[i-x]])
            tmp.extend([a-b for a in dp[x] for b in dp[i-x]])
            tmp.extend([a*b for a in dp[x] for b in dp[i-x]])
            tmp.extend([int(a/b) for a in dp[x] for b in dp[i-x] if a*b != 0])
        tmp.append(int(str(N)*i))
        if number in tmp:
            return i
        tmp = list(set(tmp))
        dp.append(tmp)

    return -1

print(solution(5, 12) == 4) # 4
print(solution(2, 11) == 3) # 3