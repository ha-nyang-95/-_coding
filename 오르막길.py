import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
num = list(map(int, input().split()))

max_height = 0  # 오르막길 최대 높이
current_height = 0  # 현재 오르막길 높이

# 한 번의 반복으로 오르막길 계산
for i in range(1, N):
    if num[i] > num[i - 1]:  # 이전 값보다 크면 오르막길
        current_height += num[i] - num[i - 1]
    else:  # 오르막길이 끝났으면 초기화
        max_height = max(max_height, current_height)
        current_height = 0

# 마지막 오르막길 고려
max_height = max(max_height, current_height)

print(max_height)