from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque([[x, y] for x, y in zip(progresses, speeds)])

    while q:
        for i in range(len(q)):
            q[i][0] += q[i][1]
        
        n_pop = 0
        while q and q[0][0] >= 100:
            q.popleft()
            n_pop += 1

        if n_pop:
            answer.append(n_pop)

    return answer

def another_solution(progresses, speeds):

    def cal_time(progress, speed):
        '''
        progress + x*speed >= 100
        x*speed >= 100-progress
        x * >= (100-progress)/speed
        '''
        return math.ceil((100-progress)/speed)
    
    times = [cal_time(p, s) for p, s in zip(progresses, speeds)]
    
    answer = []

    n = 0
    val = times[0]
    for i in range(len(times)):
        if val >= times[i]:
            n += 1
        else:
            answer.append(n)
            n = 1
            val = times[i]
    else:
        answer.append(n)
        
    return answer



print(solution([93, 30, 55], [1, 30, 5]) == [2, 1])
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2])
print(another_solution([93, 30, 55], [1, 30, 5]) == [2, 1])
print(another_solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2])