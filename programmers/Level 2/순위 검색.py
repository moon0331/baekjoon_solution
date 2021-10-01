import re
from collections import defaultdict

# class Person:
#     def __init__(self, info):
#         self.info_list = info.split()
#         self.info_list[-1] = int(self.info_list[-1])

#         self.language = self.info_list[0]
#         self.job = self.info_list[1]
#         self.career = self.info_list[2]
#         self.soulfood = self.info_list[3]
#         self.score = self.info_list[4]

#     def __repr__(self):
#         return str(self.info_list)

#     def get_query(self, query):
#         self.query = [tok for tok in re.split(' |and', query) if tok]
#         self.query[-1] = int(self.query[-1])

#     def is_satisfied(self):
#         for p_info, q_info in zip(self.info_list, self.query):
#             if isinstance(q_info, int) and p_info >= q_info:
#                 pass
#             elif q_info == '-' or p_info == q_info:
#                 pass
#             else:
#                 return False
#         return True

class Info:
    def __init__(self):
        self.info = defaultdict(list)
    
    def write(self, info_list):
        for info in info_list:
            lang, job, career, soulfood, score = info.split()
            score = int(score)
            self.info[f'{lang}{job}{career}{soulfood}'].append(score)

    def find(self, query):
        q_info = [tok for tok in re.split(' |and', query) if tok]
        q_info, score = q_info[:-1], int(q_info[-1])
        q_info = [tok if tok != '-' else '' for tok in q_info]
        self.search_score(q_info, score)

    def search_score(self, key, score):
        for info_key in self.info:
            if all([w in info_key for w in key]):
                binary_search()

def solution(info, query):
    pass

# def solution(info, query):
    answer = []
    person_info = [Person(p_info) for p_info in info]
    for q in query:
        tmp = 0
        for p in person_info:
            p.get_query(q)
            if p.is_satisfied():
                tmp += 1
        answer.append(tmp)

    return answer

info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
    ]

query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
    ]

print(solution(info, query) == [1,1,1,1,2,4])