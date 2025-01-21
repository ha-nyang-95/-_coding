import sys

sys.stdin = open('practice.txt', 'r')

num = [int(input()) for _ in range(28)]
num.sort()
for i in range(1,31):
    if i not in num:
        print(i)


# # 전체 학생 집합 생성
# all_students = set(range(1, 31))
#
# # 입력받아 제출한 학생 번호 집합 생성
# submitted_students = set(int(input()) for _ in range(28))
#
# # 미제출자 번호 계산
# missing_students = sorted(all_students - submitted_students)
#
# # 출력
# print(missing_students[0])
# print(missing_students[1])