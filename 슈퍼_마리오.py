import sys

sys.stdin = open('practice.txt', 'r')

num = [int(input()) for _ in range(10)]


def sum_num():
    sum_num_1 = 0
    for i in num:
        sum_num_1 += i
        if sum_num_1 >= 100:
            if abs(sum_num_1 - 100) <= abs(100 - sum_num_1 + i):
                return sum_num_1
            else:
                return sum_num_1 - i
    return sum_num_1


print(sum_num())

# for i in range(len(num)):
#     while sum_num_1 < 100:
#         sum_num_1 += num[i]
#     if sum_num_1 - 100 >= sum_num_1 - num[i - 1] - 100:
#         print(sum_num_1)
#     else:
#         print(sum_num_1 - num[i - 1])
