"""
BOJ : 마법사 상어와 파이어볼

시작 시간 : 2시 09분
구상 완료 : 2시 12분
1회 오답 : 2시 31분
제출 시간 : 2시 32분
"""

# 시뮬레이션, 구현

n, m, k = map(int, input().split())
board = [[[] for __ in range(n)] for _ in range(n)]
directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
for fireball in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r - 1][c - 1].append((m, s, d))
for move in range(k):
    moved_board = [[[] for __ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for m, s, d in board[i][j]:
                di, dj = directions[d]
                ni, nj = (i + di * s) % n, (j + dj * s) % n
                moved_board[ni][nj].append((m, s, d))
    for i in range(n):
        for j in range(n):
            if len(moved_board[i][j]) > 1:
                cnt = len(moved_board[i][j])
                tm, ts, rd = moved_board[i][j][0]
                all_same = True
                is_odd = rd & 1
                for k in range(1, cnt):
                    m, s, d = moved_board[i][j][k]
                    tm += m
                    ts += s
                    if (d & 1) ^ is_odd:
                        all_same = False
                m = tm // 5
                s = ts // cnt
                if m:
                    moved_board[i][j] = [(m, s, fd - all_same) for fd in range(1, 8, 2)]
                else:
                    moved_board[i][j].clear()
    board = moved_board

print(sum(sum(sum(m for m, s, d in board[i][j]) for j in range(n)) for i in range(n)))
