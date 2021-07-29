import sys

n = int(sys.stdin.readline())

last_popped = 0
max_in_stack = 0
is_max_popped = False
popped = [False for _ in range(n+1)]
ans=''
not_available = False

for _ in range(n):
    val = int(sys.stdin.readline())
    if not_available:
        continue
    if not is_max_popped:
        if last_popped < val:
            # print('오름차순 : {}->{}'.format(last_popped, val))
            for i in range(last_popped+1, val+1):
                # print(i)
                if popped[i]: continue
                ans += '+'
            ans += '-'
        else:
            # print('내림차순 : {}->{}'.format(last_popped, val))
            if last_popped - val >= 2:
                not_available = True
            else:
                ans += '-'
    else:
        if last_popped < val:
            not_available = True
        else:
            ans += '-'
    last_popped = val
    popped[val] = True
    # ans += ' '
    if val == n:
        is_max_popped = True

if not_available:
    print('NO')
else:
    print(*[c for c in ans], sep='\n')