n, m = map(int, input().split())
name_length_list = [int(input()) for _ in range(n)]

remaining_space = 20
score = 0
for i in range(n):
    if remaining_space >= name_length_list[i] + 1:
        if remaining_space != 20:
            remaining_space -= 1
        remaining_space -= name_length_list[i]
    else:
        score += remaining_space ** 2
        remaining_space = 20 - name_length_list[i]
    
    print(i, name_length_list[i], remaining_space, score)

print(score)


'''
dp[i]
- 자리가 있으면, 무조건 낑겨넣는게 최소
- 자리가 없으면, 무조건 줄 띄워야 함

그러면 안됨

dp[i][j]
i개의 이름, j줄 사용
j의 제약조건 확인해보기

가로칸 1<=m<=1000, 이름 1<=n<=1000이므로
i==
'''

