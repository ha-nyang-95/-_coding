import sys

sys.stdin = open('practice.txt', 'r')

A, B = input().split()
def same():
    for i in A:
        for j in B:
            if i == j:
                same_A = A.index(i)
                same_B = B.index(j)
                return same_A, same_B
            else:
                pass


same_A, same_B = same()

for k in range(len(B)):
    if k == same_B:
        print(A, end='')
    else:
        for l in range(len(A)):
            if l == same_A:
                print(B[k], end='')
            else:
                print('.', end='')
    print()
