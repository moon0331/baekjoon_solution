import sys

K, N = map(int, sys.stdin.readline().split())

lans = []
for _ in range(K):
    lans.append(int(sys.stdin.readline()))

left, right = 1, max(lans) #not min !!!!!!!!!!!

result = 0

while left <= right:
    center = (left+right)//2 # 기준값
    cut_sum = sum([lan//center for lan in lans]) # 기준값에 따른 결과
    if cut_sum >= N: # 얘가 만족하면
        left = center + 1 # 기준을 다시 정하기 위해 left 재설정 (오른쪽 절반에서 서치)
        result = center
    else:
        right = center - 1 # 기준을 다시 정하기 위해 RIGHT 재설정 (오른쪽 절반에서 서치)

print(result)