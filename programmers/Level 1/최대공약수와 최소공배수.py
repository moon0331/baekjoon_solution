def solution(n, m):
    if n > m: 
        n, m = m, n

    gcd = 1
    for i in range(1, n//2+1):
        div = n/i
        print(n, i, div)
        if int(n/i) == n/i and m%div == 0:
            gcd = div
            break
    print(gcd, n*m/gcd)
    return [int(gcd), int(n*m/gcd)]

print(solution(3, 12) == [3, 12])
print(solution(2, 5) == [1, 10])