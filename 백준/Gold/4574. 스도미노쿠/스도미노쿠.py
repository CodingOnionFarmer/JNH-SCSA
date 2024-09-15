directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
pos = {alp + str(digit): (ord(alp) - 65, digit - 1) for alp in 'ABCDEFGHI' for digit in range(1, 10)}


def solve_puzzle(depth, blank):
    if depth == pieces:
        return True
    if blank >= 81:
        return False
    bi, bj = blank // 9, blank % 9
    bs = bi // 3 * 3 + bj // 3
    for num in range(1, 10):
        if remain_row[bi][num] and remain_col[bj][num] and remain_sqr[bs][num]:
            board[blank] = num
            remain_row[bi][num] = False
            remain_col[bj][num] = False
            remain_sqr[bs][num] = False
            for adj_blank in adj[blank]:
                if board[adj_blank]:
                    continue
                ai, aj = adj_blank // 9, adj_blank % 9
                asq = ai // 3 * 3 + aj // 3
                for adj_num in range(1, 10):
                    if remain_row[ai][adj_num] and remain_col[aj][adj_num] and remain_sqr[asq][adj_num] and \
                            remain_domino[num][adj_num]:
                        board[adj_blank] = adj_num
                        remain_row[ai][adj_num] = False
                        remain_col[aj][adj_num] = False
                        remain_sqr[asq][adj_num] = False
                        remain_domino[num][adj_num] = False
                        remain_domino[adj_num][num] = False
                        next_blank = blank + 1
                        while next_blank < 81 and board[next_blank]:
                            next_blank += 1
                        if solve_puzzle(depth + 1, next_blank):
                            return True
                        remain_row[ai][adj_num] = True
                        remain_col[aj][adj_num] = True
                        remain_sqr[asq][adj_num] = True
                        remain_domino[num][adj_num] = True
                        remain_domino[adj_num][num] = True
                board[adj_blank] = 0
            remain_row[bi][num] = True
            remain_col[bj][num] = True
            remain_sqr[bs][num] = True
    board[blank] = 0
    return False


puzzle_num = 0
while True:
    n = int(input())
    if not n:
        break
    puzzle_num += 1
    board = [0] * 81
    remain_row = [[True] * 10 for _ in range(9)]
    remain_col = [[True] * 10 for _ in range(9)]
    remain_sqr = [[True] * 10 for _ in range(9)]
    remain_domino = [[True] * 10 for _ in range(10)]
    for i in range(1, 10):
        remain_domino[i][i] = False
    for _ in range(n):
        u, lu, v, lv = input().split()
        u = int(u)
        v = int(v)
        ui, uj = pos[lu]
        us = ui // 3 * 3 + uj // 3
        vi, vj = pos[lv]
        vs = vi // 3 * 3 + vj // 3
        board[ui * 9 + uj] = u
        board[vi * 9 + vj] = v
        remain_row[ui][u] = False
        remain_col[uj][u] = False
        remain_sqr[us][u] = False
        remain_row[vi][v] = False
        remain_col[vj][v] = False
        remain_sqr[vs][v] = False
        remain_domino[u][v] = False
        remain_domino[v][u] = False
    mono = list(input().split())
    for idx, p in enumerate(mono, 1):
        i, j = pos[p]
        s = i // 3 * 3 + j // 3
        board[i * 9 + j] = idx
        remain_row[i][idx] = False
        remain_col[j][idx] = False
        remain_sqr[s][idx] = False
    pieces = 36 - n
    adj = [tuple((i + di) * 9 + j + dj for di, dj in directions if
                 0 <= i + di < 9 and 0 <= j + dj < 9 and not board[(i + di) * 9 + j + dj]) for i in range(9) for j in
           range(9)]
    first_blank = 0
    while board[first_blank]:
        first_blank += 1
    solve_puzzle(0, first_blank)
    print('Puzzle', puzzle_num)
    for line in range(9):
        print(*board[line * 9:line * 9 + 9], sep='')
