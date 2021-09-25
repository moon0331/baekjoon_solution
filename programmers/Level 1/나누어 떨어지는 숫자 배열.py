def solution(arr, divisor):
    newarr = [x for x in arr if x%divisor == 0]
    return sorted(newarr) if newarr else [-1]

ior = [ [[5, 9, 7, 10], 5,  [5, 10]],
        [[2, 36, 1, 3], 1,  [1, 2, 3, 36]], 
        [[3, 2, 6],     10, [-1]]
]

for i, o, r in ior:
    print(solution(i, o) == r)