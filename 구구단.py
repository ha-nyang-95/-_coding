import sys
sys.stdin = open('practice.txt','r')

N = int(input())
for i in range(1,10):
    print(f'{N} * {i} = {N*i}')