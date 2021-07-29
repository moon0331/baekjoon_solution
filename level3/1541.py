eq_list = input().split('-')

ans_list = []

for i, eq in enumerate(eq_list):
    if not '+' in eq:
        val = int(eq)
    else:
        val = sum(map(int, eq.split('+')))
    if len(ans_list) == 0:
        ans_list.append(val)
    else:
        ans_list.append(-val)

print(sum(ans_list))