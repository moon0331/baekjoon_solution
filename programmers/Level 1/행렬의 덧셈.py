def solution(arr1, arr2):
    return [[x+y for x, y in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]

print(solution([[1,2], [2,3]], [[3,4], [5,6]]) == [[4,6],[7,9]])
print(solution([[1],[2]], [[3],[4]]) == [[4],[6]])