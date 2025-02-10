# import sys
# sys.stdin = open('/Users/chulhwanjang/boj/practice.txt','r')

N = int(input())
num = list(map(int, input().split()))
cluster = int(input())
cluster_sum = 0
for i in range(N):
    if num[i] > cluster:
        if num[i]%cluster==0:
            cluster_sum += (num[i] // cluster) * cluster
        else:
            cluster_sum += (num[i] // cluster + 1) * cluster
    elif num[i] == 0:
        pass
    else:
        cluster_sum += cluster
print(cluster_sum)
