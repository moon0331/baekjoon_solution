def solution(d, budget):
    d.sort()
    answer = 0
    val = 0
    for i in range(len(d)):
        if val + d[i] > budget:
            return answer
        val += d[i]
        answer += 1
    return answer

print(solution([1,3,2,5,4], 9) == 3)
print(solution([2,2,3,3], 10) == 4)