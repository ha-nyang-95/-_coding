test=[]
while True:
    line=input().strip()
    if line=='#':
        break
    test.append(line)

gather=['a','e','i','o','u']
for t in test:
    count = 0
    t_l=t.lower()
    for k in gather:
        count+=t_l.count(k)
    print(count)