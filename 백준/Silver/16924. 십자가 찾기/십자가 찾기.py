# 구현, 시뮬레이션


n, m = map(int, input().split())
board = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
left = 0
crosses = []
for i in range(n):
    for j in range(m):
        if board[i][j] == '.':
            visited[i][j] = True
        else:
            left += 1
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == '*' and board[i][j - 1] == '*' and board[i][j + 1] == '*' and board[i - 1][j] == '*' and \
                board[i + 1][j] == '*':
            if not visited[i][j]:
                visited[i][j] = True
                left -= 1
            if not visited[i][j - 1]:
                visited[i][j - 1] = True
                left -= 1
            if not visited[i][j + 1]:
                visited[i][j + 1] = True
                left -= 1
            if not visited[i - 1][j]:
                visited[i - 1][j] = True
                left -= 1
            if not visited[i + 1][j]:
                visited[i + 1][j] = True
                left -= 1
            size = 1
            for test in range(2, min(i + 1, j + 1, n - i, m - j)):
                if board[i][j - test] == '*' and board[i][j + test] == '*' and board[i - test][j] == '*' and \
                        board[i + test][j] == '*':
                    size = test
                    if not visited[i][j - test]:
                        visited[i][j - test] = True
                        left -= 1
                    if not visited[i][j + test]:
                        visited[i][j + test] = True
                        left -= 1
                    if not visited[i - test][j]:
                        visited[i - test][j] = True
                        left -= 1
                    if not visited[i + test][j]:
                        visited[i + test][j] = True
                        left -= 1
                else:
                    break
            crosses.append((i + 1, j + 1, size))
if left:
    print(-1)
else:
    print(len(crosses))
    for cross in crosses:
        print(*cross)
