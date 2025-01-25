import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
num = list(map(int, input().split()))
print(f'{min(num)} {max(num)}')
