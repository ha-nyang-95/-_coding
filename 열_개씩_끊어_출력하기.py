import sys

sys.stdin = open('practice.txt', 'r')

ch = input()
for i in range(0, len(ch), 10):
    if i + 10 > len(ch):
        print(ch[i:])
    else:
        print(ch[i:i + 10])
