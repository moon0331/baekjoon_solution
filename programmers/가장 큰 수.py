def solution(numbers):

    def subsort(arr, n):
        newarr = [x for x in arr]
        newarr.sort(reverse=True)
        print('new', newarr)

    answer = []
    for i in range(10):
        arr = select_arr(numbers)
        answer.extend(subsort(arr, ))
    return

print(solution([6, 10, 2]) == "6210")
print(solution([3, 30, 34, 5, 9]) == "9534330")