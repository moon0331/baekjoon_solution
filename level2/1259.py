while True:
    num = input()
    if num == '0':
        break
    print('yes' if all(map(lambda x: x[0]==x[1], zip(num, num[::-1]))) else 'no')