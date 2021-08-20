def solution(money):
    l_house = len(money)
    dp = [0 for _ in range(l_house)] # 첫번째 집 O (마지막 집 못들름)
    dp2 = [0 for _ in range(l_house)] # 첫번째 집 X

    dp[0] = dp[1] = money[0]
    dp2[1] = money[1]

    for i in range(2, l_house):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
        dp2[i] = max(dp2[i-2]+money[i], dp2[i-1])
    answer = max(dp[-2], dp2[-1]) #dp는 마지막 집 못들른다고!
    return answer

print(solution([1,2,3,1]) == 4)

# dp 말고 변수 3개로 초기화 가능할듯