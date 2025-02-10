test=[]
while True:
    line=input().strip()
    if line=='0':
        break
    test.append(line)

for i in test:
    if i==i[::-1]:
        print('yes')
    else:
        print('no')