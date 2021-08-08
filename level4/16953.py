from collections import deque

A, B = map(int, input().split())

q = deque([(A, 1)])
visited = set()
while q:
    val, n = q.popleft()
    for nextval in (2*val, 10*val+1):
        if not nextval in visited and 1<=nextval<=B:
            q.append((nextval, n+1))
            visited.add(nextval)
        if nextval == B:     
            print(n+1)
            exit(0)

print(-1)