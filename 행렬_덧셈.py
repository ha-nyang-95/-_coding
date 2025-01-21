import sys

sys.stdin = open('practice.txt', 'r')

# 입력 처리
N, M = map(int, input().split())

# 행렬 A 입력
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 B 입력
B = [list(map(int, input().split())) for _ in range(N)]

# 행렬 A와 B의 합 계산 및 출력
for i in range(N):
    result = [A[i][j] + B[i][j] for j in range(M)]
    print(*result)
