from itertools import permutations

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

for pair in permutations(sorted(numbers), M):
    print(*pair)