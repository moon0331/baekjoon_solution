'''
a층의 b호에 살려면 
자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 
사람들을 데려와 살아야 한다
'''

apart=[list(range(15))]
apart.extend([[0]*15 for _ in range(14)]) #15 by 15

for floor in range(1, 15):
    for room in range(1,15):
        apart[floor][room] = sum(apart[floor-1][:room+1])

# for rev in range(14, -1, -1):
#     print(apart[rev])

T = int(input())

for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    print(apart[k][n])
