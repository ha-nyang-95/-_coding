import time

t = time.time()

N = int(input())
num_1 = list(map(int, input().split()))
M = int(input())
num_2 = list(map(int, input().split()))
# num_3 = [0] * M
num_dic={}

# for i in range(len(num_2)):
#     # num_2에 숫자를 하나 뽑아 num_1에 숫자가 있는지 확인 후
#     # 있다면 조건문 안으로 들어가 num_1 숫자 하나 하나와 비교해
#     # 몇 개 있는지 num_3에 카운트한다.
#     if num_2[i] in num_1:
#         for a in num_1:
#             if a == num_2[i]:
#                 num_3[i] += 1

# num_1에서 숫자 하나를 뽑아 num_2에 있는지 확인 후
# 있다면, 몇 번째 인덱스인지 찾아, 그 인덱스 위치에 num_3 값 +1
# for a in num_1:
#     if a in num_2:
#         # num_3[num_2.index(a)]+=1
#         for i in range(M):
#             if a == num_2[i]:
#                 num_3[i] += 1
#                 break

for a in num_1:
    if a in num_dic:
        num_dic[a]+=1
    else:
        num_dic[a]=1

for b in num_2:
    if b in num_dic:
        print(num_dic[b],end=' ')
    else:
        print(0, end=' ')


# print(*num_3)
print()
print(time.time() - t)
