T = int(input())

for i in range(T):
    N=int(input())
    print(f'{N//25} {N%25//10} {N%25%10//5} {N%25%10%5//1}')
