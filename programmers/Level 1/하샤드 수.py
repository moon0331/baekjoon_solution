def solution(x):
    return x%sum(map(int, str(x))) == 0

print(solution(10) == True)
print(solution(12) == True)
print(solution(11) == False)
print(solution(13) == False)