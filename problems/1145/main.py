num = list(map(int, input().split()))
result = 1
while True:
    count = 0
    for i in num:
        if result % i == 0:
            count += 1
    if count >= 3:
        print(result)
        break
    result += 1


