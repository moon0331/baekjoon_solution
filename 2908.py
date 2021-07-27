A, B = (int(x[::-1]) for x in map(str, input().split()))

print(A if A>B else B)