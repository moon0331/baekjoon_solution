def stack(lst, n):
    popped = {i:False for i in range(1, n+1)}
    max_idx = lst.index(max(lst))
    if sorted(lst[max_idx:], reverse=True) != lst[max_idx:]:
        print('NO')
        return

    last_popped = 0
    for idx, num in enumerate(lst[:max_idx+1]):
        #print(num, 'testing')
        if last_popped < num:
            for i in range(last_popped, num+1):
                if i == 0: continue
                if popped[i] == True:
                    #print(i, 'already popped')
                    continue
                print('+')
            print('-')

        else: # last_popped > num
            for i in range(last_popped, num-1, -1):
                if popped[i] == True:
                    #print(i, 'already popped')
                    continue
                print('-')
        popped[num] = True
        last_popped = num
        
    for _ in range(n-max_idx-1):
        print('-')

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

stack(lst, n)