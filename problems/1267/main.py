N=int(input())
m=list(map(int,input().split()))

Y=0
M=0
for i in m:
    Y+=(i//30+1)*10
    M+=(i//60+1)*15
if Y>M:
    print('M',M)
elif Y<M:
    print('Y',Y)
else:
    print('Y','M',Y)