import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
for i in range(1, N + 1):
    star = '*' * i
    print("{:>{width}}".format(star, width=N))
