for _ in range(3):
    N=int(input())
    N_sum=0
    for _ in range(N):
        N_sum+=int(input())
    if N_sum>0:
        print('+')
    elif N_sum==0:
        print(0)
    else:
        print('-')

