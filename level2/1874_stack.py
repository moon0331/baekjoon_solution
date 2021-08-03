import sys

n = int(sys.stdin.readline())

cnt = 0
stack = []
result=''

for _ in range(n):
    x = int(sys.stdin.readline())
    while cnt < x:
        cnt += 1
        stack.append(cnt)
        result += '+'
    
    if stack[-1] == x:
        stack.pop()
        result += '-'
    else:
        print('NO')
        exit(0)

for c in result:
    print(c)
