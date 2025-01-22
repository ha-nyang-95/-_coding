import sys

sys.stdin = open('practice.txt', 'r')

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A + B)
