import sys
from collections import deque

def EmptyError(Exception):
    def __init__(self):
        super.__init__(self)

def cal():
    reverse = False
    try:
        p = sys.stdin.readline().strip()
        n = int(sys.stdin.readline())
        arr_str = sys.stdin.readline().strip()[1:-1]
        if arr_str == '':
            arr=[]
        else:
            arr = deque(map(int, arr_str.split(',')))
        for f in p:
            if f == 'R':
                reverse = not reverse
            elif f == 'D':
                if not reverse:
                    arr.popleft()
                else:
                    arr.pop()
    except:
        return 'error'
    arr = [str(x) for x in arr]
    if reverse:
        arr = arr[::-1]
    return '[{}]'.format(",".join(arr))

T = int(sys.stdin.readline())

for _ in range(T):
    print(cal())