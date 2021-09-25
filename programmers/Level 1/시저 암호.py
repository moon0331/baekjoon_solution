from string import ascii_uppercase, ascii_lowercase

def solution(s, n):
    UPPER, under = ascii_uppercase, ascii_lowercase
    alpha_large_to_num = {ascii_uppercase[i]:i for i in range(26)}
    alpha_small_to_num = {ascii_lowercase[i]:i for i in range(26)}
    string = ''
    for c in s:
        if c in UPPER:
            string += UPPER[(alpha_large_to_num[c] + n)%26]
        elif c in under:
            string += under[(alpha_small_to_num[c] + n)%26]
        else:
            string += c

    return string

print(solution('AB', 1) == 'BC')
print(solution('z', 1) == 'a')
print(solution('a B z', 4) == 'e F d')

# ord check