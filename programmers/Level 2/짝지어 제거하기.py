def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return 1 if not stack else 0

print(solution('baabaa') == 1)
print(solution('cdcd') == 0)