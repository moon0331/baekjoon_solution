def comp(pair):
    for i in range(len(pair)-1):
        if not pair[i] <= pair[i+1]:
            return False
    return True

from itertools import product

N, M = map(int, input().split())

arr = sorted(list(set(map(int, input().split()))))

for pair in product(arr, repeat=M):
    if comp(pair) == True:
        print(*pair)