board = [list(map(int, list(input()))) for _ in range(9)]
visited_r = [[False] * 10 for _ in range(9)]
visited_c = [[False] * 10 for _ in range(9)]
visited_s = [[False] * 10 for _ in range(9)]


def check(i, j, num):
    if visited_r[i][num] or visited_c[j][num] or visited_s[i // 3 * 3 + j // 3][num]:
        return False
    return True


def visit(i, j, num):
    visited_r[i][num] = True
    visited_c[j][num] = True
    visited_s[i // 3 * 3 + j // 3][num] = True


def delete(i, j, num):
    visited_r[i][num] = False
    visited_c[j][num] = False
    visited_s[i // 3 * 3 + j // 3][num] = False


def next(x, y):
    if y == 8:
        return x + 1, 0
    return x, y + 1


def dfs(x, y):
    if x == 9:
        global made
        made = True
        return
    if made:
        return
    nx, ny = next(x, y)
    if board[x][y]:
        dfs(nx, ny)
    else:
        for num in range(1, 10):
            if made:
                return
            if check(x, y, num):
                board[x][y] = num
                visit(x, y, num)
                dfs(nx, ny)
                if made:
                    return
                delete(x, y, num)
                board[x][y] = 0
    return


for i in range(9):
    for j in range(9):
        if board[i][j]:
            num = board[i][j]
            visit(i, j, num)
made = False
dfs(0, 0)
for i in range(9):
    print(*board[i], sep='')
