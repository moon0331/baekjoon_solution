import sys
A, B = map(int, sys.stdin.readline().split())

if A>B:
    ans = '<'
elif A<B:
    ans = '>'
else:
    ans = '=='

print(ans)