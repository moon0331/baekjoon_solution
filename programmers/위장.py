from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    for x, y in clothes:
        clothes_dict[y] += 1

    answer = 1
    for x in clothes_dict.values():
        answer *= (x+1)

    return answer - 1

clothes_list = [
    [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
]

returns = [5, 3]

for c, r in zip(clothes_list, returns):
    print(solution(c) == r)