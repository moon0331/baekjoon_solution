N = int(input())
val = N


cnt = 0
while True:
    # 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
    # no op need as N is int
    sumval = int(val/10) + val % 10
    val = (val%10) * 10 + sumval % 10
    cnt += 1
    if val == N:
        break
print(cnt)