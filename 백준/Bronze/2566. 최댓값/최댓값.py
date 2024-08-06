board = [list(map(int, input().split())) for _ in range(9)]
MAX = board[0][0]
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if board[i][j] > MAX:
            MAX = board[i][j]
            x = i
            y = j
print(MAX)
print(x + 1, y + 1)
