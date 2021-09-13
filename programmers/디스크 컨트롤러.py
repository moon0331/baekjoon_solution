from collections import deque
import heapq

def solution(jobs):
    jobs.sort(key=lambda x:x[0]) # (들어오는 시간, 일 걸리는 시간)
    jobs = deque(jobs)
    print(jobs)

    t = 0
    n_done = 0
    n_jobs = len(jobs)

    h = []
    idle = True
    total_time = 0
    end_time = -1
    while n_done < n_jobs:
        print(t, n_done)
        # schedule input
        if t == end_time:
            idle = True
            n_done += 1

        if jobs and t >= jobs[0][0]:
            t_input, l_work = jobs.popleft()
            print('l_work =', l_work, '| t_input =', t_input, 'input')
            heapq.heappush(h, (l_work, t_input)) # (일 걸리는 시간, 들어오는 시간)

        if idle and h:
            ll, tt = heapq.heappop(h)
            print((ll, tt), 'work start at time', t)
            total_time += t - tt + ll
            end_time = t + ll
            idle = False
        t += 1
    print('ans = ', total_time, n_jobs)
    return int(total_time/n_jobs)

# print(solution([[0,3],[1,9],[2,6]]) == 9)
print(solution([[0, 3], [4, 3], [10, 3]]) == 3)              # 3
# print(solution([[0, 10], [2, 3], [9, 3]]) == 9)              # 9
# print(solution([[1, 10], [3, 3], [10, 3]]) == 9)             # 9
# print(solution([[0, 10]]) == 10)                              # 10
# print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]) == 15)   # 15
# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]) == 74)   # 74
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]) == 74)   # 74


# 파트 나눠서 다시 해보기
# 일단 스케줄러에 넣는 것부터
# 그다음 실행시키는 것
# 따로 구현해보기