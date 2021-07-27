from collections import deque

N = int(input())

q = deque()

q.extend(range(1, N+1))

for i in range(N-1): # N-1번 하면 하나만 남음
    q.popleft()
    c = q.popleft()
    q.append(c)

print(q[0])