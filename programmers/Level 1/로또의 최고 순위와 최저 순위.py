def solution(lottos, win_nums):
    ranking = [6, 6, 5, 4, 3, 2, 1]
    n_same = len(set(lottos).intersection(win_nums))
    n_zero = sum(1 for x in lottos if x == 0)
    return [ranking[n_same + n_zero], ranking[n_same]]

ls = [
    [44, 1, 0, 0, 31, 25],
    [0, 0, 0, 0, 0, 0],
    [45, 4, 35, 20, 3, 9]
]

ws = [
    [31, 10, 45, 1, 6, 19],
    [38, 19, 20, 40, 15, 25],
    [20, 9, 3, 45, 4, 35]
]

rs = [
    [3, 5],
    [1, 6], 
    [1, 1]
]

for l, w, r in zip(ls, ws, rs):
    print(solution(l, w) == r)