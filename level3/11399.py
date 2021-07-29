import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

sum_arr = [0 for _ in range(len(arr))]

sumval = 0
for i in range(len(arr)):
    sum_arr[i] = sumval + arr[i]
    sumval += arr[i]

print(sum(sum_arr))