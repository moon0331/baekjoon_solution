# 골드바흐의 추측

def eratos(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        th = int(x ** 0.5)
        for i in range(2, th+1):
            if x % i == 0:
                return False
        return True

prime_list = [x for x in range(2, 10000) if eratos(x)]

T = int(input())

for _ in range(T):
    n = int(input())
    for val in range(int(n/2), 1, -1):
        if val in prime_list and n-val in prime_list:
            print(val, n-val)
            break
