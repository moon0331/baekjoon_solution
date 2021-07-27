import copy

result = {'max' : -1000000000, 'min' : 1000000000}

def find_value(num_list, ops, result):
    #print(num_list, ops)
    # 정답 계산하는 것 만들고
    if sum(ops) == 0:
        #print('END')
        update_result(result, num_list[0])
        return

    if ops[0]:
        # 앞수 더하고
        diff = num_list[0] + num_list[1]
        new_num_list = [diff] + num_list[2:]
        newops = ops[:]
        newops[0] -= 1
        find_value(new_num_list, newops, result)

    if ops[1]:
        diff = num_list[0] - num_list[1]
        new_num_list = [diff] + num_list[2:]
        newops = ops[:]
        newops[1] -= 1
        find_value(new_num_list, newops, result)

    if ops[2]:
        diff = num_list[0] * num_list[1]
        new_num_list = [diff] + num_list[2:]
        newops = ops[:]
        newops[2] -= 1
        find_value(new_num_list, newops, result)

    if ops[3]:
        diff = int(num_list[0] / num_list[1])
        new_num_list = [diff] + num_list[2:]
        newops = ops[:]
        newops[3] -= 1
        find_value(new_num_list, newops, result)


def update_result(result_dict, value):
    if value > result_dict['max']:
        result_dict['max'] = value
    if value < result_dict['min']:
        result_dict['min'] = value


input()

num_list = [int(x) for x in input().split()]

ops = [int(x) for x in input().split()]

find_value(num_list, ops, result)

print(result['max'], result['min'])