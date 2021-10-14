from itertools import combinations

def get_combinations(orders, course): # 전체 order에 대하여 course 수에 해당하는 세트메뉴 포함
    combs = set()
    for n_menu in course:
        for order in orders:
            combs = combs | set(combinations(order, n_menu))
    
    return combs

def count_included_order(orders, cmb):
    cnt = 0
    for order in orders:
        if all(x in order for x in cmb):
            cnt += 1
    return cnt

def solution(orders, course):
    answer = []
    most_frequent_set_menu = {x:dict() for x in course}

    for cmb in get_combinations(orders, course):
        cnt = count_included_order(orders, cmb)
        if cnt >= 2:
            most_frequent_set_menu[len(cmb)]["".join(sorted(cmb))] = cnt
    
    for n_len in most_frequent_set_menu:
        word_set = most_frequent_set_menu[n_len]
        answer.extend([x for x in word_set if word_set[x] == max(word_set.values())])
    
    return sorted(answer)

order_set = [
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
    ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
    ["XYZ", "XWY", "WXA"]
]

courses = [[2,3,4], [2,3,5], [2,3,4]]

results = [
    ["AC", "ACDE", "BCFG", "CDE"],
    ["ACD", "AD", "ADE", "CD", "XYZ"],
    ["WX", "XY"]
]

for o, c, r in zip(order_set, courses, results):
    print(solution(o, c) == r)

# combination 가지수 줄이기
# 전체 단어셋에서 comb 돌리지 말고 각 오더에서 comb 돌린걸 합해서 해보자
# 가지수 줄이기

# comb(whole_set, n) 대신 comb(word1, n) | comb(word2, n) ... 