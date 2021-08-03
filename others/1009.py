import sys

answer_dict = {
    0 : [10],
    1 : [1],
    2 : [2, 4, 8, 6],
    3 : [3, 9, 7, 1],
    4 : [4, 6],
    5 : [5],
    6 : [6],
    7 : [7, 9, 3, 1],
    8 : [8, 4, 2, 6],
    9 : [9, 1]
}

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    t = y%len(answer_dict[x%10])
    print(answer_dict[x%10][t-1])
