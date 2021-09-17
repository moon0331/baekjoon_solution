from collections import Counter

def solution(participant, completion):
    p_hash = Counter(participant)
    c_hash = Counter(completion)
    answer =  p_hash - c_hash
    return list(answer.keys())[0]

participants = [
    ["leo", "kiki", "eden"], 
    ["marina", "josipa", "nikola", "vinko", "filipa"], 
    ["mislav", "stanko", "mislav", "ana"]
]

completions = [
    ["eden", "kiki"],
    ["josipa", "filipa", "marina", "nikola"],
    ["stanko", "ana", "mislav"]
]

returns = [
    "leo", "vinko", "mislav"
]

for p, c, r in zip(participants, completions, returns):
    print(solution(p, c) == r)