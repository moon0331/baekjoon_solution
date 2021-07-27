from collections import Counter

A = int(input())
B = int(input())
C = int(input())
val = A*B*C

cnt = Counter(map(int,str(val)))
for i in range(10):
    try:
        print(cnt[i])
    except:
        print(0)