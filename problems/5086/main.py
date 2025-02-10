num=[]
while True:
    line=list(map(int,input().split()))
    if line==[0,0]:
        break
    num.append(line)

for i in range(len(num)):
    if num[i][0]>num[i][1]:
        if num[i][0]%num[i][1]==0:
            print('multiple')
        else:
            print('neither')
    elif num[i][0]<num[i][1]:
        if num[i][1]%num[i][0]==0:
            print('factor')
        else:
            print('neither')


            