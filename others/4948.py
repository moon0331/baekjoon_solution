# 베르트랑 공준

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

prime_list = [x for x in range(2, 260000) if eratos(x)]

while True:
    n = int(input())
    if not n:
        break
    print(len([x for x in prime_list if n < x <= 2*n]))
    # print(sum(list(map(lambda x: x>n and x<=2*n, prime_list))))