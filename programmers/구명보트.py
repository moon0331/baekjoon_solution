from collections import Counter

def solution(people, limit):
    cnt = Counter(people)
    print(cnt)
    print(sorted(cnt))

print(solution([70,50,80,50], 100) == 3)
print(solution([70,80,50], 100) == 3)