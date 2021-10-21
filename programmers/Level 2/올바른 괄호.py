def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
    return not stack

xy = [
    ("()()", True),
    ("(())()", True),
    (")()(", False),
    ("(()(", False)
]

for x, y in xy:
    print(solution(x) == y)

# stack 대신 숫자로 개념화시켜도 될듯