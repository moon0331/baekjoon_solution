def WeIrD(s):
    return ''.join(s[i].lower() if i%2 else s[i].upper() for i in range(len(s)))

def solution(s):
    return " ".join([WeIrD(word) for word in s.split(' ')])

print(solution('try hello world') == 'TrY HeLlO WoRlD')