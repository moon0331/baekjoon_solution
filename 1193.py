# X = int(input())
'''
n = 0

for X in range(1, 101):
    while n*(n+1)/2<X:
        n += 1
    idx = int(X-n*(n-1)/2)
    bunja = idx
    bunmo = n+1-idx
    if n%2 == 1:
        bunja, bunmo = bunmo, bunja
    print('{}/{}'.format(bunja, bunmo))

'''

# 최소한도 찾은 후
# 플러스 몇

n = 0
X = int(input())
while n*(n+1)/2<X:
    n += 1
idx = int(X-n*(n-1)/2)
bunja = idx
bunmo = n+1-idx
if n%2 == 1:
    bunja, bunmo = bunmo, bunja
print('{}/{}'.format(bunja, bunmo))