DIGIT = '0123456789ABCDEF'

def translate(val, n):
    q, r = divmod(val, n)
    if q == 0:
        return DIGIT[r]
    else:
        return translate(q, n) + DIGIT[r]

def solution(n, t, m, p):
    word = ''
    val = 0
    for val in range(m*t):
        word += translate(val, n)
        val += 1
        # print(word)

    # print(word[p-1::m][:t])
    return word[p-1::m][:t]

inputs = [
    (2, 4, 2, 1), 
    (16, 16, 2, 1), 
    (16, 16, 2, 2)
]

results = ['0111', '02468ACE11111111', '13579BDF01234567']

for x, y in zip(inputs, results):
    print(solution(*x) == y)