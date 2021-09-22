def solution(left, right):
    seq_list = [x**2 for x in range(1, 32)]
    return sum(-x if x in seq_list else x for x in range(left, right+1))

print(solution(13, 17) == 43)
print(solution(24, 27) == 52)