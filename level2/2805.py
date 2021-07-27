import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(trees)

result = 0

while left <= right:
    center = int((left+right)/2)
    tree_val = sum([tree-center if tree>center else 0 for tree in trees]) # 가져갈 수 있는 나무 길이
    if tree_val >= M: # 충분히 가져갈 수 있으면
        left = center + 1 # 범위를 더 좁혀보자
        if result < center: # 정답 기준점 재설정 (더 높은 데서도 M 길이 만큼 가져갈 수 있으므로 업데이트)
            result = center
    else:
        right = center - 1 # 못가져가면 아래쪽 절반에서 탐색 

print(result)