N, S, M = map(int, input().split())
V = list(map(int, input().split()))

volume_set = {-1:{S}}
for i in range(N):
	volume_set[i] = {pv + V[i] for pv in volume_set[i-1] if pv+V[i] <= M} | {pv - V[i] for pv in volume_set[i-1] if pv-V[i] >= 0}
	# print(volume_set[i])

print(max(volume_set[N-1]) if volume_set[N-1] else -1) 