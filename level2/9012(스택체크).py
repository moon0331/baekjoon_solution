import sys

def isStack(line):
    stack = []
    for c in line.strip():
        if c in '([':
            stack.append(c)
        else: #')]'
            if len(stack)==0:
                stack.append(c)
            else:
                if stack[-1]+c in ('()', '[]'):
                    stack.pop()
                else:
                    return False
    if not stack:
        return True
    else:
        return False

N = int(input())
for _ in range(N):
    print('YES' if isStack(sys.stdin.readline().strip()) else 'NO')