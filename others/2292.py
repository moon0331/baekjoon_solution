'''
1 : 1
2 : 2 ~ 7 (6)
3 : 8 ~ 19 (12)
4 : 20 ~ 37 (18)
5 : 38 ~ 61 (24)
'''

'''
58 - 1 = 57
57 / 6 = 9.x
1+2+3+4 > 10

4+1

ans(ans+1)/2 > (N-1)/6
ans(ans+1) > (N-1)/3
ans(ans+1) - (N-1)/3 > 0
ans^2 +ans - (N-1)/3 > 0
x > (-1 + sqrt(1+4(N-1)/3))/2

N = 13

'''

from math import sqrt, ceil
for N in range(1, 63):
    print(N, ceil((-1 + sqrt(1+4*(N-1)/3))/2+1))