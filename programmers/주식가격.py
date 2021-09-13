def solution(prices):

    total_time = len(prices)
    stack = []
    answer = [-1 for _ in range(total_time)]

    for t in range(total_time):

        val = prices[t]

        while stack and stack[-1][0] > val:
            popval = stack.pop()
            answer[popval[-1]] = t - popval[-1]

        stack.append((val, t))

    for i in range(total_time):
        if answer[i] == -1:
            answer[i] = t - i

    return answer

print(solution([1,2,3,2,3]) == [4,3,1,1,0])