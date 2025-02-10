N=input().strip()
N_set=[]
for i in range(10):
    N_set.append(N.count(f'{i}'))
N_set[6]=(N_set[6]+N_set[9]+1)//2
N_set[9]=0
print(max(N_set))

