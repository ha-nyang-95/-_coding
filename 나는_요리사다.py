import sys

sys.stdin = open('practice.txt', 'r')

num = [list(map(int, input().split())) for _ in range(5)]
num_sum = [sum(i) for i in num]
num_max = max(num_sum)
print(f'{num_sum.index(num_max) + 1} {num_max}')
