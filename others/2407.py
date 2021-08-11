n, m = map(int, input().split())

qnswk = 1
qnsah = 1
for i in range(m):
    qnswk *= (n-i)
    qnsah *= (i+1)

print(qnswk//qnsah)