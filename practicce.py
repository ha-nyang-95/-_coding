import sys

sys.stdin = open('practice.txt', 'r')

S = input().strip()
S_d = S[::-1]
if S == S_d:
    print(1)
else:
    print(0)
