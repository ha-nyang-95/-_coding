N=int(input())
A,B=divmod(N,5)
for i in range(A):
    if B%3!=0:
        A-=1
        B+=5
    else:
        print(A+B//3)
        break
if A==0:
    if B%3==0:
        print(B//3)
    else:
        print(-1)

