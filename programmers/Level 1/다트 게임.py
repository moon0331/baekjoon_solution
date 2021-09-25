import re

def calculate(scores, idx, num, op):
    op_idx = ['S', 'D', 'T']
    scores[idx] = num ** (op_idx.index(op[0])+1)
    if '*' in op:
        scores[idx] *= 2
        if idx:
            scores[idx-1] *= 2
    if '#' in op:
        scores[idx] *= -1


def solution(dartResult):
    nums = [int(n) for n in re.findall(r'\d+', dartResult)]
    ops = re.findall(r'[S|D|T|\*|\#]+', dartResult)

    scores = [0, 0, 0]
    for i, n, op in zip(range(3), nums, ops):
        calculate(scores, i, n, op)
        
    return sum(scores)

io = [  ['1S2D*3T', 37],
        ['1D2S#10S', 9],
        ['1D2S0T', 3],
        ['1S*2T*3S', 23],
        ['1D#2S*3S', 5],
        ['1T2D3D#', -4],
        ['1D2S3T*', 59]
]

for i, o in io:
    print(solution(i) == o)