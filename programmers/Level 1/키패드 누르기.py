def get_distance_list():
    return {
        0: [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1],
        2: [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4],
        5: [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3],
        8: [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2]
    } # 0 ~ 9, '*', '#'

def distance(dist_list, start, end):
    return dist_list[start][end]

def update(arr, loc, hand, val):
    arr.append(hand)
    loc[hand] = val

def solution(numbers, hand):
    hand = hand.upper()
    dist_list = get_distance_list()
    answer = []
    loc = {'L' : 10, 'R' : 11}
    for n in numbers:
        if n in (1, 4, 7):
            update(answer, loc, 'L', n)
        elif n in (3, 6, 9):
            update(answer, loc, 'R', n)
        else:
            l_dist = distance(dist_list, n, loc['L'])
            r_dist = distance(dist_list, n, loc['R'])
            if l_dist == r_dist:
                update(answer, loc, hand[0], n)
            else:
                if l_dist < r_dist:
                    update(answer, loc, 'L', n)
                else:
                    update(answer, loc, 'R', n)
    return "".join(answer)

ns = [
    [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
    [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
]

hands = ['right', 'left', 'right']

results = ["LRLLLRLLRRL", "LRLLRRLLLRR", "LLRLLRLLRL"]

for n, h, r in zip(ns, hands, results):
    print(solution(n, h) == r)