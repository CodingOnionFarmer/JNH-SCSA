field = [list(input()) for _ in range(12)]
visited = [[False] * 6 for _ in range(12)]
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def drop():
    field_columns = [[] for _ in range(6)]
    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] != '.':
                field_columns[j].append(field[i][j])
                field[i][j] = '.'
    for j in range(6):
        for idx, puyo in enumerate(field_columns[j]):
            field[11 - idx][j] = puyo


def check(i, j, puyo):
    area = 1
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 12 and 0 <= nj < 6 and not visited[ni][nj] and field[ni][nj] == puyo:
            visited[ni][nj] = True
            area += check(ni, nj, puyo)
    return area


def explode(i, j, puyo):
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 12 and 0 <= nj < 6 and field[ni][nj] == puyo:
            field[ni][nj] = '.'
            explode(ni, nj, puyo)
    return


chain = 0
bomb = []
drop()
for i in range(12):
    for j in range(6):
        if field[i][j] != '.':
            visited[i][j] = True
            if check(i, j, field[i][j]) > 3:
                bomb.append((i, j, field[i][j]))

while bomb:
    chain += 1
    for si, sj, puyo in bomb:
        field[si][sj] = '.'
        explode(si, sj, puyo)
    visited = [[False] * 6 for _ in range(12)]
    bomb = []
    drop()
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':
                visited[i][j] = True
                if check(i, j, field[i][j]) > 3:
                    bomb.append((i, j, field[i][j]))

print(chain)

