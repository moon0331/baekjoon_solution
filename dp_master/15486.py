import sys

N = int(sys.stdin.readline())
T = []
P = []
val = []

for _ in range(N):
    tval, pval = map(int, sys.stdin.readline().split())
    T.append(tval)
    P.append(pval)

val[0] = P[0]

for i in range(1, N):
    # DP 계산
    P[i] = 1