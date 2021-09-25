def solution(s):
    return "".join(sorted(s, reverse=True)) #list(s) 안해도됨

print(solution("Zbcdefg") == "gfedcbZ")