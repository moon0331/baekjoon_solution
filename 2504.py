line = input()

word = []

for c in line:
    word.append(c)
    if len(word) >= 2 and "".join(word[-2:]) == '()':
        word.pop()
        word.pop()
        word.append('2')
    if len(word) >= 2 and "".join(word[-2:]) == '[]':
        word.pop()
        word.pop()
        word.append('3')
    if len(word) >= 3 and word[-2].isdigit() and word[-3]+word[-1] == '()':
        val = int(word[-2]) * 2
        word.pop()
        word.pop()
        word.pop()
        word.append(str(val))
    if len(word) >= 3 and word[-2].isdigit() and word[-3]+word[-1] == '[]':
        val = int(word[-2]) * 3
        word.pop()
        word.pop()
        word.pop()
        word.append(str(val))
    if len(word) >= 2 and word[-2].isdigit() and word[-1].isdigit():
        val = int(word[-2]) + int(word[-1])
        word.pop()
        word.pop()
        word.append(str(val))

# (()[[]])([])
if len(word) == 1 and word[0].isdigit():
    print(word[0])
else:
    print(0)