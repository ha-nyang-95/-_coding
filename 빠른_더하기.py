# import sys
#
# sys.stdin = open('practice.txt', 'r')
#
# T = int(input())
# num = [list(map(int, input().split())) for _ in range(T)]
# for A, B in num:
#     print(A + B)


import sys
sys.stdin = open('practice.txt', 'r')
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)
