import sys
sys.stdin = open('practice.txt','r')

A,B,C=map(int,input().split())
num =[A,B,C]
num.sort()
print(num[1]) 