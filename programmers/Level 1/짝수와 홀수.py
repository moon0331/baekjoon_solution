def solution(num):
    return ('Even', 'Odd')[num%2]

print(solution(3) == 'Odd')
print(solution(4) == 'Even')