def solution(n):
    x = y = 1
    cnt = 0
    while x<=n and y<=n+1:
        val = sum(range(x, y))
        if val < n:
            y += 1
        elif val > n:
            x += 1
        else:
            cnt += 1
            x += 1
    return cnt

print(solution(15) == 4)