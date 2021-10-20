from math import inf
from itertools import combinations

def calculate_xy(line1, line2):
    a, b, e = line1
    c, d, f = line2

    if a*d-b*c == 0:
        return None
    else:
        return (b*f-e*d)/(a*d-b*c), (e*c-a*f)/(a*d-b*c)

def valid(xy):
    try:
        x, y = xy
        return int(x) == x and int(y) == y
    except:
        return False

def redefine_coordinate(coordinate, maxy, maxx):
    return [(maxy-y, maxx+x) for x, y in coordinate]

def draw_star(coordinate):
    minx = miny = inf
    maxx = maxy = -inf
    for x, y in coordinate:
        minx, miny = min(minx, x), min(miny, y)
        maxx, maxy = max(maxx, x), max(maxy, y)

    picture = [['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    new_coordinate = redefine_coordinate(coordinate, maxy, maxx)
    for x, y in new_coordinate:
        picture[x][y] = '*'

    return ["".join(line) for line in picture]

def solution(line):
    coordinate = []
    for line1, line2 in combinations(line, 2):
        xy = calculate_xy(line1, line2)
        if valid(xy):
            coordinate.append(tuple(int(v) for v in xy))
    answer = draw_star(coordinate)
    return answer


example = [
    ([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]], ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]), 
    ([[0, 1, -1], [1, 0, -1], [1, 0, 1]], ["*.*"]),
    ([[1, -1, 0], [2, -1, 0]], ["*"]),
    ([[1, -1, 0], [2, -1, 0], [4, -1, 0]], ["*"])
]

for x, y in example:
    print(solution(x) == y)

# 다시 체크해보기