N, K = map(int, input().split())

coin = []

for _ in range(N):
    coin.append(int(input()))

ans = 0

for value in coin[::-1]:
    ans += (K // value)
    K = K % value

print(ans)