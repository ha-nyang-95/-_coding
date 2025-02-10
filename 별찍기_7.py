import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
for i in range(2 * N - 1):
    if i < N - 1:
        print(' ' * (N - 1 - i) + '*' * (2 * (i + 1) - 1))
    elif i == N - 1:
        print('*' * (2 * N - 1))
    else:
        print(' ' * (i - N + 1) + '*' * (4 * N - 2 * i - 3))
