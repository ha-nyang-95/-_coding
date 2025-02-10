S = input().strip()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0
for i in cro:
    count += S.count(i)
    S = S.replace(i, " ")
S=S.replace(" ","")
print(count + len(S))
