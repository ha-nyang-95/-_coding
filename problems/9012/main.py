T=int(input())
PS=[list(input().strip()) for _ in range(T)]

for i in PS:
    count=0
    for j in i:
        if j=='(':
            count+=1
        else:
            count-=1
            if count<0:
                break
    if count==0:
        print('YES')
    else:
        print('NO')