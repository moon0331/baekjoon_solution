def solution(N, stages): # stages : user별 최종 깨지 못한 단계
    n_user = len(stages)
    n_success = {i:0 for i in range(1, N+1)} # 단계 : 성공한 수
    for s in stages:
        for i in range(1, s):
            n_success[i] += 1

    for i in range(1, N+1):
        if n_user <= 0:
            n_success[i] = 0
        else:
            n_fail = n_user - n_success[i]
            n_success[i] = n_fail/n_user
            n_user -= n_fail

    return [x for x, _ in sorted(n_success.items(), key=lambda x:x[1], reverse=True)]
    

print(solution(5, [2,1,2,6,2,4,3,3]) == [3,4,2,1,5])
print(solution(4, [4,4,4,4,4]) == [4,1,2,3])
print(solution(5, [2,2,2,2,2]))