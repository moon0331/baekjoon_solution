def nth(x):
    x = len(x)
    return int(x*(x+1)/2)

N = int(input())

for _ in range(N):
    txt = input().split('X')
    print(sum(map(nth, txt)))