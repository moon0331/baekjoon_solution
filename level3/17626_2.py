# four squares

from itertools import combinations

dp = [9999 if i != 0 else 0 for i in range(50001)]
dp_dict = {i:[] for i in range(5)}

dp_dict[0].append(0)
for i in range(1, 224):
    i_sq = i**2
    dp[i_sq] = 1
    dp_dict[1].append(i_sq)

for val in range(1, 4):
    dp_dict[val].sort(reverse=True) # 내림차순 정렬
    for startidx in dp_dict[val]:
        k = 1
        while k**2 <= startidx:
            newidx = startidx + k**2
            if newidx > 50000 or dp[newidx] < val+1:
                break
            dp[newidx] = val + 1
            # print('dp[{}+{}]={}'.format(startidx, k**2, val+1))
            dp_dict[val+1].append(newidx)
            k += 1

# for val in range(0, 4):
#     dp_dict[val].sort(reverse=True)
#     for update_start_num in dp_dict[val]: # 업데이트 시작 지점
#         k = 1
#         while True:
#             next_update = update_start_num+k**2
#             if next_update > 50000:
#                 break
#             if dp[next_update] == 9999: # not update
#                 print('dp[{}+{}^2] = {}'.format(update_start_num, k, val+1))
#                 dp[next_update] = min(dp[next_update], val + 1)
#                 dp_dict[val+1].append(next_update)
#                 k += 1

print(dp[int(input())])