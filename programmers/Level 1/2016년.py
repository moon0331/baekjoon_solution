from datetime import datetime

def solution(a, b):
    target = datetime(2016, a, b)
    first = datetime(2016, 1, 1)
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(target-first).days%7]

def solution2(a, b):
    target = datetime(2016, a, b)
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return day[target.weekday()]

print(solution(5, 24) == 'TUE')
print(solution2(5, 24) == 'TUE')