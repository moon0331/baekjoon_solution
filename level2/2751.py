N = int(input())

lst = []
for _ in range(N):
    lst.append(int(input()))
    
for value in sorted(lst):
    print(value)