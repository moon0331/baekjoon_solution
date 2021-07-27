# DP or GREEDY

def DP_answer(x):
    if x==4 or x == 7:
        return -1
    elif x==3 or x==5:
        return 1
    dp = [9999 for _ in range(x+1)]
    dp[3] = dp[5] = 1
    for i in range(6, x+1):
        dp[i] = min(dp[i-3]+1, dp[i-5]+1)
    if dp[x]>=9999:
        return -1
    else:
        return dp[x]

def iter_answer(x):
    num_five = 0
    for num_five in range(x//5, -1, -1):
        num_three = 0
        skajwl = x - num_five * 5
        while num_three * 3 < skajwl:
            num_three += 1
        if skajwl == num_three * 3:
            return num_five + num_three
    return -1

# print(iter_answer(int(input())))
print(DP_answer(int(input())))