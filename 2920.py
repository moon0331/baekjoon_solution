harmony = list(map(int ,input().split()))

if sorted(harmony) == harmony:
    print('ascending')
elif sorted(harmony, reverse=True) == harmony:
    print('descending')
else:
    print('mixed')