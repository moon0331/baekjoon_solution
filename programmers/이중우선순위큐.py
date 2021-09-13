import heapq

def insert(h, val):
    heapq.heappush(h, val)

def delete(h, delete_max=False):
    if h:
        if delete_max:
            temp_h = []
            while h:
                pop_val = heapq.heappop(h)
                if h:
                    temp_h.append(pop_val)
            for val in temp_h:
                heapq.heappush(h, val)
        else:
            heapq.heappop(h)

def solution(operations):
    h = []
    for op in operations:
        if op[0] == 'I':
            insert(h, int(op.split()[-1]))
        elif op == 'D -1':
            delete(h, False)
        else:
            delete(h, True)

    if h:
        return [max(h), min(h)]
    else:
        return [0, 0]

operation_list = [
    ["I 16","D 1"], ["I 7","I 5","I -5","D -1"]
]

returns = [
    [0,0], [7,5]
]

for o, r in zip(operation_list, returns):
    print(solution(o) == r)