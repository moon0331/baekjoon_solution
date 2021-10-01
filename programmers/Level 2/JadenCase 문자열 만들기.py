import re

def solution(s):
    splitted_string = re.findall('[ ]+|[0-9A-z]+', s)
    # return "".join(w.capitalize() for w in splitted_string)
    return "".join(w[0].upper()+w[1:].lower() for w in splitted_string)

print(solution("3people unFollowed me") == "3people Unfollowed Me")
print(solution("for the last week") == "For The Last Week")