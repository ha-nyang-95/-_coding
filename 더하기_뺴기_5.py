import sys

sys.stdin = open('practice.txt', 'r')


for line in sys.stdin:
    A, B = map(int, line.split())
    print(A + B)
