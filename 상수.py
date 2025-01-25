import sys

sys.stdin = open('practice.txt', 'r')

A, B = input().split()
t = ''
k = ''
t = A[::-1]
k = B[::-1]
print(max(int(t), int(k)))
