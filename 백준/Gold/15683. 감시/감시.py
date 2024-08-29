"""
BOJ : 감시
코드트리 : 이상한 체스

시작 시간 : 3시 03분
제출 시간 : 3시 34분
"""

n, m = map(int, input().split())
board = [list(map(int, input().split())) + [6] for _ in range(n)] + [[6] * m]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

units_directions = (
    (),
    (((0, 1),), ((1, 0),), ((0, -1),), ((-1, 0),)),
    (((0, 1), (0, -1)), ((1, 0), (-1, 0))),
    (((0, 1), (1, 0)), ((1, 0), (0, -1)), ((0, -1), (-1, 0)), ((-1, 0), (0, 1))),
    (((0, 1), (1, 0), (0, -1)), ((1, 0), (0, -1), (-1, 0)), ((0, -1), (-1, 0), (0, 1)), ((-1, 0), (0, 1), (1, 0)))
)

units = []

for i in range(n):
    for j in range(m):
        u = board[i][j]
        if u == 5:
            for di, dj in directions:
                ci, cj = i + di, j + dj
                while board[ci][cj] != 6:
                    if board[ci][cj] == 0:
                        board[ci][cj] = 7
                    ci += di
                    cj += dj
        elif 0 < u < 5:
            units.append((i, j, u))

U = len(units)
units_can_go = [[] for _ in range(U)]

for idx, (i, j, u) in enumerate(units):
    for ud in units_directions[u]:
        units_can_go[idx].append(set())
        for di, dj in ud:
            ci, cj = i + di, j + dj
            while board[ci][cj] != 6:
                if not board[ci][cj]:
                    units_can_go[idx][-1].add(ci * m + cj)
                ci += di
                cj += dj

blank = sum(line.count(0) for line in board)
least = blank
units_now_seeing = [0] * U


def dfs(depth):
    if depth == U:
        global least
        can_go = set()
        for idx, uns in enumerate(units_now_seeing):
            can_go |= units_can_go[idx][uns]
        if blank - len(can_go) < least:
            least = blank - len(can_go)
        return
    for uns in range(len(units_can_go[depth])):
        units_now_seeing[depth] = uns
        dfs(depth + 1)
    return


dfs(0)
print(least)
