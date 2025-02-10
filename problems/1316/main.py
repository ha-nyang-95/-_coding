T=int(input())
count=0
for i in range(T):
    S=input().strip()
    for j in range(len(S)-1):
        if S[j]!=S[j+1]:
            S_test=S[j+1:]
            if S_test.find(S[j])>0:
                S=0
                break
    if S!=0:
        count+=1
print(count)
                
    