def isPrime(x):
    if x == 1:
        return False
    th = int(x**0.5)
    for i in range(2, th+1):
        if x%i == 0:
            return False
    return True

def solution(n):
    return len([x for x in range(1, n+1) if isPrime(x)])

print(solution(10) == 4)
print(solution(5) == 3)

'''
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''