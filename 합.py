import sys

sys.stdin = open('practice.txt', 'r')

n = int(input())
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print(sum_n)
