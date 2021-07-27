N, K = map(int, input().split())

ans = 1

for i in range(K):
    ans *= (N-i)/(i+1)

print(int(ans))