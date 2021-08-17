import heapq

def solution(scoville, K):
    q = []
    for s in scoville:
        heapq.heappush(q, s)
    scov = 0
    cnt = 0
    while q:
        scov = heapq.heappop(q)
        if scov >= K:
            return cnt
        scov2 = heapq.heappop(q)
        heapq.heappush(q, scov + 2*scov2)
        cnt += 1
        
    return -1

scoville = list(map(int, input().split()))
K = int(input())
print(solution(scoville, K))