import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
num = list(map(int, input().split()))
v = int(input())

print(num.count(v))
