n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ms = [[board[0][i] + board[1][j] for j in range(3)] for i in range(3)]
for i in range(3):
    ms[i][i] = 2000
for i in range(2, n - 1):
    ms00 = board[i][0] + min(ms[0][1], ms[0][2])
    ms01 = board[i][1] + min(ms[0][0], ms[0][2])
    ms02 = board[i][2] + min(ms[0][0], ms[0][1])
    ms10 = board[i][0] + min(ms[1][1], ms[1][2])
    ms11 = board[i][1] + min(ms[1][0], ms[1][2])
    ms12 = board[i][2] + min(ms[1][0], ms[1][1])
    ms20 = board[i][0] + min(ms[2][1], ms[2][2])
    ms21 = board[i][1] + min(ms[2][0], ms[2][2])
    ms22 = board[i][2] + min(ms[2][0], ms[2][1])
    ms[0][0], ms[0][1], ms[0][2], ms[1][0], ms[1][1], ms[1][2], ms[2][0], ms[2][1], ms[2][
        2] = ms00, ms01, ms02, ms10, ms11, ms12, ms20, ms21, ms22

if n > 2:
    ms0 = min(ms[0][0] + board[n - 1][1], ms[0][0] + board[n - 1][2], ms[0][1] + board[n - 1][2],
              ms[0][2] + board[n - 1][1])
    ms1 = min(ms[1][1] + board[n - 1][0], ms[1][1] + board[n - 1][2], ms[1][0] + board[n - 1][2],
              ms[1][2] + board[n - 1][0])
    ms2 = min(ms[2][2] + board[n - 1][0], ms[2][2] + board[n - 1][1], ms[2][0] + board[n - 1][1],
              ms[2][1] + board[n - 1][0])
    print(min(ms0, ms1, ms2))
else:
    print(min(min(ms[0]), min(ms[1]), min(ms[2])))
