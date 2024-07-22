d = ((0, 1), (-1, 0), (0, -1), (1, 0))


def check_right(x, y):
    return any(board[x][y_] for y_ in range(y + 1, n))


def check_down(x, y):
    return any(board[x_][y] for x_ in range(x + 1, n))


def check_left(x, y):
    return any(board[x][y_] for y_ in range(y))


def check_up(x, y):
    return any(board[x_][y] for x_ in range(x))


def dfs(node, connected, wire):
    if node == c:
        if connected > best[0]:
            best[0] = connected
            best[1] = wire
        elif connected == best[0] and wire < best[1]:
            best[1] = wire
        return
    nx, ny = core[node]
    if not check_right(nx, ny):
        for ny_ in range(ny + 1, n):
            board[nx][ny_] = 1
        dfs(node + 1, connected + 1, wire + n - ny - 1)
        for ny_ in range(ny + 1, n):
            board[nx][ny_] = 0
    if not check_down(nx, ny):
        for nx_ in range(nx + 1, n):
            board[nx_][ny] = 1
        dfs(node + 1, connected + 1, wire + n - nx - 1)
        for nx_ in range(nx + 1, n):
            board[nx_][ny] = 0
    if not check_left(nx, ny):
        for ny_ in range(ny):
            board[nx][ny_] = 1
        dfs(node + 1, connected + 1, wire + ny)
        for ny_ in range(ny):
            board[nx][ny_] = 0
    if not check_up(nx, ny):
        for nx_ in range(nx):
            board[nx_][ny] = 1
        dfs(node + 1, connected + 1, wire + nx)
        for nx_ in range(nx):
            board[nx_][ny] = 0
    dfs(node + 1, connected, wire)
    return


for tc in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    core = []
    best = [0, 0]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j]:
                core.append((i, j))
    c = len(core)
    dfs(0, 0, 0)
    print(f'#{tc} {best[1]}')
