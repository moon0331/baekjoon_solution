ans = 0

croatia_alphabet = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')

word = input()

for i, c in enumerate(croatia_alphabet):
    if c in word:
        while c in word:
            word = word.replace(c, str(i))
        ans += 1
        
print(len(word))