N = int(input())

arr = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    arr[1][i] = 1

for i in range(1, N+1):
    for j in range(10):
        if j >= 1:
            arr[i][j] += arr[i-1][j-1]
        if j <= 8:
            arr[i][j] += arr[i-1][j+1]

print(sum(arr[N])%1000000000)