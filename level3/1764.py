import sys

N, M = map(int, sys.stdin.readline().split())

not_heard = []
not_seen = []

for _ in range(N):
    not_heard.append(sys.stdin.readline().strip())

for _ in range(M):
    not_seen.append(sys.stdin.readline().strip())

neither_heard_nor_seen = set(not_heard).intersection(not_seen)

print(len(neither_heard_nor_seen))
print(*sorted(neither_heard_nor_seen), sep='\n')