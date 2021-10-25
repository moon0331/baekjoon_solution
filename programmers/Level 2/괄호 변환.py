def solution(p):
    # 1번
    if not p:
        return p
    
    # 2번
    u, v = separate(p)
    print(u,v)

    # 3번
    if isRight(u):
        return u + solution(v)
    # 4번
    else:
        return add(f'({solution(v)})', u[1:-1])

def separate(p):
    stack = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack += 1
        else:
            stack -= 1
        if not stack:
            return p[:i+1], p[i+1:]

def isRight(p):
    return p[0] == '('

def add(x, y):
    rev = {'(':')', ')':'('}
    return x + ''.join(rev[c] for c in y)


print(solution("(()())()") == "(()())()")
print(solution(")(") == "()")
print(solution("()))((()") == "()(())()")