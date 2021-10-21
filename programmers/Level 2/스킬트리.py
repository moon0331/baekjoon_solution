# import re
# from string import ascii_uppercase

# def solution(skill, skill_trees):
#     legacy_skill = re.sub(f'[{skill}]','',ascii_uppercase)
#     for skill_tree in skill_trees:
#         skill_summary = re.sub(f'[{legacy_skill}]', '', skill_tree)
#         print(skill_summary)
#     return answer

def solution(skill, skill_trees):
    

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]) == 2)