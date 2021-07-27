# 네 번째 점

x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())
    if not a in x:
        x.append(a)
    else:
        x.remove(a)
    if not b in y:
        y.append(b)
    else:
        y.remove(b)

print(x[0], y[0])