import sys

sys.stdin = open('practice.txt', 'r')

N, M = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(M)]
result = [0 for _ in range(N)]
for i, j, k in num:
    for test in range(i - 1, j):
        result[test] = k

print(*result)
