def d(x):
    return sum(map(int, list(map(int, str(x))))) + x

not_selfnumber = []

for i in range(1, 10000):
    not_selfnumber.append(d(i))

selfnumber = set(range(1, 10001)) - set(not_selfnumber)

selfnumber_list = list(selfnumber)

for num in sorted(selfnumber_list):
    print(num)