def solution(nums):
    return min(len(nums)//2, len(set(nums)))

ns = [[3,1,2,3], [3,3,3,2,2,4], [3,3,3,2,2,2]]
rs = [2, 3, 2]

for n, r in zip(ns, rs):
    print(solution(n) == r)