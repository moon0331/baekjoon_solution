from collections import Counter

N = int(input())

values = []

for _ in range(N):
    values.append(int(input()))

values.sort()

print(round(sum(values)/N))
print(values[N//2])

most_common = Counter(values)
maxval = max(most_common[x] for x in most_common)
most_common_values = [x for x in most_common if most_common[x]==maxval]
if len(most_common_values) == 1:
    print(most_common_values[0])
else:
    print(sorted(most_common_values)[1])

print(max(values)-min(values))