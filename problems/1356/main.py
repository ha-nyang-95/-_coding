N=input().strip()
count_bool=0
for i in range(len(N)-1):
    N_1=int(N[i])
    N_2=int(N[i+1])
    for j in range(i):
        N_1*=int(N[j])
    if i+2<len(N):
        for k in range(i+2,len(N)):
            N_2*=int(N[k])
    if N_1==N_2:
        print('YES')
        count_bool+=1
        break
if count_bool==0:
    print('NO')
