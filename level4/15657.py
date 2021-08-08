def solve(arr, M, depth, pair):
    if depth == M:
        print(*pair)
        return
    for i in arr:
        if not pair or pair[-1] <= i:
            solve(arr, M, depth+1, pair+[i])

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

solve(arr, M, 0, [])