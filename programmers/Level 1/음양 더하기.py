def solution(absolutes, signs):
    return sum([a if s else -a for a, s in zip(absolutes, signs)])

abss = [[4,7,12], [1,2,3]]
ss = [[True, False, True], [False, False, True]]
rs = [9, 0]

for a, s, r in zip(abss, ss, rs):
    print(solution(a, s) == r)