import sys
sys.stdin = open('practice.txt','r')

num=[int(input()) for _ in range(9)]
num2=num[:]
num.sort()
num3 = num2.index(num[8])+1
print(num[8])
print(num3)