S = input().strip().upper()
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {}
for i in alp:
    dic[i] = S.count(i)
dic_max = max(dic.values())
if list(dic.values()).count(dic_max) >= 2:
    print("?")
else:
    for k, v in dic.items():
        if v == dic_max:
            print(k)


            
