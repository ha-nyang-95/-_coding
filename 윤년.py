import sys

sys.stdin = open('practice.txt', 'r')

Y = int(input())
if Y % 4 == 0:
    if Y % 100 != 0 or Y % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)