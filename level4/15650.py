from itertools import combinations

N, M = map(int, input().split())

arr = combinations(range(1, N+1), M)

for element in arr:
    print_val = True
    prev = 0
    for x in element:
        if prev > x:
            print_val = False
            break
    if print_val:
        print(*element)