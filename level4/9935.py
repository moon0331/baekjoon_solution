read = __import__('sys').stdin.readline

stack = []

input_string = read().strip()
explode_string = read().strip()
explode_string_list = [c for c in explode_string]
exp_len = len(explode_string_list)

for c in input_string:
    stack.append(c)
    try:
        while stack[-exp_len:] == explode_string_list:
            for _ in range(exp_len):
                stack.pop()
    except:
        pass

if stack:
    print("".join(stack))
else:
    print('FRULA')