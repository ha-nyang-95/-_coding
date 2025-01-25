import sys
sys.stdin = open('practice.txt','r')

eng=input().strip()
i=int(input())
print(eng[i-1])