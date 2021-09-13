data = [6]
n = len(data)
m = 5

cnt = 0
interval_sum = 0
end = 0

for start in range(n):
    print('start =', start)
    while interval_sum < m and end < n:
        print('{}+={}'.format(interval_sum, data[end]))
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        print('{}=={}'.format(interval_sum, m))
        cnt += 1
    interval_sum -= data[start]

print(cnt)