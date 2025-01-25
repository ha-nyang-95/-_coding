import sys

sys.stdin = open('practice.txt', 'r')

N, M = map(int, input().split())
num = list(map(int, input().split()))


def jack():
    test_1 = 0
    test_2 = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                test_1 = num[i] + num[j] + num[k]
                if test_1 == M:
                    return test_1
                elif test_1 < M:
                    test_2 = max(test_1, test_2)
                else:
                    pass
    return test_2


print(jack())
