directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
# spread_directions = ((7, 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7), (6, 7, 0))

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    click = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                board[i][j] = 0
            else:
                board[i][j] = 10
                visited[i][j] = True
    for i in range(n):
        for j in range(n):
            if board[i][j] > 9:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        board[ni][nj] += 1
    for i in range(n):
        for j in range(n):
            if not board[i][j] and not visited[i][j]:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if board[ni][nj] > 9:
                            break
                else:
                    click += 1
                    visited[i][j] = True
                    spread = []
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                            visited[ni][nj] = True
                            if not board[ni][nj]:
                                spread.append((ni, nj))
                    while spread:
                        next_spread = []
                        for ci, cj in spread:
                            for di, dj in directions:
                                ni, nj = ci + di, cj + dj
                                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                                    visited[ni][nj] = True
                                    if not board[ni][nj]:
                                        next_spread.append((ni, nj))
                        spread = next_spread
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                click += 1

    print(f'#{tc} {click}')
