"""
BOJ : 주사위 윷놀이

시작 시간 : 2시 11분
구상 완료 : 2시 19분
제출 시간 : 3시 08분
"""

routes = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20),
    (5, 21, 22, 23, 24, 30, 31, 20),
    (10, 25, 26, 24, 30, 31, 20),
    (15, 27, 28, 29, 24, 30, 31, 20)
)

scores = (
    (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40),
    (10, 13, 16, 19, 25, 30, 35, 40),
    (20, 22, 24, 25, 30, 35, 40),
    (30, 28, 27, 26, 25, 30, 35, 40)
)

routes_length = (21, 8, 7, 8)

move = [[100] * 6 for _ in range(71)]

for current in range(71):
    cr, ci = current // 21, current % 21
    cl = routes_length[cr]
    if ci >= cl:
        continue
    for dice in range(1, 6):
        ni = ci + dice
        if ni >= cl:
            continue
        if not cr and ni in (5, 10, 15):
            move[current][dice] = (ni // 5) * 21
        else:
            move[current][dice] = current + dice

dices = tuple(map(int, input().split()))
best = 0


def dfs(turn, positions, numbers, departed, score):
    if turn == 10:
        global best
        best = max(best, score)
        return
    if score + (10 - turn) * 40 <= best:
        return
    d = dices[turn]
    for unit in range(departed):
        cp = positions[unit]
        cn = numbers[unit]
        if cp == 100:
            continue
        np = move[cp][d]
        if np == 100:
            positions[unit] = 100
            numbers[unit] = 100
            dfs(turn + 1, positions, numbers, departed, score)
            positions[unit] = cp
            numbers[unit] = cn
        else:
            nr, ni = np // 21, np % 21
            nn = routes[nr][ni]
            if nn in numbers:
                continue
            positions[unit] = np
            numbers[unit] = nn
            dfs(turn + 1, positions, numbers, departed, score + scores[nr][ni])
            positions[unit] = cp
            numbers[unit] = cn

    if departed < 4:
        unit = departed
        cp = 0
        np = move[0][d]
        nr, ni = np // 21, np % 21
        nn = routes[nr][ni]
        if nn not in numbers:
            positions[unit] = np
            numbers[unit] = nn
            dfs(turn + 1, positions, numbers, departed + 1, score + scores[nr][ni])
            positions[unit] = cp
            numbers[unit] = 0


dfs(0, [0, 0, 0, 0], [0, 0, 0, 0], 0, 0)
print(best)
