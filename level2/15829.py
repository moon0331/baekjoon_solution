import string

def APChash(line):
    r, M = 31, 1234567891
    H = 0
    char_to_idx = {c:i+1 for i, c in enumerate(string.ascii_lowercase)}

    for i, c in enumerate(line):
        H += (char_to_idx[c] * (r ** i))
    
    return H % M

input()
print(APChash(input()))