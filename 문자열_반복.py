import sys

sys.stdin = open('practice.txt', 'r')

T = int(input())
for i in range(T):
    test = ''
    R, S = input().split()
    for j in range(len(S)):
        test += S[j] * int(R)
    print(test)
