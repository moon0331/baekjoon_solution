import math

def isPrime(x):
    if type(x) == str:
        x = int(x)
    if x<2:
        return False
    val = int(math.sqrt(x))
    for i in range(2, val+1):
        if x % i == 0:
            return False
    return True


N = int(input())

primes = {x:[] for x in range(1,N+1)}

ones = ['2', '3', '5', '7']
primes[1] = ones

for i in range(1, N):
    # print(i, '번째에서', i+1, '번째로 확장')
    for prefix in primes[i]:
        for sub in map(str, (1, 3, 7, 9)):
            newnum = prefix+sub
            if isPrime(newnum):
                primes[i+1].append(newnum)

for prime in primes[N]:
    print(prime)

'''

2 + 2,3,5,7
    소수이면 저장
    아니면 말고



'''