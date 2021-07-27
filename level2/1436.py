N = int(input())

i = 0
ans = 665
while True:
    ans += 1
    if '666' in str(ans):
        i += 1
        if i == N:
            break

print(ans)