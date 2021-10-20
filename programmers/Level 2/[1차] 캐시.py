from collections import deque

def solution(cacheSize, cities):
    time = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            cache.append(city)

    return time

xyz = [
    (3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"], 50), 
    (3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"], 21), 
    (2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], 60), 
    (5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], 52),
    (2, ["Jeju", "Pangyo", "NewYork", "newyork"], 16),
    (0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"], 25)
]

for x, y, z in xyz:
    print(solution(x, y) == z)