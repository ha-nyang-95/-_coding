# import sys
# sys.stdin = open('problems/11005/testcases/1/input.txt','r')
num_36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A, B = map(int, input().split())
num = []
while A >= B:
    num.append(A % B)
    A = A // B
print(num_36[A], end="")
for i in range(len(num) - 1, -1, -1):
    print(num_36[num[i]], end="")
