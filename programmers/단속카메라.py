def solution(routes):
    routes.sort(key=lambda x:x[0])
    print(routes)
    answer = 0
    x, y = routes[0]
    for next_x, next_y in routes[1:]:
        if y < next_x:
            print(x, y, '<', next_x, next_y)
            answer += 1
            x, y = next_x, next_y

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]) == 2)