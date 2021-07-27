import sys

A, B, C = map(int, sys.stdin.readline().split())

if C>B:
    print(A//(C-B)+1)
else:
    print(-1)

'''
A + Bx < Cx
A < (C-B)x
A/(C-B) < x
'''