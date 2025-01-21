import sys

sys.stdin = open('practice.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    score = list(map(int, input().split()))
    m = sum(score[1:]) / score[0]
    count = 0
    for i in range(1, score[0] + 1):
        if score[i] > m:
            count += 1
    result = count / score[0] * 100
    print(f'{result:.3f}%')
