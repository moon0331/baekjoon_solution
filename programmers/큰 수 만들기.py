def solution(number, k):
    number = [c for c in number]
    answer = []
    
    n_pop = 0
    for i in range(len(number)):
        while answer and n_pop < k and answer[-1] < number[i]:
            answer.pop()
            n_pop += 1
        answer.append(number[i])
        
    while n_pop < k:
        answer.pop()
        n_pop += 1
    
    return "".join(answer)

numbers=["1924", "1231234", "4177252841"]
ks = [2, 3, 4]
returns = ["94", "3234", "775841"]

for n, k, r in zip(numbers, ks, returns):
    print(solution(n, k) == r)