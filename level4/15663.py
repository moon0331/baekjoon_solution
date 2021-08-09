from itertools import permutations

M, N = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans = sorted(list(set(permutations(arr, N))))

for pair in ans:
    print(*pair)