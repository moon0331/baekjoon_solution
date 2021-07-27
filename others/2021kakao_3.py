'''
"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
'''

# n행, 첫 선택 행이 k
def solution(n, k, cmd):
    board = [1 for _ in range(n)]
    erased = []
    pointer = k
    answer = ""

    for cm in cmd:
        if len(cm) != 1:
            x, y = cm.split() # U X, D X
        else:
            x = cm

        if x == 'U': # X칸 위 행 선택
            pointer -= int(y)
        elif x == 'D': # X칸 아래 행 선택
            pointer += int(y)
        elif x == 'C': # 현재 행 삭제 후 바로 아래 행 선택 (가장 마지막 행 삭제시 바로 윗 행)
            er =
            if cm == get_last_exist_row(board):
                board[]
        elif cm =='Z': # 가장 최근에 삭제된 행 원상복구 (행 바뀌지 않음)
            pass
        print(cm, '=>', pointer)

    return answer

if __name__=='__main__':
    n, k = (int(x) for x in input().split())
    cmds = [
        ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],
        ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    ]

    for cmd in cmds:
        print(solution(n, k, cmd))