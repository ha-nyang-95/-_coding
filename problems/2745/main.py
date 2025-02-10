num_36='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
A,B=map(str,input().split())
sum=0
for i in range(len(A)):
    sum+=(num_36.find(A[i]))*(int(B)**(len(A)-1-i))
print(sum)