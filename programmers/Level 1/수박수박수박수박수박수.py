def solution(n):
    return '수박'*(n//2) + ('수' if n%2 else '') # '수'*(n%2)

print(solution(3) == '수박수')
print(solution(4) == '수박수박')