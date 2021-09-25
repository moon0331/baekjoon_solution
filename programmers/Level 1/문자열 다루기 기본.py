def solution(s):
    return s.isdigit() and len(s) in (4, 6) # or로 하는것보다 빠름?

print(solution('a234') == False)
print(solution('1234') == True)