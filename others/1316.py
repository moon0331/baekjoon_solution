N = int(input())
cnt = N

for _ in range(N):
    st = []
    word = input()
    for c in word:
        if c not in st:
            st.append(c)
        elif st[-1] != c:
            cnt -= 1
            break
        
print(cnt)