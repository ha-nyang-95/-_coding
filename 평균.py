import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
score_sum = 0
for i in range(N):
    score_sum += score[i] / max_score * 100
print(score_sum / N)
