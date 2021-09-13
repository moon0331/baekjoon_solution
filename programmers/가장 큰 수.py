from functools import cmp_to_key

def cmp(x, y):
    return int(y+x) - int(x+y)

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=cmp_to_key(cmp))
    if numbers[0] == '0':
        return '0'
    return str("".join(numbers))

print(solution([6, 10, 2]) == "6210")
print(solution([3, 30, 34, 5, 9]) == "9534330")


'''

999 99 9 998 997 996 
999 99(9) 9(99) 998 997 996
988 989 97 9798

'''