N = input().strip()
F = int(input())
N = int(N[:-2] + '00')

if N % F == 0:
    print('00')
else:
    result = F - N % F
    print(f'{result:02d}')


