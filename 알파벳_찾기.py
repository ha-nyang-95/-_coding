import sys

sys.stdin = open('practice.txt', 'r')

S = input().strip()
alp = 'abcdefghijklmnopqrstuvwxyz'
for i in alp:
    print(S.find(i), end=' ')
