board=[]
while True:
    line=input().strip()
    if line=='0':
        break
    board.append(line)

for i in board:
    width=len(i)+1
    for j in range(len(i)):
        if i[j]=='1':
            width+=2
        elif i[j]=='0':
            width+=4
        else:
            width+=3
    print(width)

