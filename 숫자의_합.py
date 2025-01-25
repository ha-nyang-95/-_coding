import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
num = input().strip()
sum_num = 0
for i in num:
    sum_num += int(i)
print(sum_num)
