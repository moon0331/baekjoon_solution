'''
가장 짧은 숫자의 자리수 : n

number[:n] 에서부터 number[:] 까지 hash값 담아버림

'''

def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    print(phone_book)
    for i in range(len(phone_book)-1):
        subword = phone_book[i]
        words_rng = phone_book[i+1:]
        for word in words_rng:
            if word.startswith(subword):
                return False
    return True

phones = [
    ["119", "97674223", "1195524421"], 
    ["123","456","789"],
    ["12","123","1235","567","88"]	
]

returns = [False, True, False]

for p, r in zip(phones, returns):
    print(solution(p) == r)