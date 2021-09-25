def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y') # counter
    
print(solution('pPoooyY') == True)
print(solution('Pyy') == False)