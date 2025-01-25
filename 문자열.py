import sys

sys.stdin = open('practice.txt', 'r')

T = int(input())
for i in range(T):
    st = input().strip()
    print(f'{st[0]}{st[len(st) - 1]}')
