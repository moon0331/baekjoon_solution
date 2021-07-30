from itertools import product

M, N = map(int, input().split())

for pair in product(*(range(1, M+1) for _ in range(N))):
    print(*pair)