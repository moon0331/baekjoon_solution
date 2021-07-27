import sys

def cal_paper(paper, row, col, length, n_papers):
    #print(row, col, length, n_papers)
    if length == 1:
        n_papers[paper[row][col]] += 1
        return
    else:
        is_allsame = True
        val = list(set(paper[row][col:col+length]))[0]
        for i in range(row, row+length):
            one_row = paper[i][col:col+length]
            maxval, minval = max(one_row), min(one_row)
            if not (val == maxval == minval):
                is_allsame = False
                break
        if is_allsame:
            n_papers[paper[row][col]] += 1
            return
        
        newlength = length//3
        for i in range(row, row+length, newlength):
            for j in range(col, col+length, newlength):
                cal_paper(paper, i, j, newlength, n_papers)
    return

N = int(input())

paper = []

n_papers = {-1:0, 0:0, 1:0}

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

cal_paper(paper, 0, 0, N, n_papers)

for val in (-1, 0, 1):
    print(n_papers[val])