'''
101 ~ H층01
102 ~ H층02
-> 층을 나타내는 것은 N % H

H번 1번방
H번 2번방
-> 방번호를 나타내는 것은 N // H + 1
'''


T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N%H if N%H else H
    doornum = N//H+1 if N%H else N//H
    print(floor*100+doornum)