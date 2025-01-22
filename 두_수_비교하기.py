import sys

sys.stdin = open('practice.txt', 'r')

A, B = map(int, input().split())
if A > B:
    print('>')
elif B > A:
    print('<')
else:
    print('==')
