def tri(x, reverse=False):
    ans = ''
    while x:
        ans += str(int(x%3))
        x = (x-(x%3))/3
    return ans[::1 if reverse else -1]

def solution(n):
    return int(tri(n, True), 3)

print(solution(45) == 7)
print(solution(125) == 229)