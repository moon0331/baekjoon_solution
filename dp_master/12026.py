N = int(input())
road = input()

dp = [float('inf') for _ in range(len(road))]
dp[0] = 0
prev_block = {'B': 'J', 'O': 'B', 'J': 'O'}

for i in range(1, len(road)):
    prev_steps = []
    for j in range(i):
        if road[j] == prev_block[road[i]] and dp[j] != -1:
            prev_steps.append(j)
    
    if prev_steps:
        for step in prev_steps:
            if dp[step] + ((i-step)**2) < dp[i]:
                dp[i] = dp[step] + ((i-step)**2)
    else:
        dp[i] = -1

print(dp[-1])