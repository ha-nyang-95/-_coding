N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
for b in B:
    if b in A:
        print(1)
    else:
        print(0)
# for b in B:
#     for a in A:
#         if a == b:
#             print(1)
#             break
#     else:
#         print(0)
