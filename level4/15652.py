def printNum(lst, N, M):
    if len(lst) == M:
        print(*lst)
        return
    start_num = lst[-1] if lst else 1
    for i in range(start_num, N+1):
        newlst = lst + [i]
        printNum(newlst, N, M)

N, M = map(int, input().split())

printNum([], N, M)

# for pair in product(*(range(1, M+1) for _ in range(N))):
#     prev_element = 0
#     print_value = True
#     for i in range(len(pair)):
#         e = pair[i]
#         if not prev_element <= e:
#             print_value = False
#             break
#         prev_element = e
#     if print_value:
#         # print(*pair)
#         for e in pair:
#             sys.stdout.write('{} '.format(e))
#         sys.stdout.write('\n')

# # 시간초과