import sys
from collections import deque

# (idx, priority)의 tuple로 생각

n_test = int(sys.stdin.readline())

for _ in range(n_test):
    N, M = map(int, sys.stdin.readline().split()) # 문서 수, 처음 인덱스가 몇번째 출력되니?
    priority = [(i, x) for i, x in enumerate(list(map(int, sys.stdin.readline().split())))]
    q = deque(priority)
    ans = 0
    while True:
        max_priority = max(x[1] for x in q)
        while q[0][1] != max_priority:
            q.append(q.popleft())
        popped = q.popleft()
        # print(popped, "popped")
        ans += 1
        if popped[0] == M:
            break
        # max 나올때까지 뽑고 넣음
    print(ans)