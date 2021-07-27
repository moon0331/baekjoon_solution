from collections import Counter

mc = Counter(input().upper())
maxval = max(mc.values())
al = [c for c in mc if mc[c]==maxval]
if len(al) == 1:
    print(al[0])
else:
    print('?')