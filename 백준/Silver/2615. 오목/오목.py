direction = ((-1, 1), (0, 1), (1, 1), (1, 0))


def judge(board):
    for j in range(19):
        for i in range(19):
            if board[i][j]:
                check = board[i][j]
                board[i][j] = -check
                for di, dj in direction:
                    if board[i - di][j - dj] == -check:
                        continue
                    cnt = 1
                    ci, cj = i, j
                    while True:
                        ci += di
                        cj += dj
                        if board[ci][cj] == check:
                            cnt += 1
                        else:
                            break
                    if cnt == 5:
                        return check, i + 1, j + 1
    return 0, 0, 0


omok = [list(map(int, input().split())) + [0] for _ in range(19)] + [[0] * 20]
winner, row, col = judge(omok)
print(winner)
if winner:
    print(row, col)
