import sys
from collections import Counter, defaultdict


N = int(sys.stdin.readline())
cards = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
query = map(int, sys.stdin.readline().split())

cards_cnt = defaultdict(int, Counter(cards)) # why int 

for q in query:
    print(cards_cnt[q], end=' ')