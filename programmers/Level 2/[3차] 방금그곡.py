def solution(m, musicinfos):
    answer = ''
    return answer

ms = ["ABCDEFG", "CC#BCC#BCC#BCC#B", "ABC"]
infos = [
    ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
    ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
    ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
]
results = ["HELLO", "FOO", "WORLD"]

for m, info, result in zip(ms, infos, results):
    print(solution(m, info) == result)

# TODO