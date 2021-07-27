'''def cal(n, k, lst, result, penny_selection = []): # n개 동전, k원
    if k == 0:
        # print('okay with', penny_selection)
        penny_selection.sort()
        if not penny_selection in result:
            result.append(penny_selection)
        return True
    elif k < 0:
        return False
    # print('{}개 동전, {}원만들기, {}, {}'.format(n, k, lst, penny_selection))
    for val in lst:
        myPenny = [x for x in penny_selection]
        myPenny.append(val)
        cal(n, k-val, lst, result, myPenny)'''

n, k = (int(x) for x in input().split())
# n, k = 3, 10

coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

# print(coin_list)
coin_list.sort()

result = [0 for _ in range(k+1)]
result[0] = 1

print(coin_list)

'''
1 += 0
2 += 1
...
10 += 9

2 += (2-2)
...
10 += (10-2)

5 += (10-5)
...
10 += (10-10)


'''

for coin in coin_list:
    for i in range(coin, k+1):
        print('result[{}] += result[{}-{}]({})'.format(i, i, coin, result[i-coin]))
        result[i] += result[i-coin]
    print(result)


# cal(n, k, coin_list, memo)

print(result[-1])