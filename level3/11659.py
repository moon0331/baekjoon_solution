import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
pre_sum = [0 for _ in range(len(arr)+1)]
val = 0

for i, e in enumerate(arr):
    val += e
    pre_sum[i+1] = val

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(pre_sum[j]-pre_sum[i-1])