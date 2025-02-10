# import sys
# sys.stdin = open('/Users/chulhwanjang/boj/practice.txt','r')

N = int(input())
num = [input()[0] for _ in range(N)]
num_set = sorted(set(num))
result = []
for i in num_set:
    if num.count(i) >= 5:
        result.append(i)
    else:
        pass
if not result:
    print('PREDAJA')
else:
    print(''.join(result))
