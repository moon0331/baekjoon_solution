# 소인수분해

N = int(input())

for i in range(2, N+1):
    cnt = 0
    while N % i == 0:
        cnt += 1
        N = int(N/i)
        print(i)
    if N == 1:
        break