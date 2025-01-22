import sys

sys.stdin = open('practice.txt', 'r')

X = int(input())
N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
sum_num = 0
for a, b in num:
    sum_num += a * b
if X == sum_num:
    print('Yes')
else:
    print('No')
