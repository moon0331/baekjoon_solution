def solution(table, languages, preference):
    job_info = {}
    for t in table:
        ts = t.split()
        job_info[ts[0]] = ts[1:] # 5 4 3 2 1 이므로 점수는 5-idx
    pref_dict = {x:val for x, val in zip(languages, preference)}

    print(job_info)
    print(pref_dict)

    answer = ''
    max_score = 0
    
    for job in job_info:
        job_score = [5-job_info[job].index(lang) if lang in job_info[job] else 0 for lang in pref_dict.keys()]
        lang_score = list(pref_dict.values())
        score = sum(x*y for x, y in zip(job_score, lang_score))
        if score > max_score or (score==max_score and answer > job):
            answer = job
            max_score = score

    return answer



print(solution(
    ["SI JAVA JAVASCRIPT SQL PYTHON C#", 
    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
    "GAME C++ C# JAVASCRIPT C JAVA"],

    ["PYTHON", "C++", "SQL"],

    [7,5,5]

    ) == "HARDWARE"
)

print(solution(
    ["SI JAVA JAVASCRIPT SQL PYTHON C#", 
    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
    "GAME C++ C# JAVASCRIPT C JAVA"],

    ["JAVA", "JAVASCRIPT"],

    [7,5]

    ) == "PORTAL"
)