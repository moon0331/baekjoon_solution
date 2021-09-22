def solution(s):
    half = len(s)/2
    print(half)
    if half == int(half):
        return s[int(half)-1:int(half)+1]
    else:
        return s[int(half)]
    

print(solution("abcde") == "c")
print(solution("qwer") == "we")

# 1 -> 0
# 2 -> 0 1
# 3 -> 1
# 4 -> 1 2
# 5 -> 2
# 6 -> 2 3