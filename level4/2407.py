n, m = map(int, input().split())

ans = 1
for i in range(m):
    ans *= (n-i)/(1+i)
print(int(ans))