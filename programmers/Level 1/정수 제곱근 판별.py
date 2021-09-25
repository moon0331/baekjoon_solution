def solution(n):
    sqrt = n**0.5
    return int((sqrt+1)**2) if sqrt == int(sqrt) else -1

print(solution(121) == 144)
print(solution(3) == -1)