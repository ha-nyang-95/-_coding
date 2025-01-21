import sys

sys.stdin = open('practice.txt', 'r')

N, M = map(int, input().split())
num = [n for n in range(1, N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    num[a - 1:b] = num[a - 1:b][::-1]
print(*num)
