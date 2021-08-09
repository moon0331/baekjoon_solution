import sys
from collections import deque

N = int(sys.stdin.readline().split())

q = deque()
for _ in range(N):
    cmd = sys.stdin.readline().split()