import sys
from collections import deque

def f(num, op): # 숫자 처리 다시해보기 (+- 버튼 누른 다음에는 숫자 안누르게)
    if op == '+':
        return num + 1
    elif op == '-':
        return num - 1 if num else 0
    else:
        return num * 10 + op

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken_button = set(map(int, sys.stdin.readline().split()))
possible_button = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-'} - broken_button)

q = deque([(100, 0)])
visited = set([100])

while q:
    channel, nth = q.popleft()
    for next_button in possible_button:
        next_channel = f(channel, next_button)  
        #print(next_channel)      
        if next_channel == N:
            print(nth+1)
            exit(0)
        if not next_channel in visited and 0 <= channel <= 500000:
            visited.add(next_channel)
            q.append((next_channel, nth+1))

print(-1)