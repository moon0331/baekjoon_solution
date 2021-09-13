def solution(genres, plays):
    genre_set = set(genres)
    genre_cnt = {genre:0 for genre in genre_set}
    genre_info = {genre:[] for genre in genre_set}
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_cnt[g] += p
        genre_info[g].append((p, i))

    genre_ranking = sorted(list(genre_cnt.keys()), key=lambda x:-genre_cnt[x])
    # print(genre_cnt)
    # print(genre_ranking)

    for k in genre_info:
        genre_info[k].sort(key=lambda x: (-x[0], x[1]))
        # print(k, genre_info[k])
    
    answer = []
    for k in genre_ranking:
        answer.append(genre_info[k][0][1])
        if len(genre_info[k]) >= 2:
            answer.append(genre_info[k][1][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4,1,3,0])
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 150, 2500]) == [4,1,0,2])
print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1, 2, 4])
print(solution(['B', 'A'], [500, 600]) == [1, 0])
print(solution(['B'], [500]) == [0])
print(solution(['B', 'A'], [600, 500]) == [0, 1])
print(solution(['A', 'B'], [600, 500]) == [0, 1])
print(solution(['A', 'A', 'B'], [600, 500, 300]) == [0, 1, 2])
print(solution(['A', 'B', 'A'], [600, 500, 600]) == [0, 2, 1])
print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
print(solution(['A', 'A', 'A'], [3, 2, 1]) == [0, 1])
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['classic'], [2500]) == [0])
print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]) == [2, 1, 0, 3])
print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) == [3, 0, 2])
print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])
print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])