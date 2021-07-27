# 회의실 배정

import sys

N = int(sys.stdin.readline())

timetable = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    timetable.append((x, y))

timetable.sort(key=lambda x:(x[1], x[0])) # why (x[1], x[0]) ?

n_time = 0
end_time = 0
for i in range(len(timetable)):
    if end_time <= timetable[i][0]:
        n_time += 1
        end_time = timetable[i][1]

print(n_time)

'''
다음 테스트 케이스에 대비해야합니다.
2
10 10
1 10
만약 끝나는 시간만 정렬한다면 (10 10)이 선택된다면 (1 10)은 선택되지 못해서 결과는 1이 나올 것입니다.
시작 하는 시간의 오름 차순으로 정렬되야 (1 10) -> (10 10) 을 선택하여 2가 나올 것입니다.
'''