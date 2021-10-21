def solution(A,B):
    A.sort(reverse=True)
    B.sort()
    return sum(a*b for a, b in zip(A, B))

print(solution([1,4,2], [5,4,4]) == 29)
print(solution([1,2], [3,4]) == 10)

# why?