def cal(x, y, z):
    if y == 1:
        return x % z
    half_cal = cal(x, y//2, z)
    if y%2:
        return ((half_cal**2)*x) % z
    else:
        return (half_cal**2) % z

A, B, C = map(int, input().split())

print(cal(A, B, C))