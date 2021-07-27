# 터렛

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    rsum_sq, rdiff_sq = (r1+r2)**2, (r1-r2)**2
    d_sq = (x2-x1)**2 + (y2-y1)**2

    if d_sq == 0:
        if rdiff_sq == 0:
            print(-1)
        else:
            print(0)
    else:
        if rdiff_sq == d_sq or rsum_sq == d_sq:
            print(1)
        elif rdiff_sq < d_sq and rsum_sq > d_sq:
            print(2)
        else:
            print(0)