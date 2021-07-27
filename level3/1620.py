import sys

N, M = map(int, sys.stdin.readline().split())

name_to_num = dict()
num_to_name = ['error']

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    name_to_num[name] = i
    num_to_name.append(name)

for _ in range(M):
    query = sys.stdin.readline().strip()
    if query.isdigit():
        print(num_to_name[int(query)])
    else:
        print(name_to_num[query])