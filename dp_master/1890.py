# q = deque([(0, 0)])
# while q:
#     i, j = q.popleft()
#     n_way = game[i][j]
#     for newi, newj in ((i+n_way, j), (i, j+n_way)):
#         if newi >= N or newj >= N:
#             continue
#         dp[newi][newj] += 1
#         if game[newi][newj]:
#             q.append((newi, newj))

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
	for j in range(N):
		if not dp[i][j] or i==j==N-1:
			continue
		newstep = game[i][j]
		if i+newstep < N:
			dp[i+newstep][j] += dp[i][j]
		if j+newstep < N:
			dp[i][j+newstep] += dp[i][j]

print(dp[-1][-1])
			

# 오른쪽이나 아래로만 가는걸로 고정되어 있으니 queue 안돌리고 걍 반복문 처리해도 되나보다
# queue 메모리 초과