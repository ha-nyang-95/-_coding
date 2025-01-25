import sys

sys.stdin = open('practice.txt', 'r')

num = [int(input()) for _ in range(10)]
test = []
for i in range(10):
    test.append(num[i] % 42)
print(len(set(test)))
