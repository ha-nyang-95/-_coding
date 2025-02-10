T = int(input())

for tc in range(T):
    input()
    N, M = map(int, input().split())
    n = sorted(list(map(int, input().split())))
    m = sorted(list(map(int, input().split())))

    SG = SB = 0
    while SB < N and SG < M:
        if n[SB] >= m[SG]:
            SG += 1
        else:
            SB += 1

    if SG > SB:
        print('S')
    elif SB > SG:
        print('B')
    else:
        print('C')



## 정답
# t = int(input())
# for i in range(t):
#     input()
#     N, M = map(int, input().split())
#     sj = sorted(list(map(int, input().split())), reverse=True)
#     sb = sorted(list(map(int, input().split())), reverse=True)
#
#     while sj and sb:
#         if sj[-1] >= sb[-1]:
#             sb.pop()
#         else:
#             sj.pop()
#
#     if sj:
#         print('S')
#     elif sb:
#         print('B')
#     else:
#         print('C')