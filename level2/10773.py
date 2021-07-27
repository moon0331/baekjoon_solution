import sys

K = int(input())

num_list = []

for _ in range(K):
    val = int(sys.stdin.readline())
    if val:
        num_list.append(val)
    else:
        num_list.pop()

print(sum(num_list))
