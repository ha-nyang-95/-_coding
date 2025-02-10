N=int(input())
for i in range(1,10000000):
    if i<N:
        N-=i
    else:
        break
if i%2==0:
    print(f'{N}/{i+1-N}')
else:
    print(f'{i+1-N}/{N}')