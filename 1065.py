def isComminDiff(x): #string x
    y = list(set(list(map(lambda x: int(x[0])+int(x[1]), list(zip(x, reversed(x)))))))
    return len(y) == 1

N = int(input())
if N < 100:
    print(N)
else:
    cnt = 99
    for val in range(100, N+1):
        if isComminDiff(str(val)):
            cnt += 1
    print(cnt)

    