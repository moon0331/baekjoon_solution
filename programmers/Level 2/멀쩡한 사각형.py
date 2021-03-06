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

'''
from math import floor, ceil

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a

def solution(w, h):
    cropped = 0
    n = gcd(w, h)
    origin = w * h
    w, h = w // gcd(w, h), h // gcd(w, h)
    
    for i in range(h):
        x1, x2 = w / h * i, w / h * (i + 1)
        l, r = floor(x1), ceil(x2)
        cropped += r - l
    
    return origin - cropped * n
'''
# 부동소수점 이슈?