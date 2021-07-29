N = int(input())

adj = []

for _ in range(N):
    adj.append([x if x != 0 else float('inf') 
                for x in list(map(int, input().split()))])

for k in range(N):
    for i in range(N):
        for j in range(N):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for row in adj:
    print(*(1 if c != float('inf') else 0 for c in row))