import sys
from collections import deque

T = int(sys.stdin.readline())

def D(x):
    return 2*x % 10000

def S(x):
    return x-1 if x else 9999

def L(x):
    return x%1000*10 + x//1000

def R(x):
    return x//10 + x%10*1000

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    q = deque([(A, '')])
    visited = set()
    while q:
        d, op = q.popleft()
        visited.add(d)
        if d == B:
            break
        for f, newop in zip((D, S, L, R),'DSLR'):
            val = f(d)
            if not val in visited:
                visited.add(val)
                q.append((val, op+newop))
    print(op)