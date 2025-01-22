import sys

sys.stdin = open('practice.txt', 'r')

T = int(input())
num = [list(map(int, input().split())) for _ in range(T)]
for A, B in num:
    print(A + B)
