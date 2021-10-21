from collections import Counter

def factorize(x):
    arr = []
    d = 2
    while d <= x:
        if x % d == 0:
            arr.append(d)
            x /= d
        else:
            d += 1
    return arr

def solution(arr):
    cnt = Counter()
    for x in arr:
        x_cnt = Counter(factorize(x))
        for val in x_cnt:
            cnt[val] = max(cnt[val], x_cnt[val])

    val = 1
    for x in cnt:
        val *= x**cnt[x]

    return val

print(solution([2,6,8,14]) == 168)
print(solution([1,2,3]) == 6)

# 소인수분해 후 카운터 합집합