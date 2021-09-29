from math import ceil, trunc

def solution(w,h):
    ans = 0
    thr = 0
    flr = 0
    slope = h/w
    for i in range(w):
        thr += slope
        ans += ceil(thr)-flr
        flr = trunc(thr)
        print(thr, flr, ans)

    return w*h-ans

print(solution(8, 12) == 80)

# 같은 상황 생기면 곱셈 처리