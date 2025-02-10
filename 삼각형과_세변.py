import sys

sys.stdin = open('practice.txt', 'r')
num = []
while True:
    line = input().strip()
    if line == '0 0 0':
        break
    num += [list(map(int, line.split()))]
for i in range(len(num)):
    num[i].sort()
    if num[i][2] >= num[i][0] + num[i][1]:
        print('Invalid')
    else:
        if num[i][0] == num[i][1] == num[i][2]:
            print('Equilateral')
        elif num[i][0] != num[i][1] != num[i][2]:
            print('Scalene')
        else:
            print('Isosceles')
