def solution(n):
    return sum(map(int, str(n)))

print(solution(123) == 6)
print(solution(987) == 24)