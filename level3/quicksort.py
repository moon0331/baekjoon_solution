import random

def partition(arr, left, right):
    pivot = arr[(left+right)//2]
    start, end = left, right
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        arr[start], arr[end] = arr[end], arr[start]
    return start

def quicksort(arr, left, right):
    while left <= right:
        q = partition(arr, left, right)
        quicksort(arr, 0, q-1)
        quicksort(arr, q+1, right)

arr = [random.randint(0, 1000) for x in range(10000)]

print(arr)

quicksort(arr, 0, len(arr)-1)

print(arr)