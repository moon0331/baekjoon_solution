from collections import defaultdict
import heapq

def solution(tickets):
    g = defaultdict(list)
    for ticket in tickets:
        dep, arriv = ticket
        heapq.heappush(g[dep], arriv)

    stack = ['ICN']
    location = []
    while stack:
        airport = stack[-1]
        if g[airport]:
            stack.append(heapq.heappop(g[airport]))
        else:
            location.append(stack.pop())

    location.reverse()

    return location

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]) == ["ICN", "B", "ICN", "A"])
# 알파벳순 DFS

# 런타임 에러??
# 인천과 연결된 모든 케이스 중 