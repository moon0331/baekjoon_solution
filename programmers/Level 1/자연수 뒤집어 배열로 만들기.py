def solution(n):
    return list(map(int, reversed(str(n)))) # [::-1]

print(solution(12345) == [5,4,3,2,1])