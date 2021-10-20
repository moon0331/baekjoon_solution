from itertools import combinations

def reverse(relation):
    return list(map(list, zip(*relation)))

def generate_available_keyset(N):
    keyset = []
    for i in range(1, N+1):
        keyset.extend(combinations(range(N), i))
    return keyset

def isUnique(data):
    return len(set(data)) == len(data)

def hasMinimality(key, answer_key):
    for already_key in answer_key:
        if already_key & set(key) == already_key:
            return False
    return True


def solution(relation):
    answer = 0
    available_key_tuple = generate_available_keyset(len(relation[0]))
    answer = []
    for key in available_key_tuple:
        query = [tuple(line[i] for i in key) for line in relation]
        if isUnique(query) and hasMinimality(key, answer):
            answer.append(set(key))

    return len(answer)

relation = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]

result = 2

print(solution(relation) == result)