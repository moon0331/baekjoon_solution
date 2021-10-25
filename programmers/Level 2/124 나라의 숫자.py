def solution(n):
    if n <= 0:
        return ''
    else:
        mod = n%3 if n%3 else 3
        return solution((n-mod)//3) + '0124'[mod]

for i in range(1, 11):
    print(i, solution(i))