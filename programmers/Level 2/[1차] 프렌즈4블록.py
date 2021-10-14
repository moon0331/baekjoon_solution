def reverse_board(board): # (m,n)
    new_board = [line[::-1] for line in list(map(list, zip(*board)))]
    return new_board # (n,m)

def search_pop_blocks(m, n, board): # board (m,n) 들어올때 지워야 할 인덱스와 지워지는 블록 수 반환 (reverse될때 확인 필요)
    erase_idx = [set() for _ in range(n)]
    pop_idx = set()
    for i in range(m-1):
        for j in range(n-1):
            if is_same(board, i, j):
                erase_idx[i] |= {j, j+1}
                erase_idx[i+1] |= {j, j+1}
                pop_idx |= {(i, j), (i, j+1), (i+1, j), (i+1, j+1)}
    n_pop_block = len(pop_idx)
    return erase_idx, n_pop_block

def is_same(b, i, j):
    four_blocks = {b[i][j], b[i+1][j], b[i][j+1], b[i+1][j+1]}
    return not 0 in four_blocks and len(four_blocks) == 1

def pop_block(board, erase_idx_by_row, m):
    for i, erase_idx in enumerate(erase_idx_by_row):
        if not erase_idx:
            continue
        minval, maxval = min(erase_idx), max(erase_idx)
        board[i][minval:maxval+1] = []
        board[i] += [0 for _ in range(m-len(board[i]))]

def solution(m, n, board):
    answer = 0
    board = reverse_board(board) 
    while True:
        erase_idx_by_row, n_pop_block = search_pop_blocks(n, m, board)
        if n_pop_block: 
            answer += n_pop_block
            pop_block(board, erase_idx_by_row, m)
            continue
        break
    return answer

ms = [4, 6]
ns = [5, 6]
boards = [
    ["CCBDE", "AAADE", "AAABF", "CCBBF"],
    ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
]
answers = [14, 15]

for m, n, board, answer in zip(ms, ns, boards, answers):
    print(solution(m, n, board) == answer)

# 7번 10번 체크 필요