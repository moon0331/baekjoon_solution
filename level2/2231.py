def cal(N):
    for num in range(1, N):
        if num + sum(map(int, str(num))) == N:
            print(num)
            return
    print(0)

cal(int(input()))