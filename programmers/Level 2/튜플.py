import re
from collections import Counter

def solution(s):
    nums = [int(x) for x in re.findall(r'[0-9]+', s)]
    cnt_nums = Counter(nums)
    return sorted(cnt_nums.keys(),key=lambda x:-cnt_nums[x])
    
s_list = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}"	
]

results = [
    [2, 1, 3, 4],
    [2, 1, 3, 4],
    [111, 20],
    [123],
    [3, 2, 4, 1]
]

for s, r in zip(s_list, results):
    print(solution(s) == r)