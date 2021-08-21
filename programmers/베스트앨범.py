from collections import defaultdict
import heapq

def solution(genres, plays):
    genre_cnt = defaultdict(int)
    genre_songs = defaultdict(list)

    for g, p in zip(genres, plays):
        genre_cnt[g] += p

    for idx in range(len(genres)):
        genre_songs[genres[idx]].append((plays[idx], idx))

    for k in genre_songs:
        genre_songs[k].sort(key = lambda x: -x[0])

    genre_ranking = sorted(genre_cnt, reverse=True) # 랭킹순

    answer = []
    for genre in genre_ranking:
        try:
            answer.append(genre_songs[genre][0][1])
            answer.append(genre_songs[genre][1][1])
        except:
            pass

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4,1,3,0])
