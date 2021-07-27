import sys
from collections import defaultdict

n_testcase = int(sys.stdin.readline())

for _ in range(n_testcase):
    wardrobe = defaultdict(int)
    n = int(sys.stdin.readline())
    for _ in range(n):
        _, x = sys.stdin.readline().split()
        wardrobe[x] += 1
    values = [wardrobe[x]+1 for x in wardrobe]
    ans = 1
    for val in values:
        ans *= val
    print(ans-1)