import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
mul = 1
for i in range(1, N + 1):
    mul *= i
print(mul)
