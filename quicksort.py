def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right
    # print('pivot : {}, i = {}, j = {} | left = {}, right = {}'.format(pivot, i, j, left, right))
    while i < j:
        while arr[i] <= pivot and i < right: # 부호 체크
            i += 1
        while arr[j] > pivot and j > left: # 부호 체크
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[left], arr[j] = arr[j], arr[left]
    return j
        

def quicksort(arr, left, right): # left 부터 right(포함) 까지 정렬
    if left >= right: return
    q = partition(arr, left, right) # partition 결정
    print('partitioned', left, q-1, '|', q+1, right, 
        '(q={})'.format(q), 'qval={}'.format(arr[q]))
    quicksort(arr, left, q-1)
    quicksort(arr, q+1, right)


import random

arr = [random.randint(0, 500) for _ in range(100)]

quicksort(arr, 0, len(arr)-1)

print(arr)
print(arr == sorted(arr))