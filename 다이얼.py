import sys

sys.stdin = open('practice.txt', 'r')

S = input().strip()
count = 0
for i in S:
    if i in 'ABC':
        count += 3
    elif i in 'DEF':
        count += 4
    elif i in 'GHI':
        count += 5
    elif i in 'JKL':
        count += 6
    elif i in 'MNO':
        count += 7
    elif i in 'PQRS':
        count += 8
    elif i in 'TUV':
        count += 9
    else:
        count += 10
print(count)
