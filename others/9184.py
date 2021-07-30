# memoization
import sys

def print_W(*args):
    val = W(*args)
    print('w({}, {}, {}) = {}'.format(a, b, c, val))

def W(ans, a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return W(ans, 20, 20, 20)
    if ans[a][b][c]:
        return ans[a][b][c]
    elif a< b < c:
        ans[a][b][c] = W(ans, a, b, c-1) + W(ans, a, b-1, c-1) - W(ans, a, b-1, c)
        return ans[a][b][c]
    else:
        ans[a][b][c] = W(ans, a-1, b, c) + W(ans, a-1, b-1, c) + W(ans, a-1, b, c-1) - W(ans, a-1, b-1, c-1)
        return ans[a][b][c]

ans = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print_W(ans, a, b, c)