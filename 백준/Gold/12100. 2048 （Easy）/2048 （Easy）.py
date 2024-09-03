n = int(input())
original_board = [list(map(int, input().split())) for _ in range(n)]
original_biggest = max(max(line) for line in original_board)
biggest = original_biggest
board_sum = sum(sum(line) for line in original_board)
maximal_biggest = biggest
while maximal_biggest << 1 <= board_sum:
    maximal_biggest <<= 1


def move_right(board, depth, temp_biggest, si, ei, sj, ej):
    global biggest, maximal_biggest
    if biggest == maximal_biggest:
        return
    if temp_biggest << (5 - depth) == biggest:
        return
    if depth == 5:
        biggest = temp_biggest
        return
    moved_board = [[0] * n for _ in range(n)]
    nej = nsj = n - 1
    for i in range(si, ei + 1):
        p = n - 1
        before = -1
        for j in range(ej, sj - 1, -1):
            num = board[i][j]
            if not num:
                continue
            if num == before:
                if num == temp_biggest:
                    temp_biggest <<= 1
                moved_board[i][p + 1] <<= 1
                before = -1
            else:
                moved_board[i][p] = num
                before = num
                p -= 1
        p += 1
        if p < nsj:
            nsj = p
    move_right(moved_board, depth + 1, temp_biggest, si, ei, nsj, nej)
    move_down(moved_board, depth + 1, temp_biggest, si, ei, nsj, nej)
    move_left(moved_board, depth + 1, temp_biggest, si, ei, nsj, nej)
    move_up(moved_board, depth + 1, temp_biggest, si, ei, nsj, nej)
    return


def move_down(board, depth, temp_biggest, si, ei, sj, ej):
    global biggest, maximal_biggest
    if biggest == maximal_biggest:
        return
    if temp_biggest << (5 - depth) == biggest:
        return
    if depth == 5:
        biggest = temp_biggest
        return
    moved_board = [[0] * n for _ in range(n)]
    nsi = nei = n - 1
    for j in range(sj, ej + 1):
        p = n - 1
        before = -1
        for i in range(ei, si - 1, -1):
            num = board[i][j]
            if not num:
                continue
            if num == before:
                if num == temp_biggest:
                    temp_biggest <<= 1
                moved_board[p + 1][j] <<= 1
                before = -1
            else:
                moved_board[p][j] = num
                before = num
                p -= 1
        p += 1
        if p < nsi:
            nsi = p
    move_right(moved_board, depth + 1, temp_biggest, nsi, nei, sj, ej)
    move_down(moved_board, depth + 1, temp_biggest, nsi, nei, sj, ej)
    move_left(moved_board, depth + 1, temp_biggest, nsi, nei, sj, ej)
    move_up(moved_board, depth + 1, temp_biggest, nsi, nei, sj, ej)
    return


def move_left(board, depth, temp_biggest, si, ei, sj, ej):
    global biggest, maximal_biggest
    if biggest == maximal_biggest:
        return
    if temp_biggest << (5 - depth) == biggest:
        return
    if depth == 5:
        biggest = temp_biggest
        return
    moved_board = [[0] * n for _ in range(n)]
    nsj = nej = 0
    for i in range(si, ei + 1):
        p = 0
        before = -1
        for j in range(sj, ej + 1):
            num = board[i][j]
            if not num:
                continue
            if num == before:
                if num == temp_biggest:
                    temp_biggest <<= 1
                moved_board[i][p - 1] <<= 1
                before = -1
            else:
                moved_board[i][p] = num
                before = num
                p += 1
        p -= 1
        if p > nej:
            nej = p
    move_right(moved_board, depth + 1, temp_biggest, si, ei, nsj, nej)
    move_down(moved_board, depth + 1, temp_biggest, si, ei, nsj, nej)
    move_left(moved_board, depth + 1, temp_biggest, si, ei, nsj, nej)
    move_up(moved_board, depth + 1, temp_biggest, si, ei, nsj, nej)
    return


def move_up(board, depth, temp_biggest, si, ei, sj, ej):
    global biggest, maximal_biggest
    if biggest == maximal_biggest:
        return
    if temp_biggest << (5 - depth) == biggest:
        return
    if depth == 5:
        biggest = temp_biggest
        return
    moved_board = [[0] * n for _ in range(n)]
    nsi = nei = 0
    for j in range(sj, ej + 1):
        p = 0
        before = -1
        for i in range(si, ei + 1):
            num = board[i][j]
            if not num:
                continue
            if num == before:
                if num == temp_biggest:
                    temp_biggest <<= 1
                moved_board[p - 1][j] <<= 1
                before = -1
            else:
                moved_board[p][j] = num
                before = num
                p += 1
        p -= 1
        if p > nei:
            nei = p
    move_right(moved_board, depth + 1, temp_biggest, nsi, nei, sj, ej)
    move_down(moved_board, depth + 1, temp_biggest, nsi, nei, sj, ej)
    move_left(moved_board, depth + 1, temp_biggest, nsi, nei, sj, ej)
    move_up(moved_board, depth + 1, temp_biggest, nsi, nei, sj, ej)
    return


move_right(original_board, 0, original_biggest, 0, n - 1, 0, n - 1)
move_down(original_board, 0, original_biggest, 0, n - 1, 0, n - 1)
move_left(original_board, 0, original_biggest, 0, n - 1, 0, n - 1)
move_up(original_board, 0, original_biggest, 0, n - 1, 0, n - 1)

print(biggest)
