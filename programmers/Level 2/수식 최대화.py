# 다른 풀이 체크

import re

def cal(x, y, op):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y
    else:
        raise Exception('not valid operation')

def solution(expression):
    answer = 0
    nums = list(map(int, re.findall(r'[0-9]+', expression)))
    ops = re.findall(r'[\+|\-|\*]', expression)
    # print(nums, ops)
    ops_order = ['+-*', '+*-', '-+*', '-*+', '*+-', '*-+']
    for present_ops_order in ops_order:
        tmp_nums = [x for x in nums]
        tmp_ops = [x for x in ops]
        for op in present_ops_order:
            while op in tmp_ops:
                # print(op, i)
                i = tmp_ops.index(op)
                if i < len(tmp_ops) and tmp_ops[i] == op:
                    x, y = tmp_nums[i], tmp_nums[i+1]
                    val = cal(x, y, op)
                    del tmp_nums[i:i+2]
                    del tmp_ops[i]
                    tmp_nums.insert(i, val)
                    # print(tmp_nums, tmp_ops)
        # print('with', present_ops_order, tmp_nums)
        # print('=======================================')
        answer = max(answer, abs(tmp_nums[0]))
    
    return answer

exps = ["100-200*300-500+20", "50*6-3*2"]
results = [60420, 300]

for e, r in zip(exps, results):
    print(solution(e) == r)