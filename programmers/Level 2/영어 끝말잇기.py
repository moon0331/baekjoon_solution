def solution(n, words):
    prev_word = words[0][0]
    used_word = set()
    for order, word in enumerate(words):
        # print(f'prev_word = {prev_word}, word = {word}')
        if word in used_word or prev_word[-1] != word[0]: # 종료 조건
            return [order%n+1, order//n+1] # 몇번째 사람, 몇번째 순서
        else:
            prev_word = word
            used_word.add(word)

    return [0, 0] 

ns = [3, 5, 2]
wordset = [
    ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"],
    ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"],
    ["hello", "one", "even", "never", "now", "world", "draw"]
]
results = [[3,3], [0,0], [1,3]]

for n, w, r in zip(ns, wordset, results):
    print(solution(n,w) == r)