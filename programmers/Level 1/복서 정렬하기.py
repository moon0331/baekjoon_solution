# def solution(weights, head2head):
#     win_info = {}
#     answer = []
#     n_people = len(weights)
#     for i in range(n_people):
#         n_game = n_win = n_underdog = 0
#         for j in range(n_people):
#             if i == j: continue
#             n_game += 1
#             if head2head[i][j] == 'W':
#                 n_win += 1
#                 if weights[i] < weights[j]:
#                     n_underdog += 1
        
#         win_info[i+1] = (n_win/n_game, n_underdog, weights[i], -i)
    
#     print(win_info)
#     print([x for x, _ in sorted(win_info.items(), key=lambda x: x[1], reverse=True)])

#     return [x for x, _ in sorted(win_info.items(), key=lambda x: x[1], reverse=True)]

# ws = [
#     [50,82,75,120], [145,92,86], [60,70,60]
# ]

# h2hs = [
#     ["NLWL","WNLL","LWNW","WWLN"], ["NLW","WNL","LWN"], ["NNN","NNN","NNN"]
# ]

# rs = [[3,4,1,2], [2,3,1], [2,1,3]]

# for w, h2h, r in zip(ws, h2hs, rs):
#     print(solution(w, h2h) == r)