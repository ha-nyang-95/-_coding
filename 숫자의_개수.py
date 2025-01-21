import sys

sys.stdin = open('practice.txt', 'r')

A = int(input())
B = int(input())
C = int(input())
mul = A * B * C
for i in range(10):
    count = 0
    for j in str(mul):
        if j == str(i):
            count += 1
    print(count)
