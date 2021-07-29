def quad(arr, i, j, size):
    subarr = []
    rowsum = 0
    for x in range(i, i+size):
        subarr.append(arr[x][j:j+size])
        rowsum += sum(arr[x][j:j+size])
    print(subarr)


