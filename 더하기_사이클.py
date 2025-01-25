import sys
sys.stdin = open('practice.txt','r')

N=input()
if int(N)<10:
    N='0'+N
test=''
test_1=''
count=0
while N!=test:
        if count==0:
            test_1=str(int(N[0])+int(N[1]))
            if int(test_1) < 10:
                test_1 = '0' + test_1
            test = N[1] + test_1[1]
        else:
            test_1=str(int(test[0])+int(test[1]))
            if int(test_1) < 10:
                test_1 = '0' + test_1
            test = test[1] + test_1[1]
        count+=1
print(count)