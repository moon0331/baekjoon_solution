from itertools import permutations
import math

def isPrime(x):
    if x == 1 or x == 0: return False
    sqrt_x = int(math.sqrt(x))
    for i in range(2, sqrt_x+1):
        if x % i == 0:
            return False
    return True

def calNumOfPrime(numbers, l, already_checked):
    n_prime = 0
    for num_tuple in permutations(numbers, l):
        num = int("".join(num_tuple))
        if num in already_checked:
            continue
        if isPrime(int(num)):
            n_prime += 1
        already_checked.append(num)
    return n_prime

def solution(numbers):
    n_prime = 0 
    already_checked = []
    for l in range(1, len(numbers)+1):
        n_prime += calNumOfPrime(numbers, l, already_checked)
    return n_prime

print(solution("011"))