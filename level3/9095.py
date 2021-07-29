T = int(input())

dp = [0, 1, 2, 4] + [0 for _ in range(11+1-4)]

for i in range(4, 12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(T):
    print(dp[int(input())])

'''
5
(1,2,3 끝에 고정시켜서 케이스 나누기)

= 2 + 3 (2(=n-3)를 만드는 경우 : dp[n-3])
= 3 + 2 (3(=n-2)을 만드는 경우 : dp[n-2])
= 4 + 1 (4(=n-1)를 만드는 경우 : dp[n-1])
'''