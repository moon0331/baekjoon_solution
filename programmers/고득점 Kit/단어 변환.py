from collections import deque

def connected(x, y):
    distance = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            distance += 1
    return distance == 1

def solution(begin, target, words):
    visited = {word:False for word in words+[target]}
    q = deque([(begin,0)])
    while q:
        word, n_step = q.popleft()
        for next_word in words:
            if not visited[next_word] and connected(word, next_word):
                q.append((next_word, n_step+1))
                visited[next_word] = True
                if visited[target]:
                    return n_step+1

    return 0 # not reachable

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0)