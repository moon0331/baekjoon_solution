def is_this_value_unique(arr, val):
    return sum(1 for x in arr if x == val) == 1

def calculate_sum(arr, is_unique=False, unique_value=0):
    if is_unique:
        return (sum(arr) - unique_value) / (len(arr) - 1)
    else:
        return sum(arr) / len(arr)

def update_score(lst, val):
    if val >= 90:
        lst.append('A')
    elif val >= 80:
        lst.append('B')
    elif val >= 70:
        lst.append('C')
    elif val >= 50:
        lst.append('D')
    else:
        lst.append('F')

def solution(scores):
    ans = []
    my_score_list = list(map(list, zip(*scores)))
    for i, score in enumerate(my_score_list):
        my_my_score = score[i]
        min_score, max_score = min(score), max(score)
        min_unique = is_this_value_unique(score, min_score)
        max_unique = is_this_value_unique(score, max_score)

        if min_score == my_my_score:
            avg = calculate_sum(score, min_unique, min_score)
        elif max_score == my_my_score:
            avg = calculate_sum(score, max_unique, max_score)
        else:
            avg = calculate_sum(score)
        
        update_score(ans, avg)

    return "".join(ans)


scoress = [
    [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]],
    [[50,90],[50,87]],
    [[70,49,90],[68,50,38],[73,31,100]]
]

results = ["FBABD", "DA", "CFD"]

for s, r in zip(scoress, results):
    print(solution(s) == r)