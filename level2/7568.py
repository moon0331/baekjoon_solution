import sys

rank = []

N = int(sys.stdin.readline())

for i in range(1, N+1):
    x, y = map(int ,sys.stdin.readline().split())
    rank.append((x,y))

ranking = [1 for _ in range(len(rank))]

for i in range(N):
    for j in range(N):
        if i == j: continue
        if rank[i][0] < rank[j][0] and rank[i][1] < rank[j][1]:
            ranking[i] += 1

print(*ranking)