import sys

sys.setrecursionlimit(2501)

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
temp_v = [[False] * m for _ in range(n)]
most_move = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] != 'H':
            board[i][j] = int(board[i][j])
            most_move[i][j] = 1
        else:
            board[i][j] = 0


def dfs(x, y):
    most = 1
    num = board[x][y]
    for dx, dy in directions:
        nx, ny = x + dx * num, y + dy * num
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
            if visited[nx][ny]:
                most = max(most, most_move[nx][ny] + 1)
                continue
            if temp_v[nx][ny]:
                return True
            temp_v[nx][ny] = True
            is_cycle = dfs(nx, ny)
            if is_cycle:
                return True
            most = max(most, most_move[nx][ny] + 1)
            temp_v[nx][ny] = False
    most_move[x][y] = most
    visited[x][y] = True
    return False


temp_v[0][0] = True
cycle = dfs(0, 0)
if cycle:
    print(-1)
else:
    print(max(max(line) for line in most_move))
