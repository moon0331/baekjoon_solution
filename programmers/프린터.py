from collections import deque

def solution(priorities, location):
    q = deque([(x, i) for i, x in enumerate(priorities)])
    idx = 0

    while q:
        max_pr = max([x for x, y in q])
        doc = q.popleft()
        if doc[0] == max_pr:
            idx += 1
            if doc[1] == location:
                return idx
        else:
            q.append(doc)

    return idx
 
print(solution([2,1,3,2], 2) == 1)
print(solution([1, 1, 9, 1, 1, 1], 0) == 5)