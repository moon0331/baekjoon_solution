def solution(n, lost, reserve):
    available = [0] + [1 for _ in range(n)]
    for l in lost:
        available[l] -= 1
    for r in reserve:
        available[r] += 1
    
    for i in range(1, n+1):
        if available[i] == 2:
            if i-1 >= 1 and not available[i-1]:
                available[i-1] += 1
                available[i] -= 1
            elif i+1 <= n and not available[i+1]:
                available[i+1] += 1
                available[i] -= 1
    
    return sum(True for val in available if val)
                

ns = [5, 5, 3, 5]
losts = [[2,4], [2,4], [3], [3,4]]
reserves = [[1,3,5], [3], [1], [2,4]]
returns = [5, 4, 2, 5]

for n, l, res, ret in zip(ns, losts, reserves, returns):
    print(solution(n, l, res) == ret)