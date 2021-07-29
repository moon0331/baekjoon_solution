import sys
from collections import defaultdict

cnt = {i:0 for i in range(1, 10001)}

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    cnt[int(sys.stdin.readline())] += 1

for k in cnt:
    for _ in range(cnt[k]):
        print(k)