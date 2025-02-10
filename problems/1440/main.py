import sys
sys.stdin=open('/Users/chulhwanjang/boj/practice.txt','r')

# 철환 버전
# 솔찬히 더 간단하다고 생각하나 백준에서는 틀림
time_num = list(map(int, input().split(':')))
cnt = 0
for i in time_num:
    if 1 <= i <= 12:
        cnt += 1
print(cnt * 2)


# # 정답
# n1, n2, n3 = map(int,input().split(":"))
# cnt = 0
#
# # 시 01-12, 분 00-59, 초 00-59
#
# #1. 3가지 숫자 모두 1-12: 6가지
# #2. 2가지 숫자 1-12 : 4가지
# #3. 1가지 숫자 1-12 : 2가지
# #4. 모두 0 : 0가지
#
# if n1==0 and n2==0 and n3==0:
#   cnt += 0
# if 0<n1<13 and 0<=n2<60 and 0<=n3<60:
#   cnt += 2
# if 0<n2<13 and 0<=n1<60 and 0<=n3<60:
#   cnt += 2
# if 0<n3<13 and 0<=n1<60 and 0<=n2<60:
#   cnt += 2
#
# print(cnt)