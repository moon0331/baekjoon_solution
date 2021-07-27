import string

word = input()
result = []
for c in string.ascii_lowercase:
    result.append(word.find(c))
print(*result)

print(*[input().find(c) for c in string.ascii_lowercase])

# print(*map(input().find,map(chr,range(97,123))))