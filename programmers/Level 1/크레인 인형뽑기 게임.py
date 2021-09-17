def solution(board, moves):
    stack_board = []
    bomb_stack = []
    for tr_line in map(list, zip(*board)):
        stack_board.append([x for x in tr_line[::-1] if x])
    
    answer = 0
    
    for move in moves:
        # bomb stack에 옮기고 터지기 확인
        if stack_board[move-1]:
            pop_doll = stack_board[move-1].pop()
        else:
            continue
        
        if bomb_stack and bomb_stack[-1] == pop_doll:
            bomb_stack.pop()
            answer += 2
        else:
            bomb_stack.append(pop_doll)

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	
result = 4

print(solution(board, moves) == result)