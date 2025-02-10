import sys

sys.stdin = open('practice.txt', 'r')

square = [list(map(int, input().split())) for _ in range(3)]

if square[0][0] == square[1][0]:
    x = square[2][0]
elif square[0][0] == square[2][0]:
    x = square[1][0]
else:
    x = square[0][0]
if square[0][1] == square[1][1]:
    y = square[2][1]
elif square[0][1] == square[2][1]:
    y = square[1][1]
else:
    y = square[0][1]
print(x, y)
