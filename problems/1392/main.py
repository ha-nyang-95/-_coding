N, Q = map(int, input().split())
num = [int(input()) for _ in range(N)]
num_time = [int(input()) for _ in range(Q)]
num_ly = []
for i in range(N):
    num_ly.extend([i + 1] * num[i])
for j in range(Q):
    print(num_ly[num_time[j]])
