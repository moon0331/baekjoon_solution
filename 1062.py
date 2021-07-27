from itertools import combinations

N, K = (int(x) for x in input().split())

words = []
words_can_read = []
learned = ['a', 'n', 't', 'i', 'c']
total_word = []

for _ in range(N):
    new_word = input()
    words.append(new_word)
    words_can_read.append([True if c in learned else False for c in new_word])

total_word.extend(c for word in words for c in word)
total_word_set = set(total_word)
#print(total_word_set)

# print(N,K)
# print(words)
# print(words_can_read)

if K < 5:
    print(0)
else:
    other_alphabet = total_word_set.difference(set(learned))

    maxn = 0
    for potential_wordset in combinations(other_alphabet, K-5):
        full_wordset = list(learned) + list(potential_wordset)
        n = 0
        available_test = [1 for word in words if all([True if c in full_wordset else False for c in word]) is True]
        n = sum(available_test)
        # [True if c in learned+potential_wordset else False for c in words]
        # all() == True인 개수 세기
        #print(n, 'avilable')
        maxn = max(maxn, n)

    print(maxn)

# 시간조절