def recursive(n_list, val, target):
    if len(n_list) == 0:
        return int(val == target)
    else:
        return recursive(n_list[:-1], val+n_list[-1], target) + \
                recursive(n_list[:-1], val-n_list[-1], target)


def solution(numbers, target):
    return recursive(numbers, 0, target)

print(solution([1,1,1,1,1], 3) == 5)