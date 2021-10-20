from collections import Counter

def solution(n):
    return Counter(bin(n))['1']

answer = [(5, 2), (6, 2), (5000, 5)]

for x, y in answer:
    print(solution(x) == y)