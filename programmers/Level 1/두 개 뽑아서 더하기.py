from itertools import combinations

def solution(numbers):
    return sorted(list(set(x+y for x, y in combinations(numbers, 2))))

print(solution([2,1,3,4,1]) == [2,3,4,5,6,7])
print(solution([5,0,2,7]) == [2,5,7,9,12])