def solution(num):
    if num == 1:
        return 0
        
    ans = -1
    for i in range(500):
        if num%2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        if num == 1:
            return i+1
    return ans

print(solution(6) == 8)
print(solution(16) == 4)
print(solution(626331) == -1)