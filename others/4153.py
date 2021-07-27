# 직각삼각형

while True:
    x, y, z = sorted(map(int, input().split()))
    if x == y == z == 0:
        break
    if x**2 + y**2 == z**2:
        print('right')
    else:
        print('wrong')