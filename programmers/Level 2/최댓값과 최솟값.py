def solution(s):
    lst = list(map(int, s.split()))
    return f'{min(lst)} {max(lst)}'
    

ss = [
    '1 2 3 4',
    '-1 -2 -3 -4',
    '-1 -1'
]

returns = ["1 4", "-4 -1", "-1 -1"]

for s, r in zip(ss, returns):
    print(solution(s) == r)