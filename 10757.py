'''
1 : 1                   1

2 : 1 1                 2

3 : 1 1 1               3
4 : 1 2 1               3

5 : 1 2 1 1             4
6 : 1 2 2 1             4

7 : 1 2 2 1 1           5
8 : 1 2 2 2 1           5
9 : 1 2 3 2 1           5

10 : 1 2 3 2 1 1        6
11 : 1 2 3 2 2 1        6
12 : 1 2 3 3 2 1        6

13 : 1 2 3 3 2 1 1      7
14 : 1 2 3 3 2 2 1      7
15 : 1 2 3 3 3 2 1      7
16 : 1 2 3 4 3 2 1      7

17 : 1 2 3 4 3 2 2 1    8
18
19
20                      8

{2, 6, 12, 20, }
n번째 항 : n * (n+1) -> 2n이 나올 수 있는 최대 이동 수
1번째 항 : 2 -> 2가 나올 수 있는 최대 이동수
2번째 항 : 6 -> 4가 나올 수 있는 최대 이동수

{1, 4, 9, 16, 25, }
n번째 항 : n**2 -> 2n-1이 나올 수 있는 최대 이동 수


1 -> 1 1
2 -> 2 1
'''

def distance(x):        # 인풋 거리
    n = 0
    while n**2 < x:
        n += 1
    center = n ** 2     # 2n-1 회 가 나오는 최대 거리
    right = n ** 2 + n  # 
    #print('{} | center = {}, right = {}'.format(x, center, right))
    # left ~ center ; 2n-1회
    # center+1 ~ right : 2n회
    print(x)
    print(center)
    if center < x:
        print('거리 {} - {}'.format(x, 2 * n))
    else:
        print('거리 {} - {}'.format(x, 2 * n - 1))


# T = int(input())
# x, y = map(int, input().split())

# print(distance(y-x))

for i in range(1, 45):
    distance(i)