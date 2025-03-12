import sys
import time
a=time.time()

K, N = map(int, sys.stdin.readline().split())
line = sorted([int(sys.stdin.readline()) for _ in range(K)], reverse=True)
result = 0
for i in range(2, N + 1):
    test = i
    value = line[0] // i
    for n in line[1:]:
        test += n // value

    if test >= N:
        result = max(result, value)

print(result)

print(time.time()-a)