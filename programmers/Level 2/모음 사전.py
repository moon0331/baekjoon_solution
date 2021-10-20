from itertools import product

def solution(word):
    wordset = []
    for i in range(1, 6):
        wordset.extend(''.join(charset) for charset in product('AEIOU', repeat=i))
    wordset.sort(key=lambda x:(x, len(x)))
    return wordset.index(word)+1

words = ['AAAAE', 'AAAE', 'I', 'EIO']
result = [6, 10, 1563, 1189]

for word, r in zip(words, result):
    print(solution(word) == r)