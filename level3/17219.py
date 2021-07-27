import sys

N, M = map(int, sys.stdin.readline().split())

pw_record = dict()

for _ in range(N):
    site, password = sys.stdin.readline().split()
    pw_record[site] = password

for _ in range(M):
    print(pw_record[sys.stdin.readline().strip()])