N = int(input())
M = int(input())
S = input()

cnt = 0
obj_s = S
i = 0
while 0 <= i < M:
    i += S.find('IO'*(N-1)+'I') + 2*N - 1
    print('startswith', i)
    while i >= 0 and (i < M and S[i] == 'O') and (i+1 < M and S[i+1] == 'I'):
        print(i, 'found')
        cnt += 1
        i += 2
    i -= 1

print(cnt)


# i가 0에서 len(s) 사이
# 우선 P(N-1) == 'IO'*(N-1)+'I'의 인덱스 찾고 그 크기만큼 포인터 이동 (2N-1)
# 거기서부터 'OI' 찾기