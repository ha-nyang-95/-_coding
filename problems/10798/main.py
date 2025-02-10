ch=[list(map(str,input().strip())) for _ in range(5)]
ch_max=0
for l in range(5):
    ch_max=max(ch_max,len(ch[l]))
for i in range(ch_max):
    for j in range(5):
        if len(ch[j])-1<i:
            print('',end='')
        else:
            print(ch[j][i],end='')
