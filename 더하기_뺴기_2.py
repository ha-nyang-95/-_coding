import sys

sys.stdin = open('practice.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{test_case}: {A + B}')
