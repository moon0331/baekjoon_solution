import math 
from itertools import combinations

def prime(x):
    if x == 2: 
        return True
    end = int(math.sqrt(x))
    for i in range(2, end+1):
        if x%i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    for ns in combinations(nums, 3):
        if prime(sum(ns)):
            answer += 1

    return answer

print(solution([1,2,3,4]) == 1)
print(solution([1,2,7,6,4]) == 4)