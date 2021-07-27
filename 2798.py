from itertools import combinations

N, M = map(int, input().split())
card = input().split()

# card.sort()

answer = -1

for val in combinations(card, 3):
    sumval = sum(map(int, val))
    if answer < sumval and sumval <= M:
        answer = sumval

print(answer)