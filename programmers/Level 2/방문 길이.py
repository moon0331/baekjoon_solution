def get_road(coord, dir):
    x, y = coord
    if dir == 'U':
        new_coord = (x, y+1) if y<=4 else (x, y)
    elif dir == 'D':
        new_coord = (x, y-1) if y >= -4 else (x, y)
    elif dir == 'R':
        new_coord = (x+1, y) if x <= 4 else (x, y)
    elif dir == 'L':
        new_coord = (x-1, y) if x >= -4 else (x, y)
    return coord, new_coord

def get_road_form(coord, new_coord):
    return str(sorted([coord, new_coord])) #(방향 다른 것 서로 같게 만들고, hashable하게 만들기 위해)

def solution(dirs):
    road = set()
    coord = (0,0)
    for dir in dirs:
        coord, new_coord = get_road(coord, dir)
        if coord != new_coord:
            road.add(get_road_form(coord, new_coord))
        coord = new_coord
    return len(road)

print(solution("ULURRDLLU") == 7)
print(solution("LULLLLLLU") == 7)

## (시작지점-끝지점) 과 (끝지점-시작지점) 동시에 저장하고 그 크기를 2로 나누어서 저장?