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

print(solution(12,8))