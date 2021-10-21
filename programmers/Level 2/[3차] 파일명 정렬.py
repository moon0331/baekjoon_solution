import re

def seperate(file):
    part = re.findall(r'[\D]+|[\d]+', file)
    head, number = part[0], part[1]
    if len(part) >= 2:
        tail = "".join(part[2:])
    else:
        tail = ''
    return head, number, tail

def join_filename(*source): #head, number, tail
    return "".join(source)

def solution(files):
    file_store = [seperate(file) for file in files]
    file_store.sort(
        key=lambda hnt: (hnt[0].lower(), int(hnt[1]))
    )
    return [join_filename(*f) for f in file_store]

xs = [
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
]

ys = [
    ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"],
    ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
]

for x, y in zip(xs, ys):
    print(solution(x) == y)