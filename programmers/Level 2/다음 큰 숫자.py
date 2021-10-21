from collections import Counter

def solution(n):
    n_ones = Counter(bin(n))['1']
    cnt = 0
    while True:
        cnt += 1
        if Counter(bin(n+cnt))['1'] == n_ones:
            return n+cnt

print(solution(78) == 83)
print(solution(15) == 23)