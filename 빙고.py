import sys

sys.stdin = open('practice.txt', 'r')

array = [list(map(int, input().split())) for _ in range(5)]  # 빙고판
num = [list(map(int, input().split())) for _ in range(5)]  # 사회자


def bingo():
    count = 0
    for t in num:  # 사회자가 부르는 숫자 한줄
        for k in range(len(t)):  # 사회자가 부르는 숫자 한줄의 한개의 숫자
            result = 0
            count += 1
            count_c_1 = 0
            count_c_2 = 0
            for l in range(len(array)):  # 빙고판 각 줄
                if t[k] in array[l]:
                    array[l][array[l].index(t[k])] = 'x'
            for i in range(len(array)):
                count_r = 0
                count_c = 0
                if array[i][i] == 'x':
                    count_c_1 += 1
                if array[i][len(array) - 1 - i] == 'x':
                    count_c_2 += 1
                for j in range(len(array)):
                    if array[i][j] == 'x':
                        count_r += 1
                    if array[j][i] == 'x':
                        count_c += 1
                if count_c == 5:
                    result += 1
                if count_r == 5:
                    result += 1
                if count_c_1 == 5:
                    result += 1
                if count_c_2 == 5:
                    result += 1

            if result >= 3:
                return count


print(bingo())


def check(tmp):
    # 가로
    for i in range(5):
        if bingo[i] == [0] * 5:
            tmp += 1
    # 세로
    for i in range(5):
        if all(bingo[j][i] == 0 for j in range(5)):
            tmp += 1
    # 대각선1
    if all(bingo[i][i] == 0 for i in range(5)):
        tmp += 1
    # 대각선2
    if all(bingo[i][4 - i] == 0 for i in range(5)):
        tmp += 1
    return tmp

bingo = [list(map(int, input().split())) for _ in range(5)]
speak = []
for _ in range(5):
    speak += list(map(int, input().split()))
cnt = 0
tmp = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if speak[i] == bingo[x][y]:
                bingo[x][y] = 0
                cnt += 1
    if cnt >= 12:
        result = check(tmp)
        if result >= 3:
            print(i + 1)  # 배열은 0 부터 시작했으므로
            break
