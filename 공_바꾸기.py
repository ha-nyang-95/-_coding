import sys

sys.stdin = open('practice.txt', 'r')

N, M = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(M)]
basket = [k for k in range(1, N + 1)]
for i, j in num:
    test = basket[i - 1]
    basket[i - 1] = basket[j - 1]
    basket[j - 1] = test
print(*basket)
