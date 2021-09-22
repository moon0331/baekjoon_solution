def solution(numbers):
    return 45-sum(numbers)

ns = [[1,2,3,4,6,7,8,0], [5,8,4,0,6,7,9]]
rs = [14, 6]

for n, r in zip(ns, rs):
    print(solution(n) == r)