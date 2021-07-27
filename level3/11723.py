# 집합

import sys

M = int(sys.stdin.readline())

S = set()
for _ in range(M):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        if cmd == 'all':
            S = set(range(1, 21))
        elif cmd == 'empty':
            S = set()
    else:
        if cmd[0] == 'add':
            S.add(cmd[1])
        elif cmd[0] == 'remove':
            if cmd[1] in S:
                S.remove(cmd[1])
        elif cmd[0] == 'check':
            print(1 if cmd[1] in S else 0)
        elif cmd[0] == 'toggle':
            if cmd[1] in S:
                S.remove(cmd[1])
            else:
                S.add(cmd[1])