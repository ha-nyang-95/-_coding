S1, S2, S3 = map(int, input().split())
S4 = []

# 주사위의 전체 경우의 수를 더한 전체 값을 S4에 저장
for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            S4.append(i + j + k)

# S1,S2는 20까지, S3는 40까지이므로 가장 큰 수는 80이다.
# 그래서 arr이라는 80번까지의 배열을 만들어 어떤 숫자가 많이 나왔는지
# 카운터 할 것이다. 후에 이 배열에서 인덱스를 활용하여 가장 많이 나온 숫자를 찾을 수 있다.
arr = [0] * 81
for t in S4:
    arr[t] += 1

print(arr.index(max(arr)))


