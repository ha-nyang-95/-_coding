# import sys
# sys.stdin = open('problems/1236/testcases/1/input.txt','r')
N,M=map(int,input().split())
num_row=[i for i in range(N)]
num_col=[j for j in range(M)]
castle=[list(map(str,input().strip())) for _ in range(N)]
for r in range(N):
    for c in range(M):
        if castle[r][c]=='X':
            if r in num_row:
                num_row.remove(r)
            if c in num_col:
                num_col.remove(c)
print(max(len(num_row),len(num_col)))



