import sys

sys.stdin = open('practice.txt', 'r')

A, B, V = map(int, input().split())
# h = 0
# count = 0
# while True:
#     count += 1
#     h += A
#     if h >= V:
#         print(count)
#         break
#     else:
#         h -= B

print(-(-(V-A)//(A-B))+1)

