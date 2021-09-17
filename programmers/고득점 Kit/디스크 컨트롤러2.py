import heapq
from collections import deque

def solution(jobs):
    jobs.sort()
    n_done, n_jobs = 0, len(jobs)
    jobs = deque(jobs)
    h = []
    t = 0
    answer = 0
    while n_done < n_jobs:
        while jobs and t >= jobs[0][0]:
            t_start, l_work = jobs.popleft()
            # print(t, 'push', (t_start, l_work))
            heapq.heappush(h, (l_work, t_start)) # why optimal?
        if h:
            l_current_work, t_current_work_start = heapq.heappop(h)
            # print(t, 'do', (l_current_work, t_current_work_start))
            t += l_current_work
            answer += t - t_current_work_start
            # print(t-t_current_work_start, 'add')
            n_done += 1
        else:
            t += 1

    # print(answer, n_jobs)
    return int(answer/n_jobs)

print(solution([[0,3],[1,9],[2,6]]) == 9)
print(solution([[0, 3], [4, 3], [10, 3]]) == 3)              # 3
print(solution([[0, 10], [2, 3], [9, 3]]) == 9)              # 9
print(solution([[1, 10], [3, 3], [10, 3]]) == 9)             # 9
print(solution([[0, 10]]) == 10)                              # 10
print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]) == 15)   # 15
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]) == 74)   # 74
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]) == 74)   # 74


# 파트 나눠서 다시 해보기
# 일단 스케줄러에 넣는 것부터
# 그다음 실행시키는 것
# 따로 구현해보기