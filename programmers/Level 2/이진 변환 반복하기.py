from collections import Counter

def solution(s):
    n_transform = n_zero = 0
    while s != '1':
        # remove 0
        # change into binary
        cnt = Counter(s)
        s = bin(cnt['1'])[2:]
        n_transform += 1
        n_zero += cnt['0']
        # counting 
    return [n_transform, n_zero]

xy = [("110010101001", [3, 8]), ("01110", [3, 3]), ("1111111", [4,1])]

for x, y in xy:
    print(solution(x) == y)

