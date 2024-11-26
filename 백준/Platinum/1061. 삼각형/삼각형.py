n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
r = sum(line.count('R') for line in board)
g = sum(line.count('G') for line in board)
b = sum(line.count('B') for line in board)


def triangle(x1, y1, x2, y2, x3, y3):
    return abs(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3)


if not r * g * b:
    print(0)
else:
    red = set()
    green = set()
    blue = set()
    r_top = min(i for i in range(n) if 'R' in board[i])
    r_bottom = max(i for i in range(n) if 'R' in board[i])
    g_top = min(i for i in range(n) if 'G' in board[i])
    g_bottom = max(i for i in range(n) if 'G' in board[i])
    b_top = min(i for i in range(n) if 'B' in board[i])
    b_bottom = max(i for i in range(n) if 'B' in board[i])
    for i in range(m):
        if board[r_top][i] == 'R':
            red.add((r_top, i))
        if board[r_bottom][i] == 'R':
            red.add((r_bottom, i))
        if board[g_top][i] == 'G':
            green.add((g_top, i))
        if board[g_bottom][i] == 'G':
            green.add((g_bottom, i))
        if board[b_top][i] == 'B':
            blue.add((b_top, i))
        if board[b_bottom][i] == 'B':
            blue.add((b_bottom, i))
    for i in range(r_top + 1, r_bottom):
        r_index = [j for j in range(m) if board[i][j] == 'R']
        if r_index:
            red.add((i, min(r_index)))
            red.add((i, max(r_index)))
    for i in range(g_top + 1, g_bottom):
        g_index = [j for j in range(m) if board[i][j] == 'G']
        if g_index:
            green.add((i, min(g_index)))
            green.add((i, max(g_index)))
    for i in range(b_top + 1, b_bottom):
        b_index = [j for j in range(m) if board[i][j] == 'B']
        if b_index:
            blue.add((i, min(b_index)))
            blue.add((i, max(b_index)))
    rg = set()
    gb = set()
    br = set()
    # print('----------r,g,b----------')
    # print(red)
    # print(green)
    # print(blue)
    for x1, y1 in red:
        for x2, y2 in green:
            big = set()
            big_size = 0
            for x3, y3 in blue:
                size = triangle(x1, y1, x2, y2, x3, y3)
                if size > big_size:
                    big = {(x1, y1, x2, y2, x3, y3)}
                    big_size = size
                elif size == big_size:
                    big.add((x1, y1, x2, y2, x3, y3))
            for t in big:
                rg.add(t)
    for x2, y2 in green:
        for x3, y3 in blue:
            big = set()
            big_size = 0
            for x1, y1 in red:
                size = triangle(x1, y1, x2, y2, x3, y3)
                if size > big_size:
                    big = {(x1, y1, x2, y2, x3, y3)}
                    big_size = size
                elif size == big_size:
                    big.add((x1, y1, x2, y2, x3, y3))
            for t in big:
                gb.add(t)
    for x3, y3 in blue:
        for x1, y1 in red:
            big = set()
            big_size = 0
            for x2, y2 in green:
                size = triangle(x1, y1, x2, y2, x3, y3)
                if size > big_size:
                    big = {(x1, y1, x2, y2, x3, y3)}
                    big_size = size
                elif size == big_size:
                    big.add((x1, y1, x2, y2, x3, y3))
            for t in big:
                br.add(t)
    # print('---------rg,gb,br,길이-----------')
    # print(rg)
    # print(gb)
    # print(br)
    # print(len(rg), len(gb), len(br))
    print(r * g * b - len(rg & gb & br))
