import sys

sys.stdin = open('practice.txt', 'r')

num = list(map(int, input().split()))
if num[0] == num[1] == num[2]:
    print(10000 + num[0] * 1000)
elif num[0] == num[1] or num[1] == num[2] or num[2] == num[0]:
    if num[0] == num[1] or num[1] == num[2]:
        print(1000 + num[1] * 100)
    else:
        print(1000 + num[2] * 100)
else:
    max_num = max(num)
    print(max_num * 100)
