# 일단 1부터 채움
# 2는 1에서부터 채움
# 3은 2에서부터

# def fourSquare(n):
#     dp = [9999 for i in range(n+1)]
#     n_zero = sum([1 for i in range(n+1) if dp[i] == 0])
#     cal_idx = [0]
#     for val in range(1, 5):
#         # print(val)
#         cal_idx = [x+i**2 for i in range(1, 225) for x in cal_idx if x+i**2 <=n]
#         cal_idx = list(set(cal_idx))
#         # print(cal_idx)
#         for idx in cal_idx:
#             if dp[idx] < val:
#                 continue 
#             dp[idx] = val
#         if dp[n] != 9999:
#             return dp[n]


#     # print(dp)

#     return dp[n]

def fourSquare(x):
    squared = tuple(i**2 for i in range(1, 225))
    if x in squared:
        return 1
    dp = [1 if i in squared else 9999 for i in range(x+1)]
    for val in range(2, 5):
        for q in range(val, x):
            val = [dp[k]+dp[q-k] for k in range(1, int(x/2)+1)]
            dp[q] = min([dp[k]+dp[q-k] for k in range(1, int(x/2)+1)]+[dp[q]]) 
    return dp[x]
    

print(fourSquare(int(input())))

# 1 2^2 3^2 4^2 5^2 ...
# 