import sys
sys.stdin = open('practice.txt','r')

chess=list(map(int,input().split()))
answer=[1,1,2,2,2,8]
num=[]
for i in range(len(chess)):
    if chess[i] > answer[i]:
        num.append(answer[i]-chess[i])
    elif chess[i]<answer[i]:
        num.append(answer[i]-chess[i])
    else:
        num.append(0)
print(*num)