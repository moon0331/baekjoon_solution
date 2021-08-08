n_stair = int(input())

arr = [0]+[int(input()) for _ in range(n_stair)]
if n_stair == 1:
    print(arr[1])
else:
    dp = [0, arr[1], arr[1]+arr[2]] + [0 for _ in range(n_stair-2)]

    for x in range(3, n_stair+1):
        dp[x] = max(dp[x-3]+arr[x-1]+arr[x], dp[x-2]+arr[x])

    print(dp[n_stair])