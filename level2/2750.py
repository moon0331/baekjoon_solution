N = int(input())

lst = []

for i in range(N):
    lst.append(int(input()))

for i in range(N):
    for j in range(i,N):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for e in lst:
    print(e)