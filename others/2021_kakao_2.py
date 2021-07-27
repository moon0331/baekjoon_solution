def getPxy(place):
    p_loc = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                p_loc.append((i,j))

    return p_loc

def distancing(place, x, y, count):
    result = 1
    print('distancing(x={}, y={}, {})'.format(x, y, count))
    if count == 0:
        #print('거리두기 됨')
        return 1
    elif count < 2 and place[x][y] == 'P':
        #print('거리두기 안됨')
        return 0

    if x+1 < 5 and place[x+1][y] != 'X':
        result *= distancing(place, x+1, y, count-1)
    if x-1 >=0 and place[x-1][y] != 'X':
        result *= distancing(place, x-1, y, count-1)
    if y+1 < 5 and place[x][y+1] != 'X':
        result *= distancing(place, x, y+1, count-1)
    if y-1 >=0 and place[x][y-1] != 'X':
        result *= distancing(place, x, y-1, count-1)
    
    return result 

places = [
    [
        "POOOP", 
        "OXXOX", 
        "OPXPX", 
        "OOXOX", 
        "POXXP"
    ], 
    
    [
        "POOPX", 
        "OXPXP", 
        "PXXXO", 
        "OXXXO", 
        "OOOPP"
    ],

    [
        "PXOPX", 
        "OXOXP", 
        "OXPXX", 
        "OXXXP", 
        "POOXX"
    ],
    
    [
        "OOOXX", 
        "XOOOX", 
        "OOOXX", 
        "OXOOX", 
        "OOOOO"
    ],

    [
        "PXPXP", 
        "XPXPX", 
        "PXPXP", 
        "XPXPX", 
        "PXPXP"
    ]    
]

places = [[
    "OOPOO", 
    "OPOOO", 
    "OOOOO", 
    "OOOOO", 
    "OOOOO"]]

def is_distancing(place, p_loc):
    for x,y in p_loc:
        if distancing(place, x, y, 2) == 0:
            return 0
    return 1

result = []
for place in places:
    p_loc = getPxy(place)
    result.append(is_distancing(place, p_loc))

print(result)

# p_loc = getPxy(places[1])
# print(p_loc)
# for x,y in p_loc:
#     print('answer =', distancing(places[1], x, y, 2))

'''
    [
        "POOPX", 
        "OXPXP", 
        "PXXXO", 
        "OXXXO", 
        "OOOPP"
    ],
'''

#https://programmers.co.kr/questions/19106