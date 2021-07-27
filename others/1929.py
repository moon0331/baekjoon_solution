# 소수 구하기

import math

def eratos(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        th = int(math.sqrt(x))
        for i in range(2, th+1):
            if x % i == 0:
                return False
        return True

M, N = map(int, input().split())

for val in range(M, N+1):
    if eratos(val):
        print(val)