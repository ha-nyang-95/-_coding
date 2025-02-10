N=int(input())
guest=list(map(int,input().split()))
seat=[0 for _ in range(101)]
cnt=0

for i in guest:
    if seat[i]==0:
        seat[i]+=1
    else:
        cnt+=1

print(cnt)