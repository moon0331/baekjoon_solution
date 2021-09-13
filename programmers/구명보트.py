def solution(people, limit):
    n_boat = 0
    people.sort(reverse=True)

    i, j = 0, len(people)-1
    while i <= j:
        x = people[i]
        y = people[j]
        if x+y <= limit:
            n_boat += 1
            i += 1
            j -= 1
        else:
            n_boat += 1
            i += 1
    return n_boat

print(solution([70,50,80,50], 100) == 3)
print(solution([70,80,50], 100) == 3)