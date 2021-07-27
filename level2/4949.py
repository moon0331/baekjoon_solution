def isBalance(line):
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

import sys
import re

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    line = re.sub('[^()\[\]]', '', line)
    print('yes' if isBalance(line) else 'no')