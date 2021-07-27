T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    print("".join(map(lambda x:int(R)*x, list(map(str, S)))))