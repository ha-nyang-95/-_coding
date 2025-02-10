array=[list(map(int,input().split())) for _ in range(9)]
max_num=0
r=0
c=0
for i in range(9):
    for j in range(9):
        if max_num<=array[i][j]:
            max_num=array[i][j]
            r=i+1
            c=j+1

print(max_num)
print(r,c)