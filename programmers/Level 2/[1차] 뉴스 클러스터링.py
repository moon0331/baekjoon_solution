from collections import Counter

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    set1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    set2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    cnt_set1, cnt_set2 = Counter(set1), Counter(set2)
    cnt_intersect = cnt_set1 & cnt_set2
    cnt_union = cnt_set1 | cnt_set2
    if not cnt_union:
        return 65536
    else:
        return int(65536 * sum(cnt_intersect.values())/sum(cnt_union.values()))

string_set = [
    ('FRANCE', 'french'),
    ('handshake', 'shake hands'),
    ('aa1+aa2', 'AAAA12'),
    ('E=M*C^2', 'e=m*c^2')
]

answer = [16384, 65536, 43690, 65536]

for (s1, s2), aval in zip(string_set, answer):
    print(solution(s1, s2) == aval)