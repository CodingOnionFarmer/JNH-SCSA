n, m = map(int, input().split())
board = [input() for _ in range(n)]
size = min(n, m)
rect = False
while size > 1:
    for i in range(n - size + 1):
        if rect:
            break
        for j in range(m - size + 1):
            if board[i][j] == board[i + size - 1][j] == board[i][j + size - 1] == board[i + size - 1][j + size - 1]:
                rect = True
                break
    if rect:
        break
    size -= 1
print(size ** 2)
