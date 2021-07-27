from collections import Counter

N, K = [int(x) for x in input().split()]

available_wordlist = ['a', 'n', 't', 'i', 'c']
print()
if K < 5:
    print(0)
else:
    for _ in range(N):
        input_word = input()[4:-4]
        print(input_word)
        available_wordlist.extend([c for c in input_word])

    available_counter = Counter(available_wordlist)

    print(available_counter)

# a n t i c r