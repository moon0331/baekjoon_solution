N = int(input())

X = list(map(int, input().split()))

sorted_X = {val:i for i, val in enumerate(sorted(list(set(X))))}

compressed_X = [sorted_X[t] for t in X]

print(" ".join(list(map(str, compressed_X))))