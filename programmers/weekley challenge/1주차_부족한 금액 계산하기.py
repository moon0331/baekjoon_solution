def solution(price, money, count):
    return max(price * count * (count+1) / 2 - money, 0)

print(solution(3, 20, 4) == 10)