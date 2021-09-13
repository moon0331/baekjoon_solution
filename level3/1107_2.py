from collections import deque

def valid(num, available_numbers):
    if num == 100:
        return 1 # 100 (숫자 입력 X)
    elif all(c in available_numbers for c in str(num)): # 다 있는 숫자들이구만
        return 2 # 숫자 입력 필요
    else:
        return 0 # not end

def if_valid_get_result(num, available_numbers, t):
    flag = valid(num, available_numbers)
    if flag == 1: # +-만 조작
        return t
    elif flag == 2: # 초기값 만들고 +-버튼 조작
        return t + min(len(str(num)), abs(100-num))
    else:
        return float('INF') # not

# def BFS(start_num, available_numbers):
    if valid(start_num, available_numbers):
        return 0
    visited = set([start_num])
    q = deque([(start_num, 0)])
    while q:
        val, n_click = q.popleft()
        cnk = valid(val, available_numbers)
        if cnk == 1:
            return n_click
        elif cnk == 2:
            return n_click + len(str(val))
        else:
            if val-1 >= 100 and not val-1 in visited:
                q.append((val-1, n_click+1))
                visited.add(val-1)
            if not val+1 in visited:
                q.append((val+1, n_click+1))
                visited.add(val+1)
    return -1

def bruteforce(start_num, available_numbers):
    if start_num == 100:
        return 0
    t = 0
    while True:
        # print(t, ':', start_num+t, start_num-t)
        plus_valid = if_valid_get_result(start_num+t, available_numbers, t)
        minus_valid = if_valid_get_result(start_num-t, available_numbers, t)
        if plus_valid != float('INF') or minus_valid != float('INF'):
            return min(plus_valid, minus_valid)
        t += 1

N = int(input())
M = int(input())
broken_buttons = set(map(int, input().split()))
avilable_numbers = [str(c) for c in set(range(10)).difference(broken_buttons)]
avilable_numbers.sort()

# result = BFS(N, avilable_numbers)
result = bruteforce(N, avilable_numbers)

print(result)

# line 196부터
  