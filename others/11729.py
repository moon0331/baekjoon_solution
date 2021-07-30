def solve_hanoi(N):
    print(2**N - 1)
    hanoi(N, 1, 2, 3)

def hanoi(N, start, via, end): # start 에서 via 거쳐 end로 이동
    if N == 1:
        print(start, end) # start -> end
    else:
        hanoi(N-1, start, end, via)
        hanoi(1, start, via, end)
        hanoi(N-1, via, start, end)

######### 다시 체크

K = int(input())
solve_hanoi(K)