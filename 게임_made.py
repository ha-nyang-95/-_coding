import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
level = [int(input()) for _ in range(N)]
count = 0
for i in range(N - 1, 0, -1):
    while level[i] <= level[i - 1]:
        count += 1
        level[i - 1] -= 1
print(count)
