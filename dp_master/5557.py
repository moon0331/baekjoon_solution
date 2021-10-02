N = int(input())
nums = list(map(int, input().split()))
val = nums[-1]

dp = [[0 for _ in range(21)] for _ in range(N-1)] #dp[x][y] : y번째 단계에서 x값이 나오는 경우의 수
dp[0][nums[0]] = 1

for i in range(1, N-1):
    for prev_val in range(21):
        n_way = dp[i-1][prev_val] # 이전 값은 dp[0][8] = 1 (prev_val=8, prev_val = 1)
        if n_way:
            present_val = nums[i] # nums[1] = 3
            if prev_val + present_val <= 20:
                dp[i][prev_val+present_val] += n_way
            if prev_val - present_val >= 0:
                dp[i][prev_val-present_val] += n_way

print(dp[-1][val])