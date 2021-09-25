def solution(a, b):
    if a>b:
        a, b = b, a
    return sum(range(a, b+1))

print(solution(3, 5) == 12)
print(solution(3, 3) == 3)
print(solution(5, 3) == 12)