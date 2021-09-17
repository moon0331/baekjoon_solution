from collections import defaultdict, deque
import heapq

def DFS(g, airport_idx, route, len_tickets):
    stack = [0]
    len_airports = len(airport_idx)
    while stack:
        loc = stack.pop()
        for next_loc in range(len_airports+1):
            if next_loc in g[loc]:
                if g[loc][next_loc] > 0:
                    g[loc][next_loc] -= 1
                    stack.append(next_loc)
                    # route[next_loc] = loc
                    route[loc].append(next_loc)
                    # route[next_loc].append(loc)

    location = [0]
    len_location = 1
    next_route = route[0].popleft()
    while len_location <= len_tickets:
        location.append(next_route)
        len_location += 1
        if len_location == len_tickets + 1:
            break
        next_route = route[next_route].popleft()
    
    return location
            

def solution(tickets):
    airport_list = set()
    for ticket in tickets:
        airport_list.add(ticket[0])
        airport_list.add(ticket[1])
    airport_list = ['ICN'] + sorted(set(airport_list)-{'ICN'})
    airport_idx = {airport:i for i, airport in enumerate(airport_list)}
    
    route = {airport : deque() for airport in range(len(airport_list))}

    g = defaultdict(dict)
    for ticket in tickets:
        departure, arrival = (airport_idx[x] for x in ticket)
        if not arrival in g[departure]:
            g[departure][arrival] = 0
        g[departure][arrival] += 1

    location = DFS(g, airport_idx, route, len(tickets), start_idx)

    return [airport_list[x] for x in location]

    # return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]) == ["ICN", "B", "ICN", "A"])
# 알파벳순 DFS

# 런타임 에러??
# 인천과 연결된 모든 케이스 중 