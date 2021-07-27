import sys

def try_int(x):
    try:
        return int(x)
    except:
        return str(x)

N = int(sys.stdin.readline())

namelist = []

for _ in range(N):
    namelist.append(tuple(map(try_int, sys.stdin.readline().split())))

namelist.sort(key=lambda x: x[0])

for name in namelist:
    print(*name)

#python sort is stable!