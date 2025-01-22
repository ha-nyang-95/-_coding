import sys

sys.stdin = open('practice.txt', 'r')

N = int(input())
N_div = N // 4
print(f'{'long ' * N_div}int')
