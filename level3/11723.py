import sys

M = int(sys.stdin.readline())

S = set()
for _ in range(M):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:
        val = int(cmd[1])
    if cmd[0] == 'all':
        S = set(range(1, 21))
    elif cmd[0] == 'empty':
        S = set()
    elif cmd[0] == 'add':
        S.add(val)
    elif cmd[0] == 'remove':
        if val in S:
            S.remove(val) # discard
    elif cmd[0] == 'check':
        print(1 if val in S else 0)
    elif cmd[0] == 'toggle':
        if val in S:
            S.remove(val)
        else:
            S.add(val)