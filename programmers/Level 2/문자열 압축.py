def get_new_subword_info(word=None):
    return {'word':word, 'n_freq':1, 'init':False}

def subword_info_to_string(subword_info):
    if subword_info['n_freq'] >= 2:
        return str(subword_info['n_freq']) + subword_info['word']
    else:
        return subword_info['word']

def solution(s):
    if len(s) == 1:
        return 1
    elif len(s)==2 or (len(s) == 3 and len(set(s)) == 1):
        return 2
        
    answer = float('inf')

    for unit in range(1, len(s)//2+1):
        words = [s[i:i+unit] for i in range(0, len(s), unit)]

        result_word = ''
        subword_info = get_new_subword_info(words[0])

        for w in words[1:]:
            if subword_info['word'] != w: # new word
                result_word += subword_info_to_string(subword_info)
                subword_info = get_new_subword_info(w)
            else:
                subword_info['n_freq'] += 1
                
        result_word += subword_info_to_string(subword_info)

        answer = min(answer, len(result_word))

    return answer



answer_sheet = [
    ("aabbaccc", 7),
    ("ababcdcdababcdcd", 9),
    ("abcabcdede", 8),
    ("abcabcabcabcdededededede", 14),
    ("xababcdcdababcdcd", 17)
]

print(solution('a') == 1)

for x, y in answer_sheet:
    print(solution(x) == y)