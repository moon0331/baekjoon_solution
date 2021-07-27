import sys

C = int(input())

for _ in range(C):
    scores = list(map(int, sys.stdin.readline().split()))[1:]
    N = len(scores)
    avg = sum(scores) / N
    good_score = list(map(lambda x:1 if x>avg else 0, scores))
    print("{:.3f}%".format(sum(good_score)/N*100))