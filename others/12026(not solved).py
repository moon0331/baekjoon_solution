# BOJ 거리

from collections import deque

def calculate(block, idx, last_alphabet_dict, answer):
    present_block = block[idx]
    print('present block', present_block)
    print('present idx', idx)

    if present_block == 'B':
        last_block = 'J'
    elif present_block == 'O':
        last_block = 'B'
    elif present_block == 'J':
        last_block = 'O'

    print('last block', last_block)
    
    target_q = last_alphabet_dict[last_block]

    print('target_idx', target_q)

    tmp = float('inf')
    while target_q and target_q[0] < idx:
        target_idx = target_q.popleft()
        if answer[target_idx] == -1:
            continue
        tmp = min(tmp, (target_idx - idx)**2)
        print(tmp)

    if tmp != float('inf'):
        answer[idx] += tmp
    else:
        answer[idx] = -1

# N = int(input())
# block = input()


N = 13
block = 'BJBBJOOOJJJJB'

answer = [0 for _ in range(N)]
last = {c:deque() for c in 'BOJ'}

first_block = block[0]
answer[0] = 0

for idx, c in enumerate(block):
    last[c].append(idx)

for q in last:
    print(q, last[q])

for idx in range(1, N): # 2 ~ N
    print('='*100)
    calculate(block, idx, last, answer)
    print(idx)
    print(answer)
    print(last)

print(answer[-1] if answer[-1] else -1)