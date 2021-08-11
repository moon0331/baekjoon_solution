def Z(r, c, base_val, l): # l == 한 변 길이
    # print('r={}, c={}, base_val={}, N={}'.format(r, c, base_val, l))
    if l == 2:
        if (r, c) == (0, 0):
            return base_val
        elif (r, c) == (0, 1):
            return base_val + 1
        elif (r, c) == (1, 0):
            return base_val + 2
        elif (r, c) == (1, 1):
            return base_val + 3
    else:
        half_l = l//2
        if 0 <= r < half_l and 0 <= c < half_l:
            return Z(r, c, base_val, half_l)
        elif 0 <= r < half_l and half_l <= c < l:
            return Z(r, c-half_l, base_val + half_l**2 , half_l)
        elif half_l <= r < l and 0 <= c < half_l:
            return Z(r-half_l, c, base_val + half_l*l , half_l)
        else:
            return Z(r-half_l, c-half_l, base_val + 3*(half_l**2), half_l)

N, r, c = map(int, input().split())
print(Z(r, c, 0, 2**N))

################
# 0   1   4   5
# 2   3   6   7
# 8   9   12  13
# 10  11  14  15
################