import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()

for _ in range(N):
    op = sys.stdin.readline().strip()
    if op.startswith('push'):
        val = int(op.split()[-1])
        q.append(val)
    elif op == 'pop':
        print(q.popleft() if len(q) != 0 else -1)
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        print(1 if len(q) == 0 else 0)
    elif op == 'front':
        print(q[0] if len(q) != 0 else -1)
    elif op == 'back':
        print(q[-1] if len(q) != 0 else -1)