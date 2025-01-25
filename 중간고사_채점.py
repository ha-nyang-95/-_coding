import sys

sys.stdin = open('practice.txt', 'r')

N, M = map(int, input().split())
score = list(map(int, input().split()))
stu = [list(input().split()) for _ in range(M)]

# 초기값 설정 (수험 번호와 점수)
test_sum = -1  # 최고 점수를 -1로 초기화 (모든 점수가 0일 경우 대비)
max_stu = float('inf')  # 학생 번호를 무한대로 초기화 (최소 번호를 찾기 위해)

for i in stu:
    score_sum = 0
    for j in range(1, N + 1):
        if i[j] == 'O':
            score_sum += score[j - 1]

    if score_sum > test_sum:
        test_sum = score_sum
        max_stu = int(i[0])
    elif score_sum == test_sum:
        max_stu = min(max_stu, int(i[0]))

print(max_stu, test_sum)
