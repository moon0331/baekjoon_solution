def calculate(chess, opt):
    move_list = [[], []]
    for row in range(8):
        # chess[row] == str
        move_list[0].append(sum(1 for i in range(8) if chess[row][i] != opt[row%2][i]))
        move_list[1].append(sum(1 for i in range(8) if chess[row][i] != opt[1-row%2][i]))
    return min(map(sum, move_list))

def getNewChess(chess, i, j):
    return [line[j:j+8] for line in chess[i:i+8]]

N, M = map(int, input().split())

opt = [ "".join('W' if i % 2 == 0 else 'B' for i in range(8)),
        "".join('B' if i % 2 == 0 else 'W' for i in range(8))]

# print(opt)

chess = []
for linenum in range(N):
    chess.append(input())

answer = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        newchess = getNewChess(chess, i, j)
        answer = min(answer, calculate(newchess, opt))

#print(calculate(chess, opt))
print(answer)