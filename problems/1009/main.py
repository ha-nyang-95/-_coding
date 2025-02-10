T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     print((a ** b) % 10)

for _ in range(T):
    a, b = map(int, input().split())
    test = a % 10

    if test == 0:
        print(10)
    elif test == 1 or test == 5 or test == 6:
        print(test)
    elif test == 4 or test == 9:
        if b % 2 == 0:
            print((test ** 2) % 10)
        else:
            print(test)
    else:
        if b % 4 == 0:
            print((test ** 4) % 10)
        else:
            print((test ** (b % 4)) % 10)

