import heapq

def solution(jobs):
    answer = 0
    heapq.heapify(jobs)
    n_jobs = len(jobs)
    time = 0
    while jobs:
        job = heapq.heappop(jobs)
        if time >= job[0]:
            print(time, job, job[1] + time - job[0])
            answer += job[1] + time - job[0]
            time += job[1]
        else:
            heapq.heappush(jobs, job)
            time += 1
    answer /= n_jobs
    return int(answer)

print(solution([[0,3],[1,9],[2,6]]) == 9)