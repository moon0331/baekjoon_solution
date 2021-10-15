# def check(x):
#     value = x+1
#     while True:
#         num_of_one = bin(x^value).count('1')
#         if num_of_one <= 2:
#             return value
#         value += 1

# def solution(numbers):
#     return [check(num) for num in numbers]

def check(x):
    if x%2 == 0 or x%4 == 1:
        return x+1
    else:
        value = x+1
        while True:
            num_of_one = bin(x^value).count('1')
            if num_of_one <= 2:
                return value
            value += 1


def solution(numbers):
    return [check(num) for num in numbers]

print(solution([2,7]) == [3, 11])

# https://www.apexcel.blog/ps/programmers/77885/77885/