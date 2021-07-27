N = int(input())
A = list(map(int, input().split()))
M = int(input())
values = list(map(int, input().split()))
in_value = {value:False for value in values}

A.sort()
values_sorted = sorted(values)

i = j = 0
while i < N and j < M:
    try:
        while A[i] < values_sorted[j]:
            i += 1
    except IndexError:
        for jdx in range(j, M):
            in_value[values_sorted[jdx]] = False
        break
    if A[i] == values_sorted[j]:
        in_value[values_sorted[j]] = True
    else:
        in_value[values_sorted[j]] = False
    j += 1

for k in values:
    print(1 if in_value[k] else 0)