import sys

sys.stdin = open('practice.txt', 'r')

A, B = map(int, input().split())
C = int(input())
test = B + C
while test >= 60:
    A += 1
    test -= 60
if A >= 24:
    A -= 24
print(f'{A} {test}')
