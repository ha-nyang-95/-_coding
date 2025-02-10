import sys
sys.stdin = open('/Users/chulhwanjang/boj/practice.txt','r')

english=''
while True:
    try:
        line=input().strip()
        english+=line.replace(' ','')
    except EOFError:
        break

alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alp_num=[0 for _ in range(len(alp))]
for i in english:
    alp_num[alp.index(i)]+=1

alp_result=''
for j in range(len(alp_num)):
    if alp_num[j]==max(alp_num):
        alp_result+=alp[j]

print(alp_result)