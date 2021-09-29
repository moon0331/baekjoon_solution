def solution(n):
    arr = []
    while n:
        arr.append(n%3)
        n = n//3
    
    return "".join(map(str, arr[::-1]))

for i in range(1, 11):
    print(solution(i))