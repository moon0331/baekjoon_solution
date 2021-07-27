def partition(lst, start, end):
    p = lst[start]
    left = start + 1
    right = end
    while left <= right:
        while p > lst[left]:
            left += 1
        while p < lst[right]:
            right -= 1
        lst[left], lst[right] = lst[right], lst[left]
    lst[start], lst[right] = lst[right], lst[start]
    return right


def quicksort(lst, start, end):
    print(start, end)
    if start < end:
        q = partition(lst, start, end)
        quicksort(lst, start, q-1)
        quicksort(lst, q+1, end)

import random

lst = [random.randint(-100,100) for _ in range(100)]
print(lst)
quicksort(lst, 0, len(lst)-1)
print(lst)