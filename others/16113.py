def determine(string, di):
    answer_sheet = [
        "######...######",
        "#####",
        "#.####.#.####.#",
        "#.#.##.#.######",
        "###....#..#####",
        "###.##.#.##.###",
        "######.#.##.###",
        "#....#....#####",
        "######.#.######",
        "###.##.#.######"
    ]
    try:
        return str(answer_sheet.index(string)), di
    except:
        return "", 1

def translate(arr, idx, period):
    concat_string = ""
    di = 0
    while idx+di < period and "".join(arr[idx+di::period]) != '.....':
        #print("".join(arr[idx+di::period]))
        concat_string += "".join(arr[idx+di::period])
        di += 1

    return determine(concat_string, di)  

def solve(N, arr):
    answer = ""
    jdx = 0
    dj = 0
    while jdx < N//5: # 가로로 훑으면서
        ans_string, dj = translate(arr, jdx, N//5)
        answer += ans_string
        jdx += dj

    return answer

N = int(input())
signal = [c for c in input()]

answer = solve(N, signal)

print(answer)