chess_board = [list(input().strip()) for _ in range(8)]
count = 0

for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):
        if i % 2 == 0 and j % 2 == 0:
            if chess_board[i][j] == 'F':
                count += 1
        elif i % 2 == 1 and j % 2 == 1:
            if chess_board[i][j] == 'F':
                count += 1

print(count)
